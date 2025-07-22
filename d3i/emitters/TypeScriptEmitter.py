from __future__ import annotations
import io
from typing import Dict
from typing import List
from typing import NamedTuple
from d3i.elements.Elements import *
from d3i.Engine import *
from d3i.emitters.utils import *


def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    """
    Creates an instance of TsClient, initializes it with the output directory and configuration,
    and then emits the dotnet code based on the provided session.
    """
    tsEmitter = TypeScriptEmitter(output_dir, configuration)

    # Generate the .ts code for the session
    results: List[ts_code] = tsEmitter.Emit(session)

    for code in results:
        dir_name = os.path.dirname(code.fullPath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(code.fullPath, "w", encoding='utf-8') as file:
            file.write(code.content)

    return results


class TypeScriptEmitter:
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        """
        Initializes the TypeScriptEmitter instance with the provided output directory and configuration.
        """
        self.configuration: ts_configuration = ts_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        """
        Emits the TypeScript code based on d3 file
        """
        result: List[ts_code] = []
        code: ts_code = None

        # Iterate over all domain in the session
        for domain in session.main.domains:
            output_path: str = self.configuration.output_dir
            for context in domain.contexts:

                # Process all enum in the context
                for enum in context.enums:
                    pass  # no client code emmited

                # Process all value_object in the context
                for valueobject in context.value_objects:
                    pass  # no client code emmited

                # Process all composite in the context
                for composite in context.composites:
                    pass  # no client code emmited

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    for enum in aggregate.enums:
                        pass  # no client code emmited

                    for valueobject in aggregate.value_objects:
                        pass  # no client code emmited

                    for aggregate_entity in aggregate.internal_entities:
                        pass  # no client code emmited

                # Process all view in the context
                for view in context.views:
                    pass  # no client code emmited

                # Process all acl in the context
                for acl in context.acls:
                    pass  # no client code emmited

                # Process all service in the context
                for service in context.services:
                    pass  # no client code emmited

                # Process all inerface in the context
                for interface in context.interfaces:
                    # Service interface for DTOs
                    code = self.beginFile(output_path, interface, "types", postfix=f"_v{interface.version}")
                    code = self.interfaceTypesText(interface, code)
                    code = self.endFile(code)
                    result.append(code)
                    # Service: GRPC controller
                    if (utils.isPublishedOn(interface, "grpc") == True):
                        pass  # no client code emmited
                    # Service: GRPC InternalClient for service-service communication
                    if (utils.isPublishedOnInternal(interface, "grpc") == True):
                        pass  # no client code emmited
                    # Client: GRPC public client for client-service communication
                    apiCollectionName: str = utils.isPublishedOnPublic(interface, "grpc")
                    if (apiCollectionName != None):
                        pass  # no client code emmited
                    # Service: REST controller
                    if (utils.isPublishedOn(interface, "rest") == True):
                        pass  # no client code emmited
                    # Service: REST InternalClient for service-service communication
                    if (utils.isPublishedOnInternal(interface, "rest") == True):
                        pass  # no client code emmited
                    # Client: REST public client for client-service communication
                    apiCollectionName: str = utils.isPublishedOnPublic(interface, "rest")
                    if (apiCollectionName != None):
                        code = self.beginFile(output_path, interface, "api", postfix=f"_v{interface.version}.RestClient")
                        code = self.interfaceRestPublicClientText(interface, code, apiCollectionName)
                        code = self.endFile(code)
                        result.append(code)

        return result

    def fileHeader(self) -> str:
        """
        Returns the file header to be included in the generated .cs files.
        """
        return self.configuration.fileHeader

    def defaultImports(self) -> str:
        """
        Returns the default 'import' statements to be included in the .cs files.
        """
        import_statements: List[str] = []

        for _import in self.configuration.defaultImports:
            import_statements.append(f"import {_import};")

        return "\n".join(import_statements) + "\n"

    def beginFile(self, output_path: str, element: base_element, subDirectoryName: str, prefix: str = "", postfix: str = "", current_namespace=None) -> ts_code:
        buffer = io.StringIO()
        domain: domain = element.getDomain()
        context: context = element.getContext()
        aggregate: aggregate = element.getAggregate()

        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultImports())
        buffer.write("<ADDITIONAL_IMPORTS>")
        buffer.write("\n")

        # set current_namespace
        if (current_namespace == None):
            current_namespace: str = f"{domain.name}.{context.name}"
            if (aggregate != None):
                current_namespace = current_namespace + f".{aggregate.name}"

        code: ts_code = ts_code(output_path, [subDirectoryName, domain.name, context.name], prefix + element.name + postfix, current_namespace)
        code.content = buffer.getvalue()
        return code

    def endFile(self, code: ts_code) -> ts_code:
        buffer = io.StringIO()
        code.content += buffer.getvalue()

        buffer = io.StringIO()
        for _import in code.imports:
            buffer.write(f"import {_import};\n")

        code.content = code.content.replace("<ADDITIONAL_IMPORTS>", buffer.getvalue())
        return code

    def interfaceTypesText(self, interface: interface, code: ts_code, indent: int = 0) -> ts_code:
        """
        Generates the TypeScript rest Public client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        for enum in interface.enums:
            code = self.enumText(enum, code, indent)

        for dto in interface.dtos:
            code = self.dtoText(dto, code, indent)

        code.content += buffer.getvalue()
        return code

    def interfaceRestPublicClientText(self, interface: interface, code: ts_code, apiCollectionName:str, indent: int = 0) -> ts_code:
        """
        Generates the TypeScript rest Public client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        # add imports
        code.imports.add( f"{{ {apiCollectionName}RestClient }} from \"../../{apiCollectionName}RestClient\"")
        code.imports.add( f"* as {versionedName} from \"../../../types/{interface.getDomain().name}/{interface.getContext().name}/{versionedName}\"")

        buffer = io.StringIO()
        buffer.write(f"const apiClient = {apiCollectionName.upper()}RestClient.getInstance().apiClient\n");
        buffer.write("\n")
        buffer.write(f"{utils.tab(indent)}export const {interface.name} = {{\n")
        buffer.write(f"{utils.tab(indent+1)}V{interface.version}: {{\n")

        

        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(self.documentLines(operation, indent+2))
            buffer.write(f"{utils.tab(indent+1)}async {operation.name}(\n{utils.tab(indent+2)}")
            buffer.write(f",\n{utils.tab(indent+2)}".join([param.name + ":" + self.typeText(param.type, code,fullName=True) for param in operation.operation_params]))
            buffer.write(f"{utils.tab(indent+1)}) : ")
            if (operation.operation_return != None ):
                buffer.write(f"Promise<{self.typeText(operation.operation_return.type, code,fullName=True)}>\n")
            else:
                buffer.write("Promise<{}>\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+1)}}}\n")
            buffer.write(f"{utils.tab(indent+1)},\n")

        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def enumText(self, enum: enum, code: ts_code, indent: int = 1) -> ts_code:
        """
        Generates the typescript code for an enum.
        """
        buffer = io.StringIO()
        buffer.write("\n")
        # Add documentation lines for the enum
        buffer.write(self.documentLines(enum, indent))
        # Write the enum declaration with indentation
        buffer.write(f"{utils.tab(indent)}export enum {enum.name} {{\n")
        # Loop through each enum element and generate code for each
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent+1))
            # Write each enum element value
            buffer.write(f"{utils.tab(indent+1)}{enum_element.value},\n")
            if (len(enum_element.document_lines) > 0):
                buffer.write("\n")

        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def dtoText(self, dto: dto, code: ts_code, indent: int = 1) -> ts_code:
        """
        Generates the .NET code for an data object
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        for inherit in dto.inherits:
            base = Engine.get_referenced_element(dto.parent, inherit)
            if (isinstance(base, composite) == True):
                utils.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            else:
                inherit_names.append(inherit.getText())

        buffer = io.StringIO()

        # Add documentation lines for the composite
        buffer.write(self.documentLines(dto, indent))
        # Write the data class declaration with indentation
        buffer.write(f"{utils.tab(indent)}export interface {dto.name} {{\n")
        # flush current text
        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        hasChild: bool = False
        if (len(dto.enums) > 0 or len(dto.dtos) > 0):
            hasChild = True

        # Loop through each coposite members and generate code for each
        for base_composite in base_composites:
            buffer.write(f"{utils.tab(indent+1)}//region I{base_composite.name}\n")

            if (hasChild == False):
                if (len(base_composite.enums) > 0 or len(base_composite.dtos) > 0):
                    hasChild = True

            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member, code, indent+1))
            buffer.write(f"{utils.tab(indent+1)}//endregion I{base_composite.name}\n\n")

        # Loop through each valueobject members and generate code for each
        for member in dto.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member, code, indent+1))

        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"\n")

        if (hasChild == True):
            buffer.write(f"{utils.tab(indent)}export namespace {dto.name} {{\n")
            code.content += buffer.getvalue()
            buffer.seek(0)
            buffer.truncate(0)
            # write internal enums if Any
            for child_enum in dto.enums:
                code = self.enumText(child_enum, code, indent+1)

            for child_dto in dto.dtos:
                code = self.dtoText(child_dto, code, indent+1)

            buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def propertyText(self, member: hinted_base_element, code: ts_code, indent: int) -> str:
        return f"{utils.tab(indent)}{member.name}:{self.typeText(member.type, code)};\n"

    def typeText(self, type: type, code: ts_code, *, fullName: bool = False) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type, code, fullName=fullName)
            case type.Kind.Reference:
                return self.typeTextReference(type, code, fullName=fullName)
            case type.Kind.List:
                return self.typeTextList(type, code, fullName=fullName)
            case type.Kind.Map:
                return self.typeTextMap(type, code, fullName=fullName)

    def typeTextPrimitive(self, type: primitive_type, code: ts_code, *, fullName: bool = False) -> str:
        """
        Converts a primitive type to its ts representation.
        """
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "object"
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                code.imports.add("Decimal from \"decimal.js\"")
                return "Decimal"
            case primitive_type.PrimtiveKind.Float:
                return "double"
            case primitive_type.PrimtiveKind.Date:
                return "string"
            case primitive_type.PrimtiveKind.Time:
                return "string"
            case primitive_type.PrimtiveKind.DateTime:
                return "Date"
            case primitive_type.PrimtiveKind.String:
                return "string"
            case primitive_type.PrimtiveKind.I18NString:
                return "i18nstring"
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes:
                return "byte[]"
            case primitive_type.PrimtiveKind.Stream:
                return "Stream"

    def typeTextReference(self, type: reference_type, code: ts_code, fullName: bool = False) -> str:
        referenced_element: base_element = Engine.get_referenced_element(type.parent, type.reference_name)
        if (referenced_element != None and code.current_namespace != f"{referenced_element.getDomain().name}.{referenced_element.getContext().name}"):
            code.imports.add(f"{referenced_element.getDomain().name}.{referenced_element.getContext().name}")

        if (fullName == True):
            return code.getTsFullName(referenced_element)
        else:
            return code.getTsName(referenced_element)

    def typeTextList(self, type: list_type, code: ts_code, fullName: bool = False) -> str:
        return f"{self.typeText(type.item_type, code, fullName=fullName)}[]"

    def typeTextMap(self, type: map_type, code, fullName: bool = False) -> str:
        return f"Dictionary<{self.typeText(type.key_type, code, fullName)},{self.typeText(type.value_type, code, fullName)}>"

    def documentLines(self, hinted_element: hinted_base_element, indent: int = 1) -> str:
        """
        Generates documentation lines for the provided element.
        """
        buffer = io.StringIO()
        # Loop through each document line of the hinted element
        for document_line in hinted_element.document_lines:
            # Write the documentation line with the specified indentation
            buffer.write(f"{utils.tab(indent)}///{document_line}")
            buffer.write("\n")
        return buffer.getvalue()


class ts_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir

        self.__read_fileHeader(configuration)
        self.__read_defaultImports(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """
