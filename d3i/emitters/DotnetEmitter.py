import os
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

        # Iterate over all domain in the session
        for domain in session.main.domains:
            path: str = self.configuration.output_dir
            for context in domain.contexts:

                # Process all enum in the context
                for enum in context.enums:
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.enumText(enum, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, enum.name, content))

                # Process all value_object in the context
                for valueobject in context.value_objects:
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.valueobjectText(valueobject, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, valueobject.name, content))

                # Process all composite in the context
                for composite in context.composites:
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.compositeText(composite, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, "I"+composite.name, content))

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    for enum in aggregate.enums:
                        content: str = self.beginFile({domain.name, context.name, aggregate.name})
                        content += self.enumText(enum, indent=1)
                        content += self.endFile()
                        result.append(dotnet_code(path, enum.name, content))

                    for valueobject in aggregate.value_objects:
                        content: str = self.beginFile({domain.name, context.name, aggregate.name})
                        content += self.valueobjectText(valueobject, indent=1)
                        content += self.endFile()
                        result.append(dotnet_code(path, valueobject.name, content))

                    for aggregate_entity in aggregate.internal_entities:
                        content: str = self.beginFile({domain.name, context.name, aggregate.name})
                        content += self.entityText(aggregate_entity.entity, indent=1)
                        content += self.endFile()
                        result.append(dotnet_code(path, aggregate_entity.entity.name, content))

                # Process all view in the context
                for view in context.views:
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.viewText(view, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, view.name, content))

                # Process all acl in the context
                for acl in context.acls:
                    # interface
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.aclInterfaceText(acl, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, "I"+acl.name, content))

                    # proto
                    content = self.aclProtoFile(domain, context, acl, indent=0)
                    result.append(dotnet_code(path, acl.name, content, ".proto"))

                    # proto service file
                    content = self.aclGrpcControllerFile(domain, context, acl, indent=1)
                    result.append(dotnet_code(path, acl.name+"GrpcController", content))

                # Process all service in the context
                for service in context.services:
                    # interface
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.serviceInterfaceText(service, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, "I"+service.name, content))

                    # proto
                    content = self.serviceProtoFile(domain, context, service, indent=0)
                    result.append(dotnet_code(path, service.name, content, ".proto"))

                    # proto service file
                    content = self.serviceGrpcControllerFile(domain, context, service, indent=1)
                    result.append(dotnet_code(path, service.name+"GrpcController", content))

                # Process all inerface in the context
                for interface in context.interfaces:
                    # interface
                    content: str = self.beginFile({domain.name, context.name})
                    content += self.interfaceInterfaceText(interface, indent=1)
                    content += self.endFile()
                    result.append(dotnet_code(path, "I"+interface.name, content))

                    # proto
                    content = self.interfaceProtoFile(domain, context, interface, indent=0)
                    result.append(dotnet_code(path, interface.name, content, ".proto"))

                    # proto service file
                    content = self.interfaceGrpcControllerFile(domain, context, interface, indent=1)
                    result.append(dotnet_code(path, interface.name+"GrpcController", content))


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

    def beginFile(self, names: List[str]) -> str:
        buffer = io.StringIO()
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("\n")
        buffer.write(f"namespace {".".join(names)}\n")
        buffer.write("{\n")
        return buffer.getvalue()

    def endFile(self):
        buffer = io.StringIO()
        buffer.write("}\n")
        return buffer.getvalue()

    def enumText(self, enum: enum, indent: int = 1):
        """
        Generates the .NET code for an enum.
        """
        buffer = io.StringIO()
        buffer.write("\n")
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
        buffer.write(f"{self.tab(indent)}}}\n")
        return buffer.getvalue()

    def valueobjectText(self, valueobject: value_object, indent: int = 1):
        """
        Generates the .NET code for an value_object
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        for inherit in valueobject.inherits:
            base = utils.get_referenced_element(valueobject.parent, inherit)
            if (isinstance(base, composite) == True):
                base_composites.append(base)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, value_object) == True):
                inherit_names.append(inherit.getText())

        buffer = io.StringIO()
        buffer.write("\n")
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
            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member.name, member.type, indent+1))
            buffer.write(f"{self.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # Loop through each valueobject members and generate code for each
        for member in valueobject.members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member.name, member.type, indent+1))

        buffer.write(f"{self.tab(indent)}}}\n")

        return buffer.getvalue()

    def entityText(self, _entity: entity, indent: int = 1):
        """
        Generates the .NET code for an entity
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        hasBaseEntity = False
        for inherit in _entity.inherits:
            base = utils.get_referenced_element(_entity.parent, inherit)
            if (isinstance(base, composite) == True):
                base_composites.append(base)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, entity) == True):
                hasBaseEntity = True
                inherit_names.append(inherit.getText())

        if (hasBaseEntity == False):
            inherit_names.insert(0, "Entity")

        buffer = io.StringIO()
        buffer.write("\n")
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

        return buffer.getvalue()

    def viewText(self, _view: view, indent: int = 1):
        """
        Generates the .NET code for an view
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        hasBaseView = False
        for inherit in _view.inherits:
            base = utils.get_referenced_element(_view.parent, inherit)
            if (isinstance(base, composite) == True):
                base_composites.append(base)
                inherit_names.append(utils.join_with_I(inherit.names))
            if (isinstance(base, view) == True):
                hasBaseView = True
                inherit_names.append(inherit.getText())

        if (hasBaseView == False):
            inherit_names.insert(0, "Entity")

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

        return buffer.getvalue()

    def compositeText(self, composite: composite, indent: int = 1):
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

        return buffer.getvalue()

    def aclInterfaceText(self, acl: acl, indent: int = 1):
        """
        Generates the .NET code for acl, just the interface.
        """
        return self.interfaceClassText( acl, acl.name, acl.operations, indent)

    def serviceInterfaceText(self, service: service, indent: int = 1):
        """
        Generates the .NET code for service, just the interface.
        """
        return self.interfaceClassText( service, service.name, service.operations, indent)

    def interfaceInterfaceText(self, interface: interface, indent: int = 1):
        """
        Generates the .NET code for interface, just the interface.
        """
        return self.interfaceClassText( interface, interface.name, interface.operations, indent)

    def interfaceClassText(self, element: hinted_base_element, elementName:str, operations: List[operation], indent: int = 1):
        """
        Generates the .NET code for element, just the interface.
        """
        buffer = io.StringIO()
        buffer.write("\n")
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

        buffer.write(f"{self.tab(indent)}}}\n")
        return buffer.getvalue()

    def interfaceFunctionText(self, operation: operation, indent: int):
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
        buffer.write(f" {operation.name}( CallingContext ctx")
        # Add parameters
        if (len(operation.operation_params) > 0):
            buffer.write(f", ")
        buffer.write(", ".join([self.typeText(param.type) + " " + param.name for param in operation.operation_params]))
        buffer.write(");\n")

        return buffer.getvalue()

    def aclProtoFile(self, domain: domain, context: context, acl: acl, indent: int = 1):
        return self.protoFile( domain, context, acl, acl.name, acl.operations, indent )

    def serviceProtoFile(self, domain: domain, context: context, service: service, indent: int = 1):
        return self.protoFile( domain, context, service, service.name, service.operations, indent )

    def interfaceProtoFile(self, domain: domain, context: context, interface: interface, indent: int = 1):
        return self.protoFile( domain, context, interface, interface.name, interface.operations, indent )

    def protoFile(self, domain: domain, context: context, element: hinted_base_element, elementName: str, operations: List[operation], indent: int = 1):
        """
        Generates the proto file for element        """
        buffer = io.StringIO()

        # proto 3 syntax
        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write("syntax = \"proto3\";")
        buffer.write("\n")

        # namespace
        buffer.write("\n")
        buffer.write(f"option csharp_namespace = \"{domain.name}.{context.name}\";")
        buffer.write("\n")

        # package
        buffer.write("\n")
        buffer.write(f"package {elementName}Package\";")
        buffer.write("\n")

        # imports
        buffer.write("\n")
        buffer.write("import \"google/protobuf/empty.proto\";\n")
        buffer.write("import \"servicekit/protobuf/error.proto\";\n")
        buffer.write("\n")

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
                buffer.write(f"{self.tab(indent+2)}{self.typeText(param.type)} {param.name} = {index};\n")
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
                    buffer.write(f"{self.tab(indent+2)}{self.typeText(returns.type)} Value{index} = {index};\n")
                    index = index+1
                buffer.write(f"{self.tab(indent+2)}servicekit.protobuf.Error Error = {index};\n")

            buffer.write(f"{self.tab(1)}}}\n")
            buffer.write(f"}}\n")

        return buffer.getvalue()

    def aclGrpcControllerFile(self, domain: domain, context: context, acl: acl, indent: int = 1):
        return self.grpcControllerFile( domain, context, acl, acl.name, acl.operations, indent )

    def serviceGrpcControllerFile(self, domain: domain, context: context, service: service, indent: int = 1):
        return self.grpcControllerFile( domain, context, service, service.name, service.operations, indent )

    def interfaceGrpcControllerFile(self, domain: domain, context: context, interface: interface, indent: int = 1):
        return self.grpcControllerFile( domain, context, interface, interface.name, interface.operations, indent )

    def grpcControllerFile(self, domain: domain, context: context, element: hinted_base_element, elementName:str, operations: List[operation], indent: int = 1):
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
        buffer.write(f"namespace {domain.name}.{context.name};\n")
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
            buffer.write(f"{self.tab(indent+2)}public async Task<{operation.name}Response> {operation.name}( {operation.name}Request, ServerCallContext grpcContext)\n")
            buffer.write(f"{self.tab(indent+2)}{{\n")
            buffer.write(f"{self.tab(indent+3)}using(LogContext.PushProperty( \"Scope\", \"{elementName}.{operation.name}\" ))\n")
            buffer.write(f"{self.tab(indent+3)}{{\n")
            buffer.write(f"{self.tab(indent+4)}CallingContext ctx = grpcContext.CreateCallingContext( Logger );\n")
            buffer.write(f"{self.tab(indent+4)}try\n")
            buffer.write(f"{self.tab(indent+4)}{{\n")
            buffer.write(f"{self.tab(indent+5)}var response = await _service.{operation.name}( ctx );\n")
            buffer.write(f"{self.tab(indent+5)}\n")
            if (len(operation.operation_returns) > 0):
                index: int = 1
                for returns in operation.operation_returns:
                    buffer.write(f"{self.tab(indent+5)}if( response.HasValue{index}() == true )\n")
                    buffer.write(f"{self.tab(indent+5)}{{\n")
                    buffer.write(f"{self.tab(indent+6)}return new {operation.name}Response {{\n")
                    buffer.write(f"{self.tab(indent+7)} Value{index} = response.Value{index}\n")
                    buffer.write(f"{self.tab(indent+6)}}}\n")
                    buffer.write(f"{self.tab(indent+5)}}}\n")
                    buffer.write(f"{self.tab(indent+5)}\n")
                    index = index+1

                buffer.write(f"{self.tab(indent+5)}if( response.IsSuccess() == false )\n")
                buffer.write(f"{self.tab(indent+5)}{{\n")
                buffer.write(f"{self.tab(indent+6)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+7)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+8)}Status = response.Error.Status,\n")
                buffer.write(f"{self.tab(indent+8)}MessageText = response.Error.MessageText,\n")
                buffer.write(f"{self.tab(indent+8)}AdditionalInformation = response.Error.AdditionalInformation\n")
                buffer.write(f"{self.tab(indent+7)}}}\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+5)}\n")

                buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+6)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+7)}Status = Statuses.NotImplemented,\n")
                buffer.write(f"{self.tab(indent+7)}MessageText = \"Not handled reponse in GRPC Controller when calling '{element.name}.{operation.name}'\",\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
            else:
                buffer.write(f"{self.tab(indent+5)}if( response.IsSuccess() == true )\n")
                buffer.write(f"{self.tab(indent+5)}{{\n")
                buffer.write(f"{self.tab(indent+6)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+7)}Success = new Empty();\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+5)}else\n")
                buffer.write(f"{self.tab(indent+5)}{{\n")
                buffer.write(f"{self.tab(indent+6)}return new {operation.name}Response {{\n")
                buffer.write(f"{self.tab(indent+7)}Error = new () {{\n")
                buffer.write(f"{self.tab(indent+8)}Status = response.Error.Status,\n")
                buffer.write(f"{self.tab(indent+8)}MessageText = response.Error.MessageText,\n")
                buffer.write(f"{self.tab(indent+8)}AdditionalInformation = response.Error.AdditionalInformation\n")
                buffer.write(f"{self.tab(indent+7)}}}\n")
                buffer.write(f"{self.tab(indent+6)}}}\n")
                buffer.write(f"{self.tab(indent+5)}}}\n")
                buffer.write(f"{self.tab(indent+5)}\n")

            buffer.write(f"{self.tab(indent+5)}\n")
            buffer.write(f"{self.tab(indent+4)}}}\n")
            buffer.write(f"{self.tab(indent+4)}catch(Exception ex)\n")
            buffer.write(f"{self.tab(indent+4)}{{\n")
            buffer.write(f"{self.tab(indent+5)}return new {operation.name}Response {{\n")
            buffer.write(f"{self.tab(indent+6)}Error = new () {{\n")
            buffer.write(f"{self.tab(indent+7)}Status = InternalError,\n")
            buffer.write(f"{self.tab(indent+7)}MessageText = ex.Message,\n")
            buffer.write(f"{self.tab(indent+7)}AdditionalInformation = ex.ToString()\n")
            buffer.write(f"{self.tab(indent+6)}}}\n")
            buffer.write(f"{self.tab(indent+5)}}}\n")
            buffer.write(f"{self.tab(indent+4)}}}\n")
            buffer.write(f"{self.tab(indent+3)}}}\n")
            buffer.write(f"{self.tab(indent+2)}}}\n")

        # end of class and namepace
        buffer.write(f"{self.tab(indent)}}}\n")
        buffer.write("}")
        return buffer.getvalue()

    def propertyText(self, member_name: str, type: type, indent: int):
        buffer = io.StringIO()
        buffer.write(f"{'\t'*indent}public {self.typeText(type)} {member_name} {{ get; set; }}\n")
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

    def typeTextPrimitive(self, type: primitive_type):
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
            case primitive_type.PrimtiveKind.Boolean:
                return "bool"
            case primitive_type.PrimtiveKind.Bytes:
                return "byte[]"
            case primitive_type.PrimtiveKind.Stream:
                return "Stream"

    def typeTextReference(self, type: reference_type):
        return type.reference_name.getText()

    def typeTextList(self, type: list_type):
        return f"System.Generic.List<{self.typeText(type.item_type)}>"

    def typeTextMap(self, type: map_type):
        return f"System.Generic.Dictionary<{self.typeText(type.key_type)},{self.typeText(type.value_type)}>"

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
        self.defaultUsings: List[str] = ["System", "System.Collections.Generic"]
        if "dotnet.default_usings" in configuration:
            value = configuration["dotnet.default_usings"]
            if (isinstance(value, list) and all(isinstance(item, str) for item in value)):
                self.defaultUsings = value
        self.defaultUsings.append("PolyPersist.Net")
        self.defaultUsings.append("PolyPersist.Net.Core")
        self.defaultUsings.append("ServiceKit.Net")

    def __read_createFolderStructure(self, configuration: Dict[str, str]):
        self.createFolderStructure: bool = True
        if "dotnet.create_folder_structure" in configuration:
            self.createFolderStructure = bool(configuration["dotnet.create_folder_structure"])

    def __read_eachClassSeparateFile(self, configuration: Dict[str, str]):
        self.eachClassSeparateFile: bool = True
        if "dotnet.each_class_separate_file" in configuration:
            self.eachClassSeparateFile = bool(configuration["dotnet.each_class_separate_file"])


class dotnet_code:
    def __init__(self, directory: str, name: str, content: str, extension: str = ".cs"):
        """
        Initializes a dotnet_code instance with the file path, file name, and content.
        """
        self.fileName: str = name + extension
        self.fullPath: str = os.path.join(directory, self.fileName)
        self.content: str = content
