from decimal import Decimal
from d3i.grammar.d3iGrammar import *
from d3i.grammar.d3iGrammarVisitor import *
from d3i.interpreter.Elements import *


class ElementVisitor(d3iGrammarVisitor):
    def __init__(self, fileName):
        self.fileName = fileName

    # Visit a parse tree produced by d3iGrammar#d3i.
    def visitD3i(self, ctx: d3iGrammar.D3iContext):
        result = d3i()
        counter = 0
        while True:
            directive = ctx.directive((counter))
            if (directive == None):
                break
            counter = counter + 1
            result.directives.append(self.visit(directive))

        counter = 0
        while True:
            domain = ctx.domain((counter))
            if (domain == None):
                break
            counter = counter + 1
            result.domains.append(self.visit(domain))

        return result

    # Visit a parse tree produced by d3iGrammar#directive.
    def visitDirective(self, ctx: d3iGrammar.DirectiveContext):
        result = directive(self.fileName, ctx.start)
        result.keyword = ctx.IDENTIFIER().getText()
        result.value = self.visit(ctx.qualifiedName())
        return result

    # Visit a parse tree produced by d3iGrammar#domain.
    def visitDomain(self, ctx: d3iGrammar.DomainContext):
        result = domain(self.fileName, ctx.start)
        ctx.start.line
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            domain_element: d3iGrammar.Domain_elementContext = ctx.domain_element(
                (counter))
            if (domain_element == None):
                break
            elif (domain_element.context() != None):
                result.contexts.append(self.visit(domain_element.context()))
            elif (domain_element.event()):
                result.domain_events.append(self.visit(domain_element.event()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#domain_element.
    def visitDomain_element(self, ctx: d3iGrammar.Domain_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#context.
    def visitContext(self, ctx: d3iGrammar.ContextContext):
        result = context(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            context_element: d3iGrammar.Context_elementContext = ctx.context_element(
                (counter))
            if (context_element == None):
                break
            elif (context_element.enum() != None):
                result.enums.append(self.visit(context_element.enum()))
            elif (context_element.value_object() != None):
                result.value_objects.append(
                    self.visit(context_element.value_object()))
            elif (context_element.entity() != None):
                result.entities.append(self.visit(context_element.entity()))
            elif (context_element.aggregate() != None):
                result.aggregates.append(
                    self.visit(context_element.aggregate()))
            elif (context_element.repository() != None):
                result.repositories.append(
                    self.visit(context_element.repository()))
            elif (context_element.acl()):
                result.acls.append(self.visit(context_element.acl()))
            elif (context_element.event()):
                result.context_events.append(
                    self.visit(context_element.event()))
            elif (context_element.service()):
                result.services.append(self.visit(context_element.service()))
            elif (context_element.interface()):
                result.interfaces.append(
                    self.visit(context_element.interface()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#context_element.
    def visitContext_element(self, ctx: d3iGrammar.Context_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#value_object.
    def visitValue_object(self, ctx: d3iGrammar.Value_objectContext):
        result = value_object(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            value_object_element: d3iGrammar.Value_object_elementContext = ctx.value_object_element(
                (counter))
            if (value_object_element == None):
                break
            elif (value_object_element.value_object_member() != None):
                result.members.append(self.visit(
                    value_object_element.value_object_member()))
            elif (value_object_element.enum()):
                result.internal_enums.append(
                    self.visit(value_object_element.enum()))
            elif (value_object_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(value_object_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#value_object_element.
    def visitValue_object_element(self, ctx: d3iGrammar.Value_object_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#value_object_member.
    def visitValue_object_member(self, ctx: d3iGrammar.Value_object_memberContext):
        result = value_object_member(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.type = self.visit(ctx.type_())
        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#event.
    def visitEvent(self, ctx: d3iGrammar.EventContext):
        result = event(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            event_element: d3iGrammar.Event_elementContext = ctx.event_element(
                (counter))
            if (event_element == None):
                break
            elif (event_element.event_member() != None):
                result.members.append(
                    self.visit(event_element.event_member()))
            elif (event_element.enum()):
                result.internal_enums.append(
                    self.visit(event_element.enum()))
            elif (event_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(event_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#event_element.
    def visitEvent_element(self, ctx: d3iGrammar.Event_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#event_member.
    def visitEvent_member(self, ctx: d3iGrammar.Event_memberContext):
        result = event_member(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.type = self.visit(ctx.type_())
        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#entity.
    def visitEntity(self, ctx: d3iGrammar.EntityContext):
        result = entity(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            entity_element: d3iGrammar.Entity_elementContext = ctx.entity_element(
                (counter))
            if (entity_element == None):
                break
            elif (entity_element.entity_member() != None):
                result.members.append(
                    self.visit(entity_element.entity_member()))
            elif (entity_element.enum()):
                result.internal_enums.append(
                    self.visit(entity_element.enum()))
            elif (entity_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(entity_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#entity_element.
    def visitEntity_element(self, ctx: d3iGrammar.Entity_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#entity_member.
    def visitEntity_member(self, ctx: d3iGrammar.Entity_memberContext):
        result = entity_member(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.type = self.visit(ctx.type_())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#aggregate.
    def visitAggregate(self, ctx: d3iGrammar.AggregateContext):
        result = aggregate(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            aggregate_element: d3iGrammar.Aggregate_elementContext = ctx.aggregate_element(
                (counter))
            if (aggregate_element == None):
                break
            elif (aggregate_element.aggregate_entity() != None):
                result.internal_entities.append(
                    self.visit(aggregate_element.aggregate_entity()))
            elif (aggregate_element.enum()):
                result.internal_enums.append(
                    self.visit(aggregate_element.enum()))
            elif (aggregate_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(aggregate_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#aggregate_element.
    def visitAggregate_element(self, ctx: d3iGrammar.Aggregate_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#aggregate_entity.
    def visitAggregate_entity(self, ctx: d3iGrammar.Aggregate_entityContext):
        result = aggregate_entity(self.fileName, ctx.start)
        result.entity = self.visit(ctx.entity())
        if (ctx.ROOT() != None):
            result.isRoot = True
        else:
            result.isRoot = False

        return result

    # Visit a parse tree produced by d3iGrammar#repository.
    def visitRepository(self, ctx: d3iGrammar.RepositoryContext):
        result = repository(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.element_name = self.visit(ctx.qualifiedName())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#service.
    def visitService(self, ctx: d3iGrammar.ServiceContext):
        result = service(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            service_element: d3iGrammar.Service_elementContext = ctx.service_element(
                (counter))
            if (service_element == None):
                break
            elif (service_element.operation() != None):
                result.operations.append(self.visit(
                    service_element.operation()))
            elif (service_element.enum()):
                result.internal_enums.append(
                    self.visit(service_element.enum()))
            elif (service_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(service_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#service_element.
    def visitService_element(self, ctx: d3iGrammar.Service_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#interface.
    def visitInterface(self, ctx: d3iGrammar.InterfaceContext):
        result = interface(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            interface_element: d3iGrammar.Interface_elementContext = ctx.interface_element(
                (counter))
            if (interface_element == None):
                break
            elif (interface_element.operation() != None):
                result.operations.append(self.visit(
                    interface_element.operation()))
            elif (interface_element.enum()):
                result.internal_enums.append(
                    self.visit(interface_element.enum()))
            elif (interface_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(interface_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#interface_element.
    def visitInterface_element(self, ctx: d3iGrammar.Interface_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#operation.
    def visitOperation(self, ctx: d3iGrammar.OperationContext):
        result = operation(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            operation_param = ctx.operation_param((counter))
            if (operation_param == None):
                break
            counter = counter + 1
            result.operation_params.append(self.visit(operation_param))

        counter = 0
        while True:
            operation_return = ctx.operation_return((counter))
            if (operation_return == None):
                break
            counter = counter + 1
            result.operation_returns.append(self.visit(operation_return))

        return result

    # Visit a parse tree produced by d3iGrammar#operation_param.
    def visitOperation_param(self, ctx: d3iGrammar.Operation_paramContext):
        result = operation_param(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.type = self.visit(ctx.type_())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

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
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#acl.
    def visitAcl(self, ctx: d3iGrammar.AclContext):
        result = acl(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            acl_element: d3iGrammar.Acl_elementContext = ctx.acl_element(
                (counter))
            if (acl_element == None):
                break
            elif (acl_element.method() != None):
                result.methods.append(self.visit(
                    acl_element.method()))
            elif (acl_element.enum()):
                result.internal_enums.append(
                    self.visit(acl_element.enum()))
            elif (acl_element.value_object()):
                result.internal_value_objects.append(
                    self.visit(acl_element.value_object()))
            counter = counter + 1

        return result

    # Visit a parse tree produced by d3iGrammar#acl_element.
    def visitAcl_element(self, ctx: d3iGrammar.Acl_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#method.
    def visitMethod(self, ctx: d3iGrammar.MethodContext):
        result = method(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        if (ctx.type_() != None):
            result.return_type = self.visit(ctx.type_())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            method_param = ctx.method_param((counter))
            if (method_param == None):
                break
            counter = counter + 1
            result.method_params.append(self.visit(method_param))

        return result

    # Visit a parse tree produced by d3iGrammar#method_param.
    def visitMethod_param(self, ctx: d3iGrammar.Method_paramContext):
        result = method_param(self.fileName, ctx.start)
        result.name = ctx.IDENTIFIER().getText()
        result.type = self.visit(ctx.type_())

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result

    # Visit a parse tree produced by d3iGrammar#type.
    def visitType(self, ctx: d3iGrammar.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by d3iGrammar#primitive_type.
    def visitPrimitive_type(self, ctx: d3iGrammar.Primitive_typeContext):
        result = primitive_type(self.fileName, ctx.start)
        result.Kind = type.Kind.Primitive

        if (ctx.INTEGER() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Integer
        elif (ctx.NUMBER() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Number
        elif (ctx.FLOAT() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Float
        elif (ctx.DATE() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Date
        elif (ctx.TIME() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Time
        elif (ctx.DATETIME() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.DateTime
        elif (ctx.STRING() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.String
        elif (ctx.BOOLEAN() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Boolean
        elif (ctx.BYTES() != None):
            result.PrimtiveType = primitive_type.PrimtiveType.Bytes

        return result

    # Visit a parse tree produced by d3iGrammar#reference_type.
    def visitReference_type(self, ctx: d3iGrammar.Reference_typeContext):
        result = reference_type(self.fileName, ctx.start)
        result.Kind = type.Kind.Reference
        result.reference_name = self.visit(ctx.qualifiedName())

        return result

    # Visit a parse tree produced by d3iGrammar#list_type.
    def visitList_type(self, ctx: d3iGrammar.List_typeContext):
        result = list_type(self.fileName, ctx.start)
        result.Kind = type.Kind.List
        result.item_type = self.visit(ctx.type_())

        return result

    # Visit a parse tree produced by d3iGrammar#map_type.
    def visitMap_type(self, ctx: d3iGrammar.Map_typeContext):
        result = map_type(self.fileName, ctx.start)
        result.Kind = type.Kind.Map
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
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            param = ctx.decorator_param(counter)
            if (param == None):
                break
            counter = counter + 1
            result.params.append(self.visit(param))

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
        result.name = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        counter = 0
        while True:
            enum_element = ctx.enum_element((counter))
            if (enum_element == None):
                break
            counter = counter + 1
            result.enum_elements.append(self.visit(enum_element))

        return result

    # Visit a parse tree produced by d3iGrammar#enum_element.
    def visitEnum_element(self, ctx: d3iGrammar.Enum_elementContext):
        result = enum_element(self.fileName, ctx.start)
        result.value = ctx.IDENTIFIER().getText()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if (decorator == None):
                break
            counter = counter + 1
            result.decorators.append(self.visit(decorator))

        return result
