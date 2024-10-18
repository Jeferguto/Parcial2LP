import sys
from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser
from FourierVisitor import FourierVisitor

class FourierEvalVisitor(FourierVisitor):
    def visitFunc_expr(self, ctx):
        # Lógica para manejar funciones de Fourier
        if ctx.FOURIER():
            return f"Transformada de Fourier de {ctx.expr().getText()}"
        elif ctx.INVFOURIER():
            return f"Transformada Inversa de Fourier de {ctx.expr().getText()}"
        return None

    def visitIntegral_expr(self, ctx):
        return f"Integración de {ctx.expr().getText()} respecto a {ctx.getChild(2).getText()}"

    def visitTerm(self, ctx):
        return self.visitChildren(ctx)

    def visitAtom(self, ctx):
        return ctx.getText()

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:  # Verificar si la línea está vacía
            continue
        
        print(f"Procesando línea: {line}")
        input_stream = InputStream(line)
        lexer = FourierLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FourierParser(stream)

        tree = parser.expr()
        evaluator = FourierEvalVisitor()

        result = evaluator.visit(tree)
        print(f"Resultado de la evaluación: {result}\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <archivo_de_expresiones.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

