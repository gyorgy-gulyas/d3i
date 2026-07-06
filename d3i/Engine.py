import os
from pathlib import Path
from typing import Dict

from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
from d3i.grammar.d3iLexer import *
from d3i.grammar.d3iGrammar import *
from d3i.elements.Elements import *
from d3i.elements.ElementBuilder import *


class Source:
    """
    Represents the source of a d3 file, which could be a file or a text string.
    Provides methods to create Source instances from either.
    """

    def __init__(self):
        self.fileName: str = None
        self.content: str = None

    @staticmethod
    def CreateFromText(content, fileName="internal string"):
        """
        Creates a Source instance from a given text content.
        """
        source = Source()
        source.content = content
        source.fileName = fileName
        return source

    @staticmethod
    def CreateFromFile(fileName):
        """
        Creates a Source instance from a file.
        Reads the content of the file.
        """
        source = Source()
        # Normalize and get the absolute path of the file
        source.fileName = os.path.normpath(os.path.abspath(fileName))

        # Open and read the file content
        with open(fileName, 'r', encoding='utf-8') as file:
            source.content = file.read()
        return source


class Session:
    """
    Manages the state of a d3 processing session, including diagnostics and syntax trees.
    """

    def __init__(self, source: Source, projectName: str = None):
        self.source: Source = source
        self.syntaxTree: d3iGrammar.D3Context = []
        self.diagnostics: List[Diagnostic] = []
        self.main: d3 = None
        self.all: Dict[str, d3] = {}

        self.sources: List[Source] = []
        self.syntaxTrees: List[d3iGrammar.D3Context] = []
        self.elementTrees: List[d3] = []
        self.diagnostics: List[Diagnostic] = []
        self.main: d3 = None
        self.projectName: str = projectName

    def HasDiagnostic(self):
        """
        Checks if there are any diagnostics recorded.
        """
        # Return true if diagnostics list is not empty
        return len(self.diagnostics) > 0

    def HasAnyError(self):
        """
        Checks if there are any errors in diagnostics.
        """
        # Iterate through diagnostics and look for errors
        for msg in self.diagnostics:
            if msg.severity == Diagnostic.Severity.Error:
                return True
        return False

    def HasAnyWarning(self):
        """
        Checks if there are any warnings in diagnostics.
        """
        # Iterate through diagnostics and look for warnings
        for msg in self.diagnostics:
            if msg.severity == Diagnostic.Severity.Warning:
                return True
        return False

    def PrintDiagnostics(self):
        """
        Prints all recorded diagnostics.
        """
        print("\n")
        for msg in self.diagnostics:
            print(f"{msg.toText()}")

    def ClearDiagnostics(self):
        """
        Clears all diagnostics from the session.
        """
        self.diagnostics.clear()

    def ReportDiagnostic(self, message, severity, fileName="", line=0, column=0):
        """
        Records a new diagnostic message.
        """
        # Create a new Diagnostic instance and populate its fields
        diagnostic: Diagnostic = Diagnostic()
        diagnostic.severity = severity
        diagnostic.fileName = fileName
        diagnostic.line = line
        diagnostic.column = column
        diagnostic.message = message
        # Append the diagnostic to the list
        self.diagnostics.append(diagnostic)


