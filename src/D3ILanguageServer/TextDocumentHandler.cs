using OmniSharp.Extensions.LanguageServer.Protocol.Models;
using OmniSharp.Extensions.LanguageServer.Protocol.Document;
using MediatR;
using OmniSharp.Extensions.LanguageServer.Protocol.Client.Capabilities;
using Range = OmniSharp.Extensions.LanguageServer.Protocol.Models.Range;
using OmniSharp.Extensions.LanguageServer.Protocol.Server;

public class TextDocumentHandler : DidOpenTextDocumentHandlerBase
{
    private readonly ILanguageServerFacade _server;

    public TextDocumentHandler(ILanguageServerFacade server)
    {
        _server = server;
    }

    public override Task<Unit> Handle(DidOpenTextDocumentParams request, CancellationToken cancellationToken)
    {
        var diagnostics = new Container<Diagnostic>(
            new Diagnostic
            {
                Range = new Range(
                    new Position(0, 0),
                    new Position(0, 5)
                ),
                Severity = DiagnosticSeverity.Warning,
                Message = "Demo diagnostic from .NET LSP"
            }
        );

        _server.TextDocument.PublishDiagnostics(new PublishDiagnosticsParams
        {
            Uri = request.TextDocument.Uri,
            Diagnostics = diagnostics
        });

        return Task.FromResult(Unit.Value);
    }

    public TextDocumentOpenRegistrationOptions GetRegistrationOptions()
    {
        return new TextDocumentOpenRegistrationOptions
        {
            DocumentSelector = new TextDocumentSelector(
                 new TextDocumentFilter
                 {
                     Pattern = "**/*.d3i"
                 }
             )
        };
    }

    protected override TextDocumentOpenRegistrationOptions CreateRegistrationOptions(
        TextSynchronizationCapability capability,
        ClientCapabilities clientCapabilities)
    {
        return GetRegistrationOptions();
    }
}
