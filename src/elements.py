from typing import List
from enum import Enum


class base_element:
    def __init__(self, fileName, pos):
        self.decorators = List[decorator] = []
        self.fileName = fileName
        self.line = pos.line
        self.column = pos.column


class decorated_base_element(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.decorators = []


class d3i:
    def __init__(self):
        self.directives = []
        self.domain = None


class directive(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.keyword = None
        self.value = None


class qualified_name(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.names = []


class decorator(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.params = []


class decorator_param(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type = None
        self.value = None

    class Type(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 2
        String = 3


class domain(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.decorators = []
        self.name = None
        self.contexts = []
        self.domain_events = []


class context(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enums = []
        self.value_objects = []
        self.entities = []
        self.aggregates = []
        self.repositories = []
        self.acls = []
        self.domain_events = []
        self.services = []
        self.iterfaces = []


class enum(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.enum_elements = []


class enum_element(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.Value = None


class value_object(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members = []
        self.internal_enums = []
        self.internal_value_objects = []


class value_object_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.Type = None


class event(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_enums = []
        self.internal_value_objects = []


class event_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None


class entity(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.members = []
        self.internal_enums = []
        self.internal_value_objects = []

class entity_member(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

class aggregate(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_entities = []
        self.internal_enums = []
        self.internal_value_objects = []

class aggregate_entity(base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.isRoot = None
        self.entity = None

class repository(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.element_name = None

class service(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_enums = []
        self.internal_value_objects = []
        self.operations = []

class interface(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_enums = []
        self.internal_value_objects = []
        self.operations = []

class operation(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.operation_params = []
        self.operation_returns = []

class operation_param(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.type = None

class operation_return(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.type = None


class acl(decorated_base_element):
    def __init__(self, fileName, pos):
        super().__init__(fileName, pos)
        self.name = None
        self.internal_enums = []
        self.internal_value_objects = []
        self.methods = []
