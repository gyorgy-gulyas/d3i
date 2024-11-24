import os
import io
from typing import Dict
from d3i.elements.Elements import *
from d3i.Engine import Session


def DoEmit(session: Session, output_dir: str, args: Dict[str, str]):
    pass


class DotnetEmmiter:
    def __init__(self, configuration: Dict[str, str]):
        self.configuration: dotnet_configuration = dotnet_configuration(configuration)

    def fileHeader(self) -> str:
        return self.configuration.fileHeader

    def defaultUsings(self) -> str:
        using_statements: List[str] = []

        for using in self.configuration.defaultUsings:
            using_statements.append(f"using {using};")

        return "\n".join(using_statements)

    def contextEnumText(self, domain: domain, context: context, enum: enum):
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(f"namespace {domain.name}.{context.name}")
        buffer.write("{")
        buffer.write(f"{self.enumText(enum, indent=1)}")
        buffer.write("}")
        return buffer.getvalue()

    def contextValueObjectText(self, domain: domain, context: context, value_object: value_object):
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("\n")
        buffer.write(f"namespace {domain.name}.{context.name}")
        buffer.write("{")
        buffer.write(f"\t{self.valueObjectText(value_object)}")
        buffer.write("}")
        return buffer.getvalue()

    def enumText(self, enum: enum, indent: int = 1):
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(f"{'\t'*indent}enum {enum.name}")
        buffer.write("{")
        for enum_element in enum.enum_elements:
            buffer.write(f"{'\t'*(indent+1)}{enum_element.value},")
        buffer.write(f"{'\t'*indent}enum {enum.name}")
        return buffer.getvalue()

    def valueObjectText(self, value_object: value_object, indent: int = 1):
        buffer = io.StringIO()
        buffer.write("\n")
        buffer.write(f"{'\t'*indent}enum {enum.name}")
        buffer.write("{")
        for member in value_object.members:
            buffer.write(f"{self.memberText(member.name, member.type, indent+1)},")
        buffer.write(f"{'\t'*indent}enum {enum.name}")
        return buffer.getvalue()

    def memberText(self, member_name: str, type: type, indent: int):
        buffer = io.StringIO()
        buffer.write(f"{'\t'*indent}public {self.typeText(type)} {member_name} {{ get; set; }}")
        return buffer.getvalue()

    def typeText(self, type: type):
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type)
            case type.Kind.List:
                return self.typeTextList(type)
            case type.Kind.Map:
                return self.typeTextMap(type)

    def typeTextPrimitive(self, type: primitive_type, indent: int):
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                return "decimal"
            case primitive_type.PrimtiveKind.Float:
                return "double"
            case primitive_type.PrimtiveKind.Date:
                return "System.DateOnly"
            case primitive_type.PrimtiveKind.Time:
                return "System.TimeOnly"
            case primitive_type.PrimtiveKind.DateTime:
                return "System.DateTime"
            case primitive_type.PrimtiveKind.String:
                return "string"
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes:
                return "byte[]"

    def typeTextReference(self, type: reference_type, indent: int):
        return type.reference_name.getText()

    def typeTextList(self, type: list_type, indent: int):
        return f"System.Generic.List<{self.typeText(type.item_type)}>"

    def typeTextMap(self, type: map_type, indent: int):
        return f"System.Generic.Dictionary<{self.typeText(type.key_type)},{self.typeText(type.value_type)}>"


class utils:
    def __create_folder__(output_dir: str, folder_name: str):
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    def __create_cs_file__(output_dir: str, file_name: str, content: str):
        file_path = os.path.join(output_dir, file_name + ".cs")
        with open(file_path, "w") as file:
            file.write(content)


class dotnet_configuration:
    def __init__(self, configuration: Dict[str, str]):
        self.__init_fileHeader__(configuration)
        self.__init_defaultUsings__(configuration)
        self.__init_createFolderStructure__(configuration)
        self.__init_eachClassSeparateFile__(configuration)

    def __init_fileHeader__(self, configuration: Dict[str, str]):
        self.fileHeader: str = """
// <auto-generated>
//     This code was generated by d3i.interpreter
//
//     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
// </auto-generated>"""

        if "dotnet.file_header_lines" in configuration:
            value = configuration["dotnet.file_header_lines"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.fileHeader = "\n".join(value)

    def __init_defaultUsings__(self, configuration: Dict[str, str]):
        self.defaultUsings: List[str] = ["System", "System.Collections.Generic"]
        if "dotnet.default_usings" in configuration:
            value = configuration["dotnet.default_usings"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultUsings = value

    def __init_createFolderStructure__(self, configuration: Dict[str, str]):
        self.createFolderStructure:bool = True
        if "dotnet.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["dotnet.create_folder_structure"])

    def __init_eachClassSeparateFile__(self, configuration: Dict[str, str]):
        self.eachClassSeparateFile:bool = True
        if "dotnet.each_class_separate_file" in configuration:
            self.eachClassSeparateFile = bool(configuration["dotnet.each_class_separate_file"])