// <auto-generated>
//     This code was generated by d3i.interpreter
//
//     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
// </auto-generated>"""

        if "typescript.file_header_lines" in configuration:
            value = configuration["typescript.file_header_lines"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.fileHeader = "\n".join(value)

    def __read_defaultImports(self, configuration: Dict[str, str]):
        self.defaultImports: List[str] = []
        if "typescript.default_imports" in configuration:
            value = configuration["typescript.default_imports"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultImports = value


class ts_code:
    def __init__(self, output_path: str, subdirs: List[str], name: str, current_namespace: str):
        """
        Initializes a ts_code instance with the file path, file name, and content.
        """
        self.output_path = output_path
        self.fileName: str = name + ".ts"
        self.fullPath: str = os.path.join(output_path + "/".join(subdirs), self.fileName)
        self.current_namespace: str = current_namespace
        self.imports: set[str] = set()
        self.content: str = ""

    def getTsFullName(self, element: base_element) -> str:
        dotnetNames: List[str] = []
        while True:
            if (element == None or isinstance(element, d3)):
                break
            if (Engine.has_version_int_member(element)):
                dotnetNames.insert(0, f"{element.name}_v{element.version}")
            else:
                dotnetNames.insert(0, element.name)

            element = element.parent

        current_namespaces = self.current_namespace.split(".")

        if dotnetNames[:len(current_namespaces)] == current_namespaces:
            dotnetNames = dotnetNames[len(current_namespaces):]

        return ".".join(dotnetNames)


    def getTsName(self, element: base_element) -> str:
        dtoNames: List[str] = []
        parent = element.parent
        while True:
            if (parent == None or isinstance(parent, dto) == False ):
                break
            
            dtoNames.insert(0, parent.name)
            parent = parent.parent

        dtoNames.append(element.name)

        return ".".join(dtoNames)
