from typing import Any, Dict
from d3i.Engine import *
from d3i.elements.Elements import *
from d3i.elements.ElementVisitor import *


def DoLint(session: Session, output_dir: str, args: Dict[str, str]):
    linter = SemanticChecker(session)
    data = session.main.visit(linter, None)


class SemanticChecker(ElementVisitor):
    def __init__(self, session: Session):
        self.session: Session = session

    def visitd3(self, d3: d3, parentData: Any) -> Any:
        pass

    def visitImport(self, _import: import_, parentData: Any) -> Any:
        pass

    def visitDomain(self, domain: domain, parentData: Any) -> Any:
        pass

    def visitContext(self, context: context, parentData: Any) -> Any:
        pass

    def visitEvent(self, the_event: event, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_event.parent)

        for inherit in the_event.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_event.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, event) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an event.")

        for neighbour in scope.getChildren():
            if (neighbour is the_event):
                continue
            if (neighbour.name == the_event.name):
                if (isinstance(neighbour, event) == False):
                    self.__error(the_event, f"An event '{the_event.name}' with same name is already exists in {neighbour.locationText()}.")
                else:
                    other_event: event = neighbour
                    if (other_event.version == the_event.version):
                        self.__error(the_event, f"An event '{the_event.name}' with same name and version is already exists in {neighbour.locationText()}.")



    def visitEventMember(self, eventMember: event_member, parentData: Any) -> Any:
        parent_event: event = eventMember.parent
        for neighbour in parent_event.members:
            if (neighbour is eventMember):
                continue
            if (neighbour.name == eventMember.name):
                self.__error(eventMember, f"An event member '{eventMember.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEventHandler(self, the_eventhandler: eventhandler, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_eventhandler.parent)

        for neighbour in scope.getChildren():
            if (neighbour is the_eventhandler):
                continue
            if (neighbour.name == the_eventhandler.name):
                self.__error(the_eventhandler, f"An eventhandler '{the_eventhandler.name}' conflicts with same name with element in {neighbour.locationText()}.")

        referenced_event, message = Engine.get_referenced_element_with_message( the_eventhandler, the_eventhandler.handledEvent)
        if (referenced_event == None):
            self.__error(the_eventhandler.handledEvent, f"The handled event '{the_eventhandler.handledEvent.getText()}' is not found. {message}")
        elif (isinstance(referenced_event, event) == False):
            self.__error(the_eventhandler.handledEvent, f"The element '{the_eventhandler.handledEvent.getText()}' is not an event.")

    def visitEnum(self, enum: enum, parentData: Any) -> Any:
        scope = Engine.get_current_scope(enum.parent)
        for neighbour in scope.getChildren():
            if (neighbour is enum):
                continue
            if (neighbour.name == enum.name):
                self.__error(enum, f"An enum '{enum.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEnumElement(self, enum_element: enum_element, parentData: Any) -> Any:
        parent_enum: enum = enum_element.parent
        for neighbour in parent_enum.enum_elements:
            if (neighbour is enum_element):
                continue
            if (neighbour.value == enum_element.value):
                self.__error(enum_element, f"An enum element '{enum_element.value}' with this value already exists in {neighbour.locationText()}.")
        pass

    def visitValueObject(self, the_value_object: value_object, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_value_object.parent)

        for inherit in the_value_object.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_value_object.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, value_object) == False and isinstance(base_class, composite) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not a value object or composite.")

        for neighbour in scope.getChildren():
            if (neighbour is the_value_object):
                continue
            if (neighbour.name == the_value_object.name):
                self.__error(the_value_object, f"A value object '{the_value_object.name}' conflicts with same name with element in {neighbour.locationText()}.")

        # value objects are immutable, so they may only expose query operations.
        for op in the_value_object.operations:
            if (op.kind == operation.Kind.Command):
                self.__error(op, f"A value object operation '{op.name}' cannot be a command; value objects are immutable and may only have query operations.")

    def visitValueObjectMember(self, member: value_object_member, parentData: Any) -> Any:
        parent_value_object: value_object = member.parent
        for neighbour in parent_value_object.members:
            if (neighbour is member):
                continue
            if (neighbour.name == member.name):
                self.__error(member, f"An member '{member.name}' conflicts with same name with element in {neighbour.locationText()}.")
        self.__check_validate(member)

    def visitDto(self, the_dto: dto, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_dto.parent)

        for inherit in the_dto.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_dto.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, dto) == False and isinstance(base_class, composite) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not a dto or composite.")

        for neighbour in scope.getChildren():
            if (neighbour is the_dto):
                continue
            if (neighbour.name == the_dto.name):
                self.__error(the_dto, f"A dto '{the_dto.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitDtoMember(self, member: dto_member, parentData: Any) -> Any:
        parent_dto: dto = member.parent
        for neighbour in parent_dto.members:
            if (neighbour is member):
                continue
            if (neighbour.name == member.name):
                self.__error(member, f"An member '{member.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitComposite(self, the_composite: composite, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_composite.parent)

        for inherit in the_composite.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_composite.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, composite) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not a composite.")

        for neighbour in scope.getChildren():
            if (neighbour is the_composite):
                continue
            if (neighbour.name == the_composite.name):
                self.__error(the_composite, f"A composite '{the_composite.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitCompositeMember(self, member: composite_member, parentData: Any) -> Any:
        parent_composite: composite = member.parent
        for neighbour in parent_composite.members:
            if (neighbour is member):
                continue
            if (neighbour.name == member.name):
                self.__error(member, f"An member '{member.name}' conflicts with same name with element in {neighbour.locationText()}.")
        self.__check_validate(member)

    def visitEntity(self, the_entity: entity, parentData: Any) -> Any:
        parent_aggregate: aggregate = the_entity.parent.parent
        parent_context: context = parent_aggregate.parent

        for inherit in the_entity.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_entity.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, entity) == False and isinstance(base_class, composite) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an entity or composite.")

        for aggr in parent_context.aggregates:
            for aggr_entity in aggr.internal_entities:
                neighbour = aggr_entity.entity
                if (neighbour is the_entity):
                    continue
                if (neighbour.name == the_entity.name):
                    self.__error(the_entity, f"An entity '{the_entity.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitEntityMember(self, entity_member: entity_member, parentData: Any) -> Any:
        parent_entity: entity = entity_member.parent
        for neighbour in parent_entity.members:
            if (neighbour is entity_member):
                continue
            if (neighbour.name == entity_member.name):
                self.__error(entity_member, f"A member '{entity_member.name}' conflicts with same name with element in {neighbour.locationText()}.")
        self.__check_validate(entity_member)

    def visitAggregate(self, aggregate: aggregate, parentData: Any) -> Any:
        scope = Engine.get_current_scope(aggregate.parent)
        for neighbour in scope.getChildren():
            if (neighbour is aggregate):
                continue
            if (neighbour.name == aggregate.name):
                self.__error(aggregate, f"An aggregate '{aggregate.name}' with same name is already exists in {neighbour.locationText()}.")

        countOfRoot: int = 0
        for aggregate_entity in aggregate.internal_entities:
            if (aggregate_entity.isRoot == True):
                countOfRoot = countOfRoot + 1

        if (countOfRoot == 0):
            self.__error(aggregate, f"There is no root entity defined, in aggregate {aggregate.name}")
        elif (countOfRoot > 1):
            self.__error(aggregate, f"More than one root entity defined, in aggregate {aggregate.name}")

    def visitAggregateEntity(self, aggregate_entity: aggregate_entity, parentData: Any) -> Any:
        pass

    def visitView(self, the_view: view, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_view.parent)

        for projection in the_view.view_projections:
            base_class, message = Engine.get_referenced_element_with_message(the_view.parent, projection)
            if (base_class == None):
                self.__error(projection, f"The element '{projection.getText()}' referred in projection is not found. {message}")
            elif (isinstance(base_class, entity) == False):
                self.__error(projection, f"The element '{projection.getText()}' referred in inheritance is not an entity.")

        for inherit in the_view.inherits:
            base_class, message = Engine.get_referenced_element_with_message(the_view.parent, inherit)
            if (base_class == None):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not found. {message}")
            elif (isinstance(base_class, view) == False):
                self.__error(inherit, f"The element '{inherit.getText()}' referred in inheritance is not an view.")

        for neighbour in scope.getChildren():
            if (neighbour is the_view):
                continue
            if (neighbour.name == the_view.name):
                self.__error(the_view, f"A view '{the_view.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitViewMember(self, view_member: view_member, parentData: Any) -> Any:
        parent_view: view = view_member.parent
        for neighbour in parent_view.members:
            if (neighbour is view_member):
                continue
            if (neighbour.name == view_member.name):
                self.__error(view_member, f"A member '{view_member.name}' conflicts with same name with element in {neighbour.locationText()}.")

    def visitRepository(self, repository: repository, parentData: Any) -> Any:
        scope = Engine.get_current_scope(repository.parent)
        for neighbour in scope.getChildren():
            if (neighbour is repository):
                continue
            if (neighbour.name == repository.name):
                self.__error(repository, f"A repository '{repository.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitAcl(self, acl: acl, parentData: Any) -> Any:
        scope = Engine.get_current_scope(acl.parent)
        for neighbour in scope.getChildren():
            if (neighbour is acl):
                continue
            if (neighbour.name == acl.name):
                self.__error(acl, f"An acl '{acl.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitService(self, service: service, parentData: Any) -> Any:
        scope = Engine.get_current_scope(service.parent)
        for neighbour in scope.getChildren():
            if (neighbour is service):
                continue
            if (neighbour.name == service.name):
                self.__error(service, f"A service '{service.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitInterface(self, the_interface: interface, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_interface.parent)
        for neighbour in scope.getChildren():
            if (neighbour is the_interface):
                continue
            if (neighbour.name == the_interface.name):
                if (isinstance(neighbour, interface) == False):
                    self.__error(the_interface, f"An interface '{the_interface.name}' with same name is already exists in {neighbour.locationText()}.")
                else:
                    other_interface: interface = neighbour
                    if (other_interface.version == the_interface.version):
                        self.__error(the_interface, f"An interface '{the_interface.name}' with same name and version is already exists in {neighbour.locationText()}.")

    def visitWorkflow(self, the_workflow: workflow, parentData: Any) -> Any:
        scope = Engine.get_current_scope(the_workflow.parent)
        for neighbour in scope.getChildren():
            if (neighbour is the_workflow):
                continue
            if (neighbour.name == the_workflow.name):
                self.__error(the_workflow, f"A workflow '{the_workflow.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitStep(self, the_step: step, parentData: Any) -> Any:
        the_workflow: workflow = the_step.parent
        for neighbour in the_workflow.steps:
            if (neighbour is the_step):
                continue
            if (neighbour.name == the_step.name):
                self.__error(the_step, f"A step '{the_step.name}' with same name is already exists in {neighbour.locationText()}.")

        # `compensate` must reference an existing step in the same workflow.
        if (the_step.compensate != None):
            step_names = [s.name for s in the_workflow.steps]
            if (the_step.compensate not in step_names):
                self.__error(the_step, f"The compensating step '{the_step.compensate}' referenced by step '{the_step.name}' is not found in workflow '{the_workflow.name}'.")

    def visitOperation(self, operation: operation, parentData: Any) -> Any:
        for neighbour in operation.parent.operations:
            if (neighbour is operation):
                continue
            if (neighbour.name == operation.name):
                self.__error(operation, f"An operation '{operation.name}' with same name is already exists in {neighbour.locationText()}.")

        # only commands may emit events (a command records; the service publishes).
        if (operation.kind.name == "Query" and len(operation.emits) > 0):
            self.__error(operation, f"A query operation '{operation.name}' cannot emit events; only commands may declare 'emits'.")

    def visitOperationParam(self, param: operation_param, parentData: Any) -> Any:
        parent_operation: operation = param.parent
        for neighbour in parent_operation.operation_params:
            if (neighbour is param):
                continue
            if (neighbour.name == param.name):
                self.__error(param, f"An operation parameter '{param.name}' with same name is already exists in {neighbour.locationText()}.")

    def visitOperationReturn(self, operation_return: operation_return, parentData: Any) -> Any:
        pass

    def visitType(self, type: type, parentData: Any, memberName: str) -> Any:
        pass

    def visitPrimitiveType(self, primtiveType: primitive_type, parentData: Any, memberName: str) -> Any:
        # `any` and `stream` may not appear on a domain-model field.
        if (primtiveType.primtiveKind == primitive_type.PrimtiveKind.Any or primtiveType.primtiveKind == primitive_type.PrimtiveKind.Stream):
            owner = primtiveType.parent
            while (isinstance(owner, type)):   # skip list/map wrappers
                owner = owner.parent
            if (isinstance(owner, value_object_member) or isinstance(owner, entity_member) or isinstance(owner, composite_member)):
                if (primtiveType.primtiveKind == primitive_type.PrimtiveKind.Any):
                    self.__error(primtiveType, f"The 'any' type is not allowed on a domain model field; use a concrete type (an ACL at the boundary may use 'any').")
                else:
                    self.__error(primtiveType, f"The 'stream' type is not allowed on a field; it may only appear in an operation signature (command/query/step param or return).")

    def visitReferenceType(self, reference_type: reference_type, parentData: Any, memberName: str) -> Any:
        if (len(reference_type.reference_name.names) == 0):
            self.__error(reference_type, f"Empty reference name.")

        element, message = Engine.get_referenced_element_with_message(reference_type.parent, reference_type.reference_name)
        if (element == None):
            self.__error(reference_type, message)
        # another aggregate must be referenced by identity, not embedded.
        elif (isinstance(element, aggregate)):
            name = reference_type.reference_name.getText()
            self.__error(reference_type, f"Aggregate '{name}' must be referenced by identity: use 'ref {name}'.")
        # an interface is the wire surface: it may only expose dto/enum/primitive types
        # (plus `ref`, which is a string on the wire). Domain types must not leak onto it.
        elif (self.__is_on_interface_surface(reference_type) and isinstance(element, (dto, enum)) == False):
            name = reference_type.reference_name.getText()
            self.__error(reference_type, f"An interface may only expose dto, enum and primitive types on its surface; '{name}' is a {element.__class__.__name__}. Map it to a dto for the wire contract.")

    def visitRefType(self, ref_type: ref_type, parentData: Any, memberName: str) -> Any:
        if (len(ref_type.reference_name.names) == 0):
            self.__error(ref_type, f"Empty reference name.")
            return

        element, message = Engine.get_referenced_element_with_message(ref_type.parent, ref_type.reference_name)
        if (element == None):
            self.__error(ref_type, message)
        # `ref` may only target an aggregate; embed value objects/entities directly.
        elif (isinstance(element, aggregate) == False):
            name = ref_type.reference_name.getText()
            self.__error(ref_type, f"'ref' may only reference an aggregate; '{name}' is not an aggregate (embed value objects and entities directly).")

    def visitListType(self, list_type: list_type, parentData: Any, memberName: str) -> Any:
        if (list_type.item_type.kind == type.Kind.List or list_type.item_type.kind == type.Kind.Map):
            self.__error(list_type, f"Invalid item type definition: list can only contain primitive or reference types. Nested list or map types are not supported as list elements")

        pass

    def visitMapType(self, map_type: map_type, parentData: Any, memberName: str) -> Any:
        if (map_type.key_type.kind != type.Kind.Primitive or map_type.key_type.primtiveKind != primitive_type.PrimtiveKind.String):
            self.__error(map_type, f" Invalid map key type: A map type must have string keys. Other key types are not supported")

        if (map_type.value_type.kind == type.Kind.List or map_type.value_type.kind == type.Kind.Map):
            self.__error(map_type, f"Invalid value type definition: Value of map can only contain primitive or reference types. Nested list or map types are not supported as map value elements")
        pass

    def visitDecoratedElement(self, decorated_element: hinted_base_element, parentData: Any) -> Any:
        pass

    def visitDecorator(self, decorator: decorator, parentData: Any) -> Any:
        pass

    def visitDecoratorParam(self, decorator_param: decorator_param, parentData: Any) -> Any:
        pass

    def visitDocumentLine(self, document_line: str, parentData: Any) -> Any:
        pass

    def visitBaseElement(self, base_element: base_element, parentData: Any) -> Any:
        pass

    def __warning(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Warning, element.fileName, element.line, element.column)

    def __error(self, element: base_element, msg: str):
        self.session.ReportDiagnostic(msg, Diagnostic.Severity.Error, element.fileName, element.line, element.column)

    # known validate functions -> required argument count
    __VALIDATE_FUNCS = {"len": 1, "matches": 2}

    def __check_validate(self, member: base_element):
        # Type-checks the validate expression against the field types: a rule may only use
        # operations that make sense for the type (e.g. no `> 0` on a string), and the whole
        # expression must be boolean. Categories: number, string, bool, temporal (date/time),
        # collection (list/map), enum, id (ref), unknown.
        if (member.validate_ast == None):
            return
        category = self.__validate_type(member.validate_ast, member)
        if (category != "bool" and category != "error"):
            self.__error(member, f"The 'validate' expression on '{member.name}' must be a boolean condition, but it is a '{category}'.")

    def __validate_type(self, node, member: base_element) -> str:
        if (isinstance(node, validate_literal)):
            return "number" if (node.kind == "int" or node.kind == "number") else "string"

        if (isinstance(node, validate_ref)):
            if (node.name == "value"):
                return self.__type_category(member.type)
            sibling = None
            for candidate in member.parent.members:
                if (candidate.name == node.name):
                    sibling = candidate
                    break
            if (sibling == None):
                self.__error(member, f"'{node.name}' in the 'validate' on '{member.name}' is not 'value' nor a sibling field.")
                return "error"
            return self.__type_category(sibling.type)

        if (isinstance(node, validate_call)):
            return self.__validate_call_type(node, member)

        if (isinstance(node, validate_not)):
            inner = self.__validate_type(node.operand, member)
            if (inner != "bool" and inner != "error"):
                self.__error(member, f"'not' in the 'validate' on '{member.name}' needs a boolean operand, not a '{inner}'.")
            return "bool"

        if (isinstance(node, validate_binary)):
            left = self.__validate_type(node.left, member)
            right = self.__validate_type(node.right, member)
            if (node.op == "and" or node.op == "or"):
                for side in (left, right):
                    if (side != "bool" and side != "error"):
                        self.__error(member, f"'{node.op}' in the 'validate' on '{member.name}' needs boolean operands, not a '{side}'.")
                return "bool"
            if (node.op in ("<", "<=", ">", ">=")):
                for side in (left, right):
                    if (side != "error" and side != "number" and side != "temporal"):
                        self.__error(member, f"'{node.op}' in the 'validate' on '{member.name}' needs ordered values (number or date), not a '{side}'.")
                return "bool"
            # == or !=
            if (left != "error" and right != "error" and left != right):
                self.__error(member, f"'{node.op}' in the 'validate' on '{member.name}' compares incompatible types '{left}' and '{right}'.")
            return "bool"

        if (isinstance(node, validate_in_range) or isinstance(node, validate_between)):
            term = self.__validate_type(node.term, member)
            self.__validate_type(node.low, member)
            self.__validate_type(node.high, member)
            if (term != "error" and term != "number" and term != "temporal"):
                self.__error(member, f"the range check in the 'validate' on '{member.name}' needs an ordered value (number or date), not a '{term}'.")
            return "bool"

        if (isinstance(node, validate_in_set)):
            term = self.__validate_type(node.term, member)
            for item in node.items:
                item_category = self.__validate_type(item, member)
                if (term != "error" and item_category != "error" and term != item_category):
                    self.__error(member, f"the set check in the 'validate' on '{member.name}' mixes a '{term}' with a '{item_category}'.")
            return "bool"

        return "error"

    def __validate_call_type(self, node, member: base_element) -> str:
        if (node.func not in self.__VALIDATE_FUNCS):
            self.__error(member, f"Unknown function '{node.func}' in the 'validate' on '{member.name}' (known: len, matches).")
            return "error"
        if (len(node.args) != self.__VALIDATE_FUNCS[node.func]):
            self.__error(member, f"Function '{node.func}' in the 'validate' on '{member.name}' expects {self.__VALIDATE_FUNCS[node.func]} argument(s), got {len(node.args)}.")
            return "error"
        arg_categories = [self.__validate_type(arg, member) for arg in node.args]
        if (node.func == "len"):
            if (arg_categories[0] != "error" and arg_categories[0] != "string" and arg_categories[0] != "collection"):
                self.__error(member, f"'len' in the 'validate' on '{member.name}' needs a string or a list/map, not a '{arg_categories[0]}'.")
            return "number"
        # matches
        if (arg_categories[0] != "error" and arg_categories[0] != "string"):
            self.__error(member, f"'matches' in the 'validate' on '{member.name}' needs a string, not a '{arg_categories[0]}'.")
        if (isinstance(node.args[1], validate_literal) == False or node.args[1].kind != "string"):
            self.__error(member, f"the second argument of 'matches' in the 'validate' on '{member.name}' must be a string regex literal.")
        return "bool"

    def __type_category(self, the_type) -> str:
        if (the_type == None):
            return "unknown"
        if (the_type.kind == type.Kind.List or the_type.kind == type.Kind.Map):
            return "collection"
        if (the_type.kind == type.Kind.Ref):
            return "id"
        if (the_type.kind == type.Kind.Reference):
            element = Engine.get_referenced_element(the_type.parent, the_type.reference_name)
            if (isinstance(element, enum)):
                return "enum"
            return "unknown"
        if (the_type.kind == type.Kind.Primitive):
            kind = the_type.primtiveKind
            if (kind == primitive_type.PrimtiveKind.Integer or kind == primitive_type.PrimtiveKind.Number):
                return "number"
            if (kind == primitive_type.PrimtiveKind.Date or kind == primitive_type.PrimtiveKind.Time or kind == primitive_type.PrimtiveKind.DateTime):
                return "temporal"
            if (kind == primitive_type.PrimtiveKind.String or kind == primitive_type.PrimtiveKind.I18NString):
                return "string"
            if (kind == primitive_type.PrimtiveKind.Boolean):
                return "bool"
            return "unknown"
        return "unknown"

    def __is_on_interface_surface(self, element: base_element) -> bool:
        # True when the element sits inside an interface (its dto members or its
        # operation params/returns) — the versioned wire surface. Walking up stops at
        # the context/domain boundary so domain fields never match.
        node = element
        while (node != None):
            if (isinstance(node, interface)):
                return True
            if (isinstance(node, (context, domain, d3))):
                return False
            node = node.parent
        return False

    def visitInternalScopedBaseElement(self, internal_scoped_base_element: internal_scoped_base_element, parentData: Any) -> Any:
        pass

    def visitFunctionalElement(self, functional_element: functional_element, parentData: Any) -> Any:
        pass

    def visitHintedBaseElement(self, hinted_base_element: hinted_base_element, parentData: Any) -> Any:
        pass
