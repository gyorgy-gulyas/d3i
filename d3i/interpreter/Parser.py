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
        error_listener = _ErrorListener(self.fileName)
        self.grammar.removeErrorListeners()
        self.grammar.addErrorListener(error_listener)
            
        self.tree = self.grammar.d3i()
       
        if(error_listener.has_error):
            error_listener.PrintErrors()
            if(abortWhenError):
                return None

        return self._buildElementTree()

    def PrintTree( self ):
        print(self.tree.toStringTree(recog=self.grammar))

    def _buildElementTree( self ):
        visitor = ElementVisitor(self.fileName)
        return visitor.visit(self.tree)

from antlr4.error.ErrorListener import ErrorListener

class _ErrorListener(ErrorListener):
    def __init__(self,fileName):
        super(_ErrorListener, self).__init__()
        self.fileName=fileName
        self.has_error = False  # Ezt használjuk a hiba állapotának nyomon követésére
        self.error_messages:List[_ErrorListener.error] = []

    def PrintErrors(self):
        for error in self.error_messages:
            print( f"{self.fileName}:{error.line}. column {error.column}: {error.message}\n")
            

    def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
        self.has_error = True
        error:ErrorListener.error = _ErrorListener.error()
        error.line = line
        error.column = column
        error.message = message
        self.error_messages.append(error)

    class error:
        def __init__(self):
            self.line:int=None
            self.column:int=None
            self.message:int=None

      

    
