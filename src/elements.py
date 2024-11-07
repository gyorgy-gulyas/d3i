from types import List
from enum import Enum

class d3i:
    def __init__(self):
        self.directives = List[directive] = []
        self.domain = None

class directive:
    def __init__(self):
        self.keyword = None
        self.value = None

class qualified_name:
    def __init__(self):
        self.names = []

class decorator:
    def __init__(self):
        self.name = None
        self.params = List[decorator_param] = []

class decorator_param:
    def __init__(self):
        self.type = None
        self.value = None

    class Type(Enum):
        QualifiedName = 1
        Integer = 2
        Number = 2
        String = 3

class domain:
    def __init__(self):
        self.decorators = List[decorator] = []
        self.name = None
        self.contexts = List[context] = []
        self.domain_events = List[event] = []

class context:
    def __init__(self):
        self.name = None

class event:
    def __init__(self):
        self.name = None
