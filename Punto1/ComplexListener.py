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


    # Enter a parse tree produced by ComplexParser#Suma.
    def enterSuma(self, ctx:ComplexParser.SumaContext):
        pass

    # Exit a parse tree produced by ComplexParser#Suma.
    def exitSuma(self, ctx:ComplexParser.SumaContext):
        pass


    # Enter a parse tree produced by ComplexParser#Parentesis.
    def enterParentesis(self, ctx:ComplexParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ComplexParser#Parentesis.
    def exitParentesis(self, ctx:ComplexParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ComplexParser#ComplejoSimple.
    def enterComplejoSimple(self, ctx:ComplexParser.ComplejoSimpleContext):
        pass

    # Exit a parse tree produced by ComplexParser#ComplejoSimple.
    def exitComplejoSimple(self, ctx:ComplexParser.ComplejoSimpleContext):
        pass


    # Enter a parse tree produced by ComplexParser#Resta.
    def enterResta(self, ctx:ComplexParser.RestaContext):
        pass

    # Exit a parse tree produced by ComplexParser#Resta.
    def exitResta(self, ctx:ComplexParser.RestaContext):
        pass


    # Enter a parse tree produced by ComplexParser#RealConImaginario.
    def enterRealConImaginario(self, ctx:ComplexParser.RealConImaginarioContext):
        pass

    # Exit a parse tree produced by ComplexParser#RealConImaginario.
    def exitRealConImaginario(self, ctx:ComplexParser.RealConImaginarioContext):
        pass


    # Enter a parse tree produced by ComplexParser#SoloImaginario.
    def enterSoloImaginario(self, ctx:ComplexParser.SoloImaginarioContext):
        pass

    # Exit a parse tree produced by ComplexParser#SoloImaginario.
    def exitSoloImaginario(self, ctx:ComplexParser.SoloImaginarioContext):
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