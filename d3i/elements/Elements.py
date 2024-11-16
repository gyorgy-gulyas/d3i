from __future__ import annotations
from typing import List
from enum import Enum
from d3i.elements.ElementVisitor import *


class base_element:
    def __init__(self, fileName, pos):
        self.fileName = fileName
        self.line = pos.line
        self.column = pos.column


class decorated_base_element(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.decorators: List[decorator] = []


class scoped_base_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.internal_enums: List[enum] = []
        self.internal_value_objects: List[value_object] = []


class directive(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.keyword = None
        self.value = None


class qualified_name(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.names: List[str] = []

    def getText(self):
        return '.'.join(self.names)


class decorator(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.params: List[decorator_param] = []


class decorator_param(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.kind = None
        self.value = None

    class Kind(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 2
        String = 3


class d3:
    def __init__(self):
        self.domains: List[domain] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitd3(self, parentData)
        for domain in self.domains:
            domain.visit(self, visitor, data)
        return data


class domain(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.directives: List[directive] = []
        self.contexts: List[context] = []
        self.domain_events: List[event] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDomain(self, parentData)
        for context in self.contexts:
            context.visit(self, visitor, data)
        for event in self.domain_events:
            event.visit(self, visitor, data)


class context(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enums: List[enum] = []
        self.value_objects: List[value_object] = []
        self.entities: List[entity] = []
        self.aggregates: List[aggregate] = []
        self.repositories: List[repository] = []
        self.acls: List[acl] = []
        self.context_events: List[event] = []
        self.services: List[service] = []
        self.interfaces: List[service] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitContext(self, parentData)
        for enum in self.enums:
            enum.visit(self, visitor, data)
        for value_object in self.value_objects:
            value_object.visit(self, visitor, data)
        for entity in self.entities:
            entity.visit(self, visitor, data)
        for aggregate in self.aggregates:
            aggregate.visit(self, visitor, data)
        for repository in self.repositories:
            repository.visit(self, visitor, data)
        for acl in self.acls:
            acl.visit(self, visitor, data)
        for event in self.context_events:
            event.visit(self, visitor, data)
        for service in self.services:
            service.visit(self, visitor, data)
        for interface in self.interfaces:
            interface.visit(self, visitor, data)


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enum_elements: List[enum_element] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnum(self, parent, parentData)
        for enum_element in self.enum_elements:
            enum_element.visit(self, visitor, data)


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnumElement(self, parent, parentData)


class value_object(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[value_object_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObject(self, parent, parentData)
        for member in self.members:
            member.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObjectMember(self, parent, parentData)
        self.type.visit(self, visitor, data)


class event(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[event_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEvent(self, parent, parentData)
        for member in self.members:
            member.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEventMember(self, parent, parentData)
        self.type.visit(self, visitor, data)


class entity(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[entity_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnity(self, parent, parentData)
        for member in self.members:
            member.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnityMember(self, parent, parentData)
        self.type.visit(self, visitor, data)


class aggregate(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities: List[aggregate_entity] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregate(self, parent, parentData)
        for aggregate_entity in self.internal_entities:
            aggregate_entity.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity: entity = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregateEntity(self, parent, parentData)
        self.entity.visit(self, visitor, data)


class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name: qualified_name = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitRepository(self, parent, parentData)


class service(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitService(self, parent, parentData)
        for operation in self.operations:
            operation.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class interface(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitInterface(self, parent, parentData)
        for operation in self.operations:
            operation.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operation_params: List[operation_param] = []
        self.operation_returns: List[operation_return] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperation(self, parent, parentData)
        for operation_param in self.operation_params:
            operation_param.visit(self, visitor, data)
        for operation_return in self.operation_returns:
            operation_return.visit(self, visitor, data)


class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationParam(self, parent, parentData)
        self.type.visit(self, visitor, data)


class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationReturn(self, parent, parentData)
        self.type.visit(self, visitor, data)


class acl(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.methods: List[method] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAcl(self, parent, parentData)
        for method in self.methods:
            method.visit(self, visitor, data)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor, data)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor, data)


class method(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.method_params: List[method_param] = []
        self.return_type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitMethod(self, parent, parentData)
        for method_param in self.method_params:
            method_param.visit(self, visitor, data)
        self.return_type.visit(self, visitor, data)


class method_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitMethodParam(self, parent, parentData)
        self.type.visit(self, visitor, data)


class type(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.kind = None

    class Kind(Enum):
        Primitive = 1
        Reference = 2
        List = 2
        Map = 2

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        # has been overwritten in specialized type class
        pass


class primitive_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.PrimtiveType = None

    class PrimtiveType(Enum):
        Integer = 1
        Number = 2
        Float = 2
        Date = 3,
        Time = 4,
        DateTime = 5,
        String = 6,
        Boolean = 7,
        Bytes = 8,

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitPrimitiveType(self, parentData)


class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name: qualified_name = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitReferenceType(self, parentData)


class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitListType(self, parentData)
        self.item_type.visit(self, visitor, data)


class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type = None
        self.value_type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitMapType(self, parentData)
        self.key_type.visit(self, visitor, data)
        self.value_type.visit(self, visitor, data)
