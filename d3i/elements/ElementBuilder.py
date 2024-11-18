from decimal import Decimal
from d3i.grammar.d3iGrammar import *
from d3i.grammar.d3iGrammarVisitor import *
from d3i.elements.Elements import *


class ElementBuilder(d3iGrammarVisitor):
    def __init__(self):
        self.elementTree = d3()
        self.fileName: str = ""

    # Visit a parse tree produced by d3iGrammar#d3i.
    def visitD3i(self, ctx: d3iGrammar.D3iContext):

        counter = 0
        while True:
            domain = ctx.domain((counter))
            if (domain == None):
                break
            counter = counter + 1
            self.elementTree.domains.append(self.visit(domain))

        return self.elementTree

    # Visit a parse tree produced by d3iGrammar#directive.
    def visitDirective(self, ctx: d3iGrammar.DirectiveContext):
        result = directive(self.fileName, ctx.start)
        if (ctx.IDENTIFIER() != None):
            result.keyword = ctx.IDENTIFIER().getText()
        if(ctx.qualifiedName() != None):
            result.value = self.visit(ctx.qualifiedName())
            result.value.parent = result
            
        return result

    # Visit a parse tree produced by d3iGrammar#domain.
    def visitDomain(self, ctx: d3iGrammar.DomainContext):
        result = domain(self.fileName, ctx.start)
        ctx.start.line
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            directive = ctx.directive((counter))
            if (directive == None):
                break
            counter = counter + 1
            child = self.visit(directive)
            child.parent = result
            result.directives.append(child)

        counter = 0
        while True:
            domain_element: d3iGrammar.Domain_elementContext = ctx.domain_element(
                (counter))
            if (domain_element == None):
                break
            elif (domain_element.context() != None):
                child = self.visit(domain_element.context())
                child.parent = result
                result.contexts.append(child)
            elif (domain_element.event()):
                child = self.visit(domain_element.event())
                child.parent = result
                result.domain_events.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#domain_element.
    def visitDomain_element(self, ctx: d3iGrammar.Domain_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#context.
    def visitContext(self, ctx: d3iGrammar.ContextContext):
        result = context(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            context_element: d3iGrammar.Context_elementContext = ctx.context_element(
                (counter))
            if (context_element == None):
                break
            elif (context_element.enum() != None):
                child = self.visit(context_element.enum())
                child.parent = result
                result.enums.append(child)
            elif (context_element.value_object() != None):
                child = self.visit(context_element.value_object())
                child.parent = result
                result.value_objects.append(child)
            elif (context_element.entity() != None):
                child = self.visit(context_element.entity())
                child.parent = result
                result.entities.append(child)
            elif (context_element.aggregate() != None):
                child = self.visit(context_element.aggregate())
                child.paremt = result
                result.aggregates.append(child)
            elif (context_element.repository() != None):
                child = self.visit(context_element.repository())
                child.parent = result
                result.repositories.append(child)
            elif (context_element.acl()):
                child = self.visit(context_element.acl())
                child.parent = result
                result.acls.append(child)
            elif (context_element.event()):
                child = self.visit(context_element.event())
                child.parent = result
                result.context_events.append(child)
            elif (context_element.service()):
                child = self.visit(context_element.service())
                child.parent = result
                result.services.append(child)
            elif (context_element.interface()):
                child = self.visit(context_element.interface())
                child.parent = result
                result.interfaces.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#context_element.
    def visitContext_element(self, ctx: d3iGrammar.Context_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#value_object.
    def visitValue_object(self, ctx: d3iGrammar.Value_objectContext):
        result = value_object(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            value_object_element: d3iGrammar.Value_object_elementContext = ctx.value_object_element(
                (counter))
            if (value_object_element == None):
                break
            elif (value_object_element.value_object_member() != None):
                child = self.visit(value_object_element.value_object_member())
                child.parent = result
                result.members.append(child)
            elif (value_object_element.enum()):
                child = self.visit(value_object_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (value_object_element.value_object()):
                child = self.visit(value_object_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#value_object_element.
    def visitValue_object_element(self, ctx: d3iGrammar.Value_object_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#value_object_member.
    def visitValue_object_member(self, ctx: d3iGrammar.Value_object_memberContext):
        result = value_object_member(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if(ctx.type_() != None):
            result.type = self.visit(ctx.type_())
            result.type.parent = result
            
        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#event.
    def visitEvent(self, ctx: d3iGrammar.EventContext):
        result = event(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            event_element: d3iGrammar.Event_elementContext = ctx.event_element(
                (counter))
            if (event_element == None):
                break
            elif (event_element.event_member() != None):
                child = self.visit(event_element.event_member())
                child.parent = result
                result.members.append(child)
            elif (event_element.enum()):
                child = self.visit(event_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (event_element.value_object()):
                child = self.visit(event_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#event_element.
    def visitEvent_element(self, ctx: d3iGrammar.Event_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#event_member.
    def visitEvent_member(self, ctx: d3iGrammar.Event_memberContext):
        result = event_member(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if(ctx.type_() != None):
            result.type = self.visit(ctx.type_())
            result.type.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#entity.
    def visitEntity(self, ctx: d3iGrammar.EntityContext):
        result = entity(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            entity_element: d3iGrammar.Entity_elementContext = ctx.entity_element(
                (counter))
            if (entity_element == None):
                break
            elif (entity_element.entity_member() != None):
                child = self.visit(entity_element.entity_member())
                child.parent = result
                result.members.append(child)
            elif (entity_element.enum()):
                child = self.visit(entity_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (entity_element.value_object()):
                child = self.visit(entity_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#entity_element.
    def visitEntity_element(self, ctx: d3iGrammar.Entity_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#entity_member.
    def visitEntity_member(self, ctx: d3iGrammar.Entity_memberContext):
        result = entity_member(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if(ctx.type_() != None):
            result.type = self.visit(ctx.type_())
            result.type.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#aggregate.
    def visitAggregate(self, ctx: d3iGrammar.AggregateContext):
        result = aggregate(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            aggregate_element: d3iGrammar.Aggregate_elementContext = ctx.aggregate_element(
                (counter))
            if (aggregate_element == None):
                break
            elif (aggregate_element.aggregate_entity() != None):
                child = self.visit(aggregate_element.aggregate_entity())
                child.parent = result
                result.internal_entities.append(child)
            elif (aggregate_element.enum()):
                child = self.visit(aggregate_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (aggregate_element.value_object()):
                child = self.visit(aggregate_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#aggregate_element.
    def visitAggregate_element(self, ctx: d3iGrammar.Aggregate_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#aggregate_entity.
    def visitAggregate_entity(self, ctx: d3iGrammar.Aggregate_entityContext):
        result = aggregate_entity(self.fileName, ctx.start)
        if (ctx.entity() != None):
            result.entity = self.visit(ctx.entity())
            result.entity.parent = result

        if (ctx.ROOT() != None):
            result.isRoot = True
        else:
            result.isRoot = False

        return result

    # Visit a parse tree produced by d3iGrammar#repository.
    def visitRepository(self, ctx: d3iGrammar.RepositoryContext):
        result = repository(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if(ctx.qualifiedName() != None):
            result.element_name = self.visit(ctx.qualifiedName())
            result.element_name.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#service.
    def visitService(self, ctx: d3iGrammar.ServiceContext):
        result = service(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            service_element: d3iGrammar.Service_elementContext = ctx.service_element(
                (counter))
            if (service_element == None):
                break
            elif (service_element.operation() != None):
                child = self.visit(service_element.operation())
                child.parent = result
                result.operations.append(child)
            elif (service_element.enum()):
                child = self.visit(service_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (service_element.value_object()):
                child = self.visit(service_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#service_element.
    def visitService_element(self, ctx: d3iGrammar.Service_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#interface.
    def visitInterface(self, ctx: d3iGrammar.InterfaceContext):
        result = interface(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            interface_element: d3iGrammar.Interface_elementContext = ctx.interface_element(
                (counter))
            if (interface_element == None):
                break
            elif (interface_element.operation() != None):
                child = self.visit(interface_element.operation())
                child.parent = result
                result.operations.append(child)
            elif (interface_element.enum()):
                child = self.visit(interface_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (interface_element.value_object()):
                child = self.visit(interface_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#interface_element.
    def visitInterface_element(self, ctx: d3iGrammar.Interface_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#operation.
    def visitOperation(self, ctx: d3iGrammar.OperationContext):
        result = operation(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            operation_param = ctx.operation_param((counter))
            if (operation_param == None):
                break
            counter = counter + 1
            child = self.visit(operation_param)
            child.parent = result
            result.operation_params.append(child)

        counter = 0
        while True:
            operation_return = ctx.operation_return((counter))
            if (operation_return == None):
                break
            counter = counter + 1
            child = self.visit(operation_return)
            child.parent = result
            result.operation_returns.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#operation_param.
    def visitOperation_param(self, ctx: d3iGrammar.Operation_paramContext):
        result = operation_param(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if (ctx.type_() != None):
            result.type = self.visit(ctx.type_())
            result.type.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#operation_return.
    def visitOperation_return(self, ctx: d3iGrammar.Operation_returnContext):
        result = operation_return(self.fileName, ctx.start)
        result.type = self.visit(ctx.type_())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#acl.
    def visitAcl(self, ctx: d3iGrammar.AclContext):
        result = acl(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            acl_element: d3iGrammar.Acl_elementContext = ctx.acl_element((counter))
            if (acl_element == None):
                break
            elif (acl_element.method() != None):
                child = self.visit(acl_element.method())
                child.parent = result
                result.methods.append(child)
            elif (acl_element.enum()):
                child = self.visit(acl_element.enum())
                child.parent = result
                result.internal_enums.append(child)
            elif (acl_element.value_object()):
                child = self.visit(acl_element.value_object())
                child.parent = result
                result.internal_value_objects.append(child)
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#acl_element.
    def visitAcl_element(self, ctx: d3iGrammar.Acl_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#method.
    def visitMethod(self, ctx: d3iGrammar.MethodContext):
        result = method(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if (ctx.type_() != None):
            result.return_type = self.visit(ctx.type_())
            result.return_type.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            method_param = ctx.method_param((counter))
            if (method_param == None):
                break
            counter = counter + 1
            child = self.visit(method_param)
            child.parent = result
            result.method_params.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#method_param.
    def visitMethod_param(self, ctx: d3iGrammar.Method_paramContext):
        result = method_param(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()
        if (ctx.type_() != None):
            result.type = self.visit(ctx.type_())
            result.type.parent = result

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#type.
    def visitType(self, ctx: d3iGrammar.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#primitive_type.
    def visitPrimitive_type(self, ctx: d3iGrammar.Primitive_typeContext):
        result = primitive_type(self.fileName, ctx.start)
        result.kind = type.Kind.Primitive

        if (ctx.INTEGER() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Integer
        elif (ctx.NUMBER() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Number
        elif (ctx.FLOAT() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Float
        elif (ctx.DATE() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Date
        elif (ctx.TIME() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Time
        elif (ctx.DATETIME() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.DateTime
        elif (ctx.STRING() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.String
        elif (ctx.BOOLEAN() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Boolean
        elif (ctx.BYTES() != None):
            result.primtiveKind = primitive_type.PrimtiveKind.Bytes

        return result

    # Visit a parse tree produced by d3iGrammar#reference_type.
    def visitReference_type(self, ctx: d3iGrammar.Reference_typeContext):
        result = reference_type(self.fileName, ctx.start)
        result.kind = type.Kind.Reference
        result.reference_name = self.visit(ctx.qualifiedName())

        return result

    # Visit a parse tree produced by d3iGrammar#list_type.
    def visitList_type(self, ctx: d3iGrammar.List_typeContext):
        result = list_type(self.fileName, ctx.start)
        result.kind = type.Kind.List
        result.item_type = self.visit(ctx.type_())

        return result

    # Visit a parse tree produced by d3iGrammar#map_type.
    def visitMap_type(self, ctx: d3iGrammar.Map_typeContext):
        result = map_type(self.fileName, ctx.start)
        result.kind = type.Kind.Map
        result.key_type = self.visit(ctx.type_(0))
        result.value_type = self.visit(ctx.type_(1))

        return result

    # Visit a parse tree produced by d3iGrammar#qualifiedName.
    def visitQualifiedName(self, ctx: d3iGrammar.QualifiedNameContext):
        result = qualified_name(self.fileName, ctx.start)

        counter = 0
        while True:
            identifier = ctx.IDENTIFIER(counter)
            if (identifier == None):
                break
            counter = counter + 1
            result.names.append(identifier.getText())

        return result

    # Visit a parse tree produced by d3iGrammar#decorator.
    def visitDecorator(self, ctx: d3iGrammar.DecoratorContext):
        result = decorator(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            param = ctx.decorator_param(counter)
            if (param == None):
                break
            counter = counter + 1
            child = self.visit(param)
            child.parent = result
            result.params.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#decorator_param.
    def visitDecorator_param(self, ctx: d3iGrammar.Decorator_paramContext):
        result = decorator_param(self.fileName, ctx.start)
        if (ctx.qualifiedName() != None):
            result.kind = decorator_param.Kind.QualifiedName
            result.value = self.visit(ctx.qualifiedName())
        elif (ctx.INTEGER_CONSTANS() != None):
            result.kind = decorator_param.Kind.Integer
            result.value = int(ctx.INTEGER_CONSTANS().getText())
        elif (ctx.NUMBER_CONSTANS() != None):
            result.kind = decorator_param.Kind.Number
            result.value = Decimal(ctx.NUMBER_CONSTANS().getText())
        else:
            result.kind = decorator_param.Kind.String
            result.value = ctx.STRING_LITERAL().getText().strip('"')

        return result

    # Visit a parse tree produced by d3iGrammar#enum.
    def visitEnum(self, ctx: d3iGrammar.EnumContext):
        result = enum(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        counter = 0
        while True:
            enum_element = ctx.enum_element((counter))
            if (enum_element == None):
                break
            counter = counter + 1
            child = self.visit(enum_element)
            child.parent = result
            result.enum_elements.append(child)

        return result

    # Visit a parse tree produced by d3iGrammar#enum_element.
    def visitEnum_element(self, ctx: d3iGrammar.Enum_elementContext):
        result = enum_element(self.fileName, ctx.start)
        if(ctx.IDENTIFIER() != None):
            result.value = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            child = self.visit(decorator)
            child.parent = result
            result.decorators.append(child)

        return result
