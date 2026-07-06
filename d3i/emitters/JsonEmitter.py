import json
import os
from typing import Any, Dict
from d3i.elements.Elements import *
from d3i.Engine import *


def DoEmit(session: Session, output_dir: str, configuration: Dict[str, str]):
    jsonEmmiter = JsonEmitter()

    indent = 4
    if "json.indent" in configuration:
        indent = int(configuration["indent"])

    ensure_ascii = True
    if "json.ensure_ascii" in configuration:
        ensure_ascii = bool(configuration["ensure_ascii"])

    sort_keys = False
    if "json.sort_keys" in configuration:
        sort_keys = bool(configuration["sort_keys"])

    json_result = jsonEmmiter.Emit(session, indent, ensure_ascii, sort_keys)
    with open(os.path.join(output_dir, "main.json"), "w") as file:
        file.write(json_result)
    return json_result


class JsonEmitter(ElementVisitor):
    def __init__(self, withLocation: bool = True):
        self.dict = {}
        self.withLocation = withLocation

    def Emit(self, session: Session, indent=4, ensure_ascii=True, sort_keys=False) -> str:
        data = session.main.visit(self, None)
        json_result = json.dumps(data,
                                 indent=indent,
                                 ensure_ascii=ensure_ascii,
                                 sort_keys=sort_keys)
        return json_result

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        self.dict = {
            "$type": "d3i.d3",
            "imports": [],
            "domains": [],
        }
        return self.dict

    def visitImport(self, _import: import_, parentData: Any) -> Any:
        data = {
            "$type": "d3i.import_",
            "name": _import.name,
        }
        parentData['imports'].append(data)
        return data

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        data = {
            "$type": "d3i.domain",
            "name": domain.name,
            "directives": [],
            "contexts": [],
            "domain_events": []
        }
        parentData['domains'].append(data)
        return data

    def visitDirective(self, directive: directive, parentData: Any) -> Any:
        data = {
            "$type": "d3i.directive",
            "keyword": directive.keyword,
            "value": directive.value.names,
        }
        parentData['directives'].append(data)
        return data

    def visitContext(self, context: context, parentData: Any) -> Any:
        data = {
            "$type": "d3i.context",
            "name": context.name,
            "entities": [],
            "composites": [],
            "aggregates": [],
            "views": [],
            "repositories": [],
            "acls": [],
            "services": [],
            "interfaces": [],
        }
        parentData['contexts'].append(data)
        return data

    def visitEvent(self, event: event, parentData: Any) -> Any:
        data = {
            "$type": "d3i.event",
            "name": event.name,
            "version": str(event.version),
            "inherits": [],
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

    def visitEventHandler(self, eventhandler: eventhandler, parentData: Any) -> Any:
        data = {
            "$type": "d3i.eventhandler",
            "name": eventhandler.name,
            "handled_event": eventhandler.handledEvent.getText(),
        }
        parentData["eventhandlers"].append(data)
        return data
    

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        data = {
            "$type": "d3i.enum",
            "name": enum.name,
            "enum_elements": []
        }
        parentData["enums"].append(data)
        return data

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        data = {
            "$type": "d3i.enum_element",
            "value": enum_element.value,
        }
        parentData["enum_elements"].append(data)
        return data

    def visitValueObject(self, value_object: value_object, parentData: Any) -> Any:
        data = {
            "$type": "d3i.value_object",
            "name": value_object.name,
            "inherits": [],
            "members": [],
        }
        parentData["value_objects"].append(data)
        return data

    def visitValueObjectMember(self, value_object_member: value_object_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.value_object_member",
            "name": value_object_member.name,
            "type": {},
        }
        parentData["members"].append(data)
        return data

    def visitComposite(self, composite: composite, parentData: Any) -> Any:
        data = {
            "$type": "d3i.composite",
            "name": composite.name,
            "inherits": [],
            "members": [],
        }
        parentData["composites"].append(data)
        return data

    def visitCompositeMember(self, composite_member: composite_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.composite_member",
            "name": composite_member.name,
            "type": {},
        }
        parentData["members"].append(data)
        return data

    def visitDto(self, dto: dto, parentData: Any) -> Any:
        data = {
            "$type": "d3i.dto",
            "name": dto.name,
            "inherits": [],
            "members": [],
        }
        parentData["dtos"].append(data)
        return data

    def visitDtoMember(self, dto_member: dto_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.dto_member",
            "name": dto_member.name,
            "type": {},
        }
        parentData["members"].append(data)
        return data

    def visitEntity(self, entity: entity, parentData: Any) -> Any:
        data = {
            "$type": "d3i.entity",
            "name": entity.name,
            "inherits": [],
            "members": [],
        }

        if isinstance(entity.parent, context):
            parentData["entities"].append(data)
        elif isinstance(entity.parent, aggregate_entity):
            parentData["entity"] = data

        return data

    def visitEntityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.entity_member",
            "name": entity_member.name,
            "type": {},
        }
        parentData["members"].append(data)
        return data

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        data = {
            "$type": "d3i.aggregate",
            "name": aggregate.name,
            "internal_entities": []
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

    def visitView(self, view: view, parentData: Any) -> Any:
        data = {
            "$type": "d3i.view",
            "name": view.name,
            "inherits": [],
            "members": [],
        }

        parentData["views"].append(data)

        return data

    def visitViewMember(self, view_member: view_member, parentData: Any) -> Any:
        data = {
            "$type": "d3i.view_member",
            "name": view_member.name,
        }
        parentData["members"].append(data)
        return data

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        data = {
            "$type": "d3i.repository",
            "name": repository.name,
            "operations": [],
        }
        parentData["repositories"].append(data)
        return data

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        data = {
            "$type": "d3i.acl",
            "name": acl.name,
            "operations": [],
        }
        parentData["acls"].append(data)
        return data

    def visitService(self, service: service, parentData: Any) -> Any:
        data = {
            "$type": "d3i.service",
            "name": service.name,
            "operations": [],
            "events": [],
            "eventhandlers": [],
        }
        parentData["services"].append(data)
        return data

    def visitInterface(self, interface: interface, parentData: Any) -> Any:
        data = {
            "$type": "d3i.interface",
            "name": interface.name,
            "version": str(interface.version),
            "operations": [],
            "events": [],
        }
        parentData["services"].append(data)
        return data

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        data = {
            "$type": "d3i.operation",
            "name": operation.name,
            "operation_params": [],
            "operation_return": None,
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
        parentData["operation_return"] = data
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
            "$type": "d3i.map_type",
            "kind": str(map_type.kind),
            "key_type": {},
            "value_type": {}
        }
        parentData[memberName] = data
        return data

    def visitDecorator(self, decorator: decorator, parentData: Any) -> Any:
        data = {
            "$type": "d3i.decorator",
            "name": decorator.name,
            "params": [],
        }
        parentData["decorators"].append(data)
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

    def visitDocumentLine(self, document_line: str, parentData: Any) -> Any:
        parentData["document_lines"].append(document_line)
        return parentData

    def visitInternalScopedBaseElement(self, internal_scoped_base_element: internal_scoped_base_element, parentData: Any) -> Any:
        dict: Dict[str, Any] = parentData

        if(internal_scoped_base_element.withEnum== True):
            dict["enums"] = []
        if(internal_scoped_base_element.withValueObject== True):
            dict["value_objects"] = []
        if(internal_scoped_base_element.withDto== True):
            dict["dtos"] = []
        return dict

    def visitFunctionalElement(self, functional_element: functional_element, parentData: Any) -> Any:
        dict: Dict[str, Any] = parentData

        if(functional_element.withEvent== True):
            dict["events"] = []
        if(functional_element.withEventHandler== True):
            dict["eventhandlers"] = []

        return dict

    def visitHintedBaseElement(self, hinted_base_element: hinted_base_element, parentData: Any) -> Any:
        dict: Dict[str, Any] = parentData
        dict["document_lines"] = []
        dict["decorators"] = []
        return dict

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
