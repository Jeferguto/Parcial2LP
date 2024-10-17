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


    # Visit a parse tree produced by ComplexParser#ComplejoSimpleExpr.
    def visitComplejoSimpleExpr(self, ctx:ComplexParser.ComplejoSimpleExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#ParentesisExpr.
    def visitParentesisExpr(self, ctx:ComplexParser.ParentesisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#SumaExpr.
    def visitSumaExpr(self, ctx:ComplexParser.SumaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#RestaExpr.
    def visitRestaExpr(self, ctx:ComplexParser.RestaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#RealConImaginarioExpr.
    def visitRealConImaginarioExpr(self, ctx:ComplexParser.RealConImaginarioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#SoloImaginarioExpr.
    def visitSoloImaginarioExpr(self, ctx:ComplexParser.SoloImaginarioExprContext):
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