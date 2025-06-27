import os
from d3i.Engine import *
from d3i.elements.Elements import *


class utils:
    @staticmethod
    def create_folder(output_dir: str, folder_name: str):
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    @staticmethod
    def create_cs_file(output_dir: str, file_name: str, content: str):
        file_path = os.path.join(output_dir, file_name + ".cs")
        with open(file_path, "w") as file:
            file.write(content)

    def join_with_I(words: List[str]):
        if not words:
            return ""
        if len(words) == 1:
            return "I" + words[0]
        return ".".join(words[:-1]) + ".I" + words[-1]

    @staticmethod
    def camel_to_pascal(name: str) -> str:
        if not name:
            return name
        return name[0].upper() + name[1:]

    @staticmethod
    def collectBaseRecursive(base: composite, bases: List[base_element]):
        bases.append(base)

        for inherit in base.inherits:
            base_base = Engine.get_referenced_element(base.parent, inherit)
            if (base_base != None):
                utils.collectBaseRecursive(base_base, bases)

    @staticmethod
    def collectBaseCompositsRecursive(base_composite: composite, base_composites: List[composite]):
        base_composites.append(base_composite)

        for inherit in base_composite.inherits:
            base = Engine.get_referenced_element(base_composite.parent, inherit)
            if (isinstance(base, composite) == True):
                utils.collectBaseCompositsRecursive(base, base_composites)

    @staticmethod
    def isPublishedOn( interface:interface, protocol:str  ) -> bool:
        if(interface != None):
            published = interface.find_decorator( "publish")
            if(published!= None):
                for param in published.params:
                    if( param.kind == decorator_param.Kind.String and param.value == protocol ):
                        return True
                    if( param.kind == decorator_param.Kind.QualifiedName and param.value.getText() == protocol ):
                        return True
            
        return False


class grpc_utils:
    @staticmethod
    def d3iTypeToGrpcRepresentation(type: type) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return grpc_utils.d3iTypeToGrpcRepresentation_Primitive(type)
            case type.Kind.Reference:
                return grpc_utils.d3iTypeToGrpcRepresentation_Reference(type)
            case type.Kind.List:
                return grpc_utils.d3iTypeToGrpcRepresentation_List(type)
            case type.Kind.Map:
                return grpc_utils.d3iTypeToGrpcRepresentation_Map(type)

    @staticmethod
    def d3iTypeToGrpcRepresentation_Primitive(type: primitive_type) -> str:
        """
        Converts a primitive type to its protobuf representation.
        """
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "string"  # json serialize/desialize
            case primitive_type.PrimtiveKind.Integer:
                return "int32"
            case primitive_type.PrimtiveKind.Number:
                return "string"  # must be converted to string
            case primitive_type.PrimtiveKind.Float:
                return "double"
            case primitive_type.PrimtiveKind.Date | primitive_type.PrimtiveKind.Time | primitive_type.PrimtiveKind.DateTime:
                return "string"  # must be converted to string with timezone
            case primitive_type.PrimtiveKind.String:
                return "string"
            case primitive_type.PrimtiveKind.I18NString:
                return "string"  # must be converted to json
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes | primitive_type.PrimtiveKind.Stream:
                return "bytes"

    @staticmethod
    def d3iTypeToGrpcRepresentation_Reference(type: reference_type) -> str:
        return f"Protos.{type.reference_name.getText()}"

    @staticmethod
    def d3iTypeToGrpcRepresentation_List(type: list_type) -> str:
        return f"RepeatedField<{grpc_utils.d3iTypeToGrpcRepresentation(type.item_type)}>"

    @staticmethod
    def d3iTypeToGrpcRepresentation_List(type: map_type) -> str:
        return f"MapField<{grpc_utils.d3iTypeToGrpcRepresentation(type.key_type)},{grpc_utils.d3iTypeToGrpcRepresentation(type.value_type)}>"

    @staticmethod
    def getProtoFullName(element: base_element) -> str:
        protoNames: List[str] = []
        parent = element.parent
        while True:
            if (parent == None):
                break
            if (isinstance(parent, interface)):
                protoNames.insert(0, f"{parent.name}_v{parent.version}")
                break
            else:
                protoNames.insert(0, "Types")
                protoNames.insert(0, parent.name)

            parent = parent.parent

        return ".".join(protoNames) + f".{element.name}"

    @staticmethod
    def getDotnetFullName(element: base_element) -> str:
        dotnetNames: List[str] = []
        while True:
            if (element == None):
                break
            if (Engine.has_version_int_member(element)):
                if( isinstance(element, interface)):
                    dotnetNames.insert(0, f"I{element.name}_v{element.version}")
                else:
                    dotnetNames.insert(0, f"{element.name}_v{element.version}")
            else:
                dotnetNames.insert(0, element.name)

            element = element.parent

        return ".".join(dotnetNames)
