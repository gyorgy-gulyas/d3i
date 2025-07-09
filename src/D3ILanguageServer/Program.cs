using OmniSharp.Extensions.LanguageServer.Server;

class Program
{
    static async Task Main(string[] args)
    {
        var server = await LanguageServer.From(options =>
            options
                .WithInput(Console.OpenStandardInput())
                .WithOutput(Console.OpenStandardOutput())
                .WithHandler<TextDocumentHandler>()
        );

        await server.WaitForExit;
    }
}
