"""
Language server for the .d3 DSL.

It reuses the compiler itself: a document is parsed by the same Engine and checked by the same
SemanticChecker the CLI runs, so the editor reports exactly what a build would. The diagnostics
are produced by `build_diagnostics`, which is a plain function over text - the server object only
publishes what it returns.

Install with:  pip install d3i[lsp]     Run with:  python language_server.py
"""

from typing import List

from lsprotocol import types as lsp
from pygls.lsp.server import LanguageServer

from d3i.Engine import Diagnostic, Engine, Session, Source
from d3i.linters.SemanticChecker import SemanticChecker

_SEVERITY = {
    Diagnostic.Severity.Error: lsp.DiagnosticSeverity.Error,
    Diagnostic.Severity.Warning: lsp.DiagnosticSeverity.Warning,
    Diagnostic.Severity.Message: lsp.DiagnosticSeverity.Information,
}


def build_diagnostics(text: str, uri: str) -> List[lsp.Diagnostic]:
    """
    Parses and lints one document and returns its diagnostics.

    Parsing may leave the model half-built, so the linter only runs when parsing produced no
    error - otherwise the editor would show a pile of follow-on complaints about elements that
    were never built.
    """
    session = Session(Source.CreateFromText(text, fileName=uri))
    try:
        Engine().Build(session)
        if session.HasAnyError() is False:
            session.main.visit(SemanticChecker(session), None)
    except Exception as exception:   # a crash in the compiler must not take the editor down
        return [
            lsp.Diagnostic(
                range=_range(1, 0),
                severity=lsp.DiagnosticSeverity.Error,
                source="d3i",
                message=f"internal error while analysing the document: {exception}",
            )
        ]

    return [
        lsp.Diagnostic(
            range=_range(diagnostic.line, diagnostic.column),
            severity=_SEVERITY.get(diagnostic.severity, lsp.DiagnosticSeverity.Information),
            source="d3i",
            message=diagnostic.message,
        )
        for diagnostic in session.diagnostics
    ]


def _range(line: int, column: int) -> lsp.Range:
    """
    The compiler counts lines from 1 and LSP from 0. The compiler reports a position, not a span,
    so the range is the single character at that position and the editor widens it to the word.
    """
    start = lsp.Position(line=max((line or 1) - 1, 0), character=max(column or 0, 0))
    return lsp.Range(start=start, end=lsp.Position(line=start.line, character=start.character + 1))


server = LanguageServer(name="d3i-lsp", version="0.1.0")


def _publish(ls: LanguageServer, uri: str, text: str) -> None:
    ls.text_document_publish_diagnostics(
        lsp.PublishDiagnosticsParams(uri=uri, diagnostics=build_diagnostics(text, uri))
    )


@server.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
def did_open(ls: LanguageServer, params: lsp.DidOpenTextDocumentParams) -> None:
    _publish(ls, params.text_document.uri, params.text_document.text)


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls: LanguageServer, params: lsp.DidChangeTextDocumentParams) -> None:
    document = ls.workspace.get_text_document(params.text_document.uri)
    _publish(ls, params.text_document.uri, document.source)


@server.feature(lsp.TEXT_DOCUMENT_DID_SAVE)
def did_save(ls: LanguageServer, params: lsp.DidSaveTextDocumentParams) -> None:
    document = ls.workspace.get_text_document(params.text_document.uri)
    _publish(ls, params.text_document.uri, document.source)


if __name__ == "__main__":
    server.start_io()
