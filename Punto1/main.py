import sys
from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexVisitor import ComplexVisitor

class EvaluadorComplejos(ComplexVisitor):
    def visitExpr(self, ctx):
        return self.visit(ctx.complexExpr())

    def visitSuma(self, ctx):
        left = self.visit(ctx.complexExpr(0))
        right = self.visit(ctx.complexExpr(1))
        return (left[0] + right[0], left[1] + right[1])

    def visitResta(self, ctx):
        left = self.visit(ctx.complexExpr(0))
        right = self.visit(ctx.complexExpr(1))
        return (left[0] - right[0], left[1] - right[1])

    def visitParentesis(self, ctx):
        return self.visit(ctx.complexExpr())

    def visitRealConImaginario(self, ctx):
        real = float(ctx.real().getText())
        imaginary = 0.0
        
        if ctx.signo():
            signo = ctx.signo().getText()
            imaginary_str = ctx.imaginary().real().getText()
            imaginary = float(imaginary_str)
            if signo == '-':
                imaginary = -imaginary
        else:
            if ctx.imaginary():
                imaginary_str = ctx.imaginary().real().getText()
                imaginary = float(imaginary_str)
        
        return (real, imaginary)

    def visitSoloImaginario(self, ctx):
        imaginary_str = ctx.imaginary().real().getText()
        imaginary = float(imaginary_str)
        return (0.0, imaginary)

    def visitComplejoSimple(self, ctx):
        return self.visit(ctx.complejo())

def main():
    if len(sys.argv) < 2:
        print("Ejemplo de uso: python main.py \"(2 + 7i) + (3 - 4i)\"")
        return

    input_expr = sys.argv[1]
    input_stream = InputStream(input_expr)
    lexer = ComplexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    tree = parser.expr()

    evaluator = EvaluadorComplejos()
    result = evaluator.visit(tree)

    if result is None:
        print("No se pudo evaluar la expresión.")
        return

    real, imag = result
    if imag >= 0:
        print(f"Resultado: {real} + {imag}i")
    else:
        print(f"Resultado: {real} - {abs(imag)}i")

if __name__ == '__main__':
    main()

