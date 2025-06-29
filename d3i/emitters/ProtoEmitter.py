from __future__ import annotations
import io
import os
from pathlib import Path
from typing import Dict
from typing import List
from d3i.elements.Elements import *
from d3i.Engine import *
from d3i.emitters.utils import *


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
        code: proto_code = None

        # Iterate over all domain in the session
        for domain in session.main.domains:
            output_path: str = self.configuration.output_dir
            for context in domain.contexts:

                # Process all inerface in the context
                for interface in context.interfaces:
                    code = self.beginFile(output_path, interface, "Interfaces/Protos")
                    code = self.interfaceText(interface, code)
                    code = self.endFile(code)
                    result.append(code)

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

    def beginFile(self, output_path: str, interface: interface, subDirectoryName: str) -> proto_code:
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        aggregate: aggregate = interface.getAggregate()

        # proto 3 syntax
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write("syntax = \"proto3\";")
        buffer.write("\n")

        # namespaces
        buffer.write("\n")
        buffer.write(f"option csharp_namespace = \"{domain.name}.{context.name}.Protos.{interface.name}_v{interface.version}\";")
        buffer.write("\n")
        buffer.write(f"option java_outer_classname = \"{interface.name}_v{interface.version}\";\n")
        buffer.write(f"option java_package = \"com.{context.name}\";\n")
        buffer.write(f"option java_multiple_files = true;\n")

        # package
        buffer.write("\n")
        if (aggregate == None):
            buffer.write(f"package {domain.name}.{context.name};\n")
        else:
            buffer.write(f"package {domain.name}.{context.name}.{aggregate.name};\n")
        buffer.write("\n")

        # make a placeholders for additional imports
        buffer.write("<ADDITIONAL_IMPORTS>")
        buffer.write("\n")

        code: proto_code = proto_code(output_path, [domain.name, context.name, subDirectoryName], interface.name+f"v{interface.version}")
        code.content = buffer.getvalue()
        return code

    def endFile(self, code: proto_code) -> proto_code:
        buffer = io.StringIO()
        sorted_imports: list[str] = sorted(code.imports)
        for _import in sorted_imports:
            buffer.write(f"import \"{_import}\";\n".replace("\\", "/"))

        code.content = code.content.replace("<ADDITIONAL_IMPORTS>", buffer.getvalue())
        return code

    def enumText(self, enum: enum, code: proto_code, indent: int = 0) -> str:
        """
        Generates the proto code for an enum.
        """
        buffer = io.StringIO()
        buffer.write("\n")
        # Add documentation lines for the enum
        buffer.write(self.documentLines(enum, indent))
        # Write the enum declaration with indentation
        buffer.write(f"{utils.tab(indent)}enum {enum.name} {{\n")
        # Loop through each enum element and generate code for each
        value: int = 0
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent+1))
            # Write each enum element value
            buffer.write(f"{utils.tab(indent+1)}{enum_element.value} = {value};\n")
            if (len(enum_element.document_lines) > 0):
                buffer.write("\n")
            value = value + 1

        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write("\n")

        return buffer.getvalue()

    def dtoText(self, dto: dto, code: proto_code, indent: int = 0) -> str:
        """
        Generates the proto message code for an DTO
        """
        bases: List[internal_scoped_base_element] = []
        for inherit in dto.inherits:
            base = Engine.get_referenced_element(dto.parent, inherit)
            if (base != None):
                utils.collectBaseRecursive(base, bases)

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(dto, indent))
        # Write the value_object declaration with indentation
        buffer.write(f"{utils.tab(indent)}message {dto.name} {{\n")

        index: int = 1
        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// unfold begin: {base.name}\n")

            # write internal enums if Any
            if (base.withEnum == True):
                for child_enum in base.enums:
                    buffer.write(self.enumText(child_enum, code, indent+1))

            if (base.withDto == True):
                for child_dto in dto.dtos:
                    buffer.write(self.dtoText(child_dto, code, indent))

            for member in base.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.protoMemberText(member.name, member.type, code, index, indent+1))
                index = index + 1
            buffer.write(f"{utils.tab(indent+1)}// unfold end {base.name}\n\n")

        # write internal enums if Any
        for child_enum in dto.enums:
            buffer.write(self.enumText(child_enum, code, indent+1))

        # write internal dtos if Any
        for child_dto in dto.dtos:
            buffer.write(self.dtoText(child_dto, code, indent+1))

        # Loop through each valueobject members and generate code for each
        for member in dto.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.protoMemberText(member.name, member.type, code, index, indent+1))
            index = index + 1

        buffer.write(f"{utils.tab(indent)}}}\n\n")

        return buffer.getvalue()

    def interfaceText(self, interface: interface, code: proto_code, indent: int = 0) -> proto_code:
        """
        Generates the proto service file, with rpc functions and request response messages text for element
        """
        code.imports.add("servicekit_error.proto")

        fullname: str = f"{interface.name}_v{interface.version}"

        buffer = io.StringIO()
        # Add documentation lines for the service
        buffer.write(self.documentLines(interface, indent))
        buffer.write(f"{utils.tab(indent)}service {fullname} {{\n")
        # Loop through each operations and generate code for each
        for operation in interface.operations:
            # Write each operation as RPC call
            buffer.write(self.documentLines(operation, indent+1))
            buffer.write(f"{utils.tab(indent+1)}rpc {operation.name}({fullname}_{operation.name}Request) returns ({fullname}_{operation.name}Response);\n")
        buffer.write(f"{utils.tab(indent)}}}")
        buffer.write("\n")

        # Add messages based on operations
        for operation in interface.operations:
            # Request message
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent)}message {fullname}_{operation.name}Request {{\n")
            index: int = 1
            for param in operation.operation_params:
                buffer.write(self.documentLines(param, indent+2))
                buffer.write(f"{utils.tab(indent+1)}{self.typeText(param.type, code)} {param.name} = {index};\n")
                index = index + 1
            buffer.write(f"{utils.tab(indent)}}}\n")
            buffer.write(f"\n")

            # Response message
            buffer.write(f"{utils.tab(indent)}message {fullname}_{operation.name}Response {{\n")
            buffer.write(f"{utils.tab(indent+1)}oneof result {{\n")
            if (operation.operation_return == None):
                code.imports.add("google/protobuf/empty.proto")
                buffer.write(f"{utils.tab(indent+2)}google.protobuf.Empty Success = 1;\n")
                buffer.write(f"{utils.tab(indent+2)}ServiceKit.Protos.Error Error = 2;\n")
            else:
                buffer.write(f"{utils.tab(indent+2)}{self.typeText(operation.operation_return.type, code)} Value = 1;\n")
                buffer.write(f"{utils.tab(indent+2)}ServiceKit.Protos.Error Error = 2;\n")

            buffer.write(f"{utils.tab(indent+1)}}}\n")
            buffer.write(f"{utils.tab(indent)}}}\n")

        # write internal enums if Any
        for enum in interface.enums:
            buffer.write(self.enumText(enum, code, indent))

        # write internal dto if Any
        for dto in interface.dtos:
            buffer.write(self.dtoText(dto, code, indent))

        code.content += buffer.getvalue()
        return code

    def protoMemberText(self, member_name: str, type: type, code: proto_code, index: int, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"{utils.tab(indent)}{self.typeText(type, code)} {member_name} = {index};\n")
        return buffer.getvalue()

    def typeText(self, type: type, code: proto_code) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type, code)
            case type.Kind.List:
                return self.typeTextList(type, code)
            case type.Kind.Map:
                return self.typeTextMap(type, code)

    def typeTextPrimitive(self, type: primitive_type) -> str:
        return grpc_utils.d3iTypeToGrpcRepresentation(type)

    def typeTextReference(self, type: reference_type, code: proto_code) -> str:
        return type.reference_name.getText()

    def typeTextList(self, type: list_type, code: proto_code) -> str:
        return f"repeated {self.typeText(type.item_type, code)}"

    def typeTextMap(self, type: map_type, code: proto_code) -> str:
        return f"map<{self.typeText(type.key_type, code)},{self.typeText(type.value_type, code)}>"

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
    def __init__(self, output_path: str, subdirs: List[str], name: str):
        """
        Initializes a proto_code instance with the file path, file name.
        """
        self.output_path = output_path
        self.fileName: str = name + ".proto"
        self.fullPath: str = os.path.join(output_path + "/".join(subdirs), self.fileName)
        self.imports: set[str] = set()
        self.content: str = ""