class Engine:
    """
    Processes d3i sources, generating syntax and element trees.
    """

    def __init__(self, configuration: Dict[str, str] = {}):
        self.configuration: Dict[str, str] = configuration

    def Build(self, session: Session):
        """
        Builds the d3 by generating syntax and element trees.
        """
        # Create syntax tree from the source
        session.syntaxTree = self.__create_syntax_tree(session.source, session)
        # Create element tree from the syntax tree
        session.main = self.__create_element_tree(session.syntaxTree, session.source, session)
        # Merge contracts into the main contract
        session.main = self.__merge_d3s(session)

        return session.main

    def __create_syntax_tree(self, source: Source, session: Session):
        """
        Generates a syntax tree for the given source.
        """
        # Initialize the lexer and parser for the source content
        lexer = d3iLexer(InputStream(source.content))
        grammar = d3iGrammar(CommonTokenStream(lexer))

        # Set up error handling
        error_listener = Engine.__syntaxErrorListener__(source.fileName, session)
        grammar.removeErrorListeners()
        grammar.addErrorListener(error_listener)

        return grammar.d3()

    def __create_element_tree(self, syntaxTree: d3iGrammar.D3Context, source: Source, session: Session):
        """
        Creates an element tree from the syntax tree.
        """
        # Build elements using a visitor pattern
        visitor = ElementBuilder(source.fileName)
        _d3: d3 = visitor.visit(syntaxTree)
        # Store the d3 in the session
        session.all[source.fileName] = _d3

        # Process imported d3s
        for _import in _d3.imports:
            import_path = os.path.normpath(os.path.join(Path(source.fileName).parent, _import.name.replace(".", "/") + ".d3"))
            # Import only if not already processed
            if import_path not in session.all:
                imported_d3 = self.__import_d3(import_path, _import, session)
            else:
                imported_d3 = session.all[import_path]
            _import.d3 = imported_d3

        return _d3

    def __import_d3(self, import_path: str, _import: import_, session: Session):
        """
        Imports a d3 from a given path.
        """
        # Check if the file exists
        if not os.path.exists(import_path):
            session.ReportDiagnostic(
                f"import '{import_path}' file not found",
                Diagnostic.Severity.Error,
                _import.fileName,
                _import.line,
                _import.column
            )
            return None
        # Create source from file and build its syntax and element trees
        import_source = Source.CreateFromFile(import_path)
        import_syntaxTree = self.__create_syntax_tree(import_source, session)
        imported_d3 = self.__create_element_tree(import_syntaxTree, import_source, session)

        return imported_d3

    def __merge_d3s(self, session: Session):
        """
        Merges all imported d3s into the main d3.
        """
        for imported_d3 in session.all.values():
            # Skip the main d3
            if imported_d3 is session.main:
                continue

            for imported_domain in imported_d3.domains:
                # set parent, regadless will be merged or not
                imported_domain.parent = session.main

                # Find or create the domain in the main d3
                domain_already: domain = self.__find_domain_by_name(session, imported_domain.name)
                if domain_already is None:
                    session.main.domains.append(imported_domain)
                else:
                    # merge to merged
                    for imported_context in imported_domain.contexts:
                        # find context in merged
                        context_already: context = self.__find_context_by_name(domain_already.contexts, imported_context.name)
                        if (context_already == None):
                            domain_already.contexts.append(imported_context)
                        else:
                            # merge enum
                            for imported_enum in imported_context.enums:
                                imported_enum.parent = context_already
                                context_already.enums.append(imported_enum)

                            # merge value_object
                            for imported_value_object in imported_context.value_objects:
                                imported_value_object.parent = context_already
                                context_already.value_objects.append(imported_value_object)

                            # merge composite
                            for imported_composit in imported_context.composites:
                                imported_composit.parent = context_already
                                context_already.composites.append(imported_composit)

                            # merge aggregate
                            for imported_aggregate in imported_context.aggregates:
                                imported_aggregate.parent = context_already
                                context_already.aggregates.append(imported_aggregate)

                            # merge view
                            for imported_view in imported_context.views:
                                imported_view.parent = context_already
                                context_already.views.append(imported_view)

                            # merge repository
                            for imported_repository in imported_context.repositories:
                                imported_repository.parent = context_already
                                context_already.repositories.append(imported_repository)

                            # merge acl
                            for imported_acl in imported_context.acls:
                                imported_acl.parent = context_already
                                context_already.acls.append(imported_acl)

                            # merge service
                            for imported_service in imported_context.services:
                                imported_service.parent = context_already
                                context_already.services.append(imported_service)

                            # merge interface
                            for imported_interface in imported_context.interfaces:
                                imported_interface.parent = context_already
                                context_already.interfaces.append(imported_interface)

        return session.main

    @staticmethod
    def get_current_scope(element: base_element) -> IScope:
        current_scope = element
        while True:
            if isinstance(current_scope, IScope):
                break
            elif (current_scope == None):
                break
            current_scope = current_scope.parent

        return current_scope

    @staticmethod
    def has_version_int_member(obj):
        return hasattr(obj, 'version') and isinstance(getattr(obj, 'version'), int)

    @staticmethod
    def get_referenced_element(parent: base_element, name: qualified_name) -> IScope:
        element, message = Engine.get_referenced_element_with_message(parent, name)
        return element

    @staticmethod
    def get_referenced_element_with_message(parent: base_element, name: qualified_name) -> IScope:
        scope = Engine.get_current_scope(parent)

        first_part: str = name.names[0]
        version_candidate: str = None
        if (len(name.names) > 1):
            version_candidate = name.names[1]

        rest_name_index = 1
        # go up until we find the element for the first part of the name vit version is has it
        element = None
        while True:
            if (scope == None ):
                break

            # is the scope that has a child with the name we are looking for
            if (isinstance(scope, IScope)):
                for child in scope.getChildren():
                    if (Engine.has_version_int_member(child) == True):
                        if (child.name == name.names[0] and f"v{child.version}" == version_candidate):
                            element = child
                            rest_name_index = rest_name_index + 1  # skip version
                            break
                    elif (child.name == name.names[0]):
                        element = child
                        break

                if (element != None):
                    break

            if( hasattr(scope, 'parent') == True):
                scope = scope.parent
            else:
                scope = None

        if (element == None):
            return None, f"The first part of the referenced name '{name.names[0]}' cannot be resolved."

        # processing the rest of the name part if exist
        rest_names = name.names[rest_name_index:]
        i: int = 0
        while i < len(rest_names):
            name_part = rest_names[i]
            if (isinstance(element, IScope) == False):
                return None, f"The referenced name '{name.names[0]}' cannot have an expected child: '{name_part}'."

            scope: IScope = element
            if i + 1 < len(rest_names):
                version_candidate = rest_names[i + 1]

            element = None
            for child in scope.getChildren():
                if (Engine.has_version_int_member(child)):
                    if (f"v{child.version}" == version_candidate):
                        element = child
                        i = i + 1  # skip version
                        break
                elif (child.name == name_part):
                    element = child
                    break

            if (element == None):
                if (Engine.has_version_int_member(scope)):
                    name = f"{scope.name} version {scope.version}"
                else:
                    name = scope.name
                return None, f"The referenced name '{name}' does not have an expected child: '{name_part}'."

            i = i + 1

        return element, "ok"

    @staticmethod
    def __find_domain_by_name(session: Session, name):
        for domain in session.main.domains:
            if (domain.name == name):
                return domain

        return None

    @staticmethod
    def __find_context_by_name(contexts: List[context], name):
        for context in contexts:
            if (context.name == name):
                return context

        return None

    class __syntaxErrorListener__(ErrorListener):
        """
        Custom error listener for syntax errors during parsing.
        """

        def __init__(self, fileName, session: Session):
            super(Engine.__syntaxErrorListener__, self).__init__()
            self.fileName = fileName
            self.session = session

        def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
            # Report syntax error as a diagnostic
            self.session.ReportDiagnostic(
                message,
                Diagnostic.Severity.Error,
                self.fileName,
                line,
                column
            )


class Diagnostic:
    """
    Represents a diagnostic message with severity, location, and text.
    """

    def __init__(self):
        self.severity: Diagnostic.Severity = Diagnostic.Severity.Message
        self.fileName: str = None
        self.line: int = None
        self.column: int = None
        self.message: int = None

    def toText(self):
        """
        Converts the diagnostic to a textual representation.
        """
        return f"{self.fileName}({self.line},{self.column}): {self.severity} :{self.message}"

    class Severity(Enum):
        """
        Enumeration of diagnostic severity levels.
        """
        Message = 1
        Warning = 2
        Error = 3
