# Generated from ./d3i/grammar/d3iGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .d3iGrammar import d3iGrammar
else:
    from d3iGrammar import d3iGrammar

# This class defines a complete generic visitor for a parse tree produced by d3iGrammar.

class d3iGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by d3iGrammar#d3.
    def visitD3(self, ctx:d3iGrammar.D3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#import_rule.
    def visitImport_rule(self, ctx:d3iGrammar.Import_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#domain.
    def visitDomain(self, ctx:d3iGrammar.DomainContext):
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


    # Visit a parse tree produced by d3iGrammar#dto.
    def visitDto(self, ctx:d3iGrammar.DtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#dto_element.
    def visitDto_element(self, ctx:d3iGrammar.Dto_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#dto_member.
    def visitDto_member(self, ctx:d3iGrammar.Dto_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#composite.
    def visitComposite(self, ctx:d3iGrammar.CompositeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#composite_element.
    def visitComposite_element(self, ctx:d3iGrammar.Composite_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#composite_member.
    def visitComposite_member(self, ctx:d3iGrammar.Composite_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event.
    def visitEvent(self, ctx:d3iGrammar.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_kind.
    def visitEvent_kind(self, ctx:d3iGrammar.Event_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_element.
    def visitEvent_element(self, ctx:d3iGrammar.Event_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#event_member.
    def visitEvent_member(self, ctx:d3iGrammar.Event_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#eventhandler.
    def visitEventhandler(self, ctx:d3iGrammar.EventhandlerContext):
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


    # Visit a parse tree produced by d3iGrammar#view_projections.
    def visitView_projections(self, ctx:d3iGrammar.View_projectionsContext):
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


    # Visit a parse tree produced by d3iGrammar#workflow.
    def visitWorkflow(self, ctx:d3iGrammar.WorkflowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#workflow_element.
    def visitWorkflow_element(self, ctx:d3iGrammar.Workflow_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#step.
    def visitStep(self, ctx:d3iGrammar.StepContext):
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


    # Visit a parse tree produced by d3iGrammar#emits_clause.
    def visitEmits_clause(self, ctx:d3iGrammar.Emits_clauseContext):
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


    # Visit a parse tree produced by d3iGrammar#ref_type.
    def visitRef_type(self, ctx:d3iGrammar.Ref_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#qualifiedName.
    def visitQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_expr.
    def visitValidate_expr(self, ctx:d3iGrammar.Validate_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_or.
    def visitValidate_or(self, ctx:d3iGrammar.Validate_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_and.
    def visitValidate_and(self, ctx:d3iGrammar.Validate_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_unary.
    def visitValidate_unary(self, ctx:d3iGrammar.Validate_unaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_predicate.
    def visitValidate_predicate(self, ctx:d3iGrammar.Validate_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_range.
    def visitValidate_range(self, ctx:d3iGrammar.Validate_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_set.
    def visitValidate_set(self, ctx:d3iGrammar.Validate_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by d3iGrammar#validate_term.
    def visitValidate_term(self, ctx:d3iGrammar.Validate_termContext):
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