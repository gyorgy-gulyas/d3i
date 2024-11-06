from antlr4 import *
from parser.d3iLexer import *
from parser.d3iGrammar import *
from parser.ElementVisitor import *

class d3iParser:
    def __init__( self ):
        self.lexer = None
        self.grammar = None
        self.tree = None

    def ParseText( self, input ):
        self.lexer = d3iLexer(InputStream(input))
        self.grammar = d3iGrammar(CommonTokenStream(self.lexer))
        self.tree = self.grammar.d3i()

    def PrintTree( self ):
        print(self.tree.toStringTree(recog=self.grammar))

    def BuildElementTree( self ):
        visitor = ElementVisitor()
        visitor.visit(self.tree)
