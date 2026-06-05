from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from .Elements import *

class ElementVisitor(ABC):

    @abstractmethod
    def visitd3(self, d3: d3, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitImport(self, _import: import_, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitContext(self, context: context, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEvent(self, event: event, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEventHandler(self, eventhandler: eventhandler, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitValueObjectMember(self, value_object_member: value_object_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitComposite(self, composite: composite, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitCompositeMember(self, composite_member: composite_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDto(self, dto: dto, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDtoMember(self, dto_member: dto_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEntity(self, entity: entity, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitEntityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitView(self, view: view, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitViewMember(self, view_member: view_member, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitService(self, service: service, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitOperationParam(self, operation_param: operation_param, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitType(self, type: type, parentData: Any, memberName: str) -> Any:
        pass

    @abstractmethod
    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any, memberName: str) -> Any:
        pass

    @abstractmethod
    def visitReferenceType(self, reference_type: reference_type, parentData: Any, memberName: str) -> Any:
        pass

    @abstractmethod
    def visitListType(self, list_type: list_type, parentData: Any, memberName: str) -> Any:
        pass

    @abstractmethod
    def visitMapType(self, map_type: map_type, parentData: Any, memberName: str) -> Any:
        pass

    @abstractmethod
    def visitDecorator(self, decorator: decorator, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDecoratorParam(self, decorator_param: decorator_param, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitDocumentLine(self, document_line: str, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitInternalScopedBaseElement(self, internal_scoped_base_element: internal_scoped_base_element, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitFunctionalElement(self, functional_element: functional_element, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitHintedBaseElement(self, hinted_base_element: hinted_base_element, parentData: Any) -> Any:
        pass

    @abstractmethod
    def visitBaseElement(self, base_element: base_element, parentData: Any) -> Any:
        pass
