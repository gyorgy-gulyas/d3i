from typing import List
from enum import Enum
from BaseVisitor import BaseVisitor


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

    def visit(self, session, visitor: BaseVisitor):
        visitor.visitd3(self, session)
        for domain in self.domains:
            domain.visit(self, session, visitor)


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
        visitor.visitDomain(self, session)
        for context in self.contexts:
            context.visit(self, session, visitor)
        for event in self.domain_events:
            event.visit(self, session, visitor)


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
        visitor.visitContext(self, session)
        for enum in self.enums:
            enum.visit(self, session, visitor)
        for value_object in self.value_objects:
            value_object.visit(self, session, visitor)
        for entity in self.entities:
            entity.visit(self, session, visitor)
        for aggregate in self.aggregates:
            aggregate.visit(self, session, visitor)
        for repository in self.repositories:
            repository.visit(self, session, visitor)
        for acl in self.acls:
            acl.visit(self, session, visitor)
        for event in self.context_events:
            event.visit(self, session, visitor)
        for service in self.services:
            service.visit(self, session, visitor)
        for interface in self.interfaces:
            interface.visit(self, session, visitor)


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enum_elements: List[enum_element] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnum(self, session, parent)
        for enum_element in self.enum_elements:
            enum_element.visit(self, session, visitor)


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnumElement(self, session, parent)


class value_object(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[value_object_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitValueObject(self, session, parent)
        for member in self.members:
            member.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitValueObjectMember(self, session, parent)
        self.type.visit(self, session, visitor)


class event(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[event_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEvent(self, session, parent)
        for member in self.members:
            member.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEventMember(self, session, parent)
        self.type.visit(self, session, visitor)


class entity(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members: List[entity_member] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnity(self, session, parent)
        for member in self.members:
            member.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitEnityMember(self, session, parent)
        self.type.visit(self, session, visitor)


class aggregate(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities: List[aggregate_entity] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAggregate(self, session, parent)
        for aggregate_entity in self.internal_entities:
            aggregate_entity.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity: entity = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAggregateEntity(self, session, parent)
        self.entity.visit(self, session, visitor)


class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name: qualified_name = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitRepository(self, session, parent)


class service(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitService(self, session, parent)
        for operation in self.operations:
            operation.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class interface(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations: List[operation] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitInterface(self, session, parent)
        for operation in self.operations:
            operation.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operation_params: List[operation_param] = []
        self.operation_returns: List[operation_return] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperation(self, session, parent)
        for operation_param in self.operation_params:
            operation_param.visit(self, session, visitor)
        for operation_return in self.operation_returns:
            operation_return.visit(self, session, visitor)


class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperationParam(self, session, parent)
        self.type.visit(self, session, visitor)


class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitOperationReturn(self, session, parent)
        self.type.visit(self, session, visitor)


class acl(scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.methods: List[method] = []

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitAcl(self, session, parent)
        for method in self.methods:
            method.visit(self, session, visitor)
        for internal_enum in self.internal_enums:
            internal_enum.visit(self, session, visitor)
        for internal_value_object in self.internal_value_objects:
            internal_value_object.visit(self, session, visitor)


class method(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.method_params: List[method_param] = []
        self.return_type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMethod(self, session, parent)
        for method_param in self.method_params:
            method_param.visit(self, session, visitor)
        self.return_type.visit(self, session, visitor)


class method_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type: type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMethodParam(self, session, parent)
        self.type.visit(self, session, visitor)


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
        #has been overwritten in specialized type class
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
        visitor.visitPrimitiveType(self, session)
        pass

class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name: qualified_name = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitReferenceType(self, session)


class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitListType(self, session)
        self.item_type.visit(self, session, visitor)

class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type = None
        self.value_type = None

    def visit(self, parent, session, visitor: BaseVisitor):
        visitor.visitMapType(self, session)
        self.key_type.visit(self, session, visitor)
        self.value_type.visit(self, session, visitor)
