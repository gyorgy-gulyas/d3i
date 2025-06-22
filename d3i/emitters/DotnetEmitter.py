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
    Creates an instance of DotnetEmmiter, initializes it with the output directory and configuration,
    and then emits the dotnet code based on the provided session.
    """
    dotnetEmitter = DotnetEmitter(output_dir, configuration)

    # Generate the .NET code for the session
    results: List[dotnet_code] = dotnetEmitter.Emit(session)

    for code in results:
        dir_name = os.path.dirname(code.fullPath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        with open(code.fullPath, "w") as file:
            file.write(code.content)

    return results


class DotnetEmitter:
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        """
        Initializes the DotnetEmmiter instance with the provided output directory and configuration.
        """
        self.configuration: dotnet_configuration = dotnet_configuration(configuration, output_dir)

    def Emit(self, session: Session):
        """
        Emits the .NET code based on d3 file
        """
        result: List[dotnet_code] = []
        code: dotnet_code = None

        # Iterate over all domain in the session
        for domain in session.main.domains:
            output_path: str = self.configuration.output_dir
            for context in domain.contexts:

                # Process all enum in the context
                for enum in context.enums:
                    code = self.beginFile(output_path, enum, "Models")
                    code = self.enumText(enum, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all value_object in the context
                for valueobject in context.value_objects:
                    code = self.beginFile(output_path, valueobject, "Models")
                    code = self.valueobjectText(valueobject, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all composite in the context
                for composite in context.composites:
                    code = self.beginFile(output_path, composite, "Models")
                    code = self.compositeText(composite, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    for enum in aggregate.enums:
                        code = self.beginFile(output_path, enum, "Models")
                        code = self.enumText(enum, code)
                        code = self.endFile(code)
                        result.append(code)

                    for valueobject in aggregate.value_objects:
                        code = self.beginFile(output_path, valueobject, "Models")
                        code = self.valueobjectText(valueobject, code)
                        code = self.endFile(code)
                        result.append(code)

                    for aggregate_entity in aggregate.internal_entities:
                        code = self.beginFile(output_path, aggregate_entity.entity, "Models")
                        code = self.entityText(aggregate_entity.entity, code)
                        code = self.endFile(code)
                        result.append(code)

                # Process all view in the context
                for view in context.views:
                    code = self.beginFile(output_path, view, "Models")
                    code = self.viewText(view, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all acl in the context
                for acl in context.acls:
                    # interface
                    code = self.beginFile(output_path, acl, "Service/Interfaces")
                    code = self.aclInterfaceText(acl, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all service in the context
                for service in context.services:
                    # interface
                    code = self.beginFile(output_path, service, "Service/Interfaces")
                    code = self.serviceInterfaceText(service, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all inerface in the context
                for interface in context.interfaces:
                    # interface
                    code = self.beginFile(output_path, interface, "Service/Interfaces", additionalName=f"_v{interface.version}")
                    code = self.interfaceInterfaceText(interface, code)
                    code = self.endFile(code)
                    result.append(code)
                    # grpc controller file
                    if (self.configuration.withGrpc == True):
                        code = self.beginFile(output_path, interface, "Service/Controllers", additionalName=".GrpcController")
                        code = self.interfaceGrpcControllerText(interface, code)
                        code = self.endFile(code)
                        result.append(code)

        return result

    def fileHeader(self) -> str:
        """
        Returns the file header to be included in the generated .cs files.
        """
        return self.configuration.fileHeader

    def defaultUsings(self) -> str:
        """
        Returns the default 'using' statements to be included in the .cs files.
        """
        using_statements: List[str] = []

        for using in self.configuration.defaultUsings:
            using_statements.append(f"using {using};")

        return "\n".join(using_statements) + "\n"

    def beginFile(self, output_path: str, element: base_element, subDirectoryName: str, additionalName: str = "") -> dotnet_code:
        buffer = io.StringIO()
        domain: domain = element.getDomain()
        context: context = element.getContext()
        aggregate: aggregate = element.getAggregate()

        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("<ADDITIONAL_USINGS>")
        buffer.write("\n")
        if (aggregate != None):
            buffer.write(f"namespace {domain.name}.{context.name}.{aggregate.name}\n")
        else:
            buffer.write(f"namespace {domain.name}.{context.name}\n")

        buffer.write("{\n")

        code: dotnet_code = dotnet_code(output_path, [domain.name, context.name, subDirectoryName], element.name + additionalName)
        code.content = buffer.getvalue()
        return code

    def endFile(self, code: dotnet_code) -> dotnet_code:
        buffer = io.StringIO()
        buffer.write("}\n")
        code.content += buffer.getvalue()

        buffer = io.StringIO()
        sorted_usings: list[str] = sorted(code.usings)
        for using in sorted_usings:
            buffer.write(f"using {using};\n")

        code.content = code.content.replace("<ADDITIONAL_USINGS>", buffer.getvalue())
        return code

    def enumText(self, enum: enum, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an enum.
        """
        buffer = io.StringIO()
        # Add documentation lines for the enum
        buffer.write(self.documentLines(enum, indent))
        # Write the enum declaration with indentation
        buffer.write(f"{self.tab(indent)}public enum {enum.name}\n")
        buffer.write(f"{self.tab(indent)}{{\n")
        # Loop through each enum element and generate code for each
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent+1))
            # Write each enum element value
            buffer.write(f"{self.tab(indent+1)}{enum_element.value},\n")
            if (len(enum_element.document_lines) > 0):
                buffer.write("\n")

        buffer.write(f"{self.tab(indent)}}}\n")
        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        return code

    def enumGrpcMappingText(self, enum: enum, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an enum mapping for GRPC.
        """
        buffer = io.StringIO()
        buffer.write(f"{self.tab(indent)}public static class {enum.name}Extensions\n")
        buffer.write(f"{self.tab(indent)}{{\n")

        # ToGrpc
        buffer.write(f"{self.tab(indent+1)}public static Protos.{enum.name} ToGrpc( this {enum.name} @this )\n")
        buffer.write(f"{self.tab(indent+1)}{{\n")
        buffer.write(f"{self.tab(indent+2)}return @this switch\n")
        buffer.write(f"{self.tab(indent+2)}{{\n")
        # Loop through each enum element and generate code for each mapping
        for enum_element in enum.enum_elements:
            buffer.write(f"{self.tab(indent+3)}{enum.name}.{enum_element.value} => Protos.{enum.name}.{enum_element.value},\n")
        buffer.write(f"{self.tab(indent+3)}_ => throw new NotImplementedException(), \n")
        buffer.write(f"{self.tab(indent+2)}}};\n")
        buffer.write(f"{self.tab(indent+1)}}}\n")
        buffer.write(f"\n")

        # FromGrpc
        buffer.write(f"{self.tab(indent+1)}public static {enum.name} FromGrpc( this Protos.{enum.name} @this )\n")
        buffer.write(f"{self.tab(indent+1)}{{\n")
        buffer.write(f"{self.tab(indent+2)}return @this switch\n")
        buffer.write(f"{self.tab(indent+2)}{{\n")
        # Loop through each enum element and generate code for each mapping
        for enum_element in enum.enum_elements:
            buffer.write(f"{self.tab(indent+3)}Protos.{enum.name}.{enum_element.value} => {enum.name}.{enum_element.value},\n")
        buffer.write(f"{self.tab(indent+3)}_ => throw new NotImplementedException(), \n")
        buffer.write(f"{self.tab(indent+2)}}};\n")
        buffer.write(f"{self.tab(indent+1)}}}\n")
        buffer.write(f"\n")

        buffer.write(f"{self.tab(indent)}}}\n")
        code.content += buffer.getvalue()
        return code

    def valueobjectText(self, valueobject: value_object, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(valueobject, valueobject.inherits, valueobject.name, valueobject.members, code, indent)

    def dtoText(self, dto: dto, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(dto, dto.inherits, dto.name, dto.members, code, indent)

    def entityText(self, entity: entity, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(entity, entity.inherits, entity.name, entity.members, code, indent)

    def viewText(self, view: view, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(view, view.inherits, view.name, view.members, code, indent)

    def dataClassText(self, element: internal_scoped_base_element, inherits: List[qualified_name], name: str, members: List[hinted_base_element], code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an data object
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        for inherit in inherits:
            base = utils.get_referenced_element(element.parent, inherit)
            if (isinstance(base, composite) == True):
                utils.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            else:
                inherit_names.append(inherit.getText())

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(element, indent))
        # Write the data class declaration with indentation
        buffer.write(f"{self.tab(indent)}public partial class {element.name}")
        # Write inherits if any
        if (len(inherit_names)):
            buffer.write(" : ")
            buffer.write(", ".join(inherit_names))
        buffer.write(f"\n{self.tab(indent)}{{\n")

        # Loop through each coposite members and generate code for each
        for base_composite in base_composites:
            buffer.write(f"{self.tab(indent+1)}#region I{base_composite.name}\n")

            # write internal enums if Any
            if (base_composite.withEnum == True):
                for child_enum in base_composite.enums:
                    buffer.write(self.enumText(child_enum, indent+1))

            # write internal value object if Any
            if (base_composite.withValueObject == True):
                for child_value_object in base_composite.value_objects:
                    buffer.write(self.valueobjectText(child_value_object, indent+1))

            # write internal dto if Any
            if (base_composite.withDto == True):
                for child_dto in base_composite.dtos:
                    buffer.write(self.dtoText(child_dto, indent+1))

            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member.name, member.type, code, indent+1))
            buffer.write(f"{self.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # write internal enums if Any
        if (element.withEnum == True):
            for enum in element.enums:
                buffer.write(self.enumText(enum, indent))

        # write internal valueobjects if Any
        if (element.withValueObject == True):
            for valueobject in element.value_objects:
                buffer.write(self.valueobjectText(valueobject, indent))

        # write internal valueobjects if Any
        if (element.withDto == True):
            for dto in element.dtos:
                buffer.write(self.dtoText(dto, indent))

        # Loop through each valueobject members and generate code for each
        for member in members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, code, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def dtoGrpcMappingText(self, dto: dto, code: dotnet_code, indent: int = 1) -> str:
        """
        Generates the .NET code for an data object
        """
        bases: List[internal_scoped_base_element] = []
        for inherit in dto.inherits:
            base = utils.get_referenced_element(dto.parent, inherit)
            if (base != None):
                utils.collectBaseRecursive(base, bases)

        buffer = io.StringIO()

        # ToGrpc
        buffer.write(f"\n")
        buffer.write(f"{self.tab(indent+1)}public static Protos.{dto.name} ToGrpc( {dto.name} @this )\n")
        buffer.write(f"{self.tab(indent+1)}{{\n")
        buffer.write(f"{self.tab(indent+2)}Protos.{dto.name} result = new();\n")
        buffer.write(f"\n")

        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{self.tab(indent+2)}// unfold begin: {base.name}\n")
            # Write each own member
            for member in base.members:
                buffer.write(self.dataClassMemberToGrpcMappingText(member.name, member.type, code, dst="result.", src="@this.", indent=indent+2))
                pass
            buffer.write(f"{self.tab(indent+2)}// unfold end {base.name}\n\n")
        # Write each own member
        for member in dto.members:
            buffer.write(self.dataClassMemberToGrpcMappingText(member.name, member.type, code, dst="result.", src="@this.", indent=indent+2))
            pass
        buffer.write(f"\n")
        buffer.write(f"{self.tab(indent+2)}return result;\n")
        buffer.write(f"{self.tab(indent+1)}}}\n")

        # FromGrpc
        buffer.write(f"{self.tab(indent+1)}public static {dto.name} FromGrpc( Protos.{dto.name} @from )\n")
        buffer.write(f"{self.tab(indent+1)}{{\n")
        buffer.write(f"{self.tab(indent+2)}{dto.name} result = new();\n")
        buffer.write(f"\n")
        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{self.tab(indent+2)}// unfold begin: {base.name}\n")
            # Write each own member
            for member in base.members:
                buffer.write(self.dataClassMemberFromGrpcMappingText(member.name, member.type, code, dst="result.", src="@from.", indent=indent+2))
                pass
            buffer.write(f"{self.tab(indent+2)}// unfold end {base.name}\n\n")

        for member in dto.members:
            # Write each member
            buffer.write(self.dataClassMemberFromGrpcMappingText(member.name, member.type, code, dst="result.", src="@from.", indent=indent+2))
            pass
        buffer.write(f"\n")
        buffer.write(f"{self.tab(indent+2)}return result;\n")
        buffer.write(f"{self.tab(indent+1)}}}\n")
        return buffer.getvalue()

    def dataClassMemberToGrpcMappingText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberToGrpcMappingText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberToGrpcMappingText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberToGrpcMappingText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberToGrpcMappingText_Map(memberName, memberType, code, dst, src, indent)

    def dataClassMemberFromGrpcMappingText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberFromGrpcMappingText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberFromGrpcMappingText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberFromGrpcMappingText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberFromGrpcMappingText_Map(memberName, memberType, code, dst, src, indent)

    def dataClassMemberToGrpcMappingText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        return f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)} = {self.convertExpressionToGrpcRepresentation(f"{src}{memberName}", memberType, code)};\n"

    def dataClassMemberFromGrpcMappingText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        return f"{self.tab(indent)}{dst}{memberName} = {self.convertExpressionFromGrpcRepresentation(f"{src}{utils.camel_to_pascal(memberName)}", memberType, code)};\n"

    def convertExpressionToGrpcRepresentation(self, memberName: str, memberType: type, code: dotnet_code):
        match memberType.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                pass
            case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Float:
                return f"{memberName};\n"
            case primitive_type.PrimtiveKind.Number:
                code.usings.add("System.Globalization")
                return f"{memberName}.ToString(CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Date:
                return f"{memberName}.ToString(CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Time:
                return f"{memberName}.ToString(\"HH:mm\")"
            case primitive_type.PrimtiveKind.DateTime:
                code.usings.add("Google.Protobuf.WellKnownTypes")
                return f"Timestamp.FromDateTime({memberName})"
            case primitive_type.PrimtiveKind.String:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.I18NString:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Serialize({memberName})"
            case primitive_type.PrimtiveKind.Boolean:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Bytes:
                return f"Google.Protobuf.ByteString.CopyFrom({memberName})"
            case primitive_type.PrimtiveKind.Stream:
                return f"Google.Protobuf.ByteString.FromStream({memberName})"

    def convertExpressionFromGrpcRepresentation(self, memberName: str, memberType: type, code: dotnet_code):
        match memberType.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                pass
            case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Float:
                return f"{memberName};\n"
            case primitive_type.PrimtiveKind.Number:
                code.usings.add("System.Globalization")
                return f"decimal.Parse({memberName}, CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Date:
                code.usings.add("System.Globalization")
                return f"DateOnly.Parse({memberName}, CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Time:
                return f"{memberName}.ToString(\"HH:mm\")"
            case primitive_type.PrimtiveKind.DateTime:
                code.usings.add("Google.Protobuf.WellKnownTypes")
                return f"{memberName}).ToDateTime()"
            case primitive_type.PrimtiveKind.String:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.I18NString:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Serialize({memberName})"
            case primitive_type.PrimtiveKind.Boolean:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Bytes:
                return f"Google.Protobuf.ByteString.CopyFrom({memberName})"
            case primitive_type.PrimtiveKind.Stream:
                return f"Google.Protobuf.ByteString.FromStream({memberName})"

    def dataClassMemberToGrpcMappingText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        referenced_element: base_element = utils.get_referenced_element(memberType.parent, memberType.reference_name)

        buffer = io.StringIO()
        buffer.write(f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)} = ")
        if (referenced_element != None and isinstance(referenced_element, enum) == True):
            buffer.write(f"{src}{memberName}.ToGrpc();\n")
        else:
            buffer.write(f"{src}{memberName} != null ? {memberType.reference_name.getText()}.ToGrpc( {src}{memberName}) : null;\n")
        return buffer.getvalue()

    def dataClassMemberFromGrpcMappingText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        referenced_element: base_element = utils.get_referenced_element(memberType.parent, memberType.reference_name)

        buffer = io.StringIO()
        buffer.write(f"{self.tab(indent)}{dst}{memberName} = ")
        if (referenced_element != None and isinstance(referenced_element, enum) == True):
            buffer.write(f"{src}{utils.camel_to_pascal(memberName)}.FromGrpc();\n")
        else:
            buffer.write(
                f"{src}{utils.camel_to_pascal(memberName)} != null ? {memberType.reference_name.getText()}.FromGrpc( {src}{utils.camel_to_pascal(memberName)}) : null;\n")
        return buffer.getvalue()

    def dataClassMemberToGrpcMappingText_List(self, memberName: str, memberType: list_type, code: dotnet_code, dst: str, src: str, indent: int):
        code.usings.add("Google.Protobuf.Collections")

        buffer = io.StringIO()

        match memberType.item_type.kind:
            case type.Kind.Primitive:
                if (memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Integer or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.String or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Float or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Boolean):
                    buffer.write(f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName});\n")
                else:
                    buffer.write(
                        f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName}.Select( v => {self.convertExpressionToGrpcRepresentation("v", memberType.item_type, code)} ));\n")
            case type.Kind.Reference:
                reference_type: reference_type = memberType.item_type
                buffer.write(
                    f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName}.Select( v => {reference_type.reference_name.getText()}.ToGrpc( v ) ));\n")
            case type.Kind.List:
                pass
            case type.Kind.Map:
                pass

        return buffer.getvalue()

    def dataClassMemberFromGrpcMappingText_List(self, memberName: str, memberType: list_type, code: dotnet_code, dst: str, src: str, indent: int):
        code.usings.add("Google.Protobuf.Collections")

        buffer = io.StringIO()

        match memberType.item_type.kind:
            case type.Kind.Primitive:
                if (memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Integer or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.String or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Float or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Boolean):
                    buffer.write(f"{self.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)});\n")
                else:
                    buffer.write(
                        f"{self.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)}.Select( v => {self.convertExpressionFromGrpcRepresentation("v", memberType.item_type, code)} ));\n")
            case type.Kind.Reference:
                buffer.write(
                    f"{self.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)}.Select( v => {self.typeText(memberType.item_type, code)}.FromGrpc(v) ));\n")
            case type.Kind.List:
                # not supported types
                pass
            case type.Kind.Map:
                # not supported types
                pass

        return buffer.getvalue()

    def dataClassMemberToGrpcMappingText_Map(self, memberName: str, memberType: map_type, code: dotnet_code, dst: str, src: str, indent: int):

        buffer = io.StringIO()

        match memberType.value_type.kind:
            case type.Kind.Primitive:
                if (memberType.value_type.primtiveKind == primitive_type.PrimtiveKind.Integer or memberType.value_type.primtiveKind == primitive_type.PrimtiveKind.String or memberType.value_type.primtiveKind == primitive_type.PrimtiveKind.Float or memberType.value_type.primtiveKind == primitive_type.PrimtiveKind.Boolean):
                    buffer.write(f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add({src}{memberName});\n")
                else:
                    buffer.write(f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add({src}{memberName}.ToDictionary( kvp => kvp.Key, kvp => {self.convertExpressionToGrpcRepresentation("kvp.Value", memberType.value_type, code)}));\n")
            case type.Kind.Reference:
                buffer.write(f"{self.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add( {src}{memberName}.ToDictionary( kvp => kvp.Key, kvp => {self.typeText(memberType.value_type, code)}.ToGrpc( kvp.Value ) ));\n")
            case type.Kind.List:
                # not supported types
                pass
            case type.Kind.Map:
                # not supported types
                pass

        return buffer.getvalue()

    def dataClassMemberFromGrpcMappingText_Map(self, memberName: str, memberType: map_type, code: dotnet_code, dst: str, src: str, indent: int):

        buffer = io.StringIO()

        match memberType.value_type.kind:
            case type.Kind.Primitive:
                buffer.write(f"{self.tab(indent)}foreach( var kvp in {src}{utils.camel_to_pascal(memberName)})\n")
                buffer.write(
                    f"{self.tab(indent+1)}{dst}{memberName}[kvp.Key] = {self.convertExpressionFromGrpcRepresentation("kvp.Value", memberType.value_type, code)};\n")
            case type.Kind.Reference:
                buffer.write(f"{self.tab(indent)}foreach( var kvp in {src}{utils.camel_to_pascal(memberName)})\n")
                buffer.write(f"{self.tab(indent+1)}{dst}{memberName}[kvp.Key] = {self.typeText(memberType.value_type, code)}.FromGrpc(kvp.Value);\n")
                pass
            case type.Kind.List:
                # not supported types
                pass
            case type.Kind.Map:
                # not supported types
                pass

        return buffer.getvalue()

    def compositeText(self, composite: composite, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an composite, just the interface.
        """
        buffer = io.StringIO()
        buffer.write("\n")
        # Add documentation lines for the composite
        buffer.write(self.documentLines(composite, indent))
        # Write the composite interface declaration with indentation
        buffer.write(f"{self.tab(indent)}public interface I{composite.name}\n")
        buffer.write(f"{self.tab(indent)}{{\n")
        # Loop through each composite members and generate code for each
        for member in composite.members:
            buffer.write(self.documentLines(member, indent+1))
            # Write each member
            buffer.write(self.propertyText(member.name, member.type, code, indent+1))
        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def aclInterfaceText(self, acl: acl, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(acl, acl.name, acl.operations, code, indent)

    def serviceInterfaceText(self, service: service, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(service, service.name, service.operations, code, indent)

    def interfaceInterfaceText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(interface, interface.name + f"_v{interface.version}", interface.operations, code, indent)

    def interfaceClassText(self, element: internal_scoped_base_element, elementName: str, operations: List[operation], code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for element, just the interface.
        """
        buffer = io.StringIO()
        code.usings.add("ServiceKit.Net")
        # Add documentation lines for the element
        buffer.write(self.documentLines(element, indent))
        # Write the interface class declaration with indentation
        buffer.write(f"{self.tab(indent)}public partial interface I{elementName}\n")
        buffer.write(f"{self.tab(indent)}{{\n")

        # Loop through each operations and generate code for each
        for operation in operations:
            # Write each operation
            buffer.write(self.interfaceFunctionText(operation, code, indent+1))
            buffer.write("\n")

        buffer.write(f"\n")
        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        # write internal enums if Any
        if (element.withEnum == True):
            for enum in element.enums:
                code = self.enumText(enum, code, indent+1)

        # write internal valueobjects if Any
        if (element.withValueObject == True):
            for valueobject in element.value_objects:
                code = self.valueobjectText(valueobject, code, indent+1)

        # write internal valueobjects if Any
        if (element.withDto == True):
            for dto in element.dtos:
                code = self.dtoText(dto, code, indent+1)

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def interfaceFunctionText(self, operation: operation, code: dotnet_code, indent: int) -> str:
        buffer = io.StringIO()

        # Add summary for operation
        if (len(operation.document_lines) > 0):
            buffer.write(f"{self.tab(indent)}/// <summary>\n")
            for line in operation.document_lines:
                buffer.write(f"{self.tab(indent)}/// {line}\n")
            buffer.write(f"{self.tab(indent)}/// </summary>\n")

        # Add param comments for operation
        for param in operation.operation_params:
            if (len(param.document_lines) == 1):
                buffer.write(f"{self.tab(indent)}/// <param name='{param.name}'>{param.document_lines[0]}</param>\n")
            elif (len(param.document_lines) > 1):
                buffer.write(f"{self.tab(indent)}/// <param name='{param.name}'>\n")
                for line in param.document_lines:
                    buffer.write(f"{self.tab(indent)}/// {line}\n")
                buffer.write(f"{self.tab(indent)}/// </param>\n")

        # Add response code comments
        for returns in operation.operation_returns:
            status_decorator: decorator = next((d for d in returns.decorators if d.name == "status"), None)
            if (status_decorator != None and len(status_decorator.params) > 0):
                status_code = status_decorator.params[0].value
                if (len(returns.document_lines) == 1):
                    buffer.write(f"{self.tab(indent)}/// <response code='{status_code}'>{returns.document_lines[0]}</response>\n")
                elif (len(returns.document_lines) > 1):
                    buffer.write(f"{self.tab(indent)}/// <response code='{status_code}'>\n")
                    for line in returns.document_lines:
                        buffer.write(f"{self.tab(indent)}/// {line}\n")
                    buffer.write(f"{self.tab(indent)}/// </response>\n")

        # Add return value
        buffer.write(f"{self.tab(indent)}public Task<Response")
        if (len(operation.operation_returns) > 0):
            buffer.write("<")
            buffer.write(", ".join(self.typeText(item.type, code) for item in operation.operation_returns))
            buffer.write(">")
        buffer.write(">")
        # Add function name
        buffer.write(f" {operation.name}(CallingContext ctx")
        # Add parameters
        if (len(operation.operation_params) > 0):
            buffer.write(f", ")
        buffer.write(", ".join([self.typeText(param.type, code) + " " + param.name for param in operation.operation_params]))
        buffer.write(");\n")

        return buffer.getvalue()

    def aclGrpcControllerText(self, acl: acl, code: dotnet_code) -> dotnet_code:
        return self.grpcControllerText(acl, acl.name, acl.operations, code, indent=1)

    def serviceGrpcControllerText(self, service: service, code: dotnet_code) -> dotnet_code:
        return self.grpcControllerText(service, service.name, service.operations, code, indent=1)

    def interfaceGrpcControllerText(self, interface: interface, code: dotnet_code) -> dotnet_code:
        return self.grpcControllerText(interface, interface.name+f"_v{interface.version}", interface.operations, code, indent=1)

    def grpcControllerText(self, element: hinted_base_element, elementName: str, operations: List[operation], code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET GRPC controller code for acl
        """
        buffer = io.StringIO()
        domain: domain = element.getDomain()
        context: context = element.getContext()

        code.usings.add("Google.Protobuf.WellKnownTypes")
        code.usings.add("Grpc.Core")
        code.usings.add("ServiceKit.Net")
        code.usings.add("Serilog.Context")
        code.usings.add(f"{domain.name}.{context.name}.Protos")

        # Add documentation lines for the acl
        buffer.write(self.documentLines(element, indent))
        # class declaration
        buffer.write(f"{self.tab(indent)}public class {elementName}GrpcController : {domain.name}.{context.name}.Protos.{elementName}.{elementName}Base \n")
        buffer.write(f"{self.tab(indent)}{{\n")
        # class members
        buffer.write(f"{self.tab(indent+1)}private readonly ILogger<{elementName}GrpcController> _logger;\n")
        buffer.write(f"{self.tab(indent+1)}private readonly I{elementName} _service;\n")
        buffer.write(f"\n")
        # class constructor
        buffer.write(f"{self.tab(indent+1)}public {elementName}GrpcController( ILogger<{elementName}GrpcController> logger, I{elementName} service )\n")
        buffer.write(f"{self.tab(indent+1)}{{\n")
        buffer.write(f"{self.tab(indent+2)}_logger = logger; \n")
        buffer.write(f"{self.tab(indent+2)}_service = service; \n")
        buffer.write(f"{self.tab(indent+1)}}}\n")

        # Add functions based on operations
        for operation in operations:
            buffer.write(f"\n")
            buffer.write(f"{self.tab(indent+1)}public override async Task<{elementName}_{operation.name}Response> {operation.name}( {elementName}_{operation.name}Request request, ServerCallContext grpcContext)\n")
            buffer.write(f"{self.tab(indent+1)}{{\n")
            buffer.write(f"{self.tab(indent+2)}using(LogContext.PushProperty( \"Scope\", \"{elementName}.{operation.name}\" ))\n")
            buffer.write(f"{self.tab(indent+2)}{{\n")
            buffer.write(f"{self.tab(indent+3)}CallingContext ctx = CallingContext.PoolFromGrpcContext( grpcContext, _logger );\n")
            buffer.write(f"{self.tab(indent+3)}try\n")
            buffer.write(f"{self.tab(indent+3)}{{\n")
            index: int = 1
            params: List[str] = []
            for param in operation.operation_params:
                buffer.write(f"{self.tab(indent+4)}{self.typeText(param.type,code)} {param.name};\n")
                buffer.write(f"{self.tab(indent+4)}{self.dataClassMemberFromGrpcMappingText(param.name, param.type, code, dst="", src="request.", indent=0)}")
                params.append(param.name)
                index = index + 1
            buffer.write(f"\n")
            buffer.write(f"{self.tab(indent+4)}// calling the service function itself\n")
            buffer.write(f"{self.tab(indent+4)}var response = await _service.{operation.name}( ctx {", " + ", ".join(params) if params else ""} );\n")
            buffer.write(f"\n")
            if (len(operation.operation_returns) > 0):
                index: int = 1
                for returns in operation.operation_returns:
                    buffer.write(f"{self.tab(indent+4)}if( response.HasValue{index}() == true )\n")
                    buffer.write(f"{self.tab(indent+4)}{{\n")
                    buffer.write(f"{self.tab(indent+5)}var result = new {elementName}_{operation.name}Response();\n")
                    buffer.write(f"{self.tab(indent+5)}{self.dataClassMemberToGrpcMappingText(f"Value{index}", returns.type, code, dst="result.", src="response.", indent=0)}")
                    buffer.write(f"{self.tab(indent+5)}return result;\n")
                    buffer.write(f"{self.tab(indent+4)}}}\n")
                    buffer.write(f"{self.tab(indent+4)}\n")
                    index = index+1

                buffer.write(f"{self.tab(indent+4)}if( response.IsSuccess() == false )\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {elementName}_{operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+7)}Status = response.Error.Status.ToGrpc(),\n")
                buffer.write(f"{self.tab(indent+7)}MessageText = response.Error.MessageText,\n")
                buffer.write(f"{self.tab(indent+7)}AdditionalInformation = response.Error.AdditionalInformation\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}};\n")
                buffer.write(f"{self.tab(indent+4)}}}\n")
                buffer.write(f"{self.tab(indent+4)}\n")

                buffer.write(f"{self.tab(indent+4)}return new {elementName}_{operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+5)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+6)}Status = ServiceKit.Protos.Statuses.NotImplemented,\n")
                buffer.write(f"{self.tab(indent+6)}MessageText = \"Not handled reponse in GRPC Controller when calling '{element.name}.{operation.name}'\",\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+4)}}};\n")
            else:
                buffer.write(f"{self.tab(indent+4)}if( response.IsSuccess() == true )\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {elementName}_{operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Success = new Empty();\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+4)}}}\n")
                buffer.write(f"{self.tab(indent+4)}else\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {elementName}_{operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+7)}Status = response.Error.Status,\n")
                buffer.write(f"{self.tab(indent+7)}MessageText = response.Error.MessageText,\n")
                buffer.write(f"{self.tab(indent+7)}AdditionalInformation = response.Error.AdditionalInformation\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}};\n")
                buffer.write(f"{self.tab(indent+4)}}}\n")
                buffer.write(f"{self.tab(indent+4)}\n")

            buffer.write(f"{self.tab(indent+4)}\n")
            buffer.write(f"{self.tab(indent+3)}}}\n")
            buffer.write(f"{self.tab(indent+3)}catch(Exception ex)\n")
            buffer.write(f"{self.tab(indent+3)}{{\n")
            buffer.write(f"{self.tab(indent+4)}return new {elementName}_{operation.name}Response {{\n")
            buffer.write(f"{self.tab(indent+5)}Error = new () {{\n")
            buffer.write(f"{self.tab(indent+6)}Status = ServiceKit.Protos.Statuses.InternalError,\n")
            buffer.write(f"{self.tab(indent+6)}MessageText = ex.Message,\n")
            buffer.write(f"{self.tab(indent+6)}AdditionalInformation = ex.ToString()\n")
            buffer.write(f"{self.tab(indent+5)}}}\n")
            buffer.write(f"{self.tab(indent+4)}}};\n")
            buffer.write(f"{self.tab(indent+3)}}}\n")
            buffer.write(f"{self.tab(indent+3)}finally\n")
            buffer.write(f"{self.tab(indent+3)}{{\n")
            buffer.write(f"{self.tab(indent+4)}ctx.ReturnToPool();\n")
            buffer.write(f"{self.tab(indent+3)}}}\n")
            buffer.write(f"{self.tab(indent+2)}}}\n")
            buffer.write(f"{self.tab(indent+1)}}}\n")

        # end of class
        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def interfaceInterfaceGrpcMappingText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceGrpcMappingText(interface, interface.name + f"_v{interface.version}", code, indent)

    def interfaceGrpcMappingText(self, element: internal_scoped_base_element, elementName: str, code, indent):
        """
        Generates the .NET code for element, just the interface.
        """
        buffer = io.StringIO()
        # Write the interface class declaration with indentation
        buffer.write(f"{self.tab(indent)}public partial interface I{elementName}\n")
        buffer.write(f"{self.tab(indent)}{{\n")

        # write internal enums if Any
        if (element.withEnum == True):
            for enum in element.enums:
                buffer.write(self.enumGrpcMappingText(enum, code, indent+1))

        # write internal valueobjects if Any
        if (element.withDto == True):
            for dto in element.dtos:
                buffer.write(self.dtoGrpcMappingText(dto, code, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def propertyText(self, member_name: str, type: type, code: dotnet_code, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"{self.tab(indent)}public {self.typeText(type, code)} {member_name} {{ get; set; }}\n")
        return buffer.getvalue()

    def typeText(self, type: type, code: dotnet_code) -> str:
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
        """
        Converts a primitive type to its .NET representation.
        """
        match type.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                return "object"
            case primitive_type.PrimtiveKind.Integer:
                return "int"
            case primitive_type.PrimtiveKind.Number:
                return "decimal"
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

    def typeTextReference(self, type: reference_type, code: dotnet_code) -> str:
        referenced_element: base_element = utils.get_referenced_element(type.parent, type.reference_name)
        if (referenced_element != None):
            code.usings.add(f"{referenced_element.getDomain().name}.{referenced_element.getContext().name}")

        return type.reference_name.getText()

    def typeTextList(self, type: list_type, code: dotnet_code) -> str:
        return f"List<{self.typeText(type.item_type, code)}>"

    def typeTextMap(self, type: map_type, code) -> str:
        return f"Dictionary<{self.typeText(type.key_type, code)},{self.typeText(type.value_type, code)}>"

    def tab(self, indent=1) -> str:
        return '\t'*indent

    def documentLines(self, hinted_element: hinted_base_element, indent: int = 1) -> str:
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


class dotnet_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir

        self.__read_fileHeader(configuration)
        self.__read_defaultUsings(configuration)
        self.__read_withGrpc(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """
// <auto-generated>
//     This code was generated by d3i.interpreter
//
//     Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
// </auto-generated>"""

        if "--dotnet.file_header_lines" in configuration:
            value = configuration["--dotnet.file_header_lines"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.fileHeader = "\n".join(value)

    def __read_defaultUsings(self, configuration: Dict[str, str]):
        self.defaultUsings: List[str] = []
        if "--dotnet.default_usings" in configuration:
            value = configuration["--dotnet.default_usings"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultUsings = value

    def __read_withGrpc(self, configuration: Dict[str, str]):
        self.withGrpc: bool = False
        if "--dotnet.with_grpc" in configuration:
            self.withGrpc = bool(configuration["--dotnet.with_grpc"])


class dotnet_code:
    def __init__(self, output_path: str, subdirs: List[str], name: str):
        """
        Initializes a dotnet_code instance with the file path, file name, and content.
        """
        self.output_path = output_path
        self.fileName: str = name + ".cs"
        self.fullPath: str = os.path.join(output_path + "/".join(subdirs), self.fileName)
        self.usings: set[str] = set()
        self.content: str = ""
