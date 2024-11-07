from typing import List
from enum import Enum

class base_element:
    def __init__(self):
        self.decorators = []
        self.fileName = None
        self.Line = None
        self.Column = None

class decorated_base_element(base_element):
    def __init__(self):
        self.decorators = []

class d3i:
    def __init__(self):
        self.directives = []
        self.domain = None

class directive(decorated_base_element):
    def __init__(self):
        self.keyword = None
        self.value = None

class qualified_name(base_element):
    def __init__(self):
        self.names = []

class decorator(base_element):
    def __init__(self):
        self.name = None
        self.params = []

class decorator_param(base_element):
    def __init__(self):
        self.type = None
        self.value = None

    class Type(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 2
        String = 3

class domain(decorated_base_element):
    def __init__(self):
        self.decorators = []
        self.name = None
        self.contexts = []
        self.domain_events = []

class context(decorated_base_element):
    def __init__(self):
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

class event(decorated_base_element):
    def __init__(self):
        self.name = None
