from __future__ import annotations
import io
import re
from typing import Dict
from typing import List
from typing import NamedTuple
from d3i.elements.Elements import *
from d3i.Engine import *
from d3i.emitters.utils import *


# '@timeout( "1h30m" )' - the pieces of a duration and what each unit is worth in milliseconds.
# 'ms' comes first in the alternation so it wins over 'm'.
DURATION_PARTS = re.compile(r"(\d+)(ms|s|m|h|d)")
DURATION_UNITS = {"ms": 1, "s": 1000, "m": 60 * 1000, "h": 60 * 60 * 1000, "d": 24 * 60 * 60 * 1000}


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

        with open(code.fullPath, "w", encoding='utf-8') as file:
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
                    code = self.beginFile(output_path, composite, "Models", prefix="I")
                    code = self.compositeText(composite, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process the facts owned by the context itself. An event is not nested in
                # the producing service's contract: a consumer must be able to name the fact
                # without naming who produced it.
                for context_event in context.events:
                    code = self.beginFile(output_path, context_event, "Events", postfix=self.eventPostfix(context_event))
                    code = self.eventText(context_event, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all aggregate in the context
                for aggregate in context.aggregates:
                    # The facts the root records. The stream key is the root identity, so
                    # these belong to the aggregate and travel with it.
                    for aggregate_event in aggregate.events:
                        code = self.beginFile(output_path, aggregate_event, "Events", postfix=self.eventPostfix(aggregate_event))
                        code = self.eventText(aggregate_event, code)
                        code = self.endFile(code)
                        result.append(code)

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
                    code = self.beginFile(output_path, acl, "Context/Interfaces", prefix="I")
                    code = self.aclInterfaceText(acl, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all service in the context
                for service in context.services:
                    # interface
                    code = self.beginFile(output_path, service, "Context/Interfaces", prefix="I")
                    code = self.serviceInterfaceText(service, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all repository in the context
                for service in context.repositories:
                    # interface
                    code = self.beginFile(output_path, service, "Context/Interfaces", prefix="I")
                    code = self.repositoryInterfaceText(service, code)
                    code = self.endFile(code)
                    result.append(code)

                # Process all inerface in the context
                for interface in context.interfaces:
                    # Service interface for DTOs, for controllers, for the expected implementation
                    code = self.beginFile(output_path, interface, "Interfaces", prefix="I", postfix=f"_v{interface.version}")
                    code = self.interfaceInterfaceText(interface, code)
                    code = self.endFile(code)
                    result.append(code)
                    # Service: GRPC controller
                    if( utils.isPublishedOn( interface, "grpc" ) == True):
                        code = self.beginFile(output_path, interface, "Context/Controllers", postfix=f"_v{interface.version}.GrpcController")
                        code = self.interfaceGrpcControllerText(interface, code)
                        code = self.endFile(code)
                        result.append(code)
                    # Service: GRPC InternalClient for service-service communication
                    if( utils.isPublishedOnInternal( interface, "grpc" ) == True):
                        code = self.beginFile(output_path, interface, "InternalClient", postfix=f"_v{interface.version}.GrpcClient")
                        code = self.interfaceGrpcInternalClientText(interface, code)
                        code = self.endFile(code)
                        result.append(code)
                    # Client: GRPC public client for client-service communication
                    apiCollectionName: str = utils.isPublishedOnPublic( interface, "grpc" )
                    if( apiCollectionName != None ):
                        code = self.beginFile(os.path.join(output_path, "ApiClientKit/", apiCollectionName ), interface, "", postfix=f"_v{interface.version}.GrpcClient", current_namespace=f"{apiCollectionName}.ApiClientKit")
                        code = self.interfaceGrpcPublicClientText(interface, code)
                        code = self.endFile(code)
                        result.append(code)
                    # Service: REST controller
                    if( utils.isPublishedOn( interface, "rest" ) == True):
                        code = self.beginFile(output_path, interface, "Context/Controllers", postfix=f"_v{interface.version}.RestController")
                        code = self.interfaceRestControllerText(interface, code)
                        code = self.endFile(code)
                        result.append(code)
                    # Service: REST InternalClient for service-service communication
                    if( utils.isPublishedOnInternal( interface, "rest" ) == True):
                        code = self.beginFile(output_path, interface, "InternalClient", postfix=f"_v{interface.version}.RestClient")
                        code = self.interfaceRestInternalClientText(interface, code)
                        code = self.endFile(code)
                        result.append(code)
                    # Client: REST public client for client-service communication
                    apiCollectionName: str = utils.isPublishedOnPublic( interface, "rest" )
                    if( apiCollectionName != None ):
                        code = self.beginFile(os.path.join(output_path, "ApiClientKit/", apiCollectionName ), interface, "", postfix=f"_v{interface.version}.RestClient", current_namespace=f"{apiCollectionName}.ApiClientKit")
                        code = self.interfaceRestPublicClientText(interface, code)
                        code = self.endFile(code)
                        result.append(code)

                # Process all workflow in the context. Only the .NET backend emits workflows: a
                # workflow is not a transport surface, so proto and TypeScript stay out of it.
                for the_workflow in context.workflows:
                    if (len(the_workflow.steps) > 0):
                        # activity interface - the implementation is the developer's
                        code = self.beginFile(output_path, the_workflow, "Context/Workflows", prefix="I", postfix="Activities")
                        code = self.workflowActivitiesInterfaceText(the_workflow, code)
                        code = self.endFile(code)
                        result.append(code)
                        # per step activity options built from @retry / @timeout
                        code = self.beginFile(output_path, the_workflow, "Context/Workflows", postfix="Defaults")
                        code = self.workflowDefaultsText(the_workflow, code)
                        code = self.endFile(code)
                        result.append(code)

                    # the workflow class itself, plus the saga-aware step facade
                    code = self.beginFile(output_path, the_workflow, "Context/Workflows", postfix="Workflow")
                    code = self.workflowClassText(the_workflow, code)
                    code = self.endFile(code)
                    result.append(code)

                    # worker and DI registration, task queue = "<context>.<workflow>"
                    code = self.beginFile(output_path, the_workflow, "Context/Workflows", postfix="Registration")
                    code = self.workflowRegistrationText(the_workflow, code)
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

    def beginFile(self, output_path: str, element: base_element, subDirectoryName: str, prefix: str = "", postfix: str = "", current_namespace:str=None) -> dotnet_code:
        buffer = io.StringIO()
        domain: domain = element.getDomain()
        context: context = element.getContext()
        aggregate: aggregate = element.getAggregate()

        buffer.write(self.fileHeader())
        buffer.write("\n")
        buffer.write(self.defaultUsings())
        buffer.write("<ADDITIONAL_USINGS>")
        buffer.write("\n")

        # set current_namespace
        if(current_namespace == None):
            current_namespace:str = f"{domain.name}.{context.name}"
            if (aggregate != None):
                current_namespace = current_namespace + f".{aggregate.name}"

        buffer.write(f"namespace {current_namespace}\n")
        buffer.write("{\n")

        output_path = output_path if output_path.endswith('/') else output_path + '/'
        code: dotnet_code = dotnet_code(output_path, [domain.name, context.name, subDirectoryName], prefix + element.name + postfix, current_namespace )
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
        buffer.write(f"{utils.tab(indent)}public enum {enum.name}\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # Loop through each enum element and generate code for each
        for enum_element in enum.enum_elements:
            buffer.write(self.documentLines(enum_element, indent+1))
            # Write each enum element value
            buffer.write(f"{utils.tab(indent+1)}{enum_element.value},\n")
            if (len(enum_element.document_lines) > 0):
                buffer.write("\n")

        buffer.write(f"{utils.tab(indent)}}}\n")

        # if the enum is defined under the interface and the grpc mapping is enable, then generate the mapping code
        if (enum.getInterface() != None and utils.isPublishedOn( enum.getInterface(), "grpc" ) == True):
            buffer.write(self.enumGrpcMappingText(enum, code, indent))

        code.content += buffer.getvalue()
        return code

    def enumGrpcMappingText(self, enum: enum, code:dotnet_code, indent: int) -> str:
        """
        Generates the .NET code for an enum mapping for GRPC.
        """
        dotnetFullName: str = code.getDotnetFullName(enum)
        protosFullName: str = grpc_utils.getProtoFullName(enum)

        buffer = io.StringIO()
        buffer.write(f"{utils.tab(indent)}#region GrpcMapping\n")
        buffer.write(f"{utils.tab(indent)}public static class {enum.name}Mappings\n")
        buffer.write(f"{utils.tab(indent)}{{\n")

        # ToGrpc
        buffer.write(f"{utils.tab(indent+1)}public static Protos.{protosFullName} ToGrpc( {dotnetFullName} @this )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}return @this switch\n")
        buffer.write(f"{utils.tab(indent+2)}{{\n")
        # Loop through each enum element and generate code for each mapping
        for enum_element in enum.enum_elements:
            buffer.write(f"{utils.tab(indent+3)}{dotnetFullName}.{enum_element.value} => Protos.{protosFullName}.{grpc_utils.to_grpc_enum_style(enum_element.value)},\n")
        buffer.write(f"{utils.tab(indent+3)}_ => throw new NotImplementedException(), \n")
        buffer.write(f"{utils.tab(indent+2)}}};\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"\n")

        # FromGrpc
        buffer.write(f"{utils.tab(indent+1)}public static {dotnetFullName} FromGrpc( Protos.{protosFullName} @this )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}return @this switch\n")
        buffer.write(f"{utils.tab(indent+2)}{{\n")
        # Loop through each enum element and generate code for each mapping
        for enum_element in enum.enum_elements:
            buffer.write(f"{utils.tab(indent+3)}Protos.{protosFullName}.{grpc_utils.to_grpc_enum_style(enum_element.value)} => {dotnetFullName}.{enum_element.value},\n")
        buffer.write(f"{utils.tab(indent+3)}_ => throw new NotImplementedException(), \n")
        buffer.write(f"{utils.tab(indent+2)}}};\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"\n")

        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}#endregion GrpcMapping\n")

        return buffer.getvalue()

    def valueobjectText(self, valueobject: value_object, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(valueobject, valueobject.inherits, valueobject.name, valueobject.members, code, indent=indent)

    def entityText(self, entity: entity, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(entity, entity.inherits, entity.name, entity.members, code, indent=indent)

    def viewText(self, view: view, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(view, view.inherits, view.name, view.members, code, indent=indent)

    def dtoText(self, dto: dto, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(dto, dto.inherits, dto.name, dto.members, code, indent=indent)

    def eventPostfix(self, the_event: event) -> str:
        return "" if the_event.version == None else f"_v{the_event.version}"

    def eventClassName(self, the_event: event) -> str:
        # An unversioned event is an internal fact that promises compatibility to nobody,
        # so its class carries no version suffix either. See D3I-50.
        if (the_event.version == None):
            return the_event.name
        return the_event.name + f"_v{the_event.version}"

    def eventText(self, event: event, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.dataClassText(event, event.inherits, self.eventClassName(event), event.members, code, indent=indent)

    def dataClassText(self, element: internal_scoped_base_element, inherits: List[qualified_name], name: str, members: List[hinted_base_element], code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for an data object
        """
        base_composites: List[composite] = []
        inherit_names: List[str] = []
        for inherit in inherits:
            base = Engine.get_referenced_element(element.parent, inherit)
            if (isinstance(base, composite) == True):
                utils.collectBaseCompositsRecursive(base, base_composites)
                inherit_names.append(utils.join_with_I(inherit.names))
            else:
                inherit_names.append(inherit.getText())
        inherit_names.append( f"IEquatable<{name}>")

        # collect members carrying a `validate` rule, and the members the walk has to step INTO
        # (inlined composite members + own members). A member is stepped into only when its type
        # really carries a rule, so a class of plain fields costs nothing.
        validate_members: List[hinted_base_element] = []
        cascade_members: List[hinted_base_element] = []
        for base_composite in base_composites:
            for composite_member in base_composite.members:
                if (getattr(composite_member, "validate_ast", None) != None):
                    validate_members.append(composite_member)
                if (self.__typeHasValidate(composite_member.type, set())):
                    cascade_members.append(composite_member)
        for own_member in members:
            if (getattr(own_member, "validate_ast", None) != None):
                validate_members.append(own_member)
            if (self.__typeHasValidate(own_member.type, set())):
                cascade_members.append(own_member)
        # does a non-composite base CLASS validate? then we override its walk and chain base
        base_has_validate = False
        for inherit in inherits:
            base = Engine.get_referenced_element(element.parent, inherit)
            if (base != None and isinstance(base, composite) == False and self.__classHasValidate(base)):
                base_has_validate = True
                break
        if (len(validate_members) > 0 or len(cascade_members) > 0):
            code.usings.add("PolyPersist")
            code.usings.add("PolyPersist.Net.Common")
            if (base_has_validate == False):
                inherit_names.append("IValidable")   # a base class already declares it otherwise

        buffer = io.StringIO()
        # Add documentation lines for the composite
        buffer.write(self.documentLines(element, indent))
        buffer.write(self.deprecatedText(element, indent))   # @deprecated -> [Obsolete]
        # Write the data class declaration with indentation
        buffer.write(f"{utils.tab(indent)}public partial class {name} : {", ".join(inherit_names)}\n")
        buffer.write(f"{utils.tab(indent)}{{\n")

        # flush current text
        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        # Loop through each coposite members and generate code for each
        for base_composite in base_composites:
            buffer.write(f"{utils.tab(indent+1)}#region I{base_composite.name}\n")

            # write internal enums if Any
            if (base_composite.withEnum == True):
                for child_enum in base_composite.enums:
                    code = self.enumText(child_enum, code, indent+1)

            # write internal value object if Any
            if (base_composite.withValueObject == True):
                for child_value_object in base_composite.value_objects:
                    code = self.valueobjectText(child_value_object, code, indent+1)

            # write internal dto if Any
            if (base_composite.withDto == True):
                for child_dto in base_composite.dtos:
                    code = self.dtoText(child_dto, code, indent+1)

            for member in base_composite.members:
                # Write each member
                buffer.write(self.documentLines(member, indent+1))
                buffer.write(self.propertyText(member, code, indent+1))
            buffer.write(f"{utils.tab(indent+1)}#endregion I{base_composite.name}\n\n")

        # write internal enums if Any
        if (element.withEnum == True):
            for child_enum in element.enums:
                code = self.enumText(child_enum, code, indent+1)

        # write internal valueobjects if Any
        if (element.withValueObject == True):
            for child_valueobject in element.value_objects:
                code = self.valueobjectText(child_valueobject, code, indent+1)

        # write internal dto if Any
        if (element.withDto == True):
            for child_dto in element.dtos:
                code = self.dtoText(child_dto, code, indent+1)

        # Loop through each valueobject members and generate code for each
        for member in members:
            # Write each member
            buffer.write(self.documentLines(member, indent+1))
            buffer.write(self.propertyText(member, code, indent+1))

        # clone
        buffer.write(self.dataClassCloneText(element, inherits, name, members, code, indent+1))

        # Equal and HashCode
        buffer.write(self.dataClassEqualsAndHashCodeText(element, inherits, name, members, code, indent+1))

        # Validation (IValidable) — when a member carries a `validate` rule, or holds something
        # that does. If a base class also validates, override its walk and chain base first.
        if (len(validate_members) > 0 or len(cascade_members) > 0):
            buffer.write(self.dataClassValidateText(name, validate_members, cascade_members, code, base_has_validate, indent+1))

        if ( utils.isPublishedOn(element.getInterface(), "grpc" ) == True and isinstance(element,dto)):
            buffer.write(self.dtoGrpcMappingText(element, code, indent+1))

        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"\n")

        code.content += buffer.getvalue()
        return code

    def __classHasValidate(self, element, seen: set = None) -> bool:
        # True when the class carries validation at all: its own rules, the rules of an inlined
        # composite, the rules of a base CLASS - or the rules of something it CONTAINS. The last
        # one is what makes the value object self-validating: an order with a `quantity > 0` rule
        # on its items validates, even though the order itself declares no rule of its own.
        # `seen` guards the TYPE graph, so a value object that refers to itself terminates.
        if (element == None):
            return False
        if (seen == None):
            seen = set()
        if (id(element) in seen):
            return False
        seen.add(id(element))

        for member in getattr(element, "members", []):
            if (getattr(member, "validate_ast", None) != None):
                return True
            if (self.__typeHasValidate(getattr(member, "type", None), seen)):
                return True
        for inherit in getattr(element, "inherits", []):
            base = Engine.get_referenced_element(element.parent, inherit)
            if (base == None):
                continue
            if (isinstance(base, composite)):
                base_composites: List[composite] = []
                utils.collectBaseCompositsRecursive(base, base_composites)
                for base_composite in base_composites:
                    for member in base_composite.members:
                        if (getattr(member, "validate_ast", None) != None):
                            return True
                        if (self.__typeHasValidate(getattr(member, "type", None), seen)):
                            return True
            elif (self.__classHasValidate(base, seen)):
                return True
        return False

    def __typeHasValidate(self, member_type: type, seen: set) -> bool:
        # Does a value of this type carry validation? A `ref` does not - it is an identity, not a
        # nested object - and neither does a primitive. A list/map asks about what it holds.
        if (member_type == None):
            return False
        if (member_type.kind == type.Kind.Reference):
            return self.__classHasValidate(self.__validatableTarget(member_type), seen)
        if (member_type.kind == type.Kind.List):
            return self.__typeHasValidate(member_type.item_type, seen)
        if (member_type.kind == type.Kind.Map):
            return self.__typeHasValidate(member_type.value_type, seen)
        return False

    def __validatableTarget(self, member_type: type):
        # The element a reference type points at, but only when it is one of the kinds that get a
        # generated data class (and so a ValidateInto to walk into). A composite is inlined into
        # its consumers and emitted as an interface, so there is nothing to call on it.
        if (member_type == None or member_type.kind != type.Kind.Reference):
            return None
        referenced = Engine.get_referenced_element(member_type.parent, member_type.reference_name)
        if (isinstance(referenced, (value_object, entity, dto, view, event))):
            return referenced
        return None

    def dataClassValidateText(self, name: str, validate_members: List[hinted_base_element], cascade_members: List[hinted_base_element], code: dotnet_code, call_base: bool, indent: int = 1) -> str:
        # Generates the validation of a data class in two parts.
        #
        # `Validate` is the contract (PolyPersist.IValidable) and the entry point: it starts the
        # walk with an empty path. `ValidateInto` IS the walk - it records this object's own
        # failures and then steps into whatever it holds, extending the path as it goes. The split
        # is what lets an error say `items[1].quantity`: only the walk knows where it currently is,
        # and only the entry point knows where the caller started.
        #
        # Inheritance declares `Validate` ONCE, on the topmost validating class; a derived class
        # overrides the WALK, so the entry point stays a single, unambiguous method.
        #
        # Each rule becomes an `if (<violated>)`: the guard is the NEGATION of the rule folded into
        # the operators (so `value > 0` reads `amount <= 0`, not `!(amount > 0)`) with bare field
        # names and only the parentheses precedence needs.
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}#region Validation\n")
        if (call_base == False):
            buffer.write(f"{utils.tab(indent)}public virtual bool Validate( IList<IValidationError> errors )\n")
            buffer.write(f"{utils.tab(indent)}{{\n")
            buffer.write(f"{utils.tab(indent+1)}int before = errors.Count;\n")
            buffer.write(f"{utils.tab(indent+1)}ValidateInto( errors, string.Empty );\n")
            buffer.write(f"{utils.tab(indent+1)}return errors.Count == before;\n")
            buffer.write(f"{utils.tab(indent)}}}\n")
            buffer.write(f"\n")

        modifier = "override" if call_base else "virtual"
        buffer.write(f"{utils.tab(indent)}public {modifier} void ValidateInto( IList<IValidationError> errors, string pathPrefix )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        written = False
        if (call_base):
            buffer.write(f"{utils.tab(indent+1)}base.ValidateInto( errors, pathPrefix );\n")
            written = True

        for member in validate_members:
            violated = self.__validateViolation(member.validate_ast, member, code)
            if (member.find_decorator("optional") != None):
                violated = f"{member.name} != null && ({violated})"
            message = self.__validateRuleText(member.validate_ast).replace("\\", "\\\\").replace("\"", "\\\"")
            if (written):
                buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent+1)}if ({violated})\n")
            buffer.write(f"{utils.tab(indent+2)}errors.Add( new ValidationError {{ TypeOfEntity = \"{name}\", MemberOfEntity = \"{member.name}\", Path = pathPrefix + \"{member.name}\", ErrorText = \"{member.name} must satisfy: {message}\" }} );\n")
            written = True

        for member in cascade_members:
            if (written):
                buffer.write(f"\n")
            buffer.write(self.dataClassMemberValidateIntoText(member, code, indent+1))
            written = True

        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}#endregion Validation\n")
        return buffer.getvalue()

    def dataClassMemberValidateIntoText(self, member: hinted_base_element, code: dotnet_code, indent: int) -> str:
        # The walk into one member. The path segment is the member's own name, so a UI reading
        # `items[1].quantity` can bind straight to the control that is wrong.
        buffer = io.StringIO()
        member_type: type = member.type
        if (member_type.kind == type.Kind.Reference):
            buffer.write(f"{utils.tab(indent)}{member.name}?.ValidateInto( errors, pathPrefix + \"{member.name}.\" );\n")
        elif (member_type.kind == type.Kind.List):
            buffer.write(f"{utils.tab(indent)}if ({member.name} != null)\n")
            buffer.write(f"{utils.tab(indent)}{{\n")
            buffer.write(f"{utils.tab(indent+1)}for (int index = 0; index < {member.name}.Count; index++)\n")
            buffer.write(f"{utils.tab(indent+2)}{member.name}[index]?.ValidateInto( errors, $\"{{pathPrefix}}{member.name}[{{index}}].\" );\n")
            buffer.write(f"{utils.tab(indent)}}}\n")
        elif (member_type.kind == type.Kind.Map):
            buffer.write(f"{utils.tab(indent)}if ({member.name} != null)\n")
            buffer.write(f"{utils.tab(indent)}{{\n")
            buffer.write(f"{utils.tab(indent+1)}foreach (var pair in {member.name})\n")
            buffer.write(f"{utils.tab(indent+2)}pair.Value?.ValidateInto( errors, $\"{{pathPrefix}}{member.name}[{{pair.Key}}].\" );\n")
            buffer.write(f"{utils.tab(indent)}}}\n")
        return buffer.getvalue()

    # C# for "the rule is VIOLATED" (negation folded into the operators)
    def __validateViolation(self, node: validate_node, member: hinted_base_element, code: dotnet_code) -> str:
        if (isinstance(node, validate_binary)):
            if (node.op == "and"):
                return f"{self.__violationOperand(node.left, member, code)} || {self.__violationOperand(node.right, member, code)}"
            if (node.op == "or"):
                return f"{self.__violationOperand(node.left, member, code)} && {self.__violationOperand(node.right, member, code)}"
            flipped = {"<": ">=", "<=": ">", ">": "<=", ">=": "<", "==": "!=", "!=": "=="}[node.op]
            return f"{self.__validateValue(node.left, member, code)} {flipped} {self.__validateValue(node.right, member, code)}"
        if (isinstance(node, validate_not)):
            return self.__validateTruth(node.operand, member, code)
        if (isinstance(node, validate_in_range) or isinstance(node, validate_between)):
            term = self.__validateValue(node.term, member, code)
            return f"{term} < {self.__validateValue(node.low, member, code)} || {term} > {self.__validateValue(node.high, member, code)}"
        if (isinstance(node, validate_in_set)):
            term = self.__validateValue(node.term, member, code)
            return " && ".join([f"{term} != {self.__validateValue(item, member, code)}" for item in node.items])
        if (isinstance(node, validate_call)):   # matches -> a boolean, violated is the negation
            return f"!{self.__validateTruth(node, member, code)}"
        if (isinstance(node, validate_ref)):    # a boolean field
            return f"!{self.__validateValue(node, member, code)}"
        return f"!({self.__validateTruth(node, member, code)})"

    def __violationOperand(self, node: validate_node, member: hinted_base_element, code: dotnet_code) -> str:
        text = self.__validateViolation(node, member, code)
        return f"({text})" if self.__validateCompound(node) else text

    # C# for "the rule holds" (positive form)
    def __validateTruth(self, node: validate_node, member: hinted_base_element, code: dotnet_code) -> str:
        if (isinstance(node, validate_binary)):
            if (node.op == "and" or node.op == "or"):
                op = "&&" if (node.op == "and") else "||"
                return f"{self.__truthOperand(node.left, member, code)} {op} {self.__truthOperand(node.right, member, code)}"
            return f"{self.__validateValue(node.left, member, code)} {node.op} {self.__validateValue(node.right, member, code)}"
        if (isinstance(node, validate_not)):
            return f"!({self.__validateTruth(node.operand, member, code)})"
        if (isinstance(node, validate_in_range) or isinstance(node, validate_between)):
            term = self.__validateValue(node.term, member, code)
            return f"{term} >= {self.__validateValue(node.low, member, code)} && {term} <= {self.__validateValue(node.high, member, code)}"
        if (isinstance(node, validate_in_set)):
            term = self.__validateValue(node.term, member, code)
            return " || ".join([f"{term} == {self.__validateValue(item, member, code)}" for item in node.items])
        return self.__validateValue(node, member, code)

    def __truthOperand(self, node: validate_node, member: hinted_base_element, code: dotnet_code) -> str:
        text = self.__validateTruth(node, member, code)
        return f"({text})" if self.__validateCompound(node) else text

    # does this node produce a boolean built from && / || (so it needs parens as an operand)?
    def __validateCompound(self, node: validate_node) -> bool:
        if (isinstance(node, validate_binary)):
            return node.op == "and" or node.op == "or"
        if (isinstance(node, validate_in_range) or isinstance(node, validate_between)):
            return True
        if (isinstance(node, validate_in_set)):
            return len(node.items) > 1
        if (isinstance(node, validate_not)):
            return False
        return False

    # C# for a plain value operand (bare field name, literal, or a function result)
    def __validateValue(self, node: validate_node, member: hinted_base_element, code: dotnet_code) -> str:
        if (isinstance(node, validate_ref)):
            return member.name if (node.name == "value") else node.name
        if (isinstance(node, validate_literal)):
            return node.value
        if (isinstance(node, validate_call)):
            if (node.func == "len"):
                target = self.__validateValue(node.args[0], member, code)
                accessor = "Count" if self.__validateIsCollection(node.args[0], member) else "Length"
                # A missing value has no elements. Reading .Length off null would throw INSIDE the
                # validator, and a validator that throws turns a bad request into a server error -
                # the caller is told nothing about the field that is actually wrong.
                return f"({target}?.{accessor} ?? 0)"
            if (node.func == "matches"):
                code.usings.add("System.Text.RegularExpressions")
                # same reason: Regex.IsMatch rejects null outright, and a missing value matching
                # nothing is exactly what the rule means
                return f"Regex.IsMatch({self.__validateValue(node.args[0], member, code)} ?? string.Empty, {self.__validateValue(node.args[1], member, code)})"
        return self.__validateTruth(node, member, code)

    def __validateIsCollection(self, node: validate_node, member: hinted_base_element) -> bool:
        # a len() argument is `value` (this member) or a sibling; list/map -> .Count, else .Length
        if (isinstance(node, validate_ref) == False):
            return False
        target = member
        if (node.name != "value"):
            target = None
            for candidate in member.parent.members:
                if (candidate.name == node.name):
                    target = candidate
                    break
        if (target == None or target.type == None):
            return False
        return target.type.kind == type.Kind.List or target.type.kind == type.Kind.Map

    # a readable rendering of the rule for the error message (spaces, uppercase AND/OR)
    def __validateRuleText(self, node: validate_node) -> str:
        if (isinstance(node, validate_binary)):
            op = node.op.upper() if (node.op == "and" or node.op == "or") else node.op
            return f"{self.__validateRuleText(node.left)} {op} {self.__validateRuleText(node.right)}"
        if (isinstance(node, validate_not)):
            return f"NOT ({self.__validateRuleText(node.operand)})"
        if (isinstance(node, validate_in_range)):
            return f"{self.__validateRuleText(node.term)} IN {self.__validateRuleText(node.low)}..{self.__validateRuleText(node.high)}"
        if (isinstance(node, validate_between)):
            return f"{self.__validateRuleText(node.term)} BETWEEN {self.__validateRuleText(node.low)} AND {self.__validateRuleText(node.high)}"
        if (isinstance(node, validate_in_set)):
            return f"{self.__validateRuleText(node.term)} IN {{{', '.join([self.__validateRuleText(i) for i in node.items])}}}"
        if (isinstance(node, validate_call)):
            return f"{node.func}({', '.join([self.__validateRuleText(a) for a in node.args])})"
        if (isinstance(node, validate_ref)):
            return node.name
        if (isinstance(node, validate_literal)):
            return node.value
        return ""

    def dataClassEqualsAndHashCodeText(self, element: internal_scoped_base_element, inherits: List[qualified_name], name: str, members: List[hinted_base_element], code: dotnet_code, indent: int = 1) -> str:
        bases: List[internal_scoped_base_element] = []
        for inherit in inherits:
            base = Engine.get_referenced_element(element.parent, inherit)
            if (base != None):
                utils.collectBaseRecursive(base, bases)

        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}#region Equals & HashCode \n")

        buffer.write(f"{utils.tab(indent)}public bool Equals( {name} other )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}if (other is null) return false;\n\n")
        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// begin: {base.name}\n")
            # Write each base member
            for member in base.members:
                if( member.find_decorator("system_field") != None ):
                    continue
                buffer.write(self.dataClassMemberEqualsText(member.name, member.type, code, dst="", src="other.", indent=indent+1))
                pass
            buffer.write(f"{utils.tab(indent+1)}// end: {base.name}\n\n")
        # Write each own member
        for member in element.members:
            if( member.find_decorator("system_field") != None ):
                continue
            buffer.write(self.dataClassMemberEqualsText(member.name, member.type, code, dst="", src="other.", indent=indent+1))
            pass

        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}return true;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"\n")

        buffer.write(f"{utils.tab(indent)}public override bool Equals(object obj) => Equals(obj as {name});\n")
        buffer.write(f"\n")

        buffer.write(f"{utils.tab(indent)}public override int GetHashCode()\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}var hash = new HashCode();\n")
        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// begin: {base.name}\n")
            # Write each base member
            for member in base.members:
                # a field Equals ignores may not enter the hash: two equal instances would land in
                # different buckets and a dictionary would stop finding them
                if( member.find_decorator("system_field") != None ):
                    continue
                buffer.write(self.dataClassMemberHashText(member.name, member.type, code, dst="hash", src="", indent=indent+1))
                pass
            buffer.write(f"{utils.tab(indent+1)}// end: {base.name}\n\n")
        # Write each own member
        for member in element.members:
            if( member.find_decorator("system_field") != None ):
                continue
            buffer.write(self.dataClassMemberHashText(member.name, member.type, code, dst="hash", src="", indent=indent+1))
            pass
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}return hash.ToHashCode();\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}#endregion Equals & HashCode \n")

        return buffer.getvalue()

    def dataClassCloneText(self, element: internal_scoped_base_element, inherits: List[qualified_name], name: str, members: List[hinted_base_element], code: dotnet_code, indent: int = 1) -> str:
        bases: List[internal_scoped_base_element] = []
        for inherit in inherits:
            base = Engine.get_referenced_element(element.parent, inherit)
            if (base != None):
                utils.collectBaseRecursive(base, bases)

        hasBaseClass = False
        for base in bases:
            if(isinstance(base,composite) == False ):
                hasBaseClass = True

        if(hasBaseClass == True ):
            method_modifier = "override"
        else:
            method_modifier = "virtual"

        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}#region Clone \n")
        buffer.write(f"{utils.tab(indent)}public {method_modifier} {name} Clone()\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}{name} clone = new();\n\n")

        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// begin: {base.name}\n")
            # Write each base member
            for member in base.members:
                if( member.find_decorator("system_field") != None ):
                    continue
                buffer.write(self.dataClassMemberCloneText(member.name, member.type, code, dst="clone.", src="", indent=indent+1))
                pass
            buffer.write(f"{utils.tab(indent+1)}// end: {base.name}\n\n")
        # Write each own member
        for member in element.members:
            if( member.find_decorator("system_field") != None ):
                continue
            buffer.write(self.dataClassMemberCloneText(member.name, member.type, code, dst="clone.", src="", indent=indent+1))
            pass

        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}return clone;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}#endregion Clone \n")

        return buffer.getvalue()

    def dataClassMemberEqualsText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberEqualsText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Ref:
                return self.dataClassMemberEqualsText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberEqualsText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberEqualsText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberEqualsText_Map(memberName, memberType, code, dst, src, indent)

    def dataClassMemberHashText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberHashText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Ref:
                return self.dataClassMemberHashText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberHashText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberHashText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberHashText_Map(memberName, memberType, code, dst, src, indent)
    
    def dataClassMemberHashText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        return f"{utils.tab(indent)}{dst}.Add({src}{memberName});\n"

    def dataClassMemberHashText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        referenced_element: base_element = Engine.get_referenced_element(memberType.parent, memberType.reference_name)
        
        if (isinstance(referenced_element, enum) == True):
            return f"{utils.tab(indent)}{dst}.Add({src}{memberName});\n"
        else:
            buffer = io.StringIO()
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent)}// hash of {memberName}\n")
            buffer.write(f"{utils.tab(indent)}if({src}{memberName} != null ) {dst}.Add({src}{memberName});\n")
            return buffer.getvalue()

    def dataClassMemberHashText_List(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}// hash of {memberName}\n")
        buffer.write(f"{utils.tab(indent)}foreach( var element_{memberName} in {src}{memberName})\n")
        buffer.write(f"{utils.tab(indent+1)}{dst}.Add(element_{memberName});\n")
        
        return buffer.getvalue()

    def dataClassMemberHashText_Map(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}// hash of {memberName}\n")
        buffer.write(f"{utils.tab(indent)}foreach( var kvp_{memberName} in {src}{memberName})\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}{dst}.Add(kvp_{memberName}.Key);\n")
        buffer.write(f"{utils.tab(indent+1)}{dst}.Add(kvp_{memberName}.Value);\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        
        return buffer.getvalue()

    def dataClassMemberEqualsText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        return f"{utils.tab(indent)}if({dst}{memberName} != {src}{memberName}) return false;\n"

    def dataClassMemberEqualsText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        referenced_element: base_element = Engine.get_referenced_element(memberType.parent, memberType.reference_name)
        
        if (isinstance(referenced_element, enum) == True):
            return f"{utils.tab(indent)}if({dst}{memberName} != {src}{memberName}) return false;\n"
        else:
            buffer = io.StringIO()
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent)}// equals of {memberName}\n")        
            buffer.write(f"{utils.tab(indent)}if({dst}{memberName} == null && {src}{memberName} != null ) return false;\n")
            buffer.write(f"{utils.tab(indent)}if({dst}{memberName} != null && {dst}{memberName}.Equals({src}{memberName}) == false ) return false;\n")
            return buffer.getvalue()

    def dataClassMemberEqualsText_List(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}// equals of {memberName}\n")   
        buffer.write(f"{utils.tab(indent)}if({dst}{memberName}.SequenceEqual({src}{memberName}) == false ) return false;\n" )
        return buffer.getvalue()

    def dataClassMemberEqualsText_Map(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}// equals of {memberName}\n")        
        buffer.write(f"{utils.tab(indent)}if({dst}{memberName}.Count != {src}{memberName}.Count ) return false;\n")
        buffer.write(f"{utils.tab(indent)}foreach( var kvp_{memberName} in {dst}{memberName})\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}if({src}{memberName}.TryGetValue(kvp_{memberName}.Key, out var otherValue) == false ) return false;\n")
        buffer.write(f"{utils.tab(indent+1)}if(kvp_{memberName}.Value.Equals(otherValue) == false ) return false;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        
        return buffer.getvalue()

    def dataClassMemberCloneText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberCloneText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Ref:
                return self.dataClassMemberCloneText_Ref(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberCloneText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberCloneText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberCloneText_Map(memberName, memberType, code, dst, src, indent)
            
    def dataClassMemberCloneText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        return f"{utils.tab(indent)}{dst}{memberName} = {self.dataClassMemberCloneExpression( f"{src}{memberName}", memberType, code )};\n"
    
    def dataClassMemberCloneExpression(self, memberName: str, memberType: type, code:dotnet_code ) -> str:
        """
        Returns a single C# EXPRESSION that clones one primitive value. Every caller embeds it -
        in an assignment, inside a .Select( v => ... ) lambda, or as a dictionary value - so it
        must never be a statement or span more than one expression.

        Two kinds cannot be deep-copied and are carried over by reference on purpose:
          - 'any' is 'object'; there is no generic way to duplicate an arbitrary instance;
          - 'stream' is a live handle, not data. Duplicating it would mean reading the source
            to the end, which consumes it - a clone must not damage the original.
        """
        buffer = io.StringIO()

        match memberType.primtiveKind:
            case primitive_type.PrimtiveKind.Any | primitive_type.PrimtiveKind.Stream:
                buffer.write( f"{memberName}")
            case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Float | primitive_type.PrimtiveKind.Number | primitive_type.PrimtiveKind.Boolean:
                buffer.write( f"{memberName}")
            case primitive_type.PrimtiveKind.Date | primitive_type.PrimtiveKind.Time | primitive_type.PrimtiveKind.DateTime:
                buffer.write( f"{memberName}")
            case primitive_type.PrimtiveKind.String:
                buffer.write( f"new string({memberName}.ToCharArray())")
            case primitive_type.PrimtiveKind.I18NString:
                buffer.write( f"new i18nstring({memberName})")
            case primitive_type.PrimtiveKind.Bytes:
                buffer.write( f"(byte[]){memberName}.Clone()")

        return buffer.getvalue()

    def dataClassMemberCloneText_Ref(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        # A 'ref X' is an EntityId<X>, a readonly record struct over a string. It is a VALUE, so the
        # assignment already copies it - and '?.Clone()' does not even compile on a struct, which is
        # what this branch used to emit.
        return f"{utils.tab(indent)}{dst}{memberName} = {src}{memberName};\n"

    def dataClassMemberCloneText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        referenced_element: base_element = Engine.get_referenced_element(memberType.parent, memberType.reference_name)

        buffer = io.StringIO()
        if (isinstance(referenced_element, enum) == True):
            buffer.write(f"{utils.tab(indent)}{dst}{memberName} = ")
            buffer.write(f"{src}{memberName};\n")
        else:
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent)}// clone of {memberName}\n")        
            buffer.write(f"{utils.tab(indent)}{dst}{memberName} = ")
            buffer.write(f"{src}{memberName}?.Clone();\n")

        return buffer.getvalue()
    
    def dataClassMemberCloneText_List(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}// clone of {memberName}\n")        

        match memberType.item_type.kind:
            case type.Kind.Primitive:
                buffer.write(f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{memberName}.Select( v => {self.dataClassMemberCloneExpression( "v", memberType.item_type, code )} ));\n")
            case type.Kind.Ref:
                reference_type: reference_type = memberType.item_type
            case type.Kind.Reference:
                reference_type: reference_type = memberType.item_type
                referenced_element: base_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name )
                if (isinstance(referenced_element, enum) == True):
                    buffer.write( f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{memberName} );\n")
                else:
                    buffer.write( f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{memberName}.Select( v => v.Clone() ));\n")
            case type.Kind.List:
                pass
            case type.Kind.Map:
                pass

        return buffer.getvalue()
    
    def dataClassMemberCloneText_Map(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int) -> str:
        buffer = io.StringIO()

        match memberType.value_type.kind:
            case type.Kind.Primitive:
                buffer.write(f"\n")
                buffer.write(f"{utils.tab(indent)}// clone of {memberName}\n")        
                buffer.write(f"{utils.tab(indent)}foreach( var kvp in {src}{memberName})\n")
                buffer.write( f"{utils.tab(indent+1)}{dst}{memberName}[kvp.Key] = {self.dataClassMemberCloneExpression("kvp.Value", memberType.value_type, code)};\n")
            case type.Kind.Ref:
                buffer.write(f"\n")
            case type.Kind.Reference:
                buffer.write(f"\n")
                buffer.write(f"{utils.tab(indent)}// clone of {memberName}\n")        
                buffer.write(f"{utils.tab(indent)}foreach( var kvp in {src}{memberName})\n")

                reference_type: reference_type = memberType.value_type
                referenced_element: base_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name )
                if (isinstance(referenced_element, enum) == True):
                    buffer.write(f"{utils.tab(indent+1)}{dst}{memberName}[kvp.Key] = kvp.Value;\n")
                else:
                    buffer.write(f"{utils.tab(indent+1)}{dst}{memberName}[kvp.Key] = kvp.Value?.Clone();\n")
                pass
            case type.Kind.List:
                # not supported types
                pass
            case type.Kind.Map:
                # not supported types
                pass

        return buffer.getvalue()
    
    def dtoGrpcMappingText(self, dto: dto, code: dotnet_code, indent: int = 1) -> str:
        """
        Generates the .NET code for an data object
        """
        bases: List[internal_scoped_base_element] = []
        for inherit in dto.inherits:
            base = Engine.get_referenced_element(dto.parent, inherit)
            if (base != None):
                utils.collectBaseRecursive(base, bases)

        dotnetFullName: str = code.getDotnetFullName(dto)
        protosFullName: str = grpc_utils.getProtoFullName(dto)

        buffer = io.StringIO()

        # ToGrpc
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}#region GrpcMapping\n")
        buffer.write(f"{utils.tab(indent)}public static Protos.{protosFullName} ToGrpc( {dotnetFullName} @this )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}Protos.{protosFullName} result = new();\n")
        buffer.write(f"\n")

        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// begin: {base.name}\n")
            # Write each base member
            for member in base.members:
                buffer.write(self.dataClassMemberToGrpcMappingText(member.name, member.type, code, dst="result.", src="@this.", indent=indent+1))
                pass
            buffer.write(f"{utils.tab(indent+1)}// end: {base.name}\n\n")
        # Write each own member
        for member in dto.members:
            buffer.write(self.dataClassMemberToGrpcMappingText(member.name, member.type, code, dst="result.", src="@this.", indent=indent+1))
            pass
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}return result;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        # FromGrpc
        buffer.write(f"{utils.tab(indent)}public static {dotnetFullName} FromGrpc( Protos.{protosFullName} @from )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}{dotnetFullName} result = new();\n")
        buffer.write(f"\n")
        # Loop through each base members and generate code for each
        for base in bases:
            buffer.write(f"{utils.tab(indent+1)}// begin: {base.name}\n")
            # Write each own member
            for member in base.members:
                buffer.write(self.dataClassMemberFromGrpcMappingText(member.name, member.type, code, dst="result.", src="@from.", indent=indent+1))
                pass
            buffer.write(f"{utils.tab(indent+1)}// end: {base.name}\n\n")

        for member in dto.members:
            # Write each member
            buffer.write(self.dataClassMemberFromGrpcMappingText(member.name, member.type, code, dst="result.", src="@from.", indent=indent+1))
            pass
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}return result;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}#endregion GrpcMapping\n")

        return buffer.getvalue()

    def dataClassMemberToGrpcMappingText(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        match memberType.kind:
            case type.Kind.Primitive:
                return self.dataClassMemberToGrpcMappingText_Primitive(memberName, memberType, code, dst, src, indent)
            case type.Kind.Ref:
                return self.dataClassMemberToGrpcMappingText_Reference(memberName, memberType, code, dst, src, indent)
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
            case type.Kind.Ref:
                return self.dataClassMemberFromGrpcMappingText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.Reference:
                return self.dataClassMemberFromGrpcMappingText_Reference(memberName, memberType, code, dst, src, indent)
            case type.Kind.List:
                return self.dataClassMemberFromGrpcMappingText_List(memberName, memberType, code, dst, src, indent)
            case type.Kind.Map:
                return self.dataClassMemberFromGrpcMappingText_Map(memberName, memberType, code, dst, src, indent)

    def dataClassMemberToGrpcMappingText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        return f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)} = {self.convertExpressionToGrpcRepresentation(f"{src}{memberName}", memberType, code)};\n"

    def dataClassMemberFromGrpcMappingText_Primitive(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        return f"{utils.tab(indent)}{dst}{memberName} = {self.convertExpressionFromGrpcRepresentation(f"{src}{utils.camel_to_pascal(memberName)}", memberType, code)};\n"

    def convertExpressionToGrpcRepresentation(self, memberName: str, memberType: type, code: dotnet_code):
        """
        Returns a single C# EXPRESSION converting a domain value to its gRPC representation. Every
        caller embeds it in an assignment or a lambda, so it must not carry a ';' or a newline of
        its own - doing so produced '= x;\\n;', which does not compile.

        The wire types come from the proto emitter: 'any' and i18nstring travel as a JSON string,
        date/time as their ISO text, bytes and stream as ByteString.
        """
        match memberType.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Serialize({memberName})"
            case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Float:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Number:
                code.usings.add("System.Globalization")
                return f"{memberName}.ToString(CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Date:
                code.usings.add("System.Globalization")
                return f"{memberName}.ToString( \"yyyy-MM-dd\", CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Time:
                return f"{memberName}.ToString(\"HH:mm:ss\")"
            case primitive_type.PrimtiveKind.DateTime:
                code.usings.add("Google.Protobuf.WellKnownTypes")
                # Timestamp.FromDateTime rejects anything that is not DateTimeKind.Utc, so a local
                # or unspecified DateTime threw at runtime instead of being converted.
                return f"Timestamp.FromDateTime({memberName}.ToUniversalTime())"
            case primitive_type.PrimtiveKind.String:
                # protobuf refuses null in a string field and throws on assignment, so an unset
                # member - an id the caller has not got yet, an optional field - used to take the
                # whole call down before it left the process. Absent is the empty string on the wire.
                return f"{memberName} ?? string.Empty"
            case primitive_type.PrimtiveKind.I18NString:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Serialize({memberName})"
            case primitive_type.PrimtiveKind.Boolean:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Bytes:
                return f"{memberName} != null ? Google.Protobuf.ByteString.CopyFrom({memberName}) : Google.Protobuf.ByteString.Empty"
            case primitive_type.PrimtiveKind.Stream:
                return f"{memberName} != null ? Google.Protobuf.ByteString.FromStream({memberName}) : Google.Protobuf.ByteString.Empty"

    def convertExpressionFromGrpcRepresentation(self, memberName: str, memberType: type, code: dotnet_code):
        """
        The inverse of convertExpressionToGrpcRepresentation: a single C# EXPRESSION turning a gRPC
        value back into the domain value. Several branches used to be copies of the outbound
        direction, so the value never made it home: a time came back as a re-formatted string, an
        i18nstring was serialized a second time, and bytes / stream were re-wrapped into a
        ByteString instead of being unwrapped.
        """
        match memberType.primtiveKind:
            case primitive_type.PrimtiveKind.Any:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Deserialize<object>({memberName})"
            case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Float:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Number:
                code.usings.add("System.Globalization")
                return f"decimal.Parse({memberName}, CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Date:
                code.usings.add("System.Globalization")
                return f"DateOnly.Parse({memberName}, CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.Time:
                code.usings.add("System.Globalization")
                return f"TimeOnly.Parse({memberName}, CultureInfo.InvariantCulture)"
            case primitive_type.PrimtiveKind.DateTime:
                code.usings.add("Google.Protobuf.WellKnownTypes")
                return f"{memberName}.ToDateTime()"
            case primitive_type.PrimtiveKind.String:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.I18NString:
                code.usings.add("System.Text.Json")
                return f"JsonSerializer.Deserialize<i18nstring>({memberName})"
            case primitive_type.PrimtiveKind.Boolean:
                return f"{memberName}"
            case primitive_type.PrimtiveKind.Bytes:
                return f"{memberName}.ToByteArray()"
            case primitive_type.PrimtiveKind.Stream:
                code.usings.add("System.IO")
                return f"new MemoryStream({memberName}.ToByteArray())"

    def dataClassMemberToGrpcMappingText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        referenced_element: base_element = Engine.get_referenced_element(memberType.parent, memberType.reference_name)

        buffer = io.StringIO()
        buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)} = ")
        if (isinstance(referenced_element, enum) == True):
            buffer.write(f"{code.getDotnetFullName(referenced_element)}Mappings.ToGrpc( {src}{memberName} );\n")
        else:
            buffer.write(f"{src}{memberName} != null ? {code.getDotnetFullName(referenced_element)}.ToGrpc( {src}{memberName} ) : null;\n")
        return buffer.getvalue()

    def dataClassMemberFromGrpcMappingText_Reference(self, memberName: str, memberType: type, code: dotnet_code, dst: str, src: str, indent: int):
        referenced_element: base_element = Engine.get_referenced_element(memberType.parent, memberType.reference_name)

        buffer = io.StringIO()
        buffer.write(f"{utils.tab(indent)}{dst}{memberName} = ")
        if (isinstance(referenced_element, enum) == True):
            buffer.write(f"{code.getDotnetFullName(referenced_element)}Mappings.FromGrpc( {src}{utils.camel_to_pascal(memberName)}) ;\n")
        else:
            buffer.write(f"{src}{utils.camel_to_pascal(memberName)} != null ? {code.getDotnetFullName(referenced_element)}.FromGrpc( {src}{utils.camel_to_pascal(memberName)} ) : null;\n")
        return buffer.getvalue()

    def dataClassMemberToGrpcMappingText_List(self, memberName: str, memberType: list_type, code: dotnet_code, dst: str, src: str, indent: int):
        code.usings.add("Google.Protobuf.Collections")

        buffer = io.StringIO()

        match memberType.item_type.kind:
            case type.Kind.Primitive:
                if (memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Integer or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.String or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Float or memberType.item_type.primtiveKind == primitive_type.PrimtiveKind.Boolean):
                    buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName});\n")
                else:
                    buffer.write(
                        f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName}.Select( v => {self.convertExpressionToGrpcRepresentation("v", memberType.item_type, code)} ));\n")
            case type.Kind.Ref:
                reference_type: reference_type = memberType.item_type
            case type.Kind.Reference:
                reference_type: reference_type = memberType.item_type
                referenced_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name)
                buffer.write( f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.AddRange( {src}{memberName}.Select( v => {code.getDotnetFullName(referenced_element)}.ToGrpc( v ) ));\n")
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
                    buffer.write(f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)});\n")
                else:
                    buffer.write(
                        f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)}.Select( v => {self.convertExpressionFromGrpcRepresentation("v", memberType.item_type, code)} ));\n")
            case type.Kind.Ref:
                reference_type: reference_type = memberType.item_type
            case type.Kind.Reference:
                reference_type: reference_type = memberType.item_type
                referenced_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name)
                buffer.write(f"{utils.tab(indent)}{dst}{memberName}.AddRange( {src}{utils.camel_to_pascal(memberName)}.Select( v => {code.getDotnetFullName(referenced_element)}.FromGrpc(v) ));\n")
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
                    buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add({src}{memberName});\n")
                else:
                    buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add({src}{memberName}.ToDictionary( kvp => kvp.Key, kvp => {self.convertExpressionToGrpcRepresentation("kvp.Value", memberType.value_type, code)}));\n")
            case type.Kind.Ref:
                buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add( {src}{memberName}.ToDictionary( kvp => kvp.Key, kvp => {self.typeText(memberType.value_type, code)}.ToGrpc( kvp.Value ) ));\n")
            case type.Kind.Reference:
                buffer.write(f"{utils.tab(indent)}{dst}{utils.camel_to_pascal(memberName)}.Add( {src}{memberName}.ToDictionary( kvp => kvp.Key, kvp => {self.typeText(memberType.value_type, code)}.ToGrpc( kvp.Value ) ));\n")
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
                buffer.write(f"\n")
                buffer.write(f"{utils.tab(indent)}// mapping of {memberName}\n")        
                buffer.write(f"{utils.tab(indent)}foreach( var kvp in {src}{utils.camel_to_pascal(memberName)})\n")
                buffer.write(
                    f"{utils.tab(indent+1)}{dst}{memberName}[kvp.Key] = {self.convertExpressionFromGrpcRepresentation("kvp.Value", memberType.value_type, code)};\n")
            case type.Kind.Ref:
                buffer.write(f"\n")
            case type.Kind.Reference:
                buffer.write(f"\n")
                buffer.write(f"{utils.tab(indent)}// mapping of {memberName}\n")        
                buffer.write(f"{utils.tab(indent)}foreach( var kvp in {src}{utils.camel_to_pascal(memberName)})\n")
                buffer.write(f"{utils.tab(indent+1)}{dst}{memberName}[kvp.Key] = {self.typeText(memberType.value_type, code)}.FromGrpc(kvp.Value);\n")
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
        buffer.write(f"{utils.tab(indent)}public partial interface I{composite.name}\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # Loop through each composite members and generate code for each
        for member in composite.members:
            buffer.write(self.documentLines(member, indent+1))
            # Write each member
            buffer.write(self.propertyText(member, code, indent+1))
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def aclInterfaceText(self, acl: acl, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(acl, acl.name,code=code, indent=indent)

    def serviceInterfaceText(self, service: service, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(service, service.name,code=code, indent=indent)

    def repositoryInterfaceText(self, repository: repository, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(repository, repository.name,code=code, indent=indent)

    def interfaceInterfaceText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        return self.interfaceClassText(interface, interface.name + f"_v{interface.version}",code=code, indent=indent)

    def interfaceClassText(self, element: functional_element, elementName: str, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET code for element, just the interface.
        """
        buffer = io.StringIO()
        code.usings.add("ServiceKit.Net")
        # Add documentation lines for the element
        buffer.write(self.documentLines(element, indent))
        # Write the interface class declaration with indentation
        buffer.write(f"{utils.tab(indent)}public partial interface I{elementName}\n")
        buffer.write(f"{utils.tab(indent)}{{\n")

        # Loop through each operations and generate code for each
        for operation in element.operations:
            # Write each operation
            buffer.write(self.interfaceFunctionText(operation, code, indent+1))
            buffer.write("\n")

        if (element.withEventHandler == True):
            # Write each event handler
            for eventhandler in element.eventhandlers:
                handled_event:event = Engine.get_referenced_element(eventhandler, eventhandler.handledEvent )
                if(handled_event != None ):
                    buffer.write(self.documentLines(eventhandler, indent))
                    buffer.write(f"{utils.tab(indent+1)}public Task<bool> {eventhandler.name}(CallingContext ctx, {code.getDotnetFullName(handled_event)} @event );")

        buffer.write(f"\n")
        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        if (element.withEvent == True):
            for dto in element.events:
                code = self.eventText(dto, code, indent+1)

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
            for event in element.dtos:
                code = self.dtoText(event, code, indent+1)

        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def interfaceFunctionText(self, operation: operation, code: dotnet_code, indent: int) -> str:
        buffer = io.StringIO()

        # Add summary for operation
        if (len(operation.document_lines) > 0):
            buffer.write(f"{utils.tab(indent)}/// <summary>\n")
            for line in operation.document_lines:
                buffer.write(f"{utils.tab(indent)}/// {line}\n")
            buffer.write(f"{utils.tab(indent)}/// </summary>\n")

        # Add param comments for operation
        for param in operation.operation_params:
            if (len(param.document_lines) == 1):
                buffer.write(f"{utils.tab(indent)}/// <param name='{param.name}'>{param.document_lines[0]}</param>\n")
            elif (len(param.document_lines) > 1):
                buffer.write(f"{utils.tab(indent)}/// <param name='{param.name}'>\n")
                for line in param.document_lines:
                    buffer.write(f"{utils.tab(indent)}/// {line}\n")
                buffer.write(f"{utils.tab(indent)}/// </param>\n")

        # Add return code comments
        if( operation.operation_return != None ):
            if (len(operation.operation_return.document_lines) == 1):
                buffer.write(f"{utils.tab(indent)}/// <return>{operation.operation_return.document_lines[0]}</return>\n")
            elif (len(operation.operation_return.document_lines) > 1):
                buffer.write(f"{utils.tab(indent)}/// <return>\n")
                for line in operation.operation_return.document_lines:
                    buffer.write(f"{utils.tab(indent)}/// {line}\n")
                buffer.write(f"{utils.tab(indent)}/// </return>\n")
            else:
                buffer.write(f"{utils.tab(indent)}/// <return>{self.typeText( operation.operation_return.type, code, fullName=True )}</return>\n")

        # Add return value
        buffer.write(f"{utils.tab(indent)}public Task<Response")
        if (operation.operation_return != None ):
            buffer.write(f"<{self.typeText(operation.operation_return.type, code, fullName=True )}>")
        buffer.write(f">")
        # Add function name
        buffer.write(f" {operation.name}(CallingContext ctx")
        # Add parameters
        if (len(operation.operation_params) > 0):
            buffer.write(f", ")
        buffer.write(", ".join([self.typeText(param.type, code, isInFunctionParam=True) + " " + param.name for param in operation.operation_params]))
        buffer.write(");\n")

        return buffer.getvalue()
    
    def interfaceGrpcPublicClientText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET GRPC Public client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("Google.Protobuf.WellKnownTypes")
        code.usings.add("Grpc.Core")
        code.usings.add("Grpc.Net.Client")
        code.usings.add("ServiceKit.Net")
        code.usings.add(f"{domain.name}.{context.name}.Protos.{versionedName}")

        # client class declaration
        buffer.write(f"{utils.tab(indent)}static partial class Grpc \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(self.documentLines(interface, indent+1))
        buffer.write(f"{utils.tab(indent+1)}static class {interface.name}\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}static class V{interface.version} \n")
        buffer.write(f"{utils.tab(indent+2)}{{\n")
        buffer.write(f"{utils.tab(indent+3)}private static {versionedName}.{versionedName}Client _client;\n")

        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(self.documentLines(operation, indent+2))
            # Add return value
            buffer.write(f"{utils.tab(indent+3)}public static async Task<Response")
            if (operation.operation_return != None ):
                buffer.write(f"<{self.typeText(operation.operation_return.type, code,fullName=True)}>")
            buffer.write(f"> ")
            # Add function name
            buffer.write(f"{operation.name}(")
            # Add parameters
            buffer.write(", ".join([self.typeText(param.type, code,fullName=True) + " " + param.name for param in operation.operation_params]))
            buffer.write(")\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            buffer.write(f"{utils.tab(indent+4)}try\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            
            buffer.write(f"{utils.tab(indent+5)}// fill grpc request\n")
            if(len(operation.operation_params)):
                requestType = f"{versionedName}_{operation.name}Request"
            else:
                requestType = f"Empty"
            buffer.write(f"{utils.tab(indent+5)}var request = new {requestType}();\n")
            for param in operation.operation_params:
                buffer.write(f"{utils.tab(indent+5)}{self.dataClassMemberToGrpcMappingText( param.name, param.type, code, dst="request.", src="", indent=0)}")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+5)}// calling grpc client\n")
            buffer.write(f"{utils.tab(indent+5)}_client ??= new {versionedName}.{versionedName}Client(GrpClient._channel);\n")
            buffer.write(f"{utils.tab(indent+5)}var grpc_response = await _client.{operation.name}Async( request, new CallOptions(GrpClient.GetMetadata( \"{domain.name}.{context.name}.{versionedName}.{operation.name}\" ))).ResponseAsync;\n")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+5)}// fill response\n")
            buffer.write(self.grpcClientResponseText(versionedName, operation, code, indent+5))

            buffer.write(f"{utils.tab(indent+4)}}}\n") # try
            buffer.write(f"{utils.tab(indent+4)}catch (RpcException ex)\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "ex.StatusCode.FromGrpc()", indent+5))
            buffer.write(f"{utils.tab(indent+4)}}}\n") # catch RpcException
            buffer.write(f"{utils.tab(indent+4)}catch (Exception ex)\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "Statuses.InternalError", indent+5))
            buffer.write(f"{utils.tab(indent+4)}}}\n") # catch Exception
            buffer.write(f"{utils.tab(indent+3)}}}\n") # function
            buffer.write(f"\n")

        buffer.write(self.fromGrpcErrorsText(code, indent+3))
        buffer.write(f"{utils.tab(indent+2)}}}\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def fromGrpcErrorsText(self, code: dotnet_code, indent: int) -> str:
        # The errors come home as protobuf messages; the caller only ever sees ServiceKit errors.
        # An array, because Response.Failure takes `params Error[]`.
        code.usings.add("System.Linq")
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}private static ServiceKit.Net.Error[] _FromGrpcErrors( IEnumerable<ServiceKit.Protos.Error> errors )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}return errors.Select( error => new ServiceKit.Net.Error() {{\n")
        buffer.write(f"{utils.tab(indent+2)}Path = error.Path,\n")
        buffer.write(f"{utils.tab(indent+2)}MessageText = error.MessageText,\n")
        buffer.write(f"{utils.tab(indent+2)}AdditionalInformation = error.AdditionalInformation,\n")
        buffer.write(f"{utils.tab(indent+1)}}} ).ToArray();\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        return buffer.getvalue()

    def grpcClientResponseText(self, versionedName: str, operation: operation, code: dotnet_code, indent: int) -> str:
        # The answer is read from the STATUS, not from which branch of a oneof happens to be set:
        # the status is the one thing the wire is guaranteed to carry, and it is now the same fact
        # on both sides. The value keeps its oneof only so "succeeded with no value" stays
        # distinguishable from "succeeded with the default".
        buffer = io.StringIO()
        returns = operation.operation_return != None
        responseType = f"Response<{self.typeText(operation.operation_return.type, code, fullName=True)}>" if returns else "Response"

        buffer.write(f"{utils.tab(indent)}if( grpc_response.Status != ServiceKit.Protos.Statuses.Ok )\n")
        buffer.write(f"{utils.tab(indent+1)}return {responseType}.Failure( grpc_response.Status.FromGrpc(), _FromGrpcErrors( grpc_response.Errors ) );\n")
        buffer.write(f"\n")
        if (returns == False):
            buffer.write(f"{utils.tab(indent)}return Response.Success();\n")
            return buffer.getvalue()

        buffer.write(f"{utils.tab(indent)}if( grpc_response.ResultCase == {versionedName}_{operation.name}Response.ResultOneofCase.Value )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        if( operation.operation_return.type.kind == type.Kind.List or operation.operation_return.type.kind == type.Kind.Map ):
            buffer.write(f"{utils.tab(indent+1)}{self.typeText( operation.operation_return.type, code, fullName=True)} value = new();\n")
            buffer.write(f"{utils.tab(indent+1)}{self.dataClassMemberFromGrpcMappingText( "value", operation.operation_return.type, code, dst="", src="grpc_response.Value.", indent=0)}")
        else:
            buffer.write(f"{utils.tab(indent+1)}{self.typeText( operation.operation_return.type, code, fullName=True)} value;\n")
            buffer.write(f"{utils.tab(indent+1)}{self.dataClassMemberFromGrpcMappingText( "value", operation.operation_return.type, code, dst="", src="grpc_response.", indent=0)}")
        buffer.write(f"{utils.tab(indent+1)}return {responseType}.Success( value );\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}return {responseType}.Failure( Statuses.NotImplemented, \"Not handled reponse in GRPC client when calling '{versionedName}_{operation.name}'\" );\n")
        return buffer.getvalue()

    def clientFailureText(self, operation: operation, code: dotnet_code, statusExpression: str, indent: int) -> str:
        # One failure the caller can act on: the status of the answer, and the single thing that
        # went wrong on the way. The transport never produces a field-level list.
        buffer = io.StringIO()
        if (operation.operation_return != None):
            responseType = f"Response<{self.typeText(operation.operation_return.type, code, fullName=True)}>"
        else:
            responseType = "Response"
        buffer.write(f"{utils.tab(indent)}return {responseType}.Failure( {statusExpression}, new ServiceKit.Net.Error() {{\n")
        buffer.write(f"{utils.tab(indent+1)}MessageText = ex.Message,\n")
        buffer.write(f"{utils.tab(indent+1)}AdditionalInformation = ex.ToString(),\n")
        buffer.write(f"{utils.tab(indent)}}} );\n")
        return buffer.getvalue()

    def interfaceGrpcInternalClientText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET GRPC INTERNAL client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("Google.Protobuf.WellKnownTypes")
        code.usings.add("Grpc.Core")
        code.usings.add("Grpc.Net.Client")
        code.usings.add("ServiceKit.Net")
        code.usings.add(f"{domain.name}.{context.name}.Protos.{versionedName}")

        # Add documentation lines for the interface
        buffer.write(self.documentLines(interface, indent))
        # client class declaration
        buffer.write(f"{utils.tab(indent)}public class {versionedName}_GrpcClient : I{versionedName} \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # private members
        buffer.write(f"{utils.tab(indent+1)}private readonly GrpcChannel _channel;\n")
        buffer.write(f"{utils.tab(indent+1)}private readonly {versionedName}.{versionedName}Client _client;\n")

        # Add constructor with server address
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}public {versionedName}_GrpcClient( string serverAddress )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}_channel = GrpcChannel.ForAddress(serverAddress);\n")
        buffer.write(f"{utils.tab(indent+2)}_client = new {versionedName}.{versionedName}Client(_channel);\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"\n")
        
        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(f"{utils.tab(indent+1)}/// <inheritdoc />\n")
            # Add return value
            buffer.write(f"{utils.tab(indent+1)}async Task<Response")
            if (operation.operation_return != None ):
                buffer.write(f"<{self.typeText(operation.operation_return.type, code,fullName=True)}>")
            buffer.write(f">")
            # Add function name
            buffer.write(f" I{versionedName}.{operation.name}(CallingContext ctx")
            # Add parameters
            if (len(operation.operation_params) > 0):
                buffer.write(f", ")
            buffer.write(", ".join([self.typeText(param.type, code,fullName=True) + " " + param.name for param in operation.operation_params]))
            buffer.write(")\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+2)}try\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(f"{utils.tab(indent+3)}// fill grpc request\n")
            if(len(operation.operation_params)):
                requestType = f"{versionedName}_{operation.name}Request"
            else:
                requestType = f"Empty"
            buffer.write(f"{utils.tab(indent+3)}var request = new {requestType}();\n")
            for param in operation.operation_params:
                buffer.write(f"{utils.tab(indent+3)}{self.dataClassMemberToGrpcMappingText( param.name, param.type, code, dst="request.", src="", indent=0)}")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+3)}// calling grpc client\n")
            buffer.write(f"{utils.tab(indent+3)}var grpc_response = await _client.{operation.name}Async( request, new CallOptions(ctx.ToGrpcMetadata( \"{domain.name}.{context.name}{versionedName}\", \"{operation.name}\" ))).ResponseAsync;\n")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+3)}// fill response\n")
            buffer.write(self.grpcClientResponseText(versionedName, operation, code, indent+3))

            buffer.write(f"{utils.tab(indent+2)}}}\n") # try
            buffer.write(f"{utils.tab(indent+2)}catch (RpcException ex)\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "ex.StatusCode.FromGrpc()", indent+3))
            buffer.write(f"{utils.tab(indent+2)}}}\n") # catch RpcException
            buffer.write(f"{utils.tab(indent+2)}catch (Exception ex)\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "Statuses.InternalError", indent+3))
            buffer.write(f"{utils.tab(indent+2)}}}\n") # catch Exception
            buffer.write(f"{utils.tab(indent+1)}}}\n") # function
            buffer.write(f"\n")

        buffer.write(self.fromGrpcErrorsText(code, indent+1))
        buffer.write(f"{utils.tab(indent)}}}\n") # classs

        code.content += buffer.getvalue()
        return code

    def controllerMapFailureText(self, code: dotnet_code, indent: int) -> str:
        # A controller is the only place that sees both worlds: PolyPersist raises exceptions, the
        # wire carries a status and a list of errors. Nobody owned that translation before, so a
        # single bad field arrived at the caller as a 500 InternalError - a server fault, when in
        # truth the request was wrong and the caller could have fixed it. The types are written out
        # in full so a model may name something `ValidationError` without colliding here.
        code.usings.add("System.Linq")
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}private static (Statuses Status, IList<ServiceKit.Net.Error> Errors) _MapFailure( Exception ex )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}// a broken field is the caller's to fix, and every rule that failed is worth reporting\n")
        buffer.write(f"{utils.tab(indent+1)}if( ex is PolyPersist.Net.Common.ValidationExeption validationExeption )\n")
        buffer.write(f"{utils.tab(indent+2)}return (Statuses.BadRequest, validationExeption.ValidationErrors.Select( validationError => new ServiceKit.Net.Error() {{\n")
        buffer.write(f"{utils.tab(indent+3)}Path = validationError.Path,\n")
        buffer.write(f"{utils.tab(indent+3)}MessageText = validationError.ErrorText,\n")
        buffer.write(f"{utils.tab(indent+3)}AdditionalInformation = $\"{{validationError.TypeOfEntity}}.{{validationError.MemberOfEntity}}\",\n")
        buffer.write(f"{utils.tab(indent+2)}}} ).ToList<ServiceKit.Net.Error>());\n")
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}if( ex is PolyPersist.Net.Common.NotFoundException )\n")
        buffer.write(f"{utils.tab(indent+2)}return (Statuses.NotFound, new List<ServiceKit.Net.Error>() {{ new() {{ MessageText = ex.Message }} }});\n")
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}if( ex is PolyPersist.Net.Common.DuplicateKeyException\n")
        buffer.write(f"{utils.tab(indent+2)}|| ex is PolyPersist.Net.Common.ConcurrencyConflictException\n")
        buffer.write(f"{utils.tab(indent+2)}|| ex is PolyPersist.Net.Common.InvalidRequestException )\n")
        buffer.write(f"{utils.tab(indent+2)}return (Statuses.BadRequest, new List<ServiceKit.Net.Error>() {{ new() {{ MessageText = ex.Message }} }});\n")
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}// anything else really is ours: the caller can do nothing about it, so say so plainly\n")
        buffer.write(f"{utils.tab(indent+1)}return (Statuses.InternalError, new List<ServiceKit.Net.Error>() {{ new() {{ MessageText = ex.Message, AdditionalInformation = ex.ToString() }} }});\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        return buffer.getvalue()

    def grpcFailureText(self, responseType: str, operationName: str, indent: int) -> str:
        # Every operation has its own response message type, so the failure is built per operation.
        # One place to fill in the status and the whole error list, instead of three copies each.
        buffer = io.StringIO()
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent)}private static {responseType} _GrpcFailure_{operationName}( Statuses status, IEnumerable<ServiceKit.Net.Error> errors )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}var failure = new {responseType}() {{ Status = status.ToGrpc() }};\n")
        buffer.write(f"{utils.tab(indent+1)}foreach( var error in errors )\n")
        buffer.write(f"{utils.tab(indent+2)}failure.Errors.Add( new ServiceKit.Protos.Error() {{\n")
        buffer.write(f"{utils.tab(indent+3)}Path = error.Path ?? string.Empty,\n")
        buffer.write(f"{utils.tab(indent+3)}MessageText = error.MessageText ?? string.Empty,\n")
        buffer.write(f"{utils.tab(indent+3)}AdditionalInformation = error.AdditionalInformation ?? string.Empty,\n")
        buffer.write(f"{utils.tab(indent+2)}}} );\n")
        buffer.write(f"{utils.tab(indent+1)}return failure;\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        return buffer.getvalue()

    def interfaceGrpcControllerText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET GRPC controller code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("Google.Protobuf.WellKnownTypes")
        code.usings.add("Grpc.Core")
        code.usings.add("ServiceKit.Net")
        code.usings.add("Serilog.Context")
        code.usings.add("Microsoft.Extensions.Logging")
        code.usings.add(f"{domain.name}.{context.name}.Protos.{versionedName}")

        # Add documentation lines for the interface
        buffer.write(self.documentLines(interface, indent))
        # controller class declaration
        # Without this the host maps nothing: MapGrpcControllers registers the classes that carry
        # the attribute, so a generated controller that lacks it compiles, starts, and is never
        # reachable.
        buffer.write(f"{utils.tab(indent)}[AutoRegisterGrpc]\n")
        buffer.write(f"{utils.tab(indent)}public class {versionedName}_GrpcController : {domain.name}.{context.name}.Protos.{versionedName}.{versionedName}.{versionedName}Base \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # class members
        buffer.write(f"{utils.tab(indent+1)}private readonly ILogger<{versionedName}_GrpcController> _logger;\n")
        buffer.write(f"{utils.tab(indent+1)}private readonly I{versionedName} _service;\n")
        buffer.write(f"\n")
        # class constructor
        buffer.write(f"{utils.tab(indent+1)}public {versionedName}_GrpcController( ILogger<{versionedName}_GrpcController> logger, I{versionedName} service )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}_logger = logger; \n")
        buffer.write(f"{utils.tab(indent+2)}_service = service; \n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")

        buffer.write(self.controllerMapFailureText(code, indent+1))

        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(f"\n")
            if(len(operation.operation_params)):
                requestType = f"{versionedName}_{operation.name}Request"
            else:
                requestType = f"Empty"
            buffer.write(f"{utils.tab(indent+1)}public override async Task<{versionedName}_{operation.name}Response> {operation.name}( {requestType} request, ServerCallContext grpcContext)\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+2)}using(LogContext.PushProperty( \"Scope\", \"{versionedName}.{operation.name}\" ))\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(f"{utils.tab(indent+3)}CallingContext ctx = CallingContext.FromGrpcContext( grpcContext, _logger );\n")
            buffer.write(f"{utils.tab(indent+3)}try\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            index: int = 1
            params: List[str] = []
            for param in operation.operation_params:
                buffer.write(f"{utils.tab(indent+4)}{self.typeText(param.type, code, fullName=True)} {param.name};\n")
                buffer.write(f"{utils.tab(indent+4)}{self.dataClassMemberFromGrpcMappingText(param.name, param.type, code, dst="", src="request.", indent=0)}")
                params.append(param.name)
                index = index + 1
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent+4)}// calling the service function itself\n")
            buffer.write(f"{utils.tab(indent+4)}var response = await _service.{operation.name}( ctx {", " + ", ".join(params) if params else ""} );\n")
            buffer.write(f"\n")
            if ( operation.operation_return != None ):

                buffer.write(f"{utils.tab(indent+4)}if( response.IsSuccess() == true )\n")
                buffer.write(f"{utils.tab(indent+4)}{{\n")
                buffer.write(f"{utils.tab(indent+5)}if( response.HasValue() == true )\n")
                buffer.write(f"{utils.tab(indent+5)}{{\n")
                buffer.write(f"{utils.tab(indent+6)}var result = new {versionedName}_{operation.name}Response() {{ Status = ServiceKit.Protos.Statuses.Ok }};\n")
                if(operation.operation_return.type.kind == type.Kind.List or operation.operation_return.type.kind == type.Kind.Map ):
                    buffer.write(f"{utils.tab(indent+6)}{self.dataClassMemberToGrpcMappingText(f"Value", operation.operation_return.type, code, dst="result.Value.", src="response.", indent=0)}")
                else:
                    buffer.write(f"{utils.tab(indent+6)}{self.dataClassMemberToGrpcMappingText(f"Value", operation.operation_return.type, code, dst="result.", src="response.", indent=0)}")
                buffer.write(f"{utils.tab(indent+6)}return result;\n")
                buffer.write(f"{utils.tab(indent+5)}}}\n")
                buffer.write(f"{utils.tab(indent+5)}else\n")
                buffer.write(f"{utils.tab(indent+5)}{{\n")
                buffer.write(f"{utils.tab(indent+6)}return _GrpcFailure_{operation.name}( Statuses.NotImplemented, new [] {{ new ServiceKit.Net.Error() {{ MessageText = \"Not handled reponse in GRPC Controller when calling '{versionedName}.{operation.name}'\" }} }} );\n")
                buffer.write(f"{utils.tab(indent+5)}}}\n")
                buffer.write(f"{utils.tab(indent+4)}}}\n")
                buffer.write(f"{utils.tab(indent+4)}else\n")
                buffer.write(f"{utils.tab(indent+4)}{{\n")
                buffer.write(f"{utils.tab(indent+5)}return _GrpcFailure_{operation.name}( response.Status, response.Errors );\n")
                buffer.write(f"{utils.tab(indent+4)}}}\n")
            else:
                buffer.write(f"{utils.tab(indent+4)}if( response.IsSuccess() == true )\n")
                buffer.write(f"{utils.tab(indent+4)}{{\n")
                buffer.write(f"{utils.tab(indent+5)}return new {versionedName}_{operation.name}Response() {{ Status = ServiceKit.Protos.Statuses.Ok }};\n")
                buffer.write(f"{utils.tab(indent+4)}}}\n")
                buffer.write(f"{utils.tab(indent+4)}else\n")
                buffer.write(f"{utils.tab(indent+4)}{{\n")
                buffer.write(f"{utils.tab(indent+5)}return _GrpcFailure_{operation.name}( response.Status, response.Errors );\n")
                buffer.write(f"{utils.tab(indent+4)}}}\n")
                buffer.write(f"{utils.tab(indent+4)}\n")

            buffer.write(f"{utils.tab(indent+3)}}}\n")
            buffer.write(f"{utils.tab(indent+3)}catch(Exception ex)\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            buffer.write(f"{utils.tab(indent+4)}var failure = _MapFailure( ex );\n")
            buffer.write(f"{utils.tab(indent+4)}return _GrpcFailure_{operation.name}( failure.Status, failure.Errors );\n")
            buffer.write(f"{utils.tab(indent+3)}}}\n")
            # No 'finally' releasing the context: it may outlive the request. A service can hand it
            # to background work - the audit trail keeps a reference and reads the identity off it
            # when the entry is written - so the calling context is a plain per-request object now.
            buffer.write(f"{utils.tab(indent+2)}}}\n")
            buffer.write(f"{utils.tab(indent+1)}}}\n")

            buffer.write(self.grpcFailureText(f"{versionedName}_{operation.name}Response", operation.name, indent+1))

        # end of class
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def interfaceRestInternalClientText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET rest INTERNAL client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("System.Net")
        code.usings.add("ServiceKit.Net")

        # Add documentation lines for the interface
        buffer.write(self.documentLines(interface, indent))
        # client class declaration
        buffer.write(f"{utils.tab(indent)}public class {versionedName}_RestClient : I{versionedName} \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # private members
        buffer.write(f"{utils.tab(indent+1)}private readonly HttpClient _httpClient;\n")
        buffer.write(self.restClientJsonOptionsText(code, indent+1))

        # Add constructor with server address
        buffer.write(f"\n")
        buffer.write(f"{utils.tab(indent+1)}public {versionedName}_RestClient( string serverAddress )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}_httpClient = new HttpClient();\n")
        buffer.write(f"{utils.tab(indent+2)}_httpClient.BaseAddress = new Uri( serverAddress );\n")
        buffer.write(f"{utils.tab(indent+2)}_httpClient.DefaultRequestHeaders.Add(\"Accept\", \"application/json\");\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"\n")
        
        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(f"{utils.tab(indent+1)}/// <inheritdoc />\n")
            # Add return value
            buffer.write(f"{utils.tab(indent+1)}async Task<Response")
            if (operation.operation_return != None ):
                buffer.write(f"<{self.typeText(operation.operation_return.type, code,fullName=True)}>")
            buffer.write(f">")
            # Add function name
            buffer.write(f" I{versionedName}.{operation.name}(CallingContext ctx")
            # Add parameters
            if (len(operation.operation_params) > 0):
                buffer.write(f", ")
            buffer.write(", ".join([self.typeText(param.type, code,fullName=True) + " " + param.name for param in operation.operation_params]))
            buffer.write(")\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+2)}try\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            http_operation:rest_operation = rest_operation(operation)
            buffer.write(f"{utils.tab(indent+3)}// build request\n")

            # build route with FromRoute and Query params
            base_route = f"/{domain.name.lower()}/{context.name.lower()}/{interface.name.lower()}/v{interface.version}/{self.clientRouteText(http_operation, code)}"
            query_params = [
                f"{param.httpName}={self.convertToUrlValue(param.param.name, param.param.type, code.usings)}"
                for param in http_operation.params.values()
                if param.bindingSource == rest_param.BindingSource.FromQuery
            ]
            query_string = f"?{'&'.join(query_params)}" if query_params else ""

            buffer.write(f"{utils.tab(indent+3)}HttpRequestMessage request = new HttpRequestMessage( HttpMethod.{http_operation.verb.name}, $\"{base_route}{query_string}\" );\n")
            buffer.write(f"{utils.tab(indent+3)}ctx.FillHttpRequest( request, \"{domain.name}{context.name}{versionedName}\", \"{operation.name}\" );\n")
            buffer.write("\n")

            if(http_operation.isMultiPartFormData()):
                buffer.write(f"{utils.tab(indent+3)}// build multi part content\n")
                buffer.write(f"{utils.tab(indent+3)}MultipartFormDataContent multipartContent = new();\n")
                for http_param in http_operation.params.values():
                    match http_param.bindingSource:
                        case rest_param.BindingSource.FromRoute | rest_param.BindingSource.FromQuery | rest_param.BindingSource.FromBody:
                            pass
                        case rest_param.BindingSource.FromForm:
                            if( rest_utils.is_stream_type_param( http_param.param ) == True ):
                                buffer.write(f"{utils.tab(indent+3)}if({http_param.param.name}.CanSeek)\n")
                                buffer.write(f"{utils.tab(indent+4)}{http_param.param.name}.Seek( 0, SeekOrigin.Begin );\n")
                                buffer.write(f"{utils.tab(indent+3)}multipartContent.Add(new StreamContent({http_param.param.name}), {http_param.httpName}, \"__temp\");\n")
                            elif( rest_utils.is_body_type_param( http_param.param ) == True ):
                                code.usings.add("System.Text")
                                code.usings.add("System.Text.Json")
                                buffer.write(f"{utils.tab(indent+3)}multipartContent.Add( new StringContent( JsonSerializer.Serialize<{self.typeText( http_param.param.type, code, fullName=True)}>( {http_param.param.name}, _jsonOptions ), Encoding.UTF8, \"application/json\" ), \"{http_param.httpName}\", \"{http_param.httpName}.json\" );\n")
                buffer.write(f"{utils.tab(indent+3)}request.Content = multipartContent;\n")
                buffer.write("\n")
            else:
                count_body = rest_utils.count_body_param(operation)
                if( count_body > 0 ):
                    buffer.write(f"{utils.tab(indent+3)}// build content\n")
                    for http_param in http_operation.params.values():
                        match http_param.bindingSource:
                            case rest_param.BindingSource.FromRoute | rest_param.BindingSource.FromQuery | rest_param.BindingSource.FromForm:
                                pass
                            case rest_param.BindingSource.FromBody:
                                code.usings.add("System.Text")
                                code.usings.add("System.Text.Json")
                                # without the media type the body goes out as text/plain and the
                                # controller answers 415 before the service is ever reached
                                buffer.write(f"{utils.tab(indent+3)}request.Content = new StringContent( JsonSerializer.Serialize<{self.typeText( http_param.param.type, code, fullName=True)}>( {http_param.param.name}, _jsonOptions ), Encoding.UTF8, \"application/json\" );\n")
                    buffer.write("\n")
            
            # call hhtp
            buffer.write(f"{utils.tab(indent+3)}// call http client \n")
            buffer.write(f"{utils.tab(indent+3)}HttpResponseMessage response = await _httpClient.SendAsync( request );\n")

            # process result
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+3)}if (response.IsSuccessStatusCode)\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            if( operation.operation_return != None ):
                code.usings.add( "System.Net.Http.Json")
                buffer.write(f"{utils.tab(indent+4)}var value = await response.Content.ReadFromJsonAsync<{self.typeText( operation.operation_return.type, code, fullName=True)}>( _jsonOptions );\n")
                buffer.write(f"{utils.tab(indent+4)}return Response<{self.typeText( operation.operation_return.type, code, fullName=True)}>.Success( value );\n")
            else:
                buffer.write(f"{utils.tab(indent+4)}return Response.Success();\n")
                pass
            buffer.write(f"{utils.tab(indent+3)}}}\n")
            buffer.write(self.restClientFailureText(versionedName, operation, code, indent+3))
            buffer.write(f"{utils.tab(indent+2)}}}\n") # try
            buffer.write(f"{utils.tab(indent+2)}catch (HttpRequestException ex)\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "ex.StatusCode.HasValue ? ex.StatusCode.Value.FromHttp() : Statuses.InternalError", indent+3))
            buffer.write(f"{utils.tab(indent+2)}}}\n") # catch HttpRequestException
            buffer.write(f"{utils.tab(indent+2)}catch (Exception ex)\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "Statuses.InternalError", indent+3))
            buffer.write(f"{utils.tab(indent+2)}}}\n") # catch Exception
            buffer.write(f"{utils.tab(indent+1)}}}\n") # function
            buffer.write(f"\n")

        buffer.write(f"{utils.tab(indent)}}}\n") # classs

        code.content += buffer.getvalue()
        return code

    def restClientJsonOptionsText(self, code: dotnet_code, indent: int) -> str:
        """
        The client has to speak the host's JSON, not its own default.

        The host serialises enums by NAME, so a client reading with the plain default options fails
        on the very first answer it gets back - and it writes them as numbers, which happens to be
        accepted, which is why only one direction ever broke.
        """
        code.usings.add("System.Text.Json")
        code.usings.add("System.Text.Json.Serialization")

        buffer = io.StringIO()
        buffer.write(f"{utils.tab(indent)}// the same options the host is configured with: web defaults, and enums by name\n")
        buffer.write(f"{utils.tab(indent)}private static readonly JsonSerializerOptions _jsonOptions = new JsonSerializerOptions( JsonSerializerDefaults.Web )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}Converters = {{ new JsonStringEnumConverter() }},\n")
        buffer.write(f"{utils.tab(indent)}}};\n")
        return buffer.getvalue()

    def restClientFailureText(self, versionedName: str, operation: operation, code: dotnet_code, indent: int) -> str:
        # The body of a failed answer is a LIST of errors now: the HTTP status code already carries
        # the status, so the body is free to say every single thing that is wrong at once.
        code.usings.add("System.Net.Http.Json")
        buffer = io.StringIO()
        if (operation.operation_return != None):
            responseType = f"Response<{self.typeText(operation.operation_return.type, code, fullName=True)}>"
        else:
            responseType = "Response"
        buffer.write(f"{utils.tab(indent)}else if( response.Content != null )\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}var errors = await response.Content.ReadFromJsonAsync<List<ServiceKit.Net.Error>>( _jsonOptions );\n")
        buffer.write(f"{utils.tab(indent+1)}return {responseType}.Failure( response.StatusCode.FromHttp(), errors?.ToArray() ?? Array.Empty<ServiceKit.Net.Error>() );\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        buffer.write(f"{utils.tab(indent)}else\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}return {responseType}.Failure( response.StatusCode.FromHttp(), \"Not handled reponse in REST client when calling '{versionedName}_{operation.name}'\" );\n")
        buffer.write(f"{utils.tab(indent)}}}\n")
        return buffer.getvalue()

    def interfaceRestPublicClientText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET rest Public client code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("System.Net")
        code.usings.add("ServiceKit.Net")

        # Add documentation lines for the interface
        buffer.write(self.documentLines(interface, indent))
        # client class declaration
        buffer.write(f"{utils.tab(indent)}static partial class Rest \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(self.documentLines(interface, indent+1))
        buffer.write(f"{utils.tab(indent+1)}static class {interface.name}\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}static class V{interface.version} \n")
        buffer.write(f"{utils.tab(indent+2)}{{\n")
        buffer.write(self.restClientJsonOptionsText(code, indent+3))

        # Add functions based on operations
        for operation in interface.operations:
            buffer.write(self.documentLines(operation, indent+2))
            # Add return value
            buffer.write(f"{utils.tab(indent+3)}public static async Task<Response")
            if (operation.operation_return != None ):
                buffer.write(f"<{self.typeText(operation.operation_return.type, code,fullName=True)}>")
            buffer.write(f"> ")
            # Add function name
            buffer.write(f"{operation.name}(")
            # Add parameters
            buffer.write(", ".join([self.typeText(param.type, code,fullName=True) + " " + param.name for param in operation.operation_params]))
            buffer.write(")\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            buffer.write(f"{utils.tab(indent+4)}try\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")

            http_operation:rest_operation = rest_operation(operation)
            buffer.write(f"{utils.tab(indent+5)}// build request\n")

            # build route with FromRoute and Query params
            base_route = f"/{domain.name.lower()}/{context.name.lower()}/{interface.name.lower()}/v{interface.version}/{self.clientRouteText(http_operation, code)}"
            query_params = [
                f"{param.httpName}={self.convertToUrlValue(param.param.name, param.param.type, code.usings)}"
                for param in http_operation.params.values()
                if param.bindingSource == rest_param.BindingSource.FromQuery
            ]
            query_string = f"?{'&'.join(query_params)}" if query_params else ""

            buffer.write(f"{utils.tab(indent+5)}HttpRequestMessage request = new HttpRequestMessage( HttpMethod.{http_operation.verb.name}, $\"{base_route}{query_string}\" );\n")
            buffer.write("\n")

            if(http_operation.isMultiPartFormData()):
                buffer.write(f"{utils.tab(indent+5)}// build multi part content\n")
                buffer.write(f"{utils.tab(indent+5)}MultipartFormDataContent multipartContent = new();\n")
                for http_param in http_operation.params.values():
                    match http_param.bindingSource:
                        case rest_param.BindingSource.FromRoute | rest_param.BindingSource.FromQuery | rest_param.BindingSource.FromBody:
                            pass
                        case rest_param.BindingSource.FromForm:
                            if( rest_utils.is_stream_type_param( http_param.param ) == True ):
                                buffer.write(f"{utils.tab(indent+5)}if(content.CanSeek)\n")
                                buffer.write(f"{utils.tab(indent+6)}content.Seek( 0, SeekOrigin.Begin );\n")
                                buffer.write(f"{utils.tab(indent+6)}multipartContent.Add(new StreamContent(stream), {http_param.httpName}, \"__temp\");\n")
                            elif( rest_utils.is_body_type_param( http_param.param ) == True ):
                                code.usings.add("System.Text")
                                code.usings.add("System.Text.Json")
                                buffer.write(f"{utils.tab(indent+5)}multipartContent.Add( new StringContent( JsonSerializer.Serialize<{self.typeText( http_param.param.type, code, fullName=True)}>( {http_param.param.name}, _jsonOptions ), Encoding.UTF8, \"application/json\" ), \"{http_param.httpName}\", \"{http_param.httpName}.json\" );\n")
                buffer.write(f"{utils.tab(indent+4)}request.Content = multipartContent;\n")
                buffer.write("\n")
            else:
                count_body = rest_utils.count_body_param(operation)
                if( count_body > 0 ):
                    buffer.write(f"{utils.tab(indent+5)}// build content\n")
                    for http_param in http_operation.params.values():
                        match http_param.bindingSource:
                            case rest_param.BindingSource.FromRoute | rest_param.BindingSource.FromQuery | rest_param.BindingSource.FromForm:
                                pass
                            case rest_param.BindingSource.FromBody:
                                code.usings.add("System.Text")
                                code.usings.add("System.Text.Json")
                                buffer.write(f"{utils.tab(indent+5)}request.Content = new StringContent( JsonSerializer.Serialize<{self.typeText( http_param.param.type, code, fullName=True)}>( {http_param.param.name}, _jsonOptions ), Encoding.UTF8, \"application/json\" );\n")
                    buffer.write("\n")
            
            # call hhtp
            buffer.write(f"{utils.tab(indent+5)}// call rest client \n")
            buffer.write(f"{utils.tab(indent+5)}HttpResponseMessage response = await RestClient.Request( request, \"{domain.name}.{context.name}.{interface.name}.V{interface.version}.{operation.name}\" );\n")

            # process result
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+5)}if (response.IsSuccessStatusCode)\n")
            buffer.write(f"{utils.tab(indent+5)}{{\n")
            if( operation.operation_return != None ):
                code.usings.add( "System.Net.Http.Json")
                buffer.write(f"{utils.tab(indent+6)}var value = await response.Content.ReadFromJsonAsync<{self.typeText( operation.operation_return.type, code, fullName=True)}>( _jsonOptions );\n")
                buffer.write(f"{utils.tab(indent+6)}return Response<{self.typeText( operation.operation_return.type, code, fullName=True)}>.Success( value );\n")
            else:
                buffer.write(f"{utils.tab(indent+6)}return Response.Success();\n")
                pass
            buffer.write(f"{utils.tab(indent+5)}}}\n")
            buffer.write(self.restClientFailureText(versionedName, operation, code, indent+5))
            buffer.write(f"{utils.tab(indent+4)}}}\n") # try
            buffer.write(f"{utils.tab(indent+4)}catch (HttpRequestException ex)\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "ex.StatusCode.HasValue ? ex.StatusCode.Value.FromHttp() : Statuses.InternalError", indent+5))
            buffer.write(f"{utils.tab(indent+4)}}}\n") # catch HttpRequestException
            buffer.write(f"{utils.tab(indent+4)}catch (Exception ex)\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            buffer.write(self.clientFailureText(operation, code, "Statuses.InternalError", indent+5))
            buffer.write(f"{utils.tab(indent+4)}}}\n") # catch Exception
            buffer.write(f"{utils.tab(indent+3)}}}\n") # function
            buffer.write(f"\n")

        buffer.write(f"{utils.tab(indent+2)}}}\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def interfaceRestControllerText(self, interface: interface, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the .NET Rest controller code for interface
        """
        buffer = io.StringIO()
        domain: domain = interface.getDomain()
        context: context = interface.getContext()
        versionedName: str = f"{interface.name}_v{interface.version}"

        code.usings.add("System.Net.Mime")
        code.usings.add("Microsoft.AspNetCore.Authorization")
        code.usings.add("Microsoft.AspNetCore.Http")
        code.usings.add("Microsoft.AspNetCore.Mvc")
        code.usings.add("Microsoft.AspNetCore.RateLimiting")
        code.usings.add("Microsoft.Extensions.Logging")
        code.usings.add("Swashbuckle.AspNetCore.Annotations")
        code.usings.add("Swashbuckle.AspNetCore.Swagger")
        code.usings.add("ServiceKit.Net")
        code.usings.add("Serilog.Context")

        # Add documentation lines for the interface
        buffer.write(self.documentLines(interface, indent))

        # class declaration
        buffer.write(f"{utils.tab(indent)}[ApiController]\n")
        buffer.write(f"{utils.tab(indent)}[Route( \"{domain.name.lower()}/{context.name.lower()}/{interface.name.lower()}/v{interface.version}\" )]\n")
        if( len(interface.document_lines) > 0 ):
            buffer.write(f"{utils.tab(indent)}[SwaggerTag( \"{utils.document_lines_to_one(interface)}\" )]\n")
        buffer.write(f"{utils.tab(indent)}public class {versionedName}_RestController : ControllerBase \n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        # class members
        buffer.write(f"{utils.tab(indent+1)}private readonly ILogger<{versionedName}_RestController> _logger;\n")
        buffer.write(f"{utils.tab(indent+1)}private readonly I{versionedName} _service;\n")
        # class constructor
        buffer.write(f"{utils.tab(indent+1)}public {versionedName}_RestController( ILogger<{versionedName}_RestController> logger, I{versionedName} service )\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}_logger = logger; \n")
        buffer.write(f"{utils.tab(indent+2)}_service = service; \n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")

        buffer.write(self.controllerMapFailureText(code, indent+1))

        # Add functions based on operations
        for operation in interface.operations:

            buffer.write(f"\n")
            buffer.write(self.documentLines(operation, indent+1))
            http_operation:rest_operation = rest_operation(operation)
            match http_operation.verb:
                case rest_operation.Verb.Get:
                    buffer.write(f"{utils.tab(indent+1)}[HttpGet( \"{http_operation.full_route}\" )] \n")        
                case rest_operation.Verb.Post:
                    buffer.write(f"{utils.tab(indent+1)}[HttpPost( \"{http_operation.full_route}\" )] \n")        
            buffer.write(f"{utils.tab(indent+1)}[Produces( MediaTypeNames.Application.Json )]\n")
            if( http_operation.isMultiPartFormData() == True ):
                buffer.write(f"{utils.tab(indent+1)}[Consumes( \"multipart/form-data\" )]\n")
                
            if( len(operation.document_lines) > 0 ):
                buffer.write(f"{utils.tab(indent+1)}[SwaggerOperation( \"{utils.document_lines_to_one(operation)}\" )]\n")
            if( operation.operation_return != None ):
                buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status200OK, \"{utils.document_lines_to_one(operation.operation_return)}\", typeof({self.typeText( operation.operation_return.type, code, fullName=True )}) )]\n")
            else:
                buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status200OK, \"Ok\" )]\n")
            # a failure body is a LIST: a form with three bad fields is the ordinary case, and the
            # client has to be told about all three at once, not made to fix them one round trip
            # at a time. The status itself travels as the HTTP status code.
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status400BadRequest, nameof(StatusCodes.Status400BadRequest), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status408RequestTimeout, nameof(StatusCodes.Status408RequestTimeout), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status404NotFound, nameof(StatusCodes.Status404NotFound), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status401Unauthorized, nameof(StatusCodes.Status401Unauthorized), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status501NotImplemented, nameof(StatusCodes.Status501NotImplemented), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}[SwaggerResponse( StatusCodes.Status500InternalServerError, nameof(StatusCodes.Status500InternalServerError), typeof(IList<ServiceKit.Net.Error>) )]\n")
            buffer.write(f"{utils.tab(indent+1)}public async Task<IActionResult> {operation.name}(")
            index: int = 0
            params: List[str] = []
            for param in operation.operation_params:
                if( index> 0 ):
                    buffer.write(", ")
                
                http_param:rest_param = http_operation.params[param.name]
                match http_param.bindingSource:
                    case rest_param.BindingSource.FromRoute:
                        buffer.write( f" [FromRoute] {self.typeText(param.type, code, fullName=True)} {http_param.httpName}")
                    case rest_param.BindingSource.FromQuery:
                        if( utils.isEnumType(param.type) == False ):
                            buffer.write( f" [FromQuery] {self.typeText(param.type, code, fullName=True)} {http_param.httpName}")
                        else:
                            buffer.write( f" [FromQuery] string {http_param.httpName}")
                    case rest_param.BindingSource.FromBody:
                        buffer.write( f" [FromBody] {self.typeText(param.type, code, fullName=True)} {http_param.httpName}")
                    case rest_param.BindingSource.FromForm:
                        buffer.write( f" [FromForm] IFormFile {http_param.httpName}")
                params.append(param.name)
                index = index + 1
            buffer.write(f")\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+2)}using(LogContext.PushProperty( \"Scope\", \"{versionedName}.{operation.name}\" ))\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            buffer.write(f"{utils.tab(indent+3)}CallingContext ctx = CallingContext.FromHttpContext( HttpContext, _logger );\n")
            buffer.write(f"{utils.tab(indent+3)}try\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            for http_param in http_operation.params.values():
                match http_param.bindingSource:
                    case rest_param.BindingSource.FromRoute | rest_param.BindingSource.FromBody:
                        pass
                    case rest_param.BindingSource.FromQuery:
                        if( utils.isEnumType(http_param.param.type) == True ):
                            buffer.write(f"{utils.tab(indent+4)}{self.typeText(http_param.param.type, code, fullName=True)} {http_param.param.name} = ({self.typeText(http_param.param.type, code, fullName=True)})Enum.Parse(typeof({self.typeText(http_param.param.type, code, fullName=True)}), {http_param.httpName});\n")
                            pass
                    case rest_param.BindingSource.FromForm:
                        if( rest_utils.is_stream_type_param( http_param.param ) == True ):
                            buffer.write(f"{utils.tab(indent+4)}Stream {http_param.param.name} = {http_param.httpName}?.OpenReadStream();\n")
                            buffer.write(f"{utils.tab(indent+4)}if(content.CanSeek)\n")
                            buffer.write(f"{utils.tab(indent+5)}content.Seek( 0, SeekOrigin.Begin );\n")
                            buffer.write(f"\n")
                        elif( rest_utils.is_body_type_param( http_param.param ) == True ):
                            code.usings.add("System.Text.Json")
                            buffer.write(f"{utils.tab(indent+4)}string json_{http_param.param.name} = await new StreamReader( {http_param.httpName}.OpenReadStream() ).ReadToEndAsync();\n")
                            buffer.write(f"{utils.tab(indent+4)}{self.typeText(http_param.param.type, code, fullName=True)} {http_param.param.name} = JsonSerializer.Deserialize<{self.typeText(http_param.param.type, code, fullName=True)}>( json_{http_param.param.name} );\n")
                            buffer.write(f"\n")

            buffer.write(f"{utils.tab(indent+4)}// calling the service function itself\n")
            buffer.write(f"{utils.tab(indent+4)}var response = await _service.{operation.name}( ctx{", " + ", ".join(params) if params else ""} );\n")
            buffer.write(f"\n")
            buffer.write(f"{utils.tab(indent+4)}if( response.IsSuccess() == true )\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            if( operation.operation_return != None ):
                buffer.write(f"{utils.tab(indent+5)}if( response.HasValue() == true )\n")
                buffer.write(f"{utils.tab(indent+5)}{{\n")
                buffer.write(f"{utils.tab(indent+6)}return Ok(response.Value);\n")
                buffer.write(f"{utils.tab(indent+5)}}}\n")
                buffer.write(f"{utils.tab(indent+5)}else\n")
                buffer.write(f"{utils.tab(indent+5)}{{\n")
                buffer.write(f"{utils.tab(indent+6)}return StatusCode(Statuses.NotImplemented.ToHttp(), new List<ServiceKit.Net.Error>() {{ new() {{ MessageText = \"Not handled reponse in REST Controller when calling '{versionedName}.{operation.name}'\" }} }} );\n")
                buffer.write(f"{utils.tab(indent+5)}}}\n")
            else:
                buffer.write(f"{utils.tab(indent+5)}return Ok();\n")

            buffer.write(f"{utils.tab(indent+4)}}}\n")
            buffer.write(f"{utils.tab(indent+4)}else\n")
            buffer.write(f"{utils.tab(indent+4)}{{\n")
            buffer.write(f"{utils.tab(indent+5)}return StatusCode(response.Status.ToHttp(), response.Errors);\n")
            buffer.write(f"{utils.tab(indent+4)}}}\n")
            buffer.write(f"{utils.tab(indent+3)}}}\n")
            buffer.write(f"{utils.tab(indent+3)}catch(Exception ex)\n")
            buffer.write(f"{utils.tab(indent+3)}{{\n")
            buffer.write(f"{utils.tab(indent+4)}var failure = _MapFailure( ex );\n")
            buffer.write(f"{utils.tab(indent+4)}return StatusCode(failure.Status.ToHttp(), failure.Errors);\n")
            buffer.write(f"{utils.tab(indent+3)}}}\n")
            # No 'finally' releasing the context: it may outlive the request. A service can hand it
            # to background work - the audit trail keeps a reference and reads the identity off it
            # when the entry is written - so the calling context is a plain per-request object now.
            buffer.write(f"{utils.tab(indent+2)}}}\n")
            buffer.write(f"{utils.tab(indent+1)}}}\n")

        # end of class
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def workflowActivitiesInterfaceText(self, the_workflow: workflow, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the activity interface of a workflow: one [Activity] method per step. The
        implementation belongs to the developer, so it is never generated.
        """
        buffer = io.StringIO()
        code.usings.add("Temporalio.Activities")

        buffer.write("\n")
        buffer.write(f"{utils.tab(indent)}/// <summary>\n")
        buffer.write(f"{utils.tab(indent)}/// The activities of workflow '{the_workflow.name}'. Implement this interface and register the\n")
        buffer.write(f"{utils.tab(indent)}/// implementation as a singleton - the worker resolves it from the service container.\n")
        buffer.write(f"{utils.tab(indent)}/// </summary>\n")
        buffer.write(f"{utils.tab(indent)}public partial interface I{the_workflow.name}Activities\n")
        buffer.write(f"{utils.tab(indent)}{{\n")

        for index, the_step in enumerate(the_workflow.steps):
            if (index > 0):
                buffer.write("\n")
            buffer.write(self.documentLines(the_step, indent+1))
            buffer.write(f"{utils.tab(indent+1)}[Activity]\n")
            buffer.write(f"{utils.tab(indent+1)}{self.__stepReturnTypeText(the_step, code)} {the_step.name}({self.__stepParamsText(the_step, code)});\n")

        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def workflowClassText(self, the_workflow: workflow, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the workflow class and, next to it, the saga-aware step facade.

        The model declares a SET of steps, not an order, so the body cannot be generated. What is
        generated is the saga guarantee: the developer writes the sequence, and every step that
        declares a compensation registers it for reverse-order rollback.
        """
        buffer = io.StringIO()
        code.usings.add("ServiceKit.Net")
        code.usings.add("Temporalio.Workflows")

        has_steps: bool = len(the_workflow.steps) > 0
        start_command: operation = self.__workflowStartCommand(the_workflow)
        # The developer side of every partial, collected while the public surface is written and
        # emitted in one block at the end.
        hooks: List[str] = []

        buffer.write("\n")
        buffer.write(self.documentLines(the_workflow, indent))
        buffer.write(f"{utils.tab(indent)}[Workflow]\n")
        buffer.write(f"{utils.tab(indent)}public partial class {the_workflow.name}Workflow\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}private readonly WorkflowSaga _saga = new();\n")

        if (has_steps == True):
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+1)}/// <summary>Call the steps through this: it runs the activity AND records its rollback.</summary>\n")
            buffer.write(f"{utils.tab(indent+1)}protected {the_workflow.name}Steps Steps {{ get; }}\n")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+1)}public {the_workflow.name}Workflow()\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            buffer.write(f"{utils.tab(indent+2)}Steps = new {the_workflow.name}Steps(_saga);\n")
            buffer.write(f"{utils.tab(indent+1)}}}\n")

        for the_operation in the_workflow.operations:
            params_text: str = self.__operationParamsText(the_operation, code)
            args_text: str = ", ".join([param.name for param in the_operation.operation_params])
            hook_name: str = "On" + utils.camel_to_pascal(the_operation.name)
            returns: operation_return = the_operation.operation_return

            buffer.write("\n")
            buffer.write(self.documentLines(the_operation, indent+1))

            if (the_operation is start_command):
                # The entry point. Everything it throws rolls the saga back, in reverse order.
                return_text = "Task" if (returns == None) else f"Task<{self.typeText(returns.type, code, fullName=True)}>"
                buffer.write(f"{utils.tab(indent+1)}[WorkflowRun]\n")
                buffer.write(f"{utils.tab(indent+1)}public async {return_text} {the_operation.name}({params_text})\n")
                buffer.write(f"{utils.tab(indent+1)}{{\n")
                buffer.write(f"{utils.tab(indent+2)}try\n")
                buffer.write(f"{utils.tab(indent+2)}{{\n")
                if (returns == None):
                    buffer.write(f"{utils.tab(indent+3)}await {hook_name}({args_text});\n")
                else:
                    buffer.write(f"{utils.tab(indent+3)}return await {hook_name}({args_text});\n")
                buffer.write(f"{utils.tab(indent+2)}}}\n")
                buffer.write(f"{utils.tab(indent+2)}catch (Exception failure)\n")
                buffer.write(f"{utils.tab(indent+2)}{{\n")
                buffer.write(f"{utils.tab(indent+3)}// the failure is handed over, so it survives as the InnerException even when a compensation fails too\n")
                buffer.write(f"{utils.tab(indent+3)}await _saga.CompensateAsync(failure);\n")
                buffer.write(f"{utils.tab(indent+3)}throw;\n")
                buffer.write(f"{utils.tab(indent+2)}}}\n")
                buffer.write(f"{utils.tab(indent+1)}}}\n")
                hooks.append(f"private partial {return_text} {hook_name}({params_text});")

            elif (the_operation.kind == operation.Kind.Query):
                # A Temporal query is read-only and synchronous - it may not await anything
                return_text = "void" if (returns == None) else self.typeText(returns.type, code, fullName=True)
                buffer.write(f"{utils.tab(indent+1)}[WorkflowQuery]\n")
                buffer.write(f"{utils.tab(indent+1)}public {return_text} {the_operation.name}({params_text}) => {hook_name}({args_text});\n")
                hooks.append(f"private partial {return_text} {hook_name}({params_text});")

            elif (returns == None):
                # A command with nothing to return cannot answer the caller either: that is a signal
                buffer.write(f"{utils.tab(indent+1)}[WorkflowSignal]\n")
                buffer.write(f"{utils.tab(indent+1)}public Task {the_operation.name}({params_text}) => {hook_name}({args_text});\n")
                hooks.append(f"private partial Task {hook_name}({params_text});")

            else:
                # It returns something, so the caller waits for it - and may be turned down: update
                return_text = f"Task<{self.typeText(returns.type, code, fullName=True)}>"
                buffer.write(f"{utils.tab(indent+1)}[WorkflowUpdate]\n")
                buffer.write(f"{utils.tab(indent+1)}public {return_text} {the_operation.name}({params_text}) => {hook_name}({args_text});\n")
                hooks.append(f"private partial {return_text} {hook_name}({params_text});")

        for the_eventhandler in the_workflow.eventhandlers:
            handled_event: event = Engine.get_referenced_element(the_eventhandler, the_eventhandler.handledEvent)
            if (handled_event == None):
                continue
            event_text: str = code.getDotnetFullName(handled_event)
            hook_name: str = "Handle" + utils.camel_to_pascal(the_eventhandler.name)

            buffer.write("\n")
            buffer.write(self.documentLines(the_eventhandler, indent+1))
            buffer.write(f"{utils.tab(indent+1)}[WorkflowSignal]\n")
            buffer.write(f"{utils.tab(indent+1)}public Task {the_eventhandler.name}({event_text} @event) => {hook_name}(@event);\n")
            hooks.append(f"private partial Task {hook_name}({event_text} @event);")

        if (len(hooks) > 0):
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+1)}// The other half of the partial: this is what you write. The model declares which steps\n")
            buffer.write(f"{utils.tab(indent+1)}// exist, not in what order - so the body is yours, and the compiler will not let you forget it.\n")
            for hook in hooks:
                buffer.write(f"{utils.tab(indent+1)}{hook}\n")

        if (len(the_workflow.enums) > 0 or len(the_workflow.value_objects) > 0):
            buffer.write("\n")

        code.content += buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)

        # types declared inside the workflow live inside the generated class
        for the_enum in the_workflow.enums:
            code = self.enumText(the_enum, code, indent+1)
        for the_valueobject in the_workflow.value_objects:
            code = self.valueobjectText(the_valueobject, code, indent+1)

        buffer.write(f"{utils.tab(indent)}}}\n")
        code.content += buffer.getvalue()

        if (has_steps == True):
            code = self.workflowStepsFacadeText(the_workflow, code, indent)

        return code

    def workflowStepsFacadeText(self, the_workflow: workflow, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the typed step facade - the piece that turns a declared 'compensate' into an
        actual rollback.
        """
        buffer = io.StringIO()
        activities_name: str = f"I{the_workflow.name}Activities"
        defaults_name: str = f"{the_workflow.name}Defaults"

        buffer.write("\n")
        buffer.write(f"{utils.tab(indent)}/// <summary>\n")
        buffer.write(f"{utils.tab(indent)}/// The typed, saga-aware steps of workflow '{the_workflow.name}'. Calling a step here runs the\n")
        buffer.write(f"{utils.tab(indent)}/// activity and records its compensation, so a later failure rolls it back automatically.\n")
        buffer.write(f"{utils.tab(indent)}/// </summary>\n")
        buffer.write(f"{utils.tab(indent)}public sealed partial class {the_workflow.name}Steps\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}private readonly WorkflowSaga _saga;\n")
        buffer.write("\n")
        buffer.write(f"{utils.tab(indent+1)}internal {the_workflow.name}Steps(WorkflowSaga saga)\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}_saga = saga;\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")

        for the_step in the_workflow.steps:
            compensation: step = self.__findStep(the_workflow, the_step.compensate)
            return_text: str = self.__stepReturnTypeText(the_step, code)
            params_text: str = self.__stepParamsText(the_step, code)
            args_text: str = ", ".join([param.name for param in the_step.operation_params])
            call_text: str = f"({activities_name} activities) => activities.{the_step.name}({args_text})"

            buffer.write("\n")
            buffer.write(self.documentLines(the_step, indent+1))

            if (compensation == None):
                # nothing declared to roll it back, so the call goes straight through
                buffer.write(f"{utils.tab(indent+1)}public {return_text} {the_step.name}({params_text})\n")
                buffer.write(f"{utils.tab(indent+1)}{{\n")
                buffer.write(f"{utils.tab(indent+2)}return Workflow.ExecuteActivityAsync(\n")
                buffer.write(f"{utils.tab(indent+3)}{call_text},\n")
                buffer.write(f"{utils.tab(indent+3)}{defaults_name}.For(nameof({the_step.name})));\n")
                buffer.write(f"{utils.tab(indent+1)}}}\n")
                continue

            result_name: str = self.__resultLocalName(the_step)
            compensation_args: str = ", ".join(self.__compensationArgumentNames(the_step, compensation, result_name))
            compensation_call: str = f"({activities_name} activities) => activities.{compensation.name}({compensation_args})"

            buffer.write(f"{utils.tab(indent+1)}public async {return_text} {the_step.name}({params_text})\n")
            buffer.write(f"{utils.tab(indent+1)}{{\n")
            if (the_step.operation_return == None):
                buffer.write(f"{utils.tab(indent+2)}await Workflow.ExecuteActivityAsync(\n")
            else:
                buffer.write(f"{utils.tab(indent+2)}var {result_name} = await Workflow.ExecuteActivityAsync(\n")
            buffer.write(f"{utils.tab(indent+3)}{call_text},\n")
            buffer.write(f"{utils.tab(indent+3)}{defaults_name}.For(nameof({the_step.name})));\n")
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+2)}// the compensation arguments are bound from the step's own parameters and return value\n")
            buffer.write(f"{utils.tab(indent+2)}_saga.Push(nameof({the_step.name}), () => Workflow.ExecuteActivityAsync(\n")
            buffer.write(f"{utils.tab(indent+3)}{compensation_call},\n")
            buffer.write(f"{utils.tab(indent+3)}{defaults_name}.For(nameof({activities_name}.{compensation.name}))));\n")
            if (the_step.operation_return != None):
                buffer.write("\n")
                buffer.write(f"{utils.tab(indent+2)}return {result_name};\n")
            buffer.write(f"{utils.tab(indent+1)}}}\n")

        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def workflowDefaultsText(self, the_workflow: workflow, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the per step activity options. '@timeout' is the whole business budget
        (ScheduleToClose, retries included); the ceiling of one attempt (StartToClose) is technical,
        so it stays out of the model and lives here as an overridable default.
        """
        buffer = io.StringIO()
        code.usings.add("Temporalio.Common")
        code.usings.add("Temporalio.Workflows")

        # (step name, retry attempts, timeout text) for every step that has anything to say
        timings: List[NamedTuple] = []
        for the_step in the_workflow.steps:
            attempts = self.__timingRetryAttempts(the_step, the_workflow)
            timeout_text = self.__timingTimeoutText(the_step, the_workflow)
            if (attempts != None or timeout_text != None):
                timings.append((the_step.name, attempts, timeout_text))

        buffer.write("\n")
        buffer.write(f"{utils.tab(indent)}/// <summary>\n")
        buffer.write(f"{utils.tab(indent)}/// The activity options of the steps of workflow '{the_workflow.name}'.\n")
        buffer.write(f"{utils.tab(indent)}/// </summary>\n")
        buffer.write(f"{utils.tab(indent)}public static partial class {the_workflow.name}Defaults\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}/// <summary>The ceiling of a single attempt. Technical, not a business property, so it is not modelled.</summary>\n")
        buffer.write(f"{utils.tab(indent+1)}public static TimeSpan DefaultStartToCloseTimeout {{ get; set; }} = TimeSpan.FromMinutes(1);\n")
        buffer.write("\n")
        buffer.write(f"{utils.tab(indent+1)}public static ActivityOptions For(string stepName)\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}var options = new ActivityOptions\n")
        buffer.write(f"{utils.tab(indent+2)}{{\n")
        buffer.write(f"{utils.tab(indent+3)}StartToCloseTimeout = DefaultStartToCloseTimeout,\n")
        buffer.write(f"{utils.tab(indent+2)}}};\n")

        if (len(timings) > 0):
            buffer.write("\n")
            buffer.write(f"{utils.tab(indent+2)}switch (stepName)\n")
            buffer.write(f"{utils.tab(indent+2)}{{\n")
            for name, attempts, timeout_text in timings:
                buffer.write(f"{utils.tab(indent+3)}case \"{name}\":\n")
                if (timeout_text != None):
                    buffer.write(f"{utils.tab(indent+4)}options.ScheduleToCloseTimeout = {timeout_text};\n")
                if (attempts != None):
                    buffer.write(f"{utils.tab(indent+4)}options.RetryPolicy = new RetryPolicy {{ MaximumAttempts = {attempts} }};\n")
                buffer.write(f"{utils.tab(indent+4)}break;\n")
            buffer.write(f"{utils.tab(indent+2)}}}\n")

        buffer.write("\n")
        buffer.write(f"{utils.tab(indent+2)}Customize(stepName, options);\n")
        buffer.write(f"{utils.tab(indent+2)}return options;\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write("\n")
        buffer.write(f"{utils.tab(indent+1)}/// <summary>Implement this in your own partial to override anything above.</summary>\n")
        buffer.write(f"{utils.tab(indent+1)}static partial void Customize(string stepName, ActivityOptions options);\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def workflowRegistrationText(self, the_workflow: workflow, code: dotnet_code, indent: int = 1) -> dotnet_code:
        """
        Generates the worker registration. The task queue is derived per workflow; several workflows
        pointed at the same name end up in a single worker, so the coarser layout costs nothing.
        """
        buffer = io.StringIO()
        code.usings.add("ServiceKit.Net")

        context: context = the_workflow.getContext()
        task_queue: str = f"{context.name}.{the_workflow.name}"
        activities: str = "" if (len(the_workflow.steps) == 0) else f", typeof(I{the_workflow.name}Activities)"

        buffer.write("\n")
        buffer.write(f"{utils.tab(indent)}/// <summary>\n")
        buffer.write(f"{utils.tab(indent)}/// Registers workflow '{the_workflow.name}' with the worker host.\n")
        buffer.write(f"{utils.tab(indent)}/// </summary>\n")
        buffer.write(f"{utils.tab(indent)}public static partial class {the_workflow.name}Registration\n")
        buffer.write(f"{utils.tab(indent)}{{\n")
        buffer.write(f"{utils.tab(indent+1)}/// <summary>\n")
        buffer.write(f"{utils.tab(indent+1)}/// Derived per workflow. Hand two workflows the same name and one worker serves both -\n")
        buffer.write(f"{utils.tab(indent+1)}/// splitting a shared queue later is a migration, merging separate ones is free.\n")
        buffer.write(f"{utils.tab(indent+1)}/// </summary>\n")
        buffer.write(f"{utils.tab(indent+1)}public const string TaskQueue = \"{task_queue}\";\n")
        buffer.write("\n")
        buffer.write(f"{utils.tab(indent+1)}public static WorkflowRegistry Register(WorkflowRegistry registry, string taskQueue = TaskQueue)\n")
        buffer.write(f"{utils.tab(indent+1)}{{\n")
        buffer.write(f"{utils.tab(indent+2)}return registry.Register<{the_workflow.name}Workflow>(taskQueue{activities});\n")
        buffer.write(f"{utils.tab(indent+1)}}}\n")
        buffer.write(f"{utils.tab(indent)}}}\n")

        code.content += buffer.getvalue()
        return code

    def __workflowStartCommand(self, the_workflow: workflow) -> operation:
        # The entry point: the '@start' command, or the only command there is.
        commands = [candidate for candidate in the_workflow.operations if candidate.kind == operation.Kind.Command]
        for candidate in commands:
            if (candidate.find_decorator("start") != None):
                return candidate
        if (len(commands) == 1):
            return commands[0]
        return None

    def __findStep(self, the_workflow: workflow, name: str) -> step:
        if (name == None):
            return None
        for candidate in the_workflow.steps:
            if (candidate.name == name):
                return candidate
        return None

    def __stepReturnTypeText(self, the_step: step, code: dotnet_code) -> str:
        if (the_step.operation_return == None):
            return "Task"
        return f"Task<{self.typeText(the_step.operation_return.type, code, fullName=True)}>"

    def __stepParamsText(self, the_step: step, code: dotnet_code) -> str:
        return ", ".join([self.typeText(param.type, code, fullName=True, isInFunctionParam=True) + " " + param.name for param in the_step.operation_params])

    def __operationParamsText(self, the_operation: operation, code: dotnet_code) -> str:
        return ", ".join([self.typeText(param.type, code, fullName=True, isInFunctionParam=True) + " " + param.name for param in the_operation.operation_params])

    def __resultLocalName(self, the_step: step) -> str:
        # the step's own parameters are in scope, so the local must not collide with them
        taken = [param.name for param in the_step.operation_params]
        name = "result"
        while (name in taken):
            name = name + "_"
        return name

    def __compensationArgumentNames(self, forward: step, compensation: step, result_name: str) -> List[str]:
        # Every compensation parameter binds either to a forward parameter (name and type) or to the
        # forward return value. The linter refuses anything that does not bind, so by the time we get
        # here the mapping exists.
        forward_params = [param.name for param in forward.operation_params]
        arguments: List[str] = []
        for param in compensation.operation_params:
            if (param.name in forward_params):
                arguments.append(param.name)
            elif (forward.operation_return != None):
                arguments.append(result_name)
            else:
                arguments.append(param.name)
        return arguments

    def __timingRetryAttempts(self, the_step: step, the_workflow: workflow) -> int:
        # the step's own decorator wins over the workflow-wide default
        retry = the_step.find_decorator("retry")
        if (retry == None):
            retry = the_workflow.find_decorator("retry")
        if (retry == None or len(retry.params) != 1):
            return None
        return retry.params[0].value

    def __timingTimeoutText(self, the_step: step, the_workflow: workflow) -> str:
        timeout = the_step.find_decorator("timeout")
        if (timeout == None):
            timeout = the_workflow.find_decorator("timeout")
        if (timeout == None or len(timeout.params) != 1):
            return None
        return self.__durationToTimeSpanText(timeout.params[0].value)

    def __durationToTimeSpanText(self, text: str) -> str:
        if (isinstance(text, str) == False):
            return None
        parts = DURATION_PARTS.findall(text)
        if (len(parts) == 0):
            return None
        total_ms: int = 0
        for value, unit in parts:
            total_ms = total_ms + int(value) * DURATION_UNITS[unit]
        if (total_ms % 1000 == 0):
            return f"TimeSpan.FromSeconds({total_ms // 1000})"
        return f"TimeSpan.FromMilliseconds({total_ms})"

    def deprecatedText(self, element: hinted_base_element, indent: int) -> str:
        # @deprecated(...) -> C# [Obsolete("message")]. The optional first
        # decorator param is the message (e.g. @deprecated("use X, since 2.3")).
        deprecated = element.find_decorator("deprecated")
        if (deprecated == None):
            return ""
        message = None
        if (len(deprecated.params) > 0):
            message = deprecated.params[0].value
        if (message != None):
            return f'{utils.tab(indent)}[Obsolete("{message}")]\n'
        return f"{utils.tab(indent)}[Obsolete]\n"

    def propertyText(self, member: hinted_base_element, code: dotnet_code, indent: int) -> str:
        buffer = io.StringIO()

        dotnet_code:decorator = member.find_decorator("dotnet_code")
        if(dotnet_code != None):
            namespace = dotnet_code.find_param("namespace")
            if(namespace != None ):
                code.usings.add(f"{namespace.value}")
            value = dotnet_code.find_param("code")
            if( value != None ):
                buffer.write(f"{utils.tab(indent)}{value.value}\n")
        buffer.write(self.deprecatedText(member, indent))
        type_text = self.typeText(member.type, code, fullName=True)
        if (member.find_decorator("optional") != None):   # @optional -> nullable; unmarked = required
            type_text = type_text + "?"
        buffer.write(f"{utils.tab(indent)}public {type_text} {member.name} {{ get; set; }}")
        if(member.type.kind == type.Kind.List or member.type.kind == type.Kind.Map ):
            buffer.write(f" = new();")
        buffer.write(f"\n")

        return buffer.getvalue()

    def typeText(self, type: type, code: dotnet_code, *, fullName: bool = False, isInFunctionParam: bool = False) -> str:
        match type.kind:
            case type.Kind.Primitive:
                return self.typeTextPrimitive(type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)
            case type.Kind.Ref:
                return self.typeTextRef(type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)
            case type.Kind.Reference:
                return self.typeTextReference(type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)
            case type.Kind.List:
                return self.typeTextList(type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)
            case type.Kind.Map:
                return self.typeTextMap(type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)

    def typeTextPrimitive(self, type: primitive_type, code: dotnet_code, *, fullName: bool = False, isInFunctionParam: bool = False) -> str:
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

    def typeTextReference(self, type: reference_type, code: dotnet_code, fullName: bool = False, isInFunctionParam: bool = False) -> str:
        referenced_element: base_element = Engine.get_referenced_element(type.parent, type.reference_name)
        if (referenced_element != None):
            code.usings.add(f"{referenced_element.getDomain().name}.{referenced_element.getContext().name}")

        if (fullName == True):
            return code.getDotnetFullName(referenced_element)
        else:
            return type.reference_name.getText()

    def typeTextRef(self, type: ref_type, code: dotnet_code, fullName: bool = False, isInFunctionParam: bool = False) -> str:
        # `ref X` targets an aggregate; the typed id wraps the aggregate's ROOT
        # entity (the class that actually carries the @id). e.g. `ref Identity`
        # (aggregate) -> EntityId<IAM.Identities.Identity.Account>.
        code.usings.add("PolyPersist.Net.Core")
        referenced = Engine.get_referenced_element(type.parent, type.reference_name)
        target = referenced
        if (isinstance(referenced, aggregate)):
            for internal_entity in referenced.internal_entities:
                if (internal_entity.isRoot == True):
                    target = internal_entity.entity
                    break
        if (target != None):
            inner = code.getDotnetFullName(target)
        else:
            inner = type.reference_name.getText()
        return f"EntityId<{inner}>"

    def typeTextList(self, type: list_type, code: dotnet_code, fullName: bool = False, isInFunctionParam: bool = False) -> str:
        if(isInFunctionParam == True ):
            return f"IList<{self.typeText(type.item_type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)}>"
        else:
            return f"List<{self.typeText(type.item_type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)}>"

    def typeTextMap(self, type: map_type, code, fullName: bool = False, isInFunctionParam: bool = False) -> str:
        return f"Dictionary<{self.typeText(type.key_type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)},{self.typeText(type.value_type, code, fullName=fullName, isInFunctionParam=isInFunctionParam)}>"

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

    def convertToUrlValue(self, name: str, _type: type, usings: set[str]) -> str:
        """
        The same value, escaped for the place it is going. Escaping is per VALUE, never per URL: an
        id that carries a slash must not be able to change the route it sits in, and the slashes of
        the route itself must survive.
        """
        value = self.convertToQueryValue(name, _type, usings)
        if (value == None):
            return None

        # convertToQueryValue hands back an interpolation hole - the expression is what goes inside
        return f"{{Uri.EscapeDataString({value[1:-1]})}}"

    def clientRouteText(self, http_operation: rest_operation, code: dotnet_code) -> str:
        """
        The route as a client builds it: the same segments the controller declares, but with the
        route parameters substituted and escaped instead of left as templates.
        """
        route = http_operation.route
        for param in http_operation.params.values():
            if (param.bindingSource == rest_param.BindingSource.FromRoute):
                route += "/" + self.convertToUrlValue(param.param.name, param.param.type, code.usings)

        return route

    def convertToQueryValue(self, name: str, _type: type, usings: set[str]) -> str:
        if (_type.kind == type.Kind.Primitive):
            primitive_type: primitive_type = _type
            match primitive_type.primtiveKind:
                case primitive_type.PrimtiveKind.I18NString | primitive_type.PrimtiveKind.Any | primitive_type.PrimtiveKind.Bytes | primitive_type.PrimtiveKind.Stream:
                    return f"{{{name}}}"
                case primitive_type.PrimtiveKind.Integer | primitive_type.PrimtiveKind.Number | primitive_type.PrimtiveKind.Float:
                    usings.add("System.Globalization")
                    return f"{{{name}.ToString(CultureInfo.InvariantCulture)}}"
                case primitive_type.PrimtiveKind.Date:
                    usings.add("System.Globalization")
                    return f"{{{name}.ToString(\"yyyy-MM-dd\", CultureInfo.InvariantCulture)}}"
                case primitive_type.PrimtiveKind.Time:
                    usings.add("System.Globalization")
                    return f"{{{name}.ToString(\"HH:mm:ss\", CultureInfo.InvariantCulture)}}"
                case primitive_type.PrimtiveKind.DateTime:
                    usings.add("System.Globalization")
                    return f"{{{name}.ToString(\"o\", CultureInfo.InvariantCulture)}}"
                case primitive_type.PrimtiveKind.String:
                    return f"{{{name}}}"
                case primitive_type.PrimtiveKind.Boolean:
                    return f"{{{name}.ToString().ToLowerInvariant()}}"
        elif (_type.kind == type.Kind.Reference):
            reference_type: reference_type = _type
            referenced_element: base_element = Engine.get_referenced_element(reference_type.parent, reference_type.reference_name)
            if (isinstance(referenced_element, enum) == True):
                return f"{{{name}.ToString()}}"

class dotnet_configuration:
    def __init__(self, configuration: Dict[str, str], output_dir: str):
        self.output_dir = output_dir

        self.__read_fileHeader(configuration)
        self.__read_defaultUsings(configuration)

    def __read_fileHeader(self, configuration: Dict[str, str]):
        self.fileHeader: str = """
// <auto-generated>
// This code was generated by d3i.interpreter
//
// Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
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

class dotnet_code:
    def __init__(self, output_path: str, subdirs: List[str], name: str, current_namespace: str):
        """
        Initializes a dotnet_code instance with the file path, file name, and content.
        """
        self.output_path = output_path
        self.fileName: str = name + ".cs"
        self.fullPath: str = os.path.join(output_path + "/".join(subdirs), self.fileName)
        self.current_namespace: str = current_namespace
        self.usings: set[str] = set()
        self.content: str = ""

    def getDotnetFullName(self, element: base_element ) -> str:
        dotnetNames: List[str] = []
        while True:
            if (element == None or isinstance( element, d3 )):
                break

            if (Engine.has_version_int_member(element)):
                if (isinstance(element, interface) ):
                    dotnetNames.insert(0, f"I{element.name}_v{element.version}")
                else:
                    dotnetNames.insert(0, f"{element.name}_v{element.version}")
            elif( isinstance( element, service ) or isinstance( element, acl )):
                    dotnetNames.insert(0, f"I{element.name}")
            elif( isinstance( element, workflow )):
                    # the generated class is <Name>Workflow, so anything nested in the workflow is
                    # reached through that name
                    dotnetNames.insert(0, f"{element.name}Workflow")
            elif( isinstance( element, aggregate_entity )):
                # skip 
                pass
            else:
                dotnetNames.insert(0, element.name)

            element = element.parent

        current_namespaces = self.current_namespace.split(".")

        if dotnetNames[:len(current_namespaces)] == current_namespaces:
            dotnetNames = dotnetNames[len(current_namespaces):]

        return ".".join(dotnetNames)


