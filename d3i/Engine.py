from antlr4 import *
from d3i.grammar.d3iLexer import *
from d3i.grammar.d3iGrammar import *
from d3i.interpreter.ElementVisitor import *


class Session:
    def __init__( self ):
        self.fileName:str = None
        self.stream:InputStream= None
        self.lexer:d3iLexer = None
        self.grammar:d3iGrammar = None
        self.tree:d3iGrammar.D3iContext = None

    @staticmethod
    def CreateFromText( input ):
        result:Session = Session()
        result.stream = InputStream(input)
        result.fileName = "internal string"
        return result

    @staticmethod
    def CreateFromFile( fileName ):
        result:Session = Session()
        result.stream = FileStream(fileName)
        result.fileName = fileName
        return result

    def PrintTree( self ):
        if(self.tree!= None):
            print(self.tree.toStringTree(recog=self.grammar))

class Engine:
    def __init__( self ):
        self.abortWhenError:bool=False
        
    def Parse( self, session:Session ):
        session.lexer = d3iLexer(session.stream)
        session.grammar = d3iGrammar(CommonTokenStream(session.lexer))

        # Hozzáadjuk a saját hibafigyelőt
        error_listener = SyntaxErrorListener(session.fileName)
        session.grammar.removeErrorListeners()
        session.grammar.addErrorListener(error_listener)
            
        tree = session.grammar.d3i()
       
        if(error_listener.has_error):
            error_listener.PrintErrors()
            if(self.abortWhenError):
                return None

        return tree

    def Build( self, session:Session ):
        tree:d3iGrammar.D3iContext = self.Parse(session)
        visitor = ElementVisitor(session.fileName)
        return visitor.visit(tree)

    def Compile( self, session:Session ):
        root:d3 = self.Build(session)
        return root

from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self,fileName):
        super(SyntaxErrorListener, self).__init__()
        self.fileName=fileName
        self.has_error = False  # Ezt használjuk a hiba állapotának nyomon követésére
        self.error_messages:List[SyntaxErrorListener.error] = []

    def PrintErrors(self):
        for error in self.error_messages:
            print( f"{self.fileName}:{error.line}. column {error.column}: {error.message}\n")
            

    def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
        self.has_error = True
        error:ErrorListener.error = SyntaxErrorListener.error()
        error.line = line
        error.column = column
        error.message = message
        self.error_messages.append(error)

    class error:
        def __init__(self):
            self.line:int=None
            self.column:int=None
            self.message:int=None

      

    
