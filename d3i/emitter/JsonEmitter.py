from typing import Any
import d3i.elements.ElementVisitor
from d3i.elements.Elements import *


class JsonEmitter(d3i.elements.ElementVisitor):
    def __init__(self, withLocation: bool = True):
        self.dict = {}
        self.withLocation = withLocation

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        self.dict = {
            "$type": "d3i.d3",
            "domains": [],
        }
        return self.dict

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        data = {
            "$type": "d3i.domain",
            "name": domain.name,
            "decorators": [],
            "directives": [],
            "contexts": [],
            "domain_events": []
        }
        parentData['domains'].append(data)
        return data

    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        data = {
            "$type": "d3i.directive",
            "decorators": [],
            "keyword": directive.keyword,
            "value": directive.value.names,
        }
        parentData['directives'].append(data)
        return data

    def visitContext(self, context: context, parentData: Any) -> Any:
        data = {
            "$type": "d3i.context",
            "name": context.name,
            "decorators": [],
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

    def visitEvent(self, event: event, parentElement: Any, parentData: Any) -> Any:

        if isinstance(parentElement, context):
            key = "context_events"
        elif isinstance(parentElement, domain):
            key = "domain_events"
        else:
            key = "events"

        data = {
            "$type": "d3i.event",
            "name": event.name,
            "members": event.name
        }
        parentData[key].append(data)
        return data

    def visitEventMember(self, eventMember: event_member, parentEvent: event, parentData: Any) -> Any:
        data = {
            "$type": "d3i.event_member",
            "name": eventMember.name,
            "type": {}
        }
        parentData["members"].append(data)
        return data

    def visitEnum(self, enum: enum, parentElement: Any, parentData: Any) -> Any:
        if isinstance(parentElement, context):
            key = "enums"
        else:
            key = "internal_enums"

        data = {
            "$type": "d3i.enum",
            "name": enum.name,
            "enum_elements": []
        }
        parentData[key].append(data)
        return data

    def visitEnumElement(self, enum_element: enum_element, parentEnum: enum, parentData: Any) -> Any:
        data = {
            "$type": "d3i.enum_element",
            "name": enum_element.value,
        }
        parentData["enum_elements"].append(data)
        return data

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        pass

    def visitValueObjectMember(self, domain: value_object_member, parentValueObject: value_object, parentData: Any) -> Any:
        pass

    def visitEnity(self, entity: entity, parentData: Any) -> Any:
        pass

    def visitEnityMember(self, entity: entity_member, parentEntity: entity, parentData: Any) -> Any:
        pass

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        pass

    def visitAggregateEntity(self, aggregate: aggregate_entity, parentAggregate: aggregate, parentData: Any) -> Any:
        pass

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        pass

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        pass

    def visitService(self, service: service, parentData: Any) -> Any:
        pass

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        pass

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        pass

    def visitOperationParam(self, operation_param: operation_param, parentOperation: operation, parentData: Any) -> Any:
        pass

    def visitOperationReturn(self, operation_return: operation_return, parentOperation: operation, parentData: Any) -> Any:
        pass

    def visitMethod(self, method: method, parentData: Any) -> Any:
        pass

    def visitMethodParam(self, method_param: method_param, parentMethod: method, parentData: Any) -> Any:
        pass

    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any) -> Any:
        pass

    def visitReferenceType(self, reference_type: reference_type, parentData: Any) -> Any:
        pass

    def visitListType(self, list_type: list_type, parentData: Any) -> Any:
        pass

    def visitMapType(self, map_type: map_type, parentData: Any) -> Any:
        pass

    def visitDecoratedElement(self, decorated_element: decorated_base_element, parentData: Any) -> Any:
        data = []
        parentData["decorators"] = data
        return data

    def visitDecorator(self, decorator: decorator, parentData: Any) -> Any:
        data = {
            "$type": "d3i.decorator",
            "name": decorator.name,
            "params": [],
        }
        parentData.append(data)
        return data

    def visitDecoratorParam(self, decorator_param: decorator_param, parentData: Any) -> Any:
        data = {
            "$type": "d3i.decorator_param",
            "kind": str(decorator_param.kind),
            "value": (
                decorator_param.value.getText() if decorator_param.kind == decorator_param.Kind.QualifiedName else
                str(decorator_param.value)
            ),
        }
        parentData['params'].append(data)
        return data

    def visitBaseElement(self, base_element: base_element, parentData: Any) -> Any:
        if (self.withLocation == True):
            data = {
                "fileName": base_element.fileName,
                "line": base_element.line,
                "column": base_element.column
            }
            parentData["location"] = data
            return data
        else:
            return None
