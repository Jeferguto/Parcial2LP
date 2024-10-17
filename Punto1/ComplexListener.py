# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete listener for a parse tree produced by ComplexParser.
class ComplexListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexParser#expr.
    def enterExpr(self, ctx:ComplexParser.ExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#expr.
    def exitExpr(self, ctx:ComplexParser.ExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#ComplejoSimpleExpr.
    def enterComplejoSimpleExpr(self, ctx:ComplexParser.ComplejoSimpleExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#ComplejoSimpleExpr.
    def exitComplejoSimpleExpr(self, ctx:ComplexParser.ComplejoSimpleExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#ParentesisExpr.
    def enterParentesisExpr(self, ctx:ComplexParser.ParentesisExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#ParentesisExpr.
    def exitParentesisExpr(self, ctx:ComplexParser.ParentesisExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#SumaExpr.
    def enterSumaExpr(self, ctx:ComplexParser.SumaExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#SumaExpr.
    def exitSumaExpr(self, ctx:ComplexParser.SumaExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#RestaExpr.
    def enterRestaExpr(self, ctx:ComplexParser.RestaExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#RestaExpr.
    def exitRestaExpr(self, ctx:ComplexParser.RestaExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#RealConImaginarioExpr.
    def enterRealConImaginarioExpr(self, ctx:ComplexParser.RealConImaginarioExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#RealConImaginarioExpr.
    def exitRealConImaginarioExpr(self, ctx:ComplexParser.RealConImaginarioExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#SoloImaginarioExpr.
    def enterSoloImaginarioExpr(self, ctx:ComplexParser.SoloImaginarioExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#SoloImaginarioExpr.
    def exitSoloImaginarioExpr(self, ctx:ComplexParser.SoloImaginarioExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#real.
    def enterReal(self, ctx:ComplexParser.RealContext):
        pass

    # Exit a parse tree produced by ComplexParser#real.
    def exitReal(self, ctx:ComplexParser.RealContext):
        pass


    # Enter a parse tree produced by ComplexParser#imaginary.
    def enterImaginary(self, ctx:ComplexParser.ImaginaryContext):
        pass

    # Exit a parse tree produced by ComplexParser#imaginary.
    def exitImaginary(self, ctx:ComplexParser.ImaginaryContext):
        pass


    # Enter a parse tree produced by ComplexParser#signo.
    def enterSigno(self, ctx:ComplexParser.SignoContext):
        pass

    # Exit a parse tree produced by ComplexParser#signo.
    def exitSigno(self, ctx:ComplexParser.SignoContext):
        pass



del ComplexParser