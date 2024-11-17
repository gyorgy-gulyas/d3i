from __future__ import annotations
from typing import List
from enum import Enum
from d3i.elements.ElementVisitor import *


class base_element:
    def __init__(self, fileName, pos):
        self.fileName = fileName
        self.line = pos.line
        self.column = pos.column

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitBaseElement(self, parentData)
        return data


class decorated_base_element(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.decorators: List[decorator] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecoratedElement(self, parentData)
        super().visit(visitor, parentData)
        for decorator in self.decorators:
            decorator.visit(visitor, data)
        return data


class scoped_base_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.internal_enums: List[enum] = []
        self.internal_value_objects: List[value_object] = []


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

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecorator(self, parentData)
        super().visit(visitor, data)
        for param in self.params:
            param.visit(self, visitor, data)
        return data


class decorator_param(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.kind = None
        self.value = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecoratorParam(self, parentData)
        super().visit(visitor, data)

    class Kind(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 3
        String = 4


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
        super().visit(visitor, data)
        for directive in self.directives:
            directive.visit(self, visitor, data)
        for context in self.contexts:
            context.visit(self, visitor, data)
        for event in self.domain_events:
            event.visit(self, visitor, data)


class directive(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.keyword = None
        self.value: qualified_name = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDirective(self, parentData)
        super().visit(visitor, data)


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
        super().visit(visitor, data)
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
        data = visitor.visitEnum(self,  parent, parentData)
        super().visit(visitor, data)
        for enum_element in self.enum_elements:
            enum_element.visit(self, visitor, data)


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnumElement(self, parent, parentData)
        super().visit(visitor, data)


class value_object(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[value_object_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObject(self, parent, parentData)
        super().visit(visitor, data)
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
        super().visit(visitor, data)
        self.type.visit(visitor, data, "type")


class event(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[event_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEvent(self, parent, parentData)
        super().visit(visitor, data)
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
        super().visit(visitor, data)
        self.type.visit(visitor, data, "type")


class entity(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[entity_member] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnity(self, parent, parentData)
        super().visit(visitor, data)
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
        self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class aggregate(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities: List[aggregate_entity] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregate(self, parentData)
        super().visit(visitor, data)
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
        super().visit(visitor, data)


class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name: qualified_name = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitRepository(self, parent, parentData)
        super().visit(visitor, data)


class service(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitService(self, parent, parentData)
        super().visit(visitor, data)
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
        data = visitor.visitInterface(self, parentData)
        super().visit(visitor, data)
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
        super().visit(visitor, data)
        for operation_param in self.operation_params:
            operation_param.visit(self, visitor, data)
        for operation_return in self.operation_returns:
            operation_return.visit(self, visitor, data)


class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationParam(self, parent, parentData)
        super().visit(visitor, data)
        self.type.visit(visitor, data, "type")


class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationReturn(self, parent, parentData)
        super().visit(visitor, data)
        self.type.visit(visitor, data, "type")


class acl(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.methods: List[method] = []

    def visit(self, parent, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAcl(self, parent, parentData)
        super().visit(visitor, data)
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
        super().visit(visitor, data)
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
        super().visit(visitor, data)
        self.type.visit(visitor, data, "type")


class type(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.kind: type.Kind = None

    class Kind(Enum):
        Primitive = 1
        Reference = 2
        List = 3
        Map = 4

    def visit(self, visitor: ElementVisitor, parentData: Any, memberName: str):
        match self.kind:
            case type.Kind.Primitive:
                data = visitor.visitPrimitiveType(self, parentData, memberName)
            case type.Kind.Reference:
                data = visitor.visitReferenceType(self, parentData, memberName)
            case type.Kind.List:
                data = visitor.visitListType(self, parentData, memberName)
                self.item_type.visit(visitor, data, "item_type")
            case type.Kind.Map:
                data = visitor.visitMapType(self, parentData, memberName)
                self.key_type.visit(visitor, data, "key_type")
                self.value_type.visit(visitor, data, "value_type")

        super().visit(visitor, data)


class primitive_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.primtiveKind: primitive_type.PrimtiveKind = None

    class PrimtiveKind(Enum):
        Integer = 1
        Number = 2
        Float = 2
        Date = 3,
        Time = 4,
        DateTime = 5,
        String = 6,
        Boolean = 7,
        Bytes = 8,


class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name: qualified_name = None


class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type = None


class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type = None
        self.value_type = None
