from __future__ import annotations
import os
from d3i.Engine import *
from d3i.elements.Elements import *


class utils:
    @staticmethod
    def tab(indent=1) -> str:
        return '\t'*indent

    @staticmethod
    def document_lines_to_one(hinted_element: hinted_base_element) -> str:
        return " ".join(hinted_element.document_lines).replace("  ", " ").strip()

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
    def isPublishedOn(interface: interface, protocol: str) -> bool:
        if (interface != None):
            if (utils.isPublishedOnInternal( interface, protocol ) == True ):
                return True
            if (utils.isPublishedOnPublic( interface, protocol ) != None ):
                return True

        return False

    @staticmethod
    def isPublishedOnInternal(interface: interface, protocol: str) -> bool:
        if (interface != None):
            published = interface.find_decorator("internal_api")
            if (published != None):
                param = published.find_param(protocol)
                if (param != None):
                    return True

    @staticmethod
    def isPublishedOnPublic(interface: interface, protocol: str) -> bool:
        if (interface != None):
            published = interface.find_decorator("public_api")
            if (published != None):
                param = published.find_param(protocol)
                if (param != None):
                    collection = published.find_param("collection")
                    if(collection != None):
                        return collection.value
                    else:
                        return ""

        return None
    @staticmethod
    def isEnumType(type: type):
        if (type.kind == type.Kind.Reference):
            reference_type: reference_type = type
            referenced_element: base_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name)
            if (isinstance(referenced_element, enum) == True):
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
            case primitive_type.PrimtiveKind.Date | primitive_type.PrimtiveKind.Time:
                return "string"  # must be converted to string
            case primitive_type.PrimtiveKind.DateTime:
                return "google.protobuf.Timestamp"
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
    def d3iTypeToGrpcRepresentation_Map(type: map_type) -> str:
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


class rest_utils:
    @staticmethod
    def is_id_type_param(param: operation_param):
        if (param.type.kind == type.Kind.Primitive):
            if (param.type.primtiveKind == primitive_type.PrimtiveKind.String or param.type.primtiveKind == primitive_type.PrimtiveKind.Integer):
                return True

        return False

    def is_body_type_param(param: operation_param):
        if (param.type.kind == type.Kind.Primitive):
            primitive_type: primitive_type = param.type
            match primitive_type.primtiveKind:
                case (
                    primitive_type.PrimtiveKind.I18NString |
                    primitive_type.PrimtiveKind.Any |
                    primitive_type.PrimtiveKind.Bytes |
                    primitive_type.PrimtiveKind.Stream
                ):
                    return True
                case (
                    primitive_type.PrimtiveKind.Integer |
                    primitive_type.PrimtiveKind.Number |
                    primitive_type.PrimtiveKind.Float |
                    primitive_type.PrimtiveKind.Date |
                    primitive_type.PrimtiveKind.Time |
                    primitive_type.PrimtiveKind.DateTime |
                    primitive_type.PrimtiveKind.String |
                    primitive_type.PrimtiveKind.Boolean
                ):
                    return False
        elif (param.type.kind == type.Kind.Reference):
            reference_type: reference_type = param.type
            referenced_element: base_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name)
            if (isinstance(referenced_element, enum) == True):
                return False
            else:
                return True

        return True

    def is_stream_type_param(param: operation_param):
        if (param.type.kind == type.Kind.Primitive and param.type.primtiveKind == primitive_type.PrimtiveKind.Stream):
            return True

        return False

    @staticmethod
    def count_body_param(operation: operation) -> bool:
        count: int = 0
        for param in operation.operation_params:
            if (rest_utils.is_body_type_param(param) == True):
                count = count + 1

        return count

    @staticmethod
    def count_stream_param(operation: operation) -> int:
        count: int = 0
        for param in operation.operation_params:
            if (rest_utils.is_stream_type_param(param) == True):
                count = count + 1

        return count

    


class rest_operation:
    # only this two verb is supported, beacuse of the Hungarian National Cybersecurity Institute guidance
    class Verb(Enum):
        Get = 0
        Post = 1

    def __init__(self, _operation: operation):
        self.operation: operation = _operation
        self.verb: rest_operation.Verb = None
        self.params: Dict[str, rest_param] = {}
        self.full_route: str = None
        self.__setVerb()
        self.__setParams()
        self.__setRoute()

    def isMultiPartFormData(self) -> bool:
        for param in self.params.values():
            if (param.bindingSource == rest_param.BindingSource.FromForm):
                return True

        return False

    def getQueryString(self) -> str:

        for param in self.params.values():
            if (param.bindingSource == rest_param.BindingSource.FromQuery):
                # do something
                pass

        # do something
        return False

    def __setVerb(self):
        count_stream = rest_utils.count_stream_param(self.operation)
        count_body = rest_utils.count_body_param(self.operation)

        if (self.operation.kind == operation.Kind.Command or count_stream > 0 or count_body > 0):
            self.verb = rest_operation.Verb.Post
        else:
            self.verb = rest_operation.Verb.Get

    def __setParams(self):
        count_stream = rest_utils.count_stream_param(self.operation)
        count_body = rest_utils.count_body_param(self.operation)

        for param in self.operation.operation_params:
            if (rest_utils.is_id_type_param(param) == True):
                _rest_param = rest_param(param)
                _rest_param.bindingSource = rest_param.BindingSource.FromRoute
                _rest_param.httpName = param.name
                self.params[param.name] = _rest_param
            elif (count_stream > 0 or count_body > 1):
                _rest_param = rest_param(param)
                _rest_param.bindingSource = rest_param.BindingSource.FromForm
                if (rest_utils.is_stream_type_param(param) == True):
                    _rest_param.httpName = "_file_" + param.name
                else:
                    _rest_param.httpName = "_json_" + param.name
                self.params[param.name] = _rest_param
            elif (rest_utils.is_body_type_param(param) and count_body == 1):
                _rest_param = rest_param(param)
                _rest_param.bindingSource = rest_param.BindingSource.FromBody
                _rest_param.httpName = param.name
                self.params[param.name] = _rest_param
            else:
                _rest_param = rest_param(param)
                _rest_param.bindingSource = rest_param.BindingSource.FromQuery
                if (utils.isEnumType(param.type)):
                    _rest_param.httpName = "_str_" + param.name
                else:
                    _rest_param.httpName = param.name
                self.params[param.name] = _rest_param

    def __setRoute(self):
        http: decorator = self.operation.find_decorator("http")
        if (http != None and http.get_param_value("route") != None):
            self.route = http.get_param_value("route")
        else:
            self.route = self.operation.name.lower()

        routeParams: List[rest_param] = [param for param in self.params.values() if param.bindingSource == rest_param.BindingSource.FromRoute]
        if (len(routeParams) > 0):
            self.full_route = self.route + "/" + "/".join([f"{{{param.param.name}}}" for param in routeParams])


class rest_param:
    class BindingSource(Enum):
        FromRoute = 0
        FromQuery = 1
        FromBody = 2
        FromForm = 3
        FromHeader = 4  # currently not used

    def __init__(self, _param: operation_param):
        self.param: operation_param = _param
        self.httpName: str = _param.name
        self.bindingSource: rest_param.BindingSource = None
