# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete generic visitor for a parse tree produced by ComplexParser.

class ComplexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexParser#expr.
    def visitExpr(self, ctx:ComplexParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Suma.
    def visitSuma(self, ctx:ComplexParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Parentesis.
    def visitParentesis(self, ctx:ComplexParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#ComplejoSimple.
    def visitComplejoSimple(self, ctx:ComplexParser.ComplejoSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Resta.
    def visitResta(self, ctx:ComplexParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#RealConImaginario.
    def visitRealConImaginario(self, ctx:ComplexParser.RealConImaginarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#SoloImaginario.
    def visitSoloImaginario(self, ctx:ComplexParser.SoloImaginarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#real.
    def visitReal(self, ctx:ComplexParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#imaginary.
    def visitImaginary(self, ctx:ComplexParser.ImaginaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#signo.
    def visitSigno(self, ctx:ComplexParser.SignoContext):
        return self.visitChildren(ctx)



del ComplexParser