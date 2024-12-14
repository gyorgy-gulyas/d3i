from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from d3i.grammar.d3iLexer import *
from d3i.grammar.d3iGrammar import *
from d3i.elements.ElementBuilder import *
import d3i

class Source:
    def __init__(self):
        self.fileName: str = None
        self.content: str = None

    @staticmethod
    def CreateFromText(content, fileName="internal string"):
        source = Source()
        source.content = content
        source.fileName = fileName
        return source

    @staticmethod
    def CreateFromFile(fileName):
        source = Source()
        source.fileName = fileName
        with open(fileName, 'r') as file:
            source.content = file.read()
        return source


class Session:
    def __init__(self):
        self.sources: List[Source] = []
        self.syntaxTrees: List[d3iGrammar.D3iContext] = []
        self.elementTrees: List[d3] = []
        self.diagnostics: List[Diagnostic] = []
        self.main: d3 = None

    def AddSource(self, source: Source):
        self.sources.append(source)

    def HasDiagnostic(self):
        if (len(self.diagnostics) > 0):
            return True
        return False

    def HasAnyError(self):
        for msg in self.diagnostics:
            if(msg.severity == Diagnostic.Severity.Error):
                return True
        return False

    def HasAnyWarning(self):
        for msg in self.diagnostics:
            if(msg.severity == Diagnostic.Severity.Warning):
                return True
        return False

    def PrintDiagnostics(self):
        for msg in self.diagnostics:
            print(f"{msg.toText()}\n")

    def ClearDiagnostics(self):
        self.diagnostics.clear()

    def ReportDiagnostic(self, message, severity, fileName="", line=0, column=0 ):
        diagnostic: Diagnostic = Diagnostic()
        diagnostic.severity = severity
        diagnostic.fileName = fileName
        diagnostic.line = line
        diagnostic.column = column
        diagnostic.message = message
        self.diagnostics.append(diagnostic)


class Engine:

    def Build(self, session: Session):
        self.__create_syntax_trees__(session)
        self.__create_element_trees__(session)
        self.__merge_element_trees__(session)

        return session.main

    def __create_syntax_trees__(self, session: Session):
        for source in session.sources:
            lexer = d3iLexer(InputStream(source.content))
            grammar = d3iGrammar(CommonTokenStream(lexer))

            error_listener = Engine.__syntaxErrorListener__(source.fileName, session)
            grammar.removeErrorListeners()
            grammar.addErrorListener(error_listener)

            syntaxTree = grammar.d3i()
            syntaxTree.source = source
            session.syntaxTrees.append(syntaxTree)

    def __create_element_trees__(self, session: Session):
        visitor = ElementBuilder()
        for syntaxTree in session.syntaxTrees:
            visitor.fileName = syntaxTree.source.fileName
            elementTree = visitor.visit(syntaxTree)
            session.elementTrees.append(elementTree)

    def __merge_element_trees__(self, session: Session):
        session.main = d3()

        for elementTree in session.elementTrees:
            for domain in elementTree.domains:
                # find domain in merged
                domain_already: d3i.domain = self.__find_domain_by_name__(session.main.domains, domain.name)
                if (domain_already == None):
                    # append domain to merged
                    session.main.domains.append(domain)
                else:
                    # merge event and contexts to merged
                    domain_already.domain_events.extend(domain.domain_events)
                    for context in domain.contexts:
                        # find context in merged
                        context_already: d3i.context = self.__find_context_by_name__(
                            domain_already.contexts, context.name)
                        if (context_already == None):
                            domain.contexts.append(context)
                        else:
                            context_already.enums.extend(context.enums)
                            context_already.value_objects.extend(context.value_objects)
                            context_already.aggregates.extend(context.aggregates)
                            context_already.views.extend(context.views)
                            context_already.repositories.extend(context.repositories)
                            context_already.context_events.extend(context.context_events)
                            context_already.services.extend(context.services)
                            context_already.interfaces.extend(context.interfaces)

    @staticmethod
    def __find_domain_by_name__(domains, name):
        for domain in domains:
            if (domain.name == name):
                return domain

        return None

    @staticmethod
    def __find_context_by_name__(contexts, name):
        for context in contexts:
            if (context.name == name):
                return context

        return None

    class __syntaxErrorListener__(ErrorListener):
        def __init__(self, fileName, session: Session):
            super(Engine.__syntaxErrorListener__, self).__init__()
            self.fileName = fileName
            self.session = session

        def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
            self.session.ReportDiagnostic(message,Diagnostic.Severity.Error,self.fileName,line,column)

class Diagnostic:
    def __init__(self):
        self.severity: Diagnostic.Severity = Diagnostic.Severity.Message
        self.fileName: str = None
        self.line: int = None
        self.column: int = None
        self.message: int = None

    def toText(self):
        return f"{self.fileName}({self.line},{self.column}): {self.severity} :{self.message}\n"
    
    class Severity(Enum):
        Message = 1,
        Warning = 2,
        Error = 3,
        
