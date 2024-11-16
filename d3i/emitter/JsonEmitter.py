from typing import Any
import d3i.elements.ElementVisitor
from d3i.elements.Elements import *


class JsonEmitter(d3i.elements.ElementVisitor):
    def __init__(self):
        self.dict = {}

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        self.dict['domains'] = []
        return self.dict

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        data = {
            "name": domain.name,
            "directives": [],
            "contexts": [],
            "events": []
        }
        parentData['domains'].append(data)
        return data

    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        data = {
            "keyword": directive.keyword,
            "value": directive.value,
        }
        parentData['directives'].append(data)
        return data

    def visitContext(self, context: context, parentData: Any) -> Any:
        data = {
            "name": context.name,
            "enums": [],
            "value_objects": [],
            "entities": [],
            "aggregates": [],
            "repositories": [],
            "acls": [],
            "context_events": [],
            "services": [],
            "interfaces": [],
        }
        parentData['contexts'].append(data)
        return data
