from antlr4 import *
from interpreter.grammar.d3iLexer import *
from interpreter.grammar.d3iGrammar import *
from interpreter.ElementVisitor import *

class Parser:
    def __init__( self ):
        self.lexer = None
        self.grammar = None
        self.tree = None
        self.fileName = None

    def ParseText( self, input ):
        self.fileName = "internal string"
        self._parseInternal(InputStream(input))
        
    def ParseFile( self, fileName ):
        self.fileName = fileName
        self._parseInternal(FileStream(fileName))

    def _parseInternal( self, stream ):
        self.lexer = d3iLexer(stream)
        self.grammar = d3iGrammar(CommonTokenStream(self.lexer))
        self.tree = self.grammar.d3i()

    def PrintTree( self ):
        print(self.tree.toStringTree(recog=self.grammar))

    def BuildElementTree( self ):
        visitor = ElementVisitor(self.fileName)
        visitor.visit(self.tree)
