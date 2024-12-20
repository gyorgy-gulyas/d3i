# Generated from ./d3i/grammar/d3iGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .d3iGrammar import d3iGrammar
else:
    from d3iGrammar import d3iGrammar

# This class defines a complete listener for a parse tree produced by d3iGrammar.
class d3iGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by d3iGrammar#d3i.
    def enterD3i(self, ctx:d3iGrammar.D3iContext):
        pass

    # Exit a parse tree produced by d3iGrammar#d3i.
    def exitD3i(self, ctx:d3iGrammar.D3iContext):
        pass


    # Enter a parse tree produced by d3iGrammar#domain.
    def enterDomain(self, ctx:d3iGrammar.DomainContext):
        pass

    # Exit a parse tree produced by d3iGrammar#domain.
    def exitDomain(self, ctx:d3iGrammar.DomainContext):
        pass


    # Enter a parse tree produced by d3iGrammar#directive.
    def enterDirective(self, ctx:d3iGrammar.DirectiveContext):
        pass

    # Exit a parse tree produced by d3iGrammar#directive.
    def exitDirective(self, ctx:d3iGrammar.DirectiveContext):
        pass


    # Enter a parse tree produced by d3iGrammar#domain_element.
    def enterDomain_element(self, ctx:d3iGrammar.Domain_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#domain_element.
    def exitDomain_element(self, ctx:d3iGrammar.Domain_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#context.
    def enterContext(self, ctx:d3iGrammar.ContextContext):
        pass

    # Exit a parse tree produced by d3iGrammar#context.
    def exitContext(self, ctx:d3iGrammar.ContextContext):
        pass


    # Enter a parse tree produced by d3iGrammar#context_element.
    def enterContext_element(self, ctx:d3iGrammar.Context_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#context_element.
    def exitContext_element(self, ctx:d3iGrammar.Context_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#value_object.
    def enterValue_object(self, ctx:d3iGrammar.Value_objectContext):
        pass

    # Exit a parse tree produced by d3iGrammar#value_object.
    def exitValue_object(self, ctx:d3iGrammar.Value_objectContext):
        pass


    # Enter a parse tree produced by d3iGrammar#value_object_element.
    def enterValue_object_element(self, ctx:d3iGrammar.Value_object_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#value_object_element.
    def exitValue_object_element(self, ctx:d3iGrammar.Value_object_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#value_object_member.
    def enterValue_object_member(self, ctx:d3iGrammar.Value_object_memberContext):
        pass

    # Exit a parse tree produced by d3iGrammar#value_object_member.
    def exitValue_object_member(self, ctx:d3iGrammar.Value_object_memberContext):
        pass


    # Enter a parse tree produced by d3iGrammar#event.
    def enterEvent(self, ctx:d3iGrammar.EventContext):
        pass

    # Exit a parse tree produced by d3iGrammar#event.
    def exitEvent(self, ctx:d3iGrammar.EventContext):
        pass


    # Enter a parse tree produced by d3iGrammar#event_element.
    def enterEvent_element(self, ctx:d3iGrammar.Event_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#event_element.
    def exitEvent_element(self, ctx:d3iGrammar.Event_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#event_member.
    def enterEvent_member(self, ctx:d3iGrammar.Event_memberContext):
        pass

    # Exit a parse tree produced by d3iGrammar#event_member.
    def exitEvent_member(self, ctx:d3iGrammar.Event_memberContext):
        pass


    # Enter a parse tree produced by d3iGrammar#entity.
    def enterEntity(self, ctx:d3iGrammar.EntityContext):
        pass

    # Exit a parse tree produced by d3iGrammar#entity.
    def exitEntity(self, ctx:d3iGrammar.EntityContext):
        pass


    # Enter a parse tree produced by d3iGrammar#entity_element.
    def enterEntity_element(self, ctx:d3iGrammar.Entity_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#entity_element.
    def exitEntity_element(self, ctx:d3iGrammar.Entity_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#entity_member.
    def enterEntity_member(self, ctx:d3iGrammar.Entity_memberContext):
        pass

    # Exit a parse tree produced by d3iGrammar#entity_member.
    def exitEntity_member(self, ctx:d3iGrammar.Entity_memberContext):
        pass


    # Enter a parse tree produced by d3iGrammar#aggregate.
    def enterAggregate(self, ctx:d3iGrammar.AggregateContext):
        pass

    # Exit a parse tree produced by d3iGrammar#aggregate.
    def exitAggregate(self, ctx:d3iGrammar.AggregateContext):
        pass


    # Enter a parse tree produced by d3iGrammar#aggregate_element.
    def enterAggregate_element(self, ctx:d3iGrammar.Aggregate_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#aggregate_element.
    def exitAggregate_element(self, ctx:d3iGrammar.Aggregate_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#aggregate_entity.
    def enterAggregate_entity(self, ctx:d3iGrammar.Aggregate_entityContext):
        pass

    # Exit a parse tree produced by d3iGrammar#aggregate_entity.
    def exitAggregate_entity(self, ctx:d3iGrammar.Aggregate_entityContext):
        pass


    # Enter a parse tree produced by d3iGrammar#view.
    def enterView(self, ctx:d3iGrammar.ViewContext):
        pass

    # Exit a parse tree produced by d3iGrammar#view.
    def exitView(self, ctx:d3iGrammar.ViewContext):
        pass


    # Enter a parse tree produced by d3iGrammar#view_element.
    def enterView_element(self, ctx:d3iGrammar.View_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#view_element.
    def exitView_element(self, ctx:d3iGrammar.View_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#view_member.
    def enterView_member(self, ctx:d3iGrammar.View_memberContext):
        pass

    # Exit a parse tree produced by d3iGrammar#view_member.
    def exitView_member(self, ctx:d3iGrammar.View_memberContext):
        pass


    # Enter a parse tree produced by d3iGrammar#repository.
    def enterRepository(self, ctx:d3iGrammar.RepositoryContext):
        pass

    # Exit a parse tree produced by d3iGrammar#repository.
    def exitRepository(self, ctx:d3iGrammar.RepositoryContext):
        pass


    # Enter a parse tree produced by d3iGrammar#service.
    def enterService(self, ctx:d3iGrammar.ServiceContext):
        pass

    # Exit a parse tree produced by d3iGrammar#service.
    def exitService(self, ctx:d3iGrammar.ServiceContext):
        pass


    # Enter a parse tree produced by d3iGrammar#service_element.
    def enterService_element(self, ctx:d3iGrammar.Service_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#service_element.
    def exitService_element(self, ctx:d3iGrammar.Service_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#interface.
    def enterInterface(self, ctx:d3iGrammar.InterfaceContext):
        pass

    # Exit a parse tree produced by d3iGrammar#interface.
    def exitInterface(self, ctx:d3iGrammar.InterfaceContext):
        pass


    # Enter a parse tree produced by d3iGrammar#interface_element.
    def enterInterface_element(self, ctx:d3iGrammar.Interface_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#interface_element.
    def exitInterface_element(self, ctx:d3iGrammar.Interface_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#operation.
    def enterOperation(self, ctx:d3iGrammar.OperationContext):
        pass

    # Exit a parse tree produced by d3iGrammar#operation.
    def exitOperation(self, ctx:d3iGrammar.OperationContext):
        pass


    # Enter a parse tree produced by d3iGrammar#operation_param.
    def enterOperation_param(self, ctx:d3iGrammar.Operation_paramContext):
        pass

    # Exit a parse tree produced by d3iGrammar#operation_param.
    def exitOperation_param(self, ctx:d3iGrammar.Operation_paramContext):
        pass


    # Enter a parse tree produced by d3iGrammar#operation_return.
    def enterOperation_return(self, ctx:d3iGrammar.Operation_returnContext):
        pass

    # Exit a parse tree produced by d3iGrammar#operation_return.
    def exitOperation_return(self, ctx:d3iGrammar.Operation_returnContext):
        pass


    # Enter a parse tree produced by d3iGrammar#acl.
    def enterAcl(self, ctx:d3iGrammar.AclContext):
        pass

    # Exit a parse tree produced by d3iGrammar#acl.
    def exitAcl(self, ctx:d3iGrammar.AclContext):
        pass


    # Enter a parse tree produced by d3iGrammar#acl_element.
    def enterAcl_element(self, ctx:d3iGrammar.Acl_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#acl_element.
    def exitAcl_element(self, ctx:d3iGrammar.Acl_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#type.
    def enterType(self, ctx:d3iGrammar.TypeContext):
        pass

    # Exit a parse tree produced by d3iGrammar#type.
    def exitType(self, ctx:d3iGrammar.TypeContext):
        pass


    # Enter a parse tree produced by d3iGrammar#primitive_type.
    def enterPrimitive_type(self, ctx:d3iGrammar.Primitive_typeContext):
        pass

    # Exit a parse tree produced by d3iGrammar#primitive_type.
    def exitPrimitive_type(self, ctx:d3iGrammar.Primitive_typeContext):
        pass


    # Enter a parse tree produced by d3iGrammar#reference_type.
    def enterReference_type(self, ctx:d3iGrammar.Reference_typeContext):
        pass

    # Exit a parse tree produced by d3iGrammar#reference_type.
    def exitReference_type(self, ctx:d3iGrammar.Reference_typeContext):
        pass


    # Enter a parse tree produced by d3iGrammar#list_type.
    def enterList_type(self, ctx:d3iGrammar.List_typeContext):
        pass

    # Exit a parse tree produced by d3iGrammar#list_type.
    def exitList_type(self, ctx:d3iGrammar.List_typeContext):
        pass


    # Enter a parse tree produced by d3iGrammar#map_type.
    def enterMap_type(self, ctx:d3iGrammar.Map_typeContext):
        pass

    # Exit a parse tree produced by d3iGrammar#map_type.
    def exitMap_type(self, ctx:d3iGrammar.Map_typeContext):
        pass


    # Enter a parse tree produced by d3iGrammar#qualifiedName.
    def enterQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        pass

    # Exit a parse tree produced by d3iGrammar#qualifiedName.
    def exitQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        pass


    # Enter a parse tree produced by d3iGrammar#decorator.
    def enterDecorator(self, ctx:d3iGrammar.DecoratorContext):
        pass

    # Exit a parse tree produced by d3iGrammar#decorator.
    def exitDecorator(self, ctx:d3iGrammar.DecoratorContext):
        pass


    # Enter a parse tree produced by d3iGrammar#decorator_param.
    def enterDecorator_param(self, ctx:d3iGrammar.Decorator_paramContext):
        pass

    # Exit a parse tree produced by d3iGrammar#decorator_param.
    def exitDecorator_param(self, ctx:d3iGrammar.Decorator_paramContext):
        pass


    # Enter a parse tree produced by d3iGrammar#enum.
    def enterEnum(self, ctx:d3iGrammar.EnumContext):
        pass

    # Exit a parse tree produced by d3iGrammar#enum.
    def exitEnum(self, ctx:d3iGrammar.EnumContext):
        pass


    # Enter a parse tree produced by d3iGrammar#enum_element.
    def enterEnum_element(self, ctx:d3iGrammar.Enum_elementContext):
        pass

    # Exit a parse tree produced by d3iGrammar#enum_element.
    def exitEnum_element(self, ctx:d3iGrammar.Enum_elementContext):
        pass


    # Enter a parse tree produced by d3iGrammar#inherits.
    def enterInherits(self, ctx:d3iGrammar.InheritsContext):
        pass

    # Exit a parse tree produced by d3iGrammar#inherits.
    def exitInherits(self, ctx:d3iGrammar.InheritsContext):
        pass



del d3iGrammar