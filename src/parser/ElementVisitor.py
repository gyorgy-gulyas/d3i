from parser.d3iGrammar import *
from parser.d3iGrammarVisitor import *
from elements import *

class ElementVisitor(d3iGrammarVisitor):
    def visitDirective(self, ctx:d3iGrammar.DirectiveContext):
        result = directive()
        result.keyword = ctx.IDENTIFIER()
        result.value = self.visit(ctx.qualifiedName())
        return result

    def visitQualifiedName(self, ctx:d3iGrammar.QualifiedNameContext):
        counter = 0
        result = qualified_name()
        while True:
            identifier = ctx.IDENTIFIER(counter)
            if( identifier == None ):
                break
            counter = counter + 1
            result.names.append(identifier)
        return result
    
    def visitDecorator(self, ctx:d3iGrammar.DecoratorContext):
        return self.visitChildren(ctx)

    def visitDecorator_param(self, ctx:d3iGrammar.Decorator_paramContext):
        result = decorator_param()
        result.name = ctx.
        return self.visitChildren(ctx)

