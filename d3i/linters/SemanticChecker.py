import d3i.elements.ElementVisitor
from d3i.Engine import *
from d3i.elements.Elements import *


class SemanticChecker(d3i.elements.ElementVisitor):
    def __init__(self, session: Session):
        self.session: Session = session

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        pass

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        pass

    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        pass

    def visitContext(self, context: context, parentData: Any) -> Any:
        pass

    def visitEvent(self, event: event, parentData: Any) -> Any:
        if isinstance(event.parent, context):
            parent_context: context = event.parent
            for neighbour in parent_context.context_events:
                if (neighbour is event):
                    continue
                if (neighbour.name == event.name):
                    self.__error__(event, f"An event '{event.name}' with this name already exists in {neighbour.locationText()}.")
        elif isinstance(event.parent, domain):
            parent_domain: domain = event.parent
            for neighbour in parent_domain.domain_events:
                if (neighbour is event):
                    continue
                if (neighbour.name == event.name):
                    self.__error__(event, f"An event '{event.name}' with this name already exists in {neighbour.locationText()}.")

    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        parent_event: event = eventMember.parent
        for neighbour in parent_event.members:
            if (neighbour is eventMember):
                continue
            if (neighbour.name == eventMember.name):
                self.__error__(eventMember, f"An event member '{eventMember.name}' with this name already exists in {neighbour.locationText()}.")
        pass

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        if isinstance(enum.parent, context):
            parent_context: context = enum.parent
            for neighbour in parent_context.enums:
                if (neighbour is enum):
                    continue
                if (neighbour.name == enum.name):
                    self.__error__(enum, f"An enum '{enum.name}' with this name already exists in {neighbour.locationText()}.")
        elif isinstance(enum.parent, scoped_base_element):
            parent_scope: scoped_base_element = enum.parent
            for neighbour in parent_scope.internal_enums:
                if (neighbour is enum):
                    continue
                if (neighbour.name == enum.name):
                    self.__error__(enum, f"An enum '{enum.name}' with this name already exists in {neighbour.locationText()}.")

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        parent_enum: enum = enum_element.parent
        for neighbour in parent_enum.enum_elements:
            if (neighbour is enum_element):
                continue
            if (neighbour.value == enum_element.value):
                self.__error__(enum_element, f"An enum element '{enum_element.value}' with this value already exists in {neighbour.locationText()}.")
        pass

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        pass

    def visitValueObjectMember(self, value_object_member: value_object_member, parentData: Any) -> Any:
        pass

    def visitEnity(self, entity: entity, parentData: Any) -> Any:
        pass

    def visitEnityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        pass

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        pass

    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        pass

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        pass

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        pass

    def visitService(self, service: service, parentData: Any) -> Any:
        pass

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        pass

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        pass

    def visitOperationParam(self, operation_param: operation_param, parentData: Any) -> Any:
        pass

    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
        pass

    def visitMethod(self, method: method, parentData: Any) -> Any:
        pass

    def visitMethodParam(self, method_param: method_param, parentData: Any) -> Any:
        pass

    def visitType(self, type: type, parentData: Any, memberName: str) -> Any:
        pass

    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any, memberName: str) -> Any:
        pass

    def visitReferenceType(self, reference_type: reference_type, parentData: Any, memberName: str) -> Any:
        pass

    def visitListType(self, list_type: list_type, parentData: Any, memberName: str) -> Any:
        pass

    def visitMapType(self, map_type: map_type, parentData: Any, memberName: str) -> Any:
        pass

    def visitDecoratedElement(self, decorated_element: decorated_base_element, parentData: Any) -> Any:
        pass

    def visitDecorator(self, decorator: decorator, parentData: Any) -> Any:
        pass

    def visitDecoratorParam(self, decorator_param: decorator_param, parentData: Any) -> Any:
        pass

    def visitBaseElement(self, base_element: base_element, parentData: Any) -> Any:
        pass

    def __warning__(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Warning, element.fileName, element.line, element.column)

    def __error__(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Error, element.fileName, element.line, element.column)