#import os
import io
from typing import Dict
from typing import List
from d3i.elements.Elements import *
from d3i.Engine import *

def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    """
    Creates an instance of ProtoEmmiter, initializes it with the output directory and configuration,
    and then emits the protobuf code based on the provided session.
    """
    protoEmitter = ProtoEmitter(output_dir, configuration)

    # Generate the .NET code for the session
    results: List[proto_code] = protoEmitter.Emit(session)

    for code in results:
        dir_name = os.path.dirname(code.fullPath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(code.fullPath, "w") as file:
            file.write(code.content)

    return results


class ProtoEmitter:
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        """
        Initializes the ProtoEmmiter instance with the provided output directory and configuration.
        """
        self.configuration: protobuf_configuration = protobuf_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        """
        Emits the protobuf codes based on d3 file
        """
        result: List[proto_code] = []

        # Iterate over all domain in the session
        for domain in session.main.domains:
            output_path: str = self.configuration.output_dir
            for context in domain.contexts:
                imports:set[str] = set()

                # Process all enum in the context
                for enum in context.enums:
                    content: str = self.beginFile([domain.name, context.name], context.name, imports )
                    content += self.enumText(enum, imports)
                    content = self.endFile( content, imports )
                    result.append(proto_code(output_path, [domain.name, context.name, "models"], enum.name, content))

                # Process all value_object in the context
                for valueobject in context.value_objects:
                    content: str = self.beginFile([domain.name, context.name], context.name, imports)
                    content += self.valueobjectText(valueobject, imports)
                    content = self.endFile( content, imports )
                    result.append(proto_code(output_path, [domain.name, context.name, "models"], valueobject.name, content))

                # Process all composite in the context
                for composite in context.composites:
                    # composite contetn is directly inculded in the valueobject/dto/entity no separate file is neccessary
                    pass

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    for enum in aggregate.enums:
                        content: str = self.beginFile([domain.name, context.name], aggregate.name, imports)
                        content += self.enumText(enum, imports)
                        content = self.endFile( content, imports )
                        result.append(proto_code(output_path, [domain.name, context.name, "models"], enum.name, content ))

                    for valueobject in aggregate.value_objects:
                        content: str = self.beginFile([domain.name, context.name], aggregate.name, imports)
                        content += self.valueobjectText(valueobject, imports)
                        content = self.endFile( content, imports )
                        result.append(proto_code(output_path, [domain.name, context.name, "models"], valueobject.name, content ))

                    for aggregate_entity in aggregate.internal_entities:
                        content: str = self.beginFile([domain.name, context.name], aggregate.name, imports)
                        content += self.entityText(aggregate_entity.entity, imports)
                        content = self.endFile( content, imports )
                        result.append(proto_code(output_path, [domain.name, context.name, "models"], aggregate_entity.entity.name, content ))

                # Process all view in the context
                for view in context.views:
                    content: str = self.beginFile([domain.name, context.name], imports)
                    content += self.viewText(view, imports)
                    content = self.endFile( content, imports)
                    result.append(proto_code(output_path, [domain.name, context.name, "models"], view.name, content))

                # Process all acl in the context
                for acl in context.acls:
                    content = self.beginFile([domain.name, context.name], acl.name, imports )
                    content += self.aclText(domain, context, acl, imports)
                    content = self.endFile( content, imports )
                    result.append(proto_code(output_path, [domain.name, context.name, acl.name, "Service"], acl.name, content ))

                    # proto service file
                    #content = self.aclGrpcControllerFile(domain, context, acl )
                    #result.append(proto_code(output_path, [domain.name, context.name, acl.name, "Service/controllers"], acl.name+"GrpcController", content))

                # Process all service in the context
                for service in context.services:
                    content = self.beginFile([domain.name, context.name], service.name, imports )
                    content += self.serviceText(domain, context, service, imports)
                    content = self.endFile( content, imports )
                    result.append(proto_code(output_path, [domain.name, context.name, "Service"], service.name, content, ".proto"))

                    # proto service file
                    #content = self.serviceGrpcControllerFile(domain, context, service)
                    #result.append(proto_code(output_path, [domain.name, context.name, service.name, "Service/controllers"], service.name+"GrpcController", content))

                # Process all inerface in the context
                for interface in context.interfaces:
                    content = self.beginFile([domain.name, context.name], service.name, imports )
                    content += self.interfaceText(domain, context, interface, imports)
                    content = self.endFile( content, imports )
                    result.append(proto_code(output_path, [domain.name, context.name, interface.name, "Service"], interface.name, content))

                    # proto service file
                    #content = self.interfaceGrpcControllerFile(domain, context, interface, indent=1)
                    #result.append(proto_code(output_path, [domain.name, context.name, interface.name, "Service/controllers"], interface.name+"GrpcController", content))

        return result

    def fileHeader(self) -> str:
        """
        Returns the file header to be included in the generated .proto files.
        """
        return self.configuration.fileHeader

    def defaultImports(self) -> str:
        """
        Returns the default 'import' statements to be included in the .proto files.
        """
        import_statements: List[str] = []

        for import_file in self.configuration.defaultImports:
            import_statements.append(f"import {import_file};")

        return "\n".join(import_statements) + "\n"

    def beginFile(self, names: List[str], packageName:str, imports:set[str]) -> str:
        buffer = io.StringIO()

        # proto 3 syntax
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write("syntax = \"proto3\";")
        buffer.write("\n")

        # namespaces
        buffer.write("\n")
        buffer.write(f"option csharp_namespace = \"{".".join(names)}\";")
        buffer.write("\n")    
        buffer.write(f"option java_outer_classname = \"{names[-1]}\";\n")
        buffer.write(f"option java_package = \"com.{packageName}\";\n" )
        buffer.write(f"option java_multiple_files = true;\n" )
                     
        # package
        buffer.write("\n")
        buffer.write(f"package {packageName}Package;")
        buffer.write("\n")

        # make a placeholders for additional imports
        imports.clear()
        buffer.write("<ADDITIONAL_IMPORTS>")
        buffer.write("\n")
        return buffer.getvalue()

    def endFile(self, content:str, imports:set[str] ):
        buffer = io.StringIO()
        sorted_imports: list[str] = sorted(imports)
        for _import in sorted_imports:
            buffer.write(f"import \"{_import}\";\n")
        
        content = content.replace( "<ADDITIONAL_IMPORTS>", buffer.getvalue() )
        return content

    def enumText(self, enum: enum, imports:set[str], indent: int = 0):
        """
        Generates the proto code for an enum.
        """
        buffer = io.StringIO()
        buffer.write("\n")
        # Add documentation lines for the enum
        buffer.write(self.documentLines(enum, indent))
        # Write the enum declaration with indentation
        buffer.write(f"{self.tab(indent)}enum {enum.name}\n")
        buffer.write(f"{self.tab(indent)}{{\n")
        # Loop through each enum element and generate code for each
        value:int = 0
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent+1))
            # Write each enum element value
            buffer.write(f"{self.tab(indent+1)}{enum_element.value} = {value};\n")
            if(len(enum_element.document_lines)>0):
                buffer.write("\n")
            value = value + 1

        buffer.write(f"{self.tab(indent)}}}\n")
        return buffer.getvalue()

    def collectBaseRecursive(self, base: composite, bases: List[base_element]):
        bases.insert(0, base)

        for inherit in base.inherits:
            base_base = utils.get_referenced_element(base.parent, inherit)
            if (base_base != None):
                self.collectBaseRecursive(base_base, bases)

    def collectBaseCompositsRecursive(self, base_composite: composite, base_composites: List[composite]):
        base_composites.insert(0, base_composite)

        for inherit in base_composite.inherits:
            base = utils.get_referenced_element(base_composite.parent, inherit)
            if (isinstance(base, composite) == True):
                self.collectBaseCompositsRecursive(base, base_composites)

    def valueobjectText(self, _valueobject: value_object, imports:set[str], indent: int = 0):
        """
        Generates the proto code for an value_object
        """
        bases: List[internal_scoped_base_element] = []
        for inherit in _valueobject.inherits:
            base = utils.get_referenced_element(_valueobject.parent, inherit)
            if (isinstance(base, base) == True):
                self.collectBaseRecursive(base, bases)

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(_valueobject, indent))
        # Write the value_object declaration with indentation
        buffer.write(f"{self.tab(indent)}message {_valueobject.name} {{\n")

        # Loop through each coposite members and generate code for each
        for base in bases:
            buffer.write(f"{self.tab(indent+1)} // unfold begin: {base.name}\n")

            # write internal enums if Any
            if(base.withEnum== True):
                for enum in base.enums:
                    buffer.write(self.enumText( enum, imports, indent+1))

            # write internal value object if Any
            if(base.withValueObject== True):
                for value_object in base.value_objects:
                    buffer.write(self.valueobjectText( value_object, imports, indent+1))

            index:int = 1
            for member in base.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.protoMemberText(member.name, member.type, index, indent+1))
                index = index + 1
            buffer.write(f"{self.tab(indent+1)}// unfold end {base.name}\n\n")

        # write internal enums if Any
        if( _valueobject.withEnum==True):
            for enum in _valueobject.enums:
                buffer.write( self.enumText( enum, imports, indent))

        # write internal valueobjects if Any
        if( _valueobject.withValueObject==True):
            for _valueobject in _valueobject.value_objects:
                buffer.write( self.valueobjectText( _valueobject, imports, indent))

        # Loop through each valueobject members and generate code for each
        index:int = 1
        for member in _valueobject.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.protoMemberText(member.name, member.type, imports, index, indent+1))
            index = index + 1

        buffer.write(f"{self.tab(indent)}}}\n")

        return buffer.getvalue()
    
    def entityText(self, _entity: entity, imports:set[str], indent: int = 0):
        """
        Generates the proto code for an entity
        """
        bases: List[internal_scoped_base_element] = []
        for inherit in _entity.inherits:
            base = utils.get_referenced_element(_entity.parent, inherit)
            if (isinstance(base, base) == True):
                self.collectBaseRecursive(base, bases)

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(_entity, indent))
        # Write the entity declaration with indentation
        buffer.write(f"{self.tab(indent)}message {_entity.name} {{\n")

        # Loop through each members and generate code for each
        for base in bases:
            buffer.write(f"{self.tab(indent+1)} // unfold begin: {base.name}\n")

            # write internal enums if Any
            if(base.withEnum== True):
                for enum in base.enums:
                    buffer.write(self.enumText( enum, imports, indent+1))

            # write internal value object if Any
            if(base.withValueObject== True):
                for value_object in base.value_objects:
                    buffer.write(self.valueobjectText( value_object, imports, indent+1))

            index:int = 1
            for member in base.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.protoMemberText(member.name, member.type, imports, index, indent+1))
                index = index + 1
            buffer.write(f"{self.tab(indent+1)}// unfold end {base.name}\n\n")

        # write internal enums if Any
        if( _entity.withEnum==True):
            for enum in _entity.enums:
                buffer.write( self.enumText( enum, imports, indent))

        # write internal valueobjects if Any
        if( _entity.withValueObject==True):
            for _entity in _entity.value_objects:
                buffer.write( self.valueobjectText( _entity, imports, indent ))

        # Loop through each valueobject members and generate code for each
        index:int = 1
        for member in _entity.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.protoMemberText(member.name, member.type, imports, index, indent+1))
            index = index + 1

        buffer.write(f"{self.tab(indent)}}}\n")

        return buffer.getvalue()

    def aclText(self, domain: domain, context: context, acl: acl, imports:set[str], indent: int = 1):
        return self.protoServiceText( domain, context, acl, acl.name, acl.operations, imports, indent )

    def serviceText(self, domain: domain, context: context, service: service, imports:set[str], indent: int = 1):
        return self.protoServiceText( domain, context, service, service.name, service.operations, imports, indent )

    def interfaceText(self, domain: domain, context: context, interface: interface, imports:set[str], indent: int = 1):
        return self.protoServiceText( domain, context, interface, interface.name, interface.operations, imports, indent )

    def protoServiceText(self, domain: domain, context: context, element: hinted_base_element, elementName: str, operations: List[operation], imports:set[str], indent: int = 1):
        """
        Generates the proto service file, with rpc functions and request response messages text for element
        """
        imports.add("google/protobuf/empty.proto")
        imports.add("servicekit_error.proto")

        buffer = io.StringIO()
        # Add documentation lines for the service
        buffer.write(self.documentLines(element, indent))
        buffer.write("\n")
        buffer.write(f"service {elementName} {{\n")
        # Loop through each operations and generate code for each
        for operation in operations:
            # Write each operation as RPC call
            buffer.write(self.documentLines(operation, indent+1))
            buffer.write(f"{self.tab(indent+1)}rpc {operation.name} ({operation.name}Request) returns ({operation.name}Response);\n")
        buffer.write("\n")
        buffer.write(f"}}")

        # Add messages based on operations
        for operation in operations:
            # Request message
            buffer.write(f"\n")
            buffer.write(f"message {operation.name}Request {{\n")
            index: int = 1
            for param in operation.operation_params:
                buffer.write(self.documentLines(param, indent+2))
                buffer.write(f"{self.tab(indent+1)}{self.typeText(param.type, imports)} {param.name} = {index};\n")
            buffer.write(f"}}\n")
            buffer.write(f"\n")

            # Response message
            buffer.write(f"message {operation.name}Response {{\n")
            buffer.write(f"{self.tab(indent+1)}oneof result {{\n")
            if (len(operation.operation_returns) == 0):
                buffer.write(f"{self.tab(indent+2)}google.protobuf.Empty Success = 1;\n")
                buffer.write(f"{self.tab(indent+2)}servicekit.protobuf.Error Error = 2;\n")
            else:
                index: int = 1
                for returns in operation.operation_returns:
                    buffer.write(f"{self.tab(indent+2)}{self.typeText(returns.type, imports)} Value{index} = {index};\n")
                    index = index+1
                buffer.write(f"{self.tab(indent+2)}servicekit.protobuf.Error Error = {index};\n")

            buffer.write(f"{self.tab(1)}}}\n")
            buffer.write(f"}}\n")

        return buffer.getvalue()

    def protoMemberText(self, member_name: str, type: type, imports:set[str], index:int, indent: int):
        buffer = io.StringIO()
        buffer.write(f"{'\t'*indent}{self.typeText(type, imports)} {member_name} = {index};\n")
        return buffer.getvalue()

    def typeText(self, type: type, imports:set[str]):
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type,imports)
            case type.Kind.List:
                return self.typeTextList(type,imports)
            case type.Kind.Map:
                return self.typeTextMap(type,imports)

    def typeTextPrimitive(self, type: primitive_type):
        """
        Converts a primitive type to its protobuf representation.
        """
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "object"
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                return "string"  # must be converted
            case primitive_type.PrimtiveKind.Float:
                return "double"
            case primitive_type.PrimtiveKind.Date:
                return "DateOnly"
            case primitive_type.PrimtiveKind.Time:
                return "TimeOnly"
            case primitive_type.PrimtiveKind.DateTime:
                return "DateTime"
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

    def typeTextReference(self, type: reference_type, imports:set[str]):
        referenced_element = utils.get_referenced_element(type.parent, type.reference_name)
        if(referenced_element != None):
            pass
        return type.reference_name.getText()

    def typeTextList(self, type: list_type, imports:set[str]):
        return f"repeated {self.typeText(type.item_type, imports)}"

    def typeTextMap(self, type: map_type, imports:set[str]):
        return f"map<{self.typeText(type.key_type, imports)},{self.typeText(type.value_type, imports)}>"

    def tab(self, indent=1):
        return '\t'*indent

    def documentLines(self, hinted_element: hinted_base_element, indent: int = 1):
        """
        Generates documentation lines for the provided element.
        """
        buffer = io.StringIO()
        # Loop through each document line of the hinted element
        for document_line in hinted_element.document_lines:
            # Write the documentation line with the specified indentation
            buffer.write(f"{self.tab(indent)}///{document_line}")
            buffer.write("\n")
        return buffer.getvalue()


