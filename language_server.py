import d3i.__main__ as main_module
from pygls.server import LanguageServer

server = LanguageServer(name='d3i-lsp', version='0.1.0')

@server.feature('initialize')
def initialize(ls: LanguageServer, params):
    return main_module.lsp_initialize(ls, params)

@server.feature('textDocument/didOpen')
def did_open(ls: LanguageServer, params):
    return main_module.lsp_did_open_text(ls, params)

if __name__ == '__main__':
    server.start_io()
