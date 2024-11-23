from __future__ import annotations
from typing import List
from enum import Enum
from d3i.elements.ElementVisitor import *

class IScope:
    def getChildren(self) -> List[base_element]:
        return []

class base_element:
    def __init__(self, fileName, pos):
        self.fileName: str = fileName
        self.line: int = pos.line
        self.column: int = pos.column
        self.parent: base_element = None

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitBaseElement(self, parentData)
        return data

    def locationText(self):
        return f"'{self.fileName}({self.line},{self.column})'"


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


class internal_scoped_base_element(decorated_base_element,IScope):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.enums: List[enum] = []
        self.value_objects: List[value_object] = []

    def getChildren(self) -> List[base_element]:
        return self.enums + self.value_objects

class qualified_name(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.names: List[str] = []

    def getText(self):
        return '.'.join(self.names)


class decorator(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.params: List[decorator_param] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecorator(self, parentData)
        super().visit(visitor, data)
        for param in self.params:
            param.visit(visitor, data)
        return data


class decorator_param(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.kind = None
        self.value = None

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecoratorParam(self, parentData)
        super().visit(visitor, data)

    class Kind(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 3
        String = 4


class d3(IScope):
    def __init__(self):
        self.domains: List[domain] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitd3(self, parentData)
        for domain in self.domains:
            domain.visit(visitor, data)
        return data
    
    def getChildren(self) -> List[base_element]:
        return self.domains


class domain(decorated_base_element,IScope):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.directives: List[directive] = []
        self.contexts: List[context] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDomain(self, parentData)
        super().visit(visitor, data)
        for directive in self.directives:
            directive.visit(visitor, data)
        for context in self.contexts:
            context.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + self.contexts


class directive(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.keyword = None
        self.value: qualified_name = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDirective(self, parentData)
        super().visit(visitor, data)


class context(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.aggregates: List[aggregate] = []
        self.repositories: List[repository] = []
        self.acls: List[acl] = []
        self.services: List[service] = []
        self.interfaces: List[interface] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitContext(self, parentData)
        super().visit(visitor, data)
        for enum in self.enums:
            enum.visit(visitor, data)
        for value_object in self.value_objects:
            value_object.visit(visitor, data)
        for aggregate in self.aggregates:
            aggregate.visit(visitor, data)
        for repository in self.repositories:
            repository.visit(visitor, data)
        for acl in self.acls:
            acl.visit(visitor, data)
        for service in self.services:
            service.visit(visitor, data)
        for interface in self.interfaces:
            interface.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + self.aggregates + self.repositories + self.acls + self.services + self.interfaces


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.enum_elements: List[enum_element] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnum(self, parentData)
        super().visit(visitor, data)
        for enum_element in self.enum_elements:
            enum_element.visit(visitor, data)


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnumElement(self, parentData)
        super().visit(visitor, data)


class value_object(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.members: List[value_object_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObject(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObjectMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class event(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.members: List[event_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEvent(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEventMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class entity(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.members: List[entity_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnity(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)


class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnityMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class aggregate(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.internal_entities: List[aggregate_entity] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregate(self, parentData)
        super().visit(visitor, data)
        for aggregate_entity in self.internal_entities:
            aggregate_entity.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super.getChildren() + [ae.entity for ae in self.internal_entities]


class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity: entity = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregateEntity(self, parentData)
        self.entity.visit(visitor, data)
        super().visit(visitor, data)


class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.referenced_name: str = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitRepository(self, parentData)
        super().visit(visitor, data)


class service(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.operations: List[operation] = []
        self.events: List[event] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitService(self, parentData)
        super().visit(visitor, data)
        for operation in self.operations:
            operation.visit(visitor, data)
        for event in self.events:
            event.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + self.events

class interface(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.operations: List[operation] = []
        self.events: List[event] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitInterface(self, parentData)
        super().visit(visitor, data)
        for operation in self.operations:
            operation.visit(visitor, data)
        for event in self.events:
            event.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + self.events

class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.operation_params: List[operation_param] = []
        self.operation_returns: List[operation_return] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperation(self, parentData)
        super().visit(visitor, data)
        for operation_param in self.operation_params:
            operation_param.visit(visitor, data)
        for operation_return in self.operation_returns:
            operation_return.visit(visitor, data)


class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationParam(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationReturn(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class acl(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.operations: List[operation] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAcl(self, parentData)
        super().visit(visitor, data)
        for operation in self.operations:
            operation.visit(visitor, data)
        for internal_enum in self.enums:
            internal_enum.visit(visitor, data)
        for internal_value_object in self.value_objects:
            internal_value_object.visit(visitor, data)


class type(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
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
                if (self.item_type != None):
                    self.item_type.visit(visitor, data, "item_type")
            case type.Kind.Map:
                data = visitor.visitMapType(self, parentData, memberName)
                if (self.key_type != None):
                    self.key_type.visit(visitor, data, "key_type")
                if (self.value_type != None):
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
        self.isExternal = False
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
