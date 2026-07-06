from __future__ import annotations
from typing import List
from enum import Enum
from .ElementVisitor import *


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

    def getDomain(self) -> domain:
        if (isinstance(self, domain)):
            return self

        if (self.parent != None and isinstance( self.parent, base_element)):
            return self.parent.getDomain()

        return None

    def getContext(self) -> context:
        if (isinstance(self, context)):
            return self

        if (self.parent != None and isinstance( self.parent, base_element)):
            return self.parent.getContext()

        return None

    def getAggregate(self) -> aggregate:
        if (isinstance(self, aggregate)):
            return self

        if (self.parent != None and isinstance( self.parent, base_element)):
            return self.parent.getAggregate()

        return None

    def getInterface(self) -> interface:
        if (isinstance(self, interface)):
            return self

        if (self.parent != None and isinstance( self.parent, base_element)):
            return self.parent.getInterface()

        return None


class hinted_base_element(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.document_lines: List[str] = []
        self.decorators: List[decorator] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitHintedBaseElement(self, parentData)
        super().visit(visitor, parentData)
        for document_line in self.document_lines:
            visitor.visitDocumentLine(document_line, parentData)
        for decorator in self.decorators:
            decorator.visit(visitor, data)
        return data
    
    def find_decorator(self, name:str ) -> decorator:
        for decorator in self.decorators:
            if( decorator.name == name ):
                return decorator

        return None


class internal_scoped_base_element(hinted_base_element, IScope):
    def __init__(self, fileName, pos, withEnum: bool, withValueObject: bool, withDto: bool):
        super().__init__(fileName, pos)
        self.withEnum = withEnum
        if (withEnum == True):
            self.enums: List[enum] = []

        self.withValueObject = withValueObject
        if (withValueObject == True):
            self.value_objects: List[value_object] = []

        self.withDto = withDto
        if (withDto == True):
            self.dtos: List[dto] = []

    def getChildren(self) -> List[base_element]:
        children: List[base_element] = []

        if (self.withEnum == True):
            children = children + self.enums

        if (self.withValueObject == True):
            children = children + self.value_objects

        if (self.withDto == True):
            children = children + self.dtos

        return children

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitInternalScopedBaseElement(self, parentData)
        super().visit(visitor, data)

        if (self.withEnum == True):
            for internal_enum in self.enums:
                internal_enum.visit(visitor, data)

        if (self.withValueObject == True):
            for internal_value_object in self.value_objects:
                internal_value_object.visit(visitor, data)

        if (self.withDto == True):
            for internal_dto in self.dtos:
                internal_dto.visit(visitor, data)

        return data


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

    def find_param(self, name:str ) -> decorator_param:
        for param in self.params:
            if( param.name == name ):
                return param

        return None

    def get_param_value(self, name:str ) -> decorator:
        for param in self.params:
            if( param.name == name ):
                return param.value

        return None

class decorator_param(base_element):
    class Kind(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 3
        String = 4

    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.kind: decorator_param.Kind = None
        self.value = None

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitDecoratorParam(self, parentData)
        super().visit(visitor, data)


class d3(IScope):
    def __init__(self):
        self.imports: List[import_] = []
        self.domains: List[domain] = []

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitd3(self, parentData)
        for _import in self.imports:
            _import.visit(visitor, data)
        for domain in self.domains:
            domain.visit(visitor, data)
        return data

    def getChildren(self) -> List[base_element]:
        return self.domains


class import_(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = ""
        self.d3: d3 = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitImport(self, parentData)
        super().visit(visitor, data)


class domain(hinted_base_element, IScope):
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
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False)
        self.name: str = None
        self.composites: List[composite] = []
        self.aggregates: List[aggregate] = []
        self.views: List[view] = []
        self.repositories: List[repository] = []
        self.acls: List[acl] = []
        self.services: List[service] = []
        self.interfaces: List[interface] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitContext(self, parentData)
        super().visit(visitor, data)
        for composit in self.composites:
            composit.visit(visitor, data)
        for aggregate in self.aggregates:
            aggregate.visit(visitor, data)
        for view in self.views:
            view.visit(visitor, data)
        for repository in self.repositories:
            repository.visit(visitor, data)
        for acl in self.acls:
            acl.visit(visitor, data)
        for service in self.services:
            service.visit(visitor, data)
        for interface in self.interfaces:
            interface.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + self.composites + self.aggregates + self.views + self.repositories + self.acls + self.services + self.interfaces


class enum(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.enum_elements: List[enum_element] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnum(self, parentData)
        super().visit(visitor, data)
        for enum_element in self.enum_elements:
            enum_element.visit(visitor, data)


class enum_element(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEnumElement(self, parentData)
        super().visit(visitor, data)


class value_object(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False)
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.members: List[value_object_member] = []
        self.operations: List[operation] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObject(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)
        for operation in self.operations:
            operation.visit(visitor, data)


class value_object_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitValueObjectMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class dto(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=False, withDto=True)
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.members: List[dto_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDto(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)


class dto_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitDtoMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class composite(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False)
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.members: List[composite_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitComposite(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)


class composite_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitCompositeMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class event(internal_scoped_base_element):
    # Q2: three explicit event kinds (no prefix / 'domain' = Domain).
    class Kind(Enum):
        Domain = 1
        Integration = 2
        Audit = 3

    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=False, withDto=False)
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.version: int = None
        self.members: List[event_member] = []
        self.kind: event.Kind = event.Kind.Domain

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEvent(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)


class event_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEventMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class eventhandler(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.handledEvent: qualified_name = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEventHandler(self, parentData)
        super().visit(visitor, data)

class entity(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False)
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.members: List[entity_member] = []
        self.operations: List[operation] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEntity(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)
        for operation in self.operations:
            operation.visit(visitor, data)


class entity_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitEntityMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class aggregate(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False)
        self.name: str = None
        self.internal_entities: List[aggregate_entity] = []
        self.eventsourced: bool = False   # Q2: 'eventsourced aggregate' marker

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregate(self, parentData)
        super().visit(visitor, data)
        for aggregate_entity in self.internal_entities:
            aggregate_entity.visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren() + [ae.entity for ae in self.internal_entities]


class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity: entity = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAggregateEntity(self, parentData)
        self.entity.visit(visitor, data)
        super().visit(visitor, data)


class view(internal_scoped_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=False, withDto=False)
        self.view_projections: List[qualified_name] = []
        self.inherits: List[qualified_name] = []
        self.name: str = None
        self.members: List[view_member] = []

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitView(self, parentData)
        super().visit(visitor, data)
        for member in self.members:
            member.visit(visitor, data)


class view_member(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitViewMember(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)

class functional_element(internal_scoped_base_element):
    def __init__(self, fileName, pos, withEnum: bool, withValueObject: bool, withDto: bool, withEvent: bool, withEventHandler: bool):
        super().__init__(fileName, pos, withEnum, withValueObject, withDto)
        self.name: str = None
        self.operations: List[operation] = []

        self.withEvent = withEvent
        if (withEvent == True):
            self.events: List[event] = []

        self.withEventHandler = withEventHandler
        if (withEventHandler == True):
            self.eventhandlers: List[eventhandler] = []

    def getChildren(self) -> List[base_element]:
        children: List[base_element] = super().getChildren()

        if (self.withEvent == True):
            children = children + self.events

        if (self.withEventHandler == True):
            children = children + self.eventhandlers

        return children

    def visit(self, visitor: ElementVisitor, parentData: Any) -> Any:
        data = visitor.visitFunctionalElement(self, parentData)
        super().visit(visitor, data)

        for operation in self.operations:
            operation.visit(visitor, data)

        if (self.withEvent == True):
            for internal_event in self.events:
                internal_event.visit(visitor, data)

        if (self.withEventHandler == True):
            for internal_eventhandler in self.eventhandlers:
                internal_eventhandler.visit(visitor, data)

        return data

class repository(functional_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=False, withValueObject=False, withDto=False, withEvent=False, withEventHandler=False)
        self.name: str = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitRepository(self, parentData)
        super().visit(visitor, data)

class service(functional_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False, withEvent=True, withEventHandler=True)
        self.name: str = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitService(self, parentData)
        super().visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren()


class interface(functional_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=False, withDto=True, withEvent=True, withEventHandler=False)
        self.name: str = None
        self.version: int = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitInterface(self, parentData)
        super().visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren()


class operation(hinted_base_element):
    class Kind(Enum):
        Command = 1
        Query = 2

    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.operation_params: List[operation_param] = []
        self.operation_return: operation_return = None
        self.kind: operation.Kind = operation.Kind.Command
        self.emits: List[qualified_name] = []   # Q2: events a command records

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperation(self, parentData)
        super().visit(visitor, data)
        for operation_param in self.operation_params:
            operation_param.visit(visitor, data)
        if(self.operation_return != None ):
            self.operation_return.visit(visitor, data)


class operation_param(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name: str = None
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationParam(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class operation_return(hinted_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type: type = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitOperationReturn(self, parentData)
        if (self.type != None):
            self.type.visit(visitor, data, "type")
        super().visit(visitor, data)


class acl(functional_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos, withEnum=True, withValueObject=True, withDto=False, withEvent=False, withEventHandler=False)
        self.name: str = None

    def visit(self, visitor: ElementVisitor, parentData: Any):
        data = visitor.visitAcl(self, parentData)
        super().visit(visitor, data)

    def getChildren(self) -> List[base_element]:
        return super().getChildren()


class type(base_element):
    class Kind(Enum):
        Primitive = 1
        Reference = 2
        List = 3
        Map = 4

    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.kind: type.Kind = None

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
        Any = 0
        Integer = 1
        Number = 2
        Float = 3
        Date = 4,
        Time = 5,
        DateTime = 6,
        String = 7,
        I18NString = 8,
        Boolean = 9,
        Bytes = 10,
        Stream = 11,


class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name: qualified_name = None


class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type: type = None


class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type: type = None
        self.value_type: type = None
