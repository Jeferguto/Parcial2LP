import sys
from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexVisitor import ComplexVisitor

class ComplexEvaluator(ComplexVisitor):
    
    def visitExpr(self, ctx):
        return self.visit(ctx.complexExpr())

    def visitRestaExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))
        rightOperand = self.visit(ctx.complexExpr(1))
        return (leftOperand[0] - rightOperand[0], leftOperand[1] - rightOperand[1])
        
    def visitSumaExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))
        rightOperand = self.visit(ctx.complexExpr(1))
        return (leftOperand[0] + rightOperand[0], leftOperand[1] + rightOperand[1])

    def visitMultiplicacionExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))
        rightOperand = self.visit(ctx.complexExpr(1))
        realPart = leftOperand[0] * rightOperand[0] - leftOperand[1] * rightOperand[1]
        imaginaryPart = leftOperand[0] * rightOperand[1] + leftOperand[1] * rightOperand[0]
        return (realPart, imaginaryPart)

    def visitDivisionExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))
        rightOperand = self.visit(ctx.complexExpr(1))

        # Verifica si el numerador es cero
        if rightOperand[0] == 0 and rightOperand[1] == 0:
            print("Error: División por cero no permitida.")
            return None
        
        # Cálculo de la división de números complejos
        denominator = rightOperand[0] ** 2 + rightOperand[1] ** 2
        realPart = (leftOperand[0] * rightOperand[0] + leftOperand[1] * rightOperand[1]) / denominator
        imaginaryPart = (leftOperand[1] * rightOperand[0] - leftOperand[0] * rightOperand[1]) / denominator
        return (realPart, imaginaryPart)

    def visitParentesisExpr(self, ctx):
        return self.visit(ctx.complexExpr())

    def visitRealConImaginarioExpr(self, ctx):
        realPart = float(ctx.real().getText())
        imaginaryPart = 0.0
        
        if ctx.signo():
            sign = ctx.signo().getText()
            imaginaryStr = ctx.imaginary().real().getText()
            imaginaryPart = float(imaginaryStr)
            if sign == '-':
                imaginaryPart = -imaginaryPart
        else:
            if ctx.imaginary():
                imaginaryStr = ctx.imaginary().real().getText()
                imaginaryPart = float(imaginaryStr)
        
        return (realPart, imaginaryPart)

    def visitSoloImaginarioExpr(self, ctx):
        imaginaryStr = ctx.imaginary().real().getText()
        imaginaryPart = float(imaginaryStr)
        return (0.0, imaginaryPart)

    def visitComplejoSimpleExpr(self, ctx):
        return self.visit(ctx.complejo())

def main():
    if len(sys.argv) < 2:
        print("Ingresar una operacion con numeros complejos. Ej -> \"(2 + 7i) + (3 - 4i)\"")
        return

    inputExpr = sys.argv[1]
    inputStream = InputStream(inputExpr)
    lexer = ComplexLexer(inputStream)
    tokenStream = CommonTokenStream(lexer)
    parser = ComplexParser(tokenStream)
    tree = parser.expr()

    evaluator = ComplexEvaluator()
    result = evaluator.visit(tree)

    if result is None:
        print("No se pudo evaluar la expresión.")
        return

    realPart, imaginaryPart = result
    
    if realPart == 0 and imaginaryPart == 0:
        print("Esta expresión no contiene números complejos.")
    else:
        if imaginaryPart >= 0:
            print(f"Resultado: {realPart} + {imaginaryPart}i")
        else:
            print(f"Resultado: {realPart} - {abs(imaginaryPart)}i")

if __name__ == '__main__':
    main()

