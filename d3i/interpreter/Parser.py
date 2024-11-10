from antlr4 import *
from d3i.grammar.d3iLexer import *
from d3i.grammar.d3iGrammar import *
from d3i.interpreter.ElementVisitor import *

class Parser:
    def __init__( self ):
        self.lexer = None
        self.grammar = None
        self.tree = None
        self.fileName = None

    def ParseText( self, input, abortWhenError:bool=None ):
        self.fileName = "internal string"
        return self._parseInternal(InputStream(input),abortWhenError)
        
    def ParseFile( self, fileName, abortWhenError:bool=None ):
        self.fileName = fileName
        return self._parseInternal(FileStream(fileName),abortWhenError)

    def _parseInternal( self, stream, abortWhenError:bool ):
        self.lexer = d3iLexer(stream)
        self.grammar = d3iGrammar(CommonTokenStream(self.lexer))

        # Hozzáadjuk a saját hibafigyelőt
        error_listener = SyntaxErrorListener()
        self.grammar.removeErrorListeners()
        self.grammar.addErrorListener(error_listener)
            
        self.tree = self.grammar.d3i()
       
        if(error_listener.has_error):
            print(error_listener.error_message)
            if(abortWhenError):
                return None

        return self._buildElementTree()

    def PrintTree( self ):
        print(self.tree.toStringTree(recog=self.grammar))

    def _buildElementTree( self ):
        visitor = ElementVisitor(self.fileName)
        return visitor.visit(self.tree)

from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.has_error = False  # Ezt használjuk a hiba állapotának nyomon követésére
        self.error_message = ""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        self.error_message += f"Hiba a {line}. sor {column}. oszlopában: {msg}\n"
        

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        self.has_error = True
        self.error_message += f"reportAmbiguity\n"
        

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        self.has_error = True
        self.error_message += f"reportAttemptingFullContext\n"
        

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.has_error = True
        self.error_message += f"reportAttemptingFullContext\n"
        
