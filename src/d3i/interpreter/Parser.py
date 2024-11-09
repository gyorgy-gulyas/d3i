from antlr4 import *
from d3i.interpreter.grammar.d3iLexer import *
from d3i.interpreter.grammar.d3iGrammar import *
from d3i.interpreter.ElementVisitor import *

class Parser:
    def __init__( self ):
        self.lexer = None
        self.grammar = None
        self.tree = None
        self.fileName = None

    def ParseText( self, input ):
        self.fileName = "internal string"
        return self._parseInternal(InputStream(input))
        
    def ParseFile( self, fileName ):
        self.fileName = fileName
        return self._parseInternal(FileStream(fileName))

    def _parseInternal( self, stream ):
        self.lexer = d3iLexer(stream)
        self.grammar = d3iGrammar(CommonTokenStream(self.lexer))
        self.tree = self.grammar.d3i()
        return self._buildElementTree()

    def PrintTree( self ):
        print(self.tree.toStringTree(recog=self.grammar))

    def _buildElementTree( self ):
        visitor = ElementVisitor(self.fileName)
        return visitor.visit(self.tree)
