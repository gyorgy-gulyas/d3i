import json
import os
from typing import Any
import d3i.elements.ElementVisitor
from d3i.elements.Elements import *
from d3i.Engine import Session

def DoEmit( session:Session, output_dir:str):
    jsonEmmiter = JsonEmitter()
    data = session.main.visit(jsonEmmiter, None)
    json_result = json.dumps(data, indent=4)
    with open(os.path.join(output_dir, "main.json"), "w") as file:
        file.write(json_result)
    return json_result


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

    def visitEvent(self, event: event, parentData: Any) -> Any:
        data = {
            "$type": "d3i.event",
            "name": event.name,
            "members": []
        }
        parentData["events"].append(data)
        return data

    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.event_member",
            "name": eventMember.name,
            "type": {}
        }
        parentData["members"].append(data)
        return data

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        if isinstance(enum.parent, context):
            key = "enums"
        else:
            key = "enums"

        data = {
            "$type": "d3i.enum",
            "name": enum.name,
            "enum_elements": []
        }
        parentData[key].append(data)
        return data

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        data = {
            "$type": "d3i.enum_element",
            "name": enum_element.value,
        }
        parentData["enum_elements"].append(data)
        return data

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        if isinstance(value_object.parent, context):
            key = "value_objects"
        else:
            key = "value_objects"

        data = {
            "$type": "d3i.value_object",
            "name": value_object.name,
            "members": [],
            "enums": [],
            "value_objects": []
        }
        parentData[key].append(data)
        return data

    def visitValueObjectMember(self, value_object_member: value_object_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.value_object_member",
            "name": value_object_member.name,
        }
        parentData["members"].append(data)
        return data

    def visitEnity(self, entity: entity, parentData: Any) -> Any:
        data = {
            "$type": "d3i.entity",
            "name": entity.name,
            "members": [],
            "enums": [],
            "value_objects": []
        }

        if isinstance(entity.parent, context):
            parentData["entities"].append(data)
        elif isinstance(entity.parent, aggregate_entity):
            parentData["entity"] = data
        
        return data

    def visitEnityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.entity_member",
            "name": entity_member.name,
        }
        parentData["members"].append(data)
        return data

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        data = {
            "$type": "d3i.aggregate",
            "name": aggregate.name,
            "internal_entities": [],
            "enums": [],
            "value_objects": []
        }
        parentData["aggregates"].append(data)
        return data

    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        data = {
            "$type": "d3i.aggregate_entity",
            "isRoot": str(aggregate_entity.isRoot),
        }
        parentData["internal_entities"].append(data)
        return data

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        data = {
            "$type": "d3i.repository",
            "name": repository.name,
            "referenced_name": repository.referenced_name,
        }
        parentData["repositories"].append(data)
        return data

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        data = {
            "$type": "d3i.acl",
            "name": acl.name,
            "operations": [],
            "enums": [],
            "value_objects": []
        }
        parentData["acls"].append(data)
        return data

    def visitService(self, service: service, parentData: Any) -> Any:
        data = {
            "$type": "d3i.service",
            "name": service.name,
            "operations": [],
            "events": [],
            "enums": [],
            "value_objects": []
        }
        parentData["services"].append(data)
        return data

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        data = {
            "$type": "d3i.interface",
            "name": interface.name,
            "operations": [],
            "events": [],
            "enums": [],
            "value_objects": []
        }
        parentData["services"].append(data)
        return data

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        data = {
            "$type": "d3i.operation",
            "name": operation.name,
            "operation_params": [],
            "operation_returns": [],
        }
        parentData["operations"].append(data)
        return data

    def visitOperationParam(self, operation_param: operation_param, parentData: Any) -> Any:
        data = {
            "$type": "d3i.operation_param",
            "name": operation_param.name,
            "type": {},
        }
        parentData["operation_params"].append(data)
        return data

    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
        data = {
            "$type": "d3i.operation_return",
            "type": {},
        }
        parentData["operation_returns"].append(data)
        return data

    def visitType(self, type: type, parentData: Any, memberName: str) -> Any:
        data = {
            "kind": str(type.kind)
        }
        parentData[memberName] = data
        return data

    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any, memberName: str) -> Any:
        data = {
            "$type": "d3i.primitive_type",
            "kind": str(primtiveType.kind),
            "primtiveKind": str(primtiveType.primtiveKind)
        }
        parentData[memberName] = data
        return data

    def visitReferenceType(self, reference_type: reference_type, parentData: Any, memberName: str) -> Any:
        data = {
            "$type": "d3i.reference_type",
            "kind": str(reference_type.kind),
            "isExternal": reference_type.isExternal,
            "reference_name": str(reference_type.reference_name.getText())
        }
        parentData[memberName] = data
        return data

    def visitListType(self, list_type: list_type, parentData: Any, memberName: str) -> Any:
        data = {
            "$type": "d3i.list_type",
            "kind": str(list_type.kind),
            "item_type": {}
        }
        parentData[memberName] = data
        return data

    def visitMapType(self, map_type: map_type, parentData: Any, memberName: str) -> Any:
        data = {
            "$type": "d3i.list_type",
            "kind": str(map_type.kind),
            "key_type": {},
            "value_type": {}
        }
        parentData[memberName] = data
        return data

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

