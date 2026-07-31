import unittest

try:
    from lsprotocol import types as lsp
    import language_server
except ImportError:                       # pygls is an optional extra (pip install d3i[lsp])
    language_server = None


@unittest.skipIf(language_server is None, "pygls is not installed (optional [lsp] extra)")
class TestLanguageServerDiagnostics(unittest.TestCase):
    """
    The server reuses the compiler, so what the editor shows must match what a build reports.
    build_diagnostics is a plain function over text, so it is testable without a live LSP session.
    """

    def test_a_valid_document_reports_nothing(self):
        diagnostics = language_server.build_diagnostics("""
domain Shop {
    context Sales {
        valueobject Money {
            amount:integer
        }
    }
}
""", "file:///main.d3")
        self.assertEqual([], diagnostics)

    def test_a_syntax_error_is_reported_at_its_position(self):
        diagnostics = language_server.build_diagnostics("domain {", "file:///main.d3")

        self.assertTrue(len(diagnostics) > 0)
        self.assertEqual(lsp.DiagnosticSeverity.Error, diagnostics[0].severity)
        self.assertEqual("d3i", diagnostics[0].source)
        # the compiler counts lines from 1, LSP from 0
        self.assertEqual(0, diagnostics[0].range.start.line)

    def test_a_semantic_error_is_reported_too(self):
        # An unresolvable type name is not a syntax error - it only surfaces once the linter runs.
        diagnostics = language_server.build_diagnostics("""
domain Shop {
    context Sales {
        valueobject Money {
            amount:NoSuchType
        }
    }
}
""", "file:///main.d3")

        self.assertTrue(len(diagnostics) > 0)
        self.assertIn("NoSuchType", " ".join(d.message for d in diagnostics))

    def test_the_linter_does_not_run_on_a_document_that_did_not_parse(self):
        # Otherwise a single typo buries the editor in follow-on errors about elements that were
        # never built.
        diagnostics = language_server.build_diagnostics("domain Shop { context {", "file:///main.d3")

        self.assertTrue(all("cannot be resolved" not in d.message for d in diagnostics))

    def test_an_empty_document_is_valid(self):
        self.assertEqual([], language_server.build_diagnostics("", "file:///main.d3"))


if __name__ == "__main__":
    unittest.main()
