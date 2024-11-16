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
        self.decorators:List[decorator] = []


class d3:
    def __init__(self):
        self.domains:List[domain] = []

class directive(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.keyword = None
        self.value = None


class qualified_name(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.names: List[str] = []
    
    def getText( self ):
        return '.'.join(self.names)
   


class decorator(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.params:List[decorator_param] = []


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
        self.directives:List[directive] = []
        self.contexts:List[context] = []
        self.domain_events:List[event] = []


class context(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enums:List[enum] = []
        self.value_objects:List[value_object] = []
        self.entities:List[entity] = []
        self.aggregates:List[aggregate] = []
        self.repositories:List[repository] = []
        self.acls:List[acl] = []
        self.context_events:List[event] = []
        self.services:List[service] = []
        self.interfaces:List[service] = []


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enum_elements:List[enum_element] = []


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.value = None


class value_object(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members:List[value_object_member] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type:type = None


class event(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []
        self.members:List[event_member] = []


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type:type = None


class entity(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members:List[entity_member] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []

class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

class aggregate(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities:List[aggregate_entity] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []

class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity:entity = None

class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name:qualified_name = None

class service(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations:List[operation] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []

class interface(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operations:List[operation] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []

class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operation_params:List[operation_param] = []
        self.operation_returns:List[operation_return] = []

class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type:type = None


class acl(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.methods:List[method] = []
        self.internal_enums:List[enum] = []
        self.internal_value_objects:List[value_object] = []

class method(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.method_params:List[method_param] = []
        self.return_type:type = None

class method_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type:type = None

class type(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.Kind = None 
    
    class Kind(Enum):
        Primitive = 1
        Reference = 2
        List = 2
        Map = 2

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

class reference_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.reference_name:qualified_name = None 

class list_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.item_type = None 

class map_type(type):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.key_type = None
        self.value_type = None 
