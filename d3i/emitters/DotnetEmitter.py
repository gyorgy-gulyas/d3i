from __future__ import annotations
# import os
import io
from typing import Dict
from typing import List
from d3i.elements.Elements import *
from d3i.Engine import *


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
                    code = self.beginFile(output_path, enum, "models")
                    code = self.enumText(enum, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all value_object in the context
                for valueobject in context.value_objects:
                    code = self.beginFile(output_path, valueobject, "models")
                    code = self.valueobjectText(valueobject, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all composite in the context
                for composite in context.composites:
                    code = self.beginFile(output_path, composite, "models")
                    code = self.compositeText(composite, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    for enum in aggregate.enums:
                        code = self.beginFile(output_path, enum, "models")
                        code = self.enumText(enum, code)
                        code = self.endFile(code)
                        result.append(code)

                    for valueobject in aggregate.value_objects:
                        code = self.beginFile(output_path, valueobject, "models")
                        code = self.valueobjectText(valueobject, code)
                        code = self.endFile(code)
                        result.append(code)

                    for aggregate_entity in aggregate.internal_entities:
                        code = self.beginFile(output_path, aggregate_entity.entity, "models")
                        code = self.entityText(aggregate_entity.entity, code)
                        code = self.endFile(code)
                        result.append(code)

                # Process all view in the context
                for view in context.views:
                    code = self.beginFile(output_path, view, "models")
                    code = self.viewText(view, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all acl in the context
                for acl in context.acls:
                    # interface
                    code = self.beginFile(output_path, acl, "Service/interfaces")
                    code = self.aclInterfaceText(acl, code)
                    code = self.endFile(code)
                    result.append(code)

                    # grpc controller file
                    # content = self.aclGrpcControllerFile(domain, context, acl, indent=1)
                    # result.append(dotnet_code(output_path, [domain.name, context.name, acl.name, "Service/controllers"], acl.name+"GrpcController", content))

                # Process all service in the context
                for service in context.services:
                    # interface
                    code = self.beginFile(output_path, service, "Service/interfaces")
                    code = self.serviceInterfaceText(service, code)
                    code = self.endFile(code)
                    result.append(code)

                    # grpc controller file
                    # content = self.serviceGrpcControllerFile(domain, context, service, indent=1)
                    # result.append(dotnet_code(output_path, [domain.name, context.name, service.name, "Service/controllers"], service.name+"GrpcController", content))

                # Process all inerface in the context
                for interface in context.interfaces:
                    # interface
                    code = self.beginFile(output_path, interface, "Service/interfaces")
                    code = self.interfaceInterfaceText(interface, code)
                    code = self.endFile(code)
                    result.append(code)

                    # grpc controller file
                    # content = self.interfaceGrpcControllerFile(domain, context, interface, indent=1)
                    # result.append(dotnet_code(output_path, [domain.name, context.name, interface.name, "Service/controllers"], interface.name+"GrpcController", content))

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

    def beginFile(self, output_path: str, element: base_element, subDirectoryName: str) -> dotnet_code:
        buffer = io.StringIO()
        domain: domain = element.getDomain()
        context: context = element.getContext()

        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("<ADDITIONAL_USINGS>")
        buffer.write("\n")
        buffer.write(f"namespace {domain.name}.{context.name}\n")
        buffer.write("{\n")

        code: dotnet_code = dotnet_code(output_path, [domain.name, context.name, subDirectoryName], element.name)
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
        return code

    def collectBaseCompositsRecursive(self, base_composite: composite, base_composites: List[composite]):
        base_composites.insert(0, base_composite)

        for inherit in base_composite.inherits:
            base = utils.get_referenced_element(base_composite.parent, inherit)
            if (isinstance(base, composite) == True):
                self.collectBaseCompositsRecursive(base, base_composites)

    def valueobjectText(self, valueobject: value_object, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an value_object
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        for inherit in valueobject.inherits:
            base = utils.get_referenced_element(valueobject.parent, inherit)
            if (isinstance(base, composite) == True):
                self.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, value_object) == True):
                inherit_names.append(inherit.getText())

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(valueobject, indent))
        # Write the value_object declaration with indentation
        buffer.write(f"{self.tab(indent)}public class {valueobject.name}")
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
                buffer.write(self.propertyText(member.name, member.type, indent+1))
            buffer.write(f"{self.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # write internal enums if Any
        if (valueobject.withEnum == True):
            for enum in valueobject.enums:
                buffer.write(self.enumText(enum, indent))

        # write internal valueobjects if Any
        if (valueobject.withValueObject == True):
            for valueobject in valueobject.value_objects:
                buffer.write(self.valueobjectText(valueobject, indent))

        # write internal valueobjects if Any
        if (valueobject.withDto == True):
            for dto in valueobject.dtos:
                buffer.write(self.dtoText(dto, indent))

        # Loop through each valueobject members and generate code for each
        for member in valueobject.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def dtoText(self, dto: dto, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an dto
        """
        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(dto, indent))
        # Write the value_object declaration with indentation
        buffer.write(f"{self.tab(indent)}public class {dto.name}")
        buffer.write(f"\n{self.tab(indent)}{{\n")

        # Loop through each valueobject members and generate code for each
        for member in dto.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def entityText(self, _entity: entity, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an entity
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        hasBaseEntity = False
        for inherit in _entity.inherits:
            base = utils.get_referenced_element(_entity.parent, inherit)
            if (isinstance(base, composite) == True):
                self.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, entity) == True):
                hasBaseEntity = True
                inherit_names.append(inherit.getText())

        buffer = io.StringIO()
        if (hasBaseEntity == False):
            inherit_names.insert(0, "Entity")
            code.usings.add("PolyPersist.Net.Core")
            
        # Add documentation lines for the composite
        buffer.write(self.documentLines(_entity, indent))
        # Write the entity declaration with indentation
        buffer.write(f"{self.tab(indent)}public partial class {_entity.name}")
        # Write inherits if any
        if (len(inherit_names)):
            buffer.write(" : ")
            buffer.write(", ".join(inherit_names))
        buffer.write(f"\n{self.tab(indent)}{{\n")

        # Loop through each coposite members and generate code for each
        for base_composite in base_composites:
            buffer.write(f"{self.tab(indent+1)}#region I{base_composite.name}\n")
            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member.name, member.type, indent+1))
            buffer.write(f"{self.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # Loop through each entity members and generate code for each
        for member in _entity.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def viewText(self, _view: view, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an view
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        hasBaseView = False
        for inherit in _view.inherits:
            base = utils.get_referenced_element(_view.parent, inherit)
            if (isinstance(base, composite) == True):
                self.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, view) == True):
                hasBaseView = True
                inherit_names.append(inherit.getText())

        if (hasBaseView == False):
            inherit_names.insert(0, "Entity")
            code.usings.add("PolyPersist.Net.Core")

        buffer = io.StringIO()
        buffer.write("\n")
        # Add documentation lines for the composite
        buffer.write(self.documentLines(_view, indent))
        # Write the view declaration with indentation
        buffer.write(f"{self.tab(indent)}public partial class {_view.name}")
        # Write inherits if any
        if (len(inherit_names)):
            buffer.write(" : ")
            buffer.write(", ".join(inherit_names))
        buffer.write(f"\n{self.tab(indent)}{{\n")

        # Loop through each coposite members and generate code for each
        for base_composite in base_composites:
            buffer.write(f"{self.tab(indent+1)}#region I{base_composite.name}\n")
            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member.name, member.type, indent+1))
            buffer.write(f"{self.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # Loop through each view members and generate code for each
        for member in _view.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

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
            buffer.write(self.propertyText(member.name, member.type, indent+1))
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
        buffer.write(f"{self.tab(indent)}public interface I{elementName}\n")
        buffer.write(f"{self.tab(indent)}{{\n")

        # Loop through each operations and generate code for each
        for operation in operations:
            # Write each operation
            buffer.write(self.interfaceFunctionText(operation, indent+1))
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

    def interfaceFunctionText(self, operation: operation, indent: int) -> str:
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
                code = status_decorator.params[0].value
                if (len(returns.document_lines) == 1):
                    buffer.write(f"{self.tab(indent)}/// <response code='{code}'>{returns.document_lines[0]}</response>\n")
                elif (len(returns.document_lines) > 1):
                    buffer.write(f"{self.tab(indent)}/// <response code='{code}'>\n")
                    for line in returns.document_lines:
                        buffer.write(f"{self.tab(indent)}/// {line}\n")
                    buffer.write(f"{self.tab(indent)}/// </response>\n")

        # Add return value
        buffer.write(f"{self.tab(indent)}public Response")
        if (len(operation.operation_returns) > 0):
            buffer.write("<")
            buffer.write(", ".join(self.typeText(item.type) for item in operation.operation_returns))
            buffer.write(">")
        # Add function name
        buffer.write(f" {operation.name}(CallingContext ctx")
        # Add parameters
        if (len(operation.operation_params) > 0):
            buffer.write(f", ")
        buffer.write(", ".join([self.typeText(param.type) + " " + param.name for param in operation.operation_params]))
        buffer.write(");\n")

        return buffer.getvalue()

    def aclGrpcControllerFile(self, domain: domain, context: context, acl: acl, indent: int = 1):
        return self.grpcControllerFile(domain, context, acl, acl.name, acl.operations, indent)

    def serviceGrpcControllerFile(self, domain: domain, context: context, service: service, indent: int = 1):
        return self.grpcControllerFile(domain, context, service, service.name, service.operations, indent)

    def interfaceGrpcControllerFile(self, domain: domain, context: context, interface: interface, indent: int = 1):
        return self.grpcControllerFile(domain, context, interface, interface.name, interface.operations, indent)

    def grpcControllerFile(self, domain: domain, context: context, element: hinted_base_element, elementName: str, operations: List[operation], indent: int = 1):
        """
        Generates the .NET GRPC controller code for acl
        """
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write(f"using Google.Protobuf.WellKnownTypes;\n")
        buffer.write(f"using Grpc.Core;\n")
        buffer.write("\n")
        buffer.write(f"namespace {domain.name}.{context.name}\n")
        buffer.write("{\n")

        # Add documentation lines for the acl
        buffer.write(self.documentLines(element, indent))
        # class declaration
        buffer.write(f"{self.tab(indent)}public class {elementName}GrpcController : {domain.name}.{context.name}.{elementName}Package.{element.name}Base \n")
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
            buffer.write(f"{self.tab(indent+1)}public async Task<{operation.name}Response> {operation.name}( {operation.name}Request request, ServerCallContext grpcContext)\n")
            buffer.write(f"{self.tab(indent+1)}{{\n")
            buffer.write(f"{self.tab(indent+2)}using(LogContext.PushProperty( \"Scope\", \"{elementName}.{operation.name}\" ))\n")
            buffer.write(f"{self.tab(indent+2)}{{\n")
            buffer.write(f"{self.tab(indent+3)}CallingContext ctx = grpcContext.CreateCallingContext( Logger );\n")
            buffer.write(f"{self.tab(indent+3)}try\n")
            buffer.write(f"{self.tab(indent+3)}{{\n")
            buffer.write(f"{self.tab(indent+4)}var response = await _service.{operation.name}( ctx );\n")
            buffer.write(f"{self.tab(indent+4)}\n")
            if (len(operation.operation_returns) > 0):
                index: int = 1
                for returns in operation.operation_returns:
                    buffer.write(f"{self.tab(indent+4)}if( response.HasValue{index}() == true )\n")
                    buffer.write(f"{self.tab(indent+4)}{{\n")
                    buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{ Value{index} = response.Value{index} }};\n")
                    buffer.write(f"{self.tab(indent+4)}}}\n")
                    buffer.write(f"{self.tab(indent+4)}\n")
                    index = index+1

                buffer.write(f"{self.tab(indent+4)}if( response.IsSuccess() == false )\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+7)}Status = response.Error.Status,\n")
                buffer.write(f"{self.tab(indent+7)}MessageText = response.Error.MessageText,\n")
                buffer.write(f"{self.tab(indent+7)}AdditionalInformation = response.Error.AdditionalInformation\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}};\n")
                buffer.write(f"{self.tab(indent+4)}}}\n")
                buffer.write(f"{self.tab(indent+4)}\n")

                buffer.write(f"{self.tab(indent+4)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+5)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+6)}Status = Statuses.NotImplemented,\n")
                buffer.write(f"{self.tab(indent+6)}MessageText = \"Not handled reponse in GRPC Controller when calling '{element.name}.{operation.name}'\",\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+4)}}};\n")
            else:
                buffer.write(f"{self.tab(indent+4)}if( response.IsSuccess() == true )\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Success = new Empty();\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+4)}}}\n")
                buffer.write(f"{self.tab(indent+4)}else\n")
                buffer.write(f"{self.tab(indent+4)}{{\n")
                buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{\n")
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
            buffer.write(f"{self.tab(indent+4)}return new {operation.name}Response {{\n")
            buffer.write(f"{self.tab(indent+5)}Error = new () {{\n")
            buffer.write(f"{self.tab(indent+6)}Status = InternalError,\n")
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

        # end of class and namepace
        buffer.write(f"{self.tab(indent)}}}\n")
        buffer.write("}")
        return buffer.getvalue()

    def propertyText(self, member_name: str, type: type, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"{'\t'*indent}public {self.typeText(type)} {member_name} {{ get; set; }}\n")
        return buffer.getvalue()

    def typeText(self, type: type) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type)
            case type.Kind.Reference:
                return self.typeTextReference(type)
            case type.Kind.List:
                return self.typeTextList(type)
            case type.Kind.Map:
                return self.typeTextMap(type)

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

    def typeTextReference(self, type: reference_type) -> str:
        return type.reference_name.getText()

    def typeTextList(self, type: list_type) -> str:
        return f"List<{self.typeText(type.item_type)}>"

    def typeTextMap(self, type: map_type) -> str:
        return f"Dictionary<{self.typeText(type.key_type)},{self.typeText(type.value_type)}>"

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
    def get_referenced_element(parent: base_element, name: qualified_name) -> IScope:

        scope = utils.__get_current_scope(parent)
        element = None
        # go up until we find the element for the first part of the name
        while True:
            if (scope == None):
                break

            # is the scope that has a child with the name we are looking for
            if (isinstance(scope, IScope) == True):
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


class dotnet_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir

        self.__read_fileHeader(configuration)
        self.__read_defaultUsings(configuration)
        self.__read_createFolderStructure(configuration)
        self.__read_eachClassSeparateFile(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
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

    def __read_defaultUsings(self, configuration: Dict[str, str]):
        self.defaultUsings: List[str] = []
        if "dotnet.default_usings" in configuration:
            value = configuration["dotnet.default_usings"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultUsings = value

    def __read_createFolderStructure(self, configuration: Dict[str, str]):
        self.createFolderStructure: bool = True
        if "dotnet.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["dotnet.create_folder_structure"])

    def __read_eachClassSeparateFile(self, configuration: Dict[str, str]):
        self.eachClassSeparateFile: bool = True
        if "dotnet.each_class_separate_file" in configuration:
            self.eachClassSeparateFile = bool(configuration["dotnet.each_class_separate_file"])


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
