# Generated from ./d3i/grammar/d3iGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .d3iGrammar import d3iGrammar
else:
    from d3iGrammar import d3iGrammar

# This class defines a complete generic visitor for a parse tree produced by d3iGrammar.

class d3iGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by d3iGrammar#d3i.
    def visitD3i(self, ctx:d3iGrammar.D3iContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#domain.
    def visitDomain(self, ctx:d3iGrammar.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#directive.
    def visitDirective(self, ctx:d3iGrammar.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#domain_element.
    def visitDomain_element(self, ctx:d3iGrammar.Domain_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#context.
    def visitContext(self, ctx:d3iGrammar.ContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#context_element.
    def visitContext_element(self, ctx:d3iGrammar.Context_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#value_object.
    def visitValue_object(self, ctx:d3iGrammar.Value_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#value_object_element.
    def visitValue_object_element(self, ctx:d3iGrammar.Value_object_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#value_object_member.
    def visitValue_object_member(self, ctx:d3iGrammar.Value_object_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event.
    def visitEvent(self, ctx:d3iGrammar.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_element.
    def visitEvent_element(self, ctx:d3iGrammar.Event_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_member.
    def visitEvent_member(self, ctx:d3iGrammar.Event_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#entity.
    def visitEntity(self, ctx:d3iGrammar.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#entity_element.
    def visitEntity_element(self, ctx:d3iGrammar.Entity_elementContext):
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


    # Visit a parse tree produced by d3iGrammar#aggregate_entity.
    def visitAggregate_entity(self, ctx:d3iGrammar.Aggregate_entityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#view.
    def visitView(self, ctx:d3iGrammar.ViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#view_element.
    def visitView_element(self, ctx:d3iGrammar.View_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#view_member.
    def visitView_member(self, ctx:d3iGrammar.View_memberContext):
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


    # Visit a parse tree produced by d3iGrammar#type.
    def visitType(self, ctx:d3iGrammar.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#primitive_type.
    def visitPrimitive_type(self, ctx:d3iGrammar.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#reference_type.
    def visitReference_type(self, ctx:d3iGrammar.Reference_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#list_type.
    def visitList_type(self, ctx:d3iGrammar.List_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#map_type.
    def visitMap_type(self, ctx:d3iGrammar.Map_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#qualifiedName.
    def visitQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#decorator.
    def visitDecorator(self, ctx:d3iGrammar.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#decorator_param.
    def visitDecorator_param(self, ctx:d3iGrammar.Decorator_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#enum.
    def visitEnum(self, ctx:d3iGrammar.EnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#enum_element.
    def visitEnum_element(self, ctx:d3iGrammar.Enum_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#inherits.
    def visitInherits(self, ctx:d3iGrammar.InheritsContext):
        return self.visitChildren(ctx)



del d3iGrammar