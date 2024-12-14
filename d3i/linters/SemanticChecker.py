from typing import Any, Dict
import d3i.elements.ElementVisitor
from d3i.Engine import *
from d3i.elements.Elements import *


def DoLint(session: Session, output_dir: str, args: Dict[str, str]):
    linter = SemanticChecker(session)
    data = session.main.visit(linter, None)

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
        scope = self.__get_current_scope(event.parent)

        for inherit in event.inherits:
            base_class, message = self.__get_referenced_element(event.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, d3i.event) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an event.")

        for neighbour in scope.getChildren():
            if (neighbour is event):
                continue
            if (neighbour.name == event.name):
                self.__error(event, f"An event '{event.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        parent_event: event = eventMember.parent
        for neighbour in parent_event.members:
            if (neighbour is eventMember):
                continue
            if (neighbour.name == eventMember.name):
                self.__error(eventMember, f"An event member '{eventMember.name}' conflicts with same name with element in {neighbour.locationText()}.")
        pass

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        scope = self.__get_current_scope(enum.parent)
        for neighbour in scope.getChildren():
            if (neighbour is enum):
                continue
            if (neighbour.name == enum.name):
                self.__error(enum, f"An enum '{enum.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        parent_enum: enum = enum_element.parent
        for neighbour in parent_enum.enum_elements:
            if (neighbour is enum_element):
                continue
            if (neighbour.value == enum_element.value):
                self.__error(enum_element, f"An enum element '{enum_element.value}' with this value already exists in {neighbour.locationText()}.")
        pass

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        scope = self.__get_current_scope(value_object.parent)

        for inherit in value_object.inherits:
            base_class, message = self.__get_referenced_element(value_object.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, d3i.value_object) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not a value object.")

        for neighbour in scope.getChildren():
            if (neighbour is value_object):
                continue
            if (neighbour.name == value_object.name):
                self.__error(value_object, f"A value object '{value_object.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitValueObjectMember(self, member: value_object_member, parentData: Any) -> Any:
        parent_value_object: value_object = member.parent
        for neighbour in parent_value_object.members:
            if (neighbour is member):
                continue
            if (neighbour.name == member.name):
                self.__error(member, f"An member '{member.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEntity(self, entity: entity, parentData: Any) -> Any:
        parent_aggregate: aggregate = entity.parent.parent
        parent_context: context = parent_aggregate.parent

        for inherit in entity.inherits:
            base_class, message = self.__get_referenced_element(entity.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, d3i.entity) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an entity.")

        for aggr in parent_context.aggregates:
            for aggr_entity in aggr.internal_entities:
                neighbour = aggr_entity.entity
                if (neighbour is entity):
                    continue
                if (neighbour.name == entity.name):
                    self.__error(entity, f"An entity '{entity.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEntityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        parent_entity: entity = entity_member.parent
        for neighbour in parent_entity.members:
            if (neighbour is entity_member):
                continue
            if (neighbour.name == entity_member.name):
                self.__error(entity_member, f"A member '{entity_member.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        scope = self.__get_current_scope(aggregate.parent)
        for neighbour in scope.getChildren():
            if (neighbour is aggregate):
                continue
            if (neighbour.name == aggregate.name):
                self.__error(aggregate, f"An aggregate '{aggregate.name}' with same name is already exists in {neighbour.locationText()}.")

        countOfRoot: int = 0
        for aggregate_entity in aggregate.internal_entities:
            if (aggregate_entity.isRoot == True):
                countOfRoot = countOfRoot + 1

        if (countOfRoot == 0):
            self.__error(aggregate, f"There is no root entity defined, in aggregate {aggregate.name}")
        elif (countOfRoot > 1):
            self.__error(aggregate, f"More than one root entity defined, in aggregate {aggregate.name}")

    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        pass

    def visitView(self, view: view, parentData: Any) -> Any:
        scope = self.__get_current_scope__(view.parent)

        for inherit in view.inherits:
            base_class, message = self.__get_referenced_element__(view.parent, inherit)
            if (base_class == None):
                self.__error__(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, d3i.view) == False):
                self.__error__(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an view.")

        for neighbour in scope.getChildren():
            if (neighbour is view):
                continue
            if (neighbour.name == view.name):
                self.__error__(view, f"A view '{view.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitViewMember(self, view_member: view_member, parentData: Any) -> Any:
        parent_view: view = view_member.parent
        for neighbour in parent_view.members:
            if (neighbour is view_member):
                continue
            if (neighbour.name == view_member.name):
                self.__error__(view_member, f"A member '{view_member.name}' conflicts with same name with element in {neighbour.locationText()}.")
    
    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        scope = self.__get_current_scope(repository.parent)
        for neighbour in scope.getChildren():
            if (neighbour is repository):
                continue
            if (neighbour.name == repository.name):
                self.__error(repository, f"A repository '{repository.name}' with same name is already exists in {neighbour.locationText()}.")

        isFound: bool = False
        parent_context: context = repository.parent
        for aggregate in parent_context.aggregates:
            if (aggregate.name == repository.referenced_name):
                isFound = True

        for view in parent_context.views:
            if (view.name == repository.referenced_name):
                isFound = True

        if (isFound == False):
            self.__error(repository, f"Unknown refrenced name: {repository.referenced_name}, in repository {repository.name}")

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        scope = self.__get_current_scope(acl.parent)
        for neighbour in scope.getChildren():
            if (neighbour is acl):
                continue
            if (neighbour.name == acl.name):
                self.__error(acl, f"An acl '{acl.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitService(self, service: service, parentData: Any) -> Any:
        scope = self.__get_current_scope(service.parent)
        for neighbour in scope.getChildren():
            if (neighbour is service):
                continue
            if (neighbour.name == service.name):
                self.__error(service, f"A service '{service.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        scope = self.__get_current_scope(interface.parent)
        for neighbour in scope.getChildren():
            if (neighbour is interface):
                continue
            if (neighbour.name == interface.name):
                self.__error(interface, f"An interface '{interface.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        for neighbour in operation.parent.operations:
            if (neighbour is operation):
                continue
            if (neighbour.name == operation.name):
                self.__error(operation, f"An operation '{operation.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperationParam(self, param: operation_param, parentData: Any) -> Any:
        parent_operation: operation = param.parent
        for neighbour in parent_operation.operation_params:
            if (neighbour is param):
                continue
            if (neighbour.name == param.name):
                self.__error(param, f"An operation parameter '{param.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
        pass

    def visitType(self, type: type, parentData: Any, memberName: str) -> Any:
        pass

    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any, memberName: str) -> Any:
        pass

    def visitReferenceType(self, reference_type: reference_type, parentData: Any, memberName: str) -> Any:
        if (len(reference_type.reference_name.names) == 0):
            self.__error(reference_type, f"Empty referenced name.")

        if (reference_type.isExternal == True):
            return

        element, message = self.__get_referenced_element(reference_type.parent, reference_type.reference_name)
        if (element == None):
            self.__error(reference_type, message)

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

    def __warning(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Warning, element.fileName, element.line, element.column)

    def __error(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Error, element.fileName, element.line, element.column)

    def __get_current_scope(self, element: base_element) -> IScope:
        current_scope = element
        while True:
            if isinstance(current_scope, IScope):
                break
            elif (current_scope == None):
                break
            current_scope = current_scope.parent

        return current_scope

    def __get_referenced_element(self, parent: base_element, name: qualified_name) -> IScope:

        scope = self.__get_current_scope(parent)
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
            return None, f"The first part of the referenced name '{name.names[0]}' cannot be resolved."

        # processing the rest of the name part if exist
        for name_part in name.names[1:]:
            if (isinstance(element, IScope) == False):
                return None, f"The referenced name '{name.names[0]}' cannot have an expected child: '{name_part}'."

            scope: IScope = element
            element = None
            for child in scope.getChildren():
                if (child.name == name_part):
                    element = child

            if (element == None):
                return None, f"The referenced name '{scope.name}' does not have an expected child: '{name_part}'."

        return element, "ok"
