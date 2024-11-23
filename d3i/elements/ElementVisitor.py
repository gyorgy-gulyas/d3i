from __future__ import annotations
from typing import Any
from d3i.elements.Elements import *

class ElementVisitor:

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        pass

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        pass

    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        pass

    def visitContext(self, context: context, parentData: Any) -> Any:
        pass

    def visitEvent(self, event: event, parentData: Any) -> Any:
        pass

    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        pass

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        pass

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
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
