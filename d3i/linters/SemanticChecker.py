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
        if isinstance(event.parent, interface):
            parent_interface: interface = event.parent
            for neighbour in parent_interface.events:
                if (neighbour is event):
                    continue
                if (neighbour.name == event.name):
                    self.__error__(event, f"An event '{event.name}' with same name already exists in {neighbour.locationText()}.")
        elif isinstance(event.parent, service):
            parent_service: service = event.parent
            for neighbour in parent_service.events:
                if (neighbour is event):
                    continue
                if (neighbour.name == event.name):
                    self.__error__(event, f"An event '{event.name}' with same name already exists in {neighbour.locationText()}.")

    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        parent_event: event = eventMember.parent
        for neighbour in parent_event.members:
            if (neighbour is eventMember):
                continue
            if (neighbour.name == eventMember.name):
                self.__error__(eventMember, f"An event member '{eventMember.name}' with same name already exists in {neighbour.locationText()}.")
        pass

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        if isinstance(enum.parent, context):
            parent_context: context = enum.parent
            for neighbour in parent_context.enums:
                if (neighbour is enum):
                    continue
                if (neighbour.name == enum.name):
                    self.__error__(enum, f"An enum '{enum.name}' with same name already exists in {neighbour.locationText()}.")
        elif isinstance(enum.parent, scoped_base_element):
            parent_scope: scoped_base_element = enum.parent
            for neighbour in parent_scope.enums:
                if (neighbour is enum):
                    continue
                if (neighbour.name == enum.name):
                    self.__error__(enum, f"An enum '{enum.name}' with same name already exists in {neighbour.locationText()}.")

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        parent_enum: enum = enum_element.parent
        for neighbour in parent_enum.enum_elements:
            if (neighbour is enum_element):
                continue
            if (neighbour.value == enum_element.value):
                self.__error__(enum_element, f"An enum element '{enum_element.value}' with this value already exists in {neighbour.locationText()}.")
        pass

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        if isinstance(value_object.parent, context):
            parent_context: context = value_object.parent
            for neighbour in parent_context.value_objects:
                if (neighbour is value_object):
                    continue
                if (neighbour.name == value_object.name):
                    self.__error__(value_object, f"A value object '{value_object.name}' with same name already exists in {neighbour.locationText()}.")
        elif isinstance(value_object.parent, scoped_base_element):
            parent_scope: scoped_base_element = value_object.parent
            for neighbour in parent_scope.value_objects:
                if (neighbour is value_object):
                    continue
                if (neighbour.name == value_object.name):
                    self.__error__(value_object, f"A value object '{value_object.name}' with same name already exists in {neighbour.locationText()}.")

    def visitValueObjectMember(self, value_object_member: value_object_member, parentData: Any) -> Any:
        parent_value_object: value_object = value_object_member.parent
        for neighbour in parent_value_object.members:
            if (neighbour is value_object_member):
                continue
            if (neighbour.name == value_object_member.name):
                self.__error__(value_object_member, f"An member '{value_object_member.name}' with same name already exists in {neighbour.locationText()}.")

    def visitEnity(self, entity: entity, parentData: Any) -> Any:
        parent_aggregate: aggregate = entity.parent.parent
        parent_context: context = parent_aggregate.parent

        for aggr in parent_context.aggregates:
            for aggr_entity in aggr.internal_entities:
                neighbour = aggr_entity.entity
                if (neighbour is entity):
                    continue
                if (neighbour.name == entity.name):
                    self.__error__(entity, f"An entity '{entity.name}' with same name already exists in {neighbour.locationText()}.")

    def visitEnityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        parent_entity: entity = entity_member.parent
        for neighbour in parent_entity.members:
            if (neighbour is entity_member):
                continue
            if (neighbour.name == entity_member.name):
                self.__error__(entity_member, f"A member '{entity_member.name}' with same name already exists in {neighbour.locationText()}.")

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        parent_context: context = aggregate.parent
        for neighbour in parent_context.aggregates:
            if (neighbour is aggregate):
                continue
            if (neighbour.name == aggregate.name):
                self.__error__(aggregate, f"An aggregate '{aggregate.name}' with same name is already exists in {neighbour.locationText()}.")

        countOfRoot: int = 0
        for aggregate_entity in aggregate.internal_entities:
            if (aggregate_entity.isRoot == True):
                countOfRoot = countOfRoot + 1

        if (countOfRoot == 0):
            self.__error__(aggregate, f"There is no root entity defined, in aggregate {aggregate.name}")
        elif (countOfRoot > 1):
            self.__error__(aggregate, f"More than one root entity defined, in aggregate {aggregate.name}")

    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        pass

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        isFound: bool = False
        parent_context: context = repository.parent
        for aggregate in parent_context.aggregates:
            if (aggregate.name == repository.referenced_name):
                isFound = True

        if (isFound == False):
            self.__error__(repository, f"Unknown refrenced name: {repository.referenced_name}, in repository {repository.name}")

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        parent_context: context = acl.parent
        for neighbour in parent_context.acls:
            if (neighbour is acl):
                continue
            if (neighbour.name == acl.name):
                self.__error__(acl, f"An acl '{acl.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitService(self, service: service, parentData: Any) -> Any:
        parent_context: context = service.parent
        for neighbour in parent_context.services:
            if (neighbour is service):
                continue
            if (neighbour.name == service.name):
                self.__error__(service, f"A service '{service.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        parent_context: context = interface.parent
        for neighbour in parent_context.interfaces:
            if (neighbour is interface):
                continue
            if (neighbour.name == interface.name):
                self.__error__(interface, f"An interface '{interface.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        for neighbour in operation.parent.operations:
            if (neighbour is operation):
                continue
            if (neighbour.name == operation.name):
                self.__error__(operation, f"An operation '{operation.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperationParam(self, param: operation_param, parentData: Any) -> Any:
        parent_operation: operation = param.parent
        for neighbour in parent_operation.operation_params:
            if (neighbour is param):
                continue
            if (neighbour.name == param.name):
                self.__error__(param, f"An operation parameter '{param.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
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
