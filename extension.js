const path = require('path');
const cp = require('child_process');
const vscode = require('vscode');
const {
    LanguageClient,
    TransportKind
} = require('vscode-languageclient/node');

let client;

function activate(context) {
    // A language server Python script elérési útja
    const serverModule = context.asAbsolutePath(
        path.join('server', 'language_server.py')
    );

    // A Python parancs (rendszertől függően lehet python3 is)
    const pythonCommand = 'python';

    const serverOptions = {
        command: pythonCommand,
        args: [serverModule]
    };

    const clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'd3i' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/*.d3')
        }
    };

    client = new LanguageClient(
        'd3iLanguageServer',
        'd3i Language Server',
        serverOptions,
        clientOptions
    );

    client.start();
}

function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}

module.exports = {
    activate,
    deactivate
};