class utils:
    @staticmethod
    def get_referenced_element(parent: base_element, name: qualified_name) -> IScope:

        scope = utils.__get_current_scope(parent)
        element = None
        # go up until we find the element for the first part of the name
        while True:
            if (scope == None):
                break

            if (isinstance(scope, IScope) == True):
                # is the scope that has a child with the name we are looking for
                for child in scope.getChildren():
                    if (child.name == name.names[0]):
                        element = child
                        break

            if (element != None):
                break

            scope = scope.parent

        if (element == None):
            return None

        # processing the rest of the name part if exist
        for name_part in name.names[1:]:
            if (isinstance(element, IScope) == False):
                return None

            scope: IScope = element
            element = None
            for child in scope.getChildren():
                if (child.name == name_part):
                    element = child

            if (element == None):
                return None

        return element

    def __get_current_scope(element: base_element) -> IScope:
        current_scope = element
        while True:
            if isinstance(current_scope, IScope):
                break
            elif (current_scope == None):
                break
            current_scope = current_scope.parent

        return current_scope


class protobuf_configuration:
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

        if "protobuf.file_header_lines" in configuration:
            value = configuration["protobuf.file_header_lines"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.fileHeader = "\n".join(value)

    def __read_defaultImports(self, configuration: Dict[str, str]):
        self.defaultImports: List[str] = []
        if "protobuf.default_imports" in configuration:
            value = configuration["protobuf.default_imports"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultImports = value

class proto_code:
    def __init__(self, directory: str, subdirs: List[str], name: str, content: str, extension: str = ".proto"):
        """
        Initializes a proto_code instance with the file path, file name, and content.
        """
        self.fileName: str = name + extension
        self.fullPath: str = os.path.join(directory + "/".join(subdirs), self.fileName)
        self.content: str = content
