from __future__ import annotations
from typing import List
from enum import Enum


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


class d3:
    def __init__(self):
        self.domains: List[domain] = []

    def visit(self, visitor: BaseVisitor):
        visitor.visitd3(self)
        for domain in self.domains:
            domain.visit(self, visitor)


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


class domain(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.directives: List[directive] = []
        self.contexts: List[context] = []
        self.domain_events: List[event] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitDomain(self)
        for context in self.contexts:
            context.visit(self, visitor)
        for event in self.domain_events:
            event.visit(self, visitor)


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

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitContext(self)
        for enum in self.enums:
            enum.visit(self, visitor)
        for value_object in self.value_objects:
            value_object.visit(self, visitor)
        for entity in self.entities:
            entity.visit(self, visitor)
        for aggregate in self.aggregates:
            aggregate.visit(self, visitor)
        for repository in self.repositories:
            repository.visit(self, visitor)
        for acl in self.acls:
            acl.visit(self, visitor)
        for event in self.context_events:
            event.visit(self, visitor)
        for service in self.services:
            service.visit(self, visitor)
        for interface in self.interfaces:
            interface.visit(self, visitor)


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enum_elements: List[enum_element] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnum(self, parent)
        for enum_element in self.enum_elements:
            enum_element.visit(self, visitor)


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnumElement(self, parent)


class value_object(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[value_object_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitValueObject(self, parent)
        for member in self.members:
            member.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitValueObjectMember(self, parent)
        self.type.visit(self, visitor)


class event(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[event_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEvent(self, parent)
        for member in self.members:
            member.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEventMember(self, parent)
        self.type.visit(self, visitor)


class entity(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[entity_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnity(self, parent)
        for member in self.members:
            member.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnityMember(self, parent)
        self.type.visit(self, visitor)


class aggregate(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities: List[aggregate_entity] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAggregate(self, parent)
        for aggregate_entity in self.internal_entities:
            aggregate_entity.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity: entity = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAggregateEntity(self, parent)
        self.entity.visit(self, visitor)


class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name: qualified_name = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitRepository(self, parent)


class service(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitService(self, parent)
        for operation in self.operations:
            operation.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class interface(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitInterface(self, parent)
        for operation in self.operations:
            operation.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operation_params: List[operation_param] = []
        self.operation_returns: List[operation_return] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperation(self, parent)
        for operation_param in self.operation_params:
            operation_param.visit(self, visitor)
        for operation_return in self.operation_returns:
            operation_return.visit(self, visitor)


class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperationParam(self, parent)
        self.type.visit(self, visitor)


class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperationReturn(self, parent)
        self.type.visit(self, visitor)


class acl(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.methods: List[method] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAcl(self, parent)
        for method in self.methods:
            method.visit(self, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, visitor)


class method(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.method_params: List[method_param] = []
        self.return_type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMethod(self, parent)
        for method_param in self.method_params:
            method_param.visit(self, visitor)
        self.return_type.visit(self, visitor)


class method_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMethodParam(self, parent)
        self.type.visit(self, visitor)


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

    def visit(self, parent, session, visitor: BaseVisitor):
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

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitPrimitiveType(self)
        pass


class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name: qualified_name = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitReferenceType(self)


class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitListType(self)
        self.item_type.visit(self, visitor)


class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type = None
        self.value_type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMapType(self)
        self.key_type.visit(self, visitor)
        self.value_type.visit(self, visitor)


class BaseVisitor:

    def visitd3(self, d3: domain):
        pass

    def visitDomain(self, domain: domain):
        pass

    def visitDirective(self, directive: directive):
        pass

    def visitContext(self, context: context):
        pass

    def visitEvent(self, event: event):
        pass

    def visitEventMember(self, eventMember: event_member, parentEvent: event):
        pass

    def visitEnum(self, domain: enum):
        pass

    def visitEnumElement(self, enum_element: enum_element, parentEnum: enum):
        pass

    def visitValueObject(self, value_object: value_object):
        pass

    def visitValueObjectMember(self, domain: value_object_member, parentValueObject: value_object):
        pass

    def visitEnity(self, entity: entity):
        pass

    def visitEnityMember(self, entity: entity_member, parentEntity: entity):
        pass

    def visitAggregate(self, aggregate: aggregate):
        pass

    def visitAggregateEntity(self, aggregate: aggregate_entity, parentAggregate: aggregate):
        pass

    def visitRepository(self, repository: repository):
        pass

    def visitAcl(self, acl: acl):
        pass

    def visitService(self, service: service):
        pass

    def visitInterface(self, interface: interface):
        pass

    def visitOperation(self, operation: operation):
        pass

    def visitOperationParam(self, operation_param: operation_param, parentOpeartion: operation):
        pass

    def visitOperationReturn(self, operation_return: operation_return, parentOpeartion: operation):
        pass

    def visitMethod(self, method: method):
        pass

    def visitMethodParam(self, method_param: method_param, parentMethod: method):
        pass

    def visitPrimitiveType(self, primtiveType: primitive_type):
        pass

    def visitReferenceType(self, reference_type: reference_type):
        pass

    def visitListType(self, list_type: list_type):
        pass

    def visitMapType(self, map_type: map_type):
        pass
