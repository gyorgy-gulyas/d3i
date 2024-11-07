from parser.d3iGrammar import *
from parser.d3iGrammarVisitor import *
from elements import *

class ElementVisitor(d3iGrammarVisitor):
    # Visit a parse tree produced by d3iGrammar#d3i.
    def visitD3i(self, ctx:d3iGrammar.D3iContext):
        result = d3i()
        counter = 0
        while True:
            directive = ctx.directive((counter))
            if( directive == None ):
                break
            counter = counter + 1
            result.directives.append(self.visit( directive))

        domain = ctx.domain(0)
        if( domain != None ):
            result.domain = self.visit( domain )

        return result

    # Visit a parse tree produced by d3iGrammar#directive.
    def visitDirective(self, ctx:d3iGrammar.DirectiveContext):
        result = directive()
        result.keyword = ctx.IDENTIFIER()
        result.value = self.visit(ctx.qualifiedName())
        return result

    # Visit a parse tree produced by d3iGrammar#domain.
    def visitDomain(self, ctx:d3iGrammar.DomainContext):
        result = domain()
        result.name = ctx.IDENTIFIER()

        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if( decorator == None ):
                break
            counter = counter + 1
            result.decorators.append(self.visit( decorator))

        counter = 0
        while True:
            domain_element: d3iGrammar.Domain_elementContext = ctx.domain_element((counter))
            if( domain_element == None ):
                break
            elif( domain_element.context() != None ):
                result.contexts.append( self.visit( domain_element.context()))
            elif( domain_element.event()):
                result.domain_events.append( self.visit( domain_element.event()))

        return result

    # Visit a parse tree produced by d3iGrammar#domain_element.
    def visitDomain_element(self, ctx:d3iGrammar.Domain_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#context.
    def visitContext(self, ctx:d3iGrammar.ContextContext):
        result = context()
        result.name = ctx.IDENTIFIER()
        
        counter = 0
        while True:
            decorator = ctx.decorator((counter))
            if( decorator == None ):
                break
            counter = counter + 1
            result.decorators.append(self.visit( decorator))

        counter = 0
        while True:
            context_element: d3iGrammar.Context_elementContext = ctx.domain_element((counter))
            if( context_element == None ):
                break
            elif( context_element.enum() != None ):
                result.enums.append( self.visit( context_element.enum()))
            elif( context_element.value_object() != None ):
                result.value_objects.append( self.visit( context_element.value_object()))
            elif( context_element.entity() != None ):
                result.entities.append( self.visit( context_element.entity()))
            elif( context_element.aggregate() != None ):
                result.aggregates.append( self.visit( context_element.aggregate()))
            elif( context_element.repository() != None ):
                result.repositories.append( self.visit( context_element.repository()))
            elif( context_element.acl()):
                result.acls.append( self.visit( context_element.acl()))
            elif( context_element.event()):
                result.domain_events.append( self.visit( context_element.event()))
            elif( context_element.service()):
                result.services.append( self.visit( context_element.service()))
            elif( context_element.interface()):
                result.iterfaces.append( self.visit( context_element.interface()))

        return result


    # Visit a parse tree produced by d3iGrammar#context_element.
    def visitContext_element(self, ctx:d3iGrammar.Context_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#value_object.
    def visitValue_object(self, ctx:d3iGrammar.Value_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#value_object_member.
    def visitValue_object_member(self, ctx:d3iGrammar.Value_object_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event.
    def visitEvent(self, ctx:d3iGrammar.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_member.
    def visitEvent_member(self, ctx:d3iGrammar.Event_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#entity.
    def visitEntity(self, ctx:d3iGrammar.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#entity_member.
    def visitEntity_member(self, ctx:d3iGrammar.Entity_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#aggregate.
    def visitAggregate(self, ctx:d3iGrammar.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#aggregate_element.
    def visitAggregate_element(self, ctx:d3iGrammar.Aggregate_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#repository.
    def visitRepository(self, ctx:d3iGrammar.RepositoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#service.
    def visitService(self, ctx:d3iGrammar.ServiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#service_element.
    def visitService_element(self, ctx:d3iGrammar.Service_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#interface.
    def visitInterface(self, ctx:d3iGrammar.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#interface_element.
    def visitInterface_element(self, ctx:d3iGrammar.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#operation.
    def visitOperation(self, ctx:d3iGrammar.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#operation_param.
    def visitOperation_param(self, ctx:d3iGrammar.Operation_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#operation_return.
    def visitOperation_return(self, ctx:d3iGrammar.Operation_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#acl.
    def visitAcl(self, ctx:d3iGrammar.AclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#acl_element.
    def visitAcl_element(self, ctx:d3iGrammar.Acl_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#acl_function.
    def visitAcl_function(self, ctx:d3iGrammar.Acl_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#acl_function_param.
    def visitAcl_function_param(self, ctx:d3iGrammar.Acl_function_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#type.
    def visitType(self, ctx:d3iGrammar.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#primitive_type.
    def visitPrimitive_type(self, ctx:d3iGrammar.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#reference_type.
    def visitReference_type(self, ctx:d3iGrammar.Reference_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#container_type.
    def visitContainer_type(self, ctx:d3iGrammar.Container_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#qualifiedName.
    def visitQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        result = qualified_name()

        counter = 0
        while True:
            identifier = ctx.IDENTIFIER(counter)
            if( identifier == None ):
                break
            counter = counter + 1
            result.names.append(identifier)

        return result

    # Visit a parse tree produced by d3iGrammar#decorator.
    def visitDecorator(self, ctx:d3iGrammar.DecoratorContext):
        result = decorator()
        result.name = ctx.IDENTIFIER()

        counter = 0
        while True:
            param = ctx.decorator_param(counter)
            if( param == None ):
                break
            counter = counter + 1
            result.params.append(param)

        return result


    # Visit a parse tree produced by d3iGrammar#decorator_param.
    def visitDecorator_param(self, ctx:d3iGrammar.Decorator_paramContext):
        result = decorator_param()
        if( ctx.qualifiedName() != None ):
            result.type =  decorator_param.Type.QualifiedName
            result.value = self.visit(ctx.qualifiedName())
        elif( ctx.INTEGER_CONSTANS() != None ):
            result.type =  decorator_param.Type.Integer
            result.value = ctx.INTEGER_CONSTANS()
        elif( ctx.NUMBER_CONSTANS() != None ):
            result.type =  decorator_param.Type.Number
            result.value = ctx.NUMBER_CONSTANS()
        else:
            result.type =  decorator_param.Type.String
            result.value = ctx.STRING_LITERAL()
        return result


    # Visit a parse tree produced by d3iGrammar#enum.
    def visitEnum(self, ctx:d3iGrammar.EnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#enum_element.
    def visitEnum_element(self, ctx:d3iGrammar.Enum_elementContext):
        return self.visitChildren(ctx)








    

