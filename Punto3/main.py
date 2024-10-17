import sys
from antlr4 import *
from FourierLexer import FourierLexer  # Asegúrate de que el nombre del archivo sea correcto
from FourierParser import FourierParser  # Asegúrate de que el nombre del archivo sea correcto

class FourierEvaluator(ParseTreeVisitor):
    def visitFunc_expr(self, ctx):
        if ctx.FOURIER():
            print("Calculando la transformada de Fourier para: ", ctx.expr().getText())
            result = self.visit(ctx.expr())
            return f"FOURIER({result})"  # Retorna el resultado
        elif ctx.INVFOURIER():
            print("Calculando la inversa de la transformada de Fourier para: ", ctx.expr().getText())
            result = self.visit(ctx.expr())
            return f"FOURIER^-1({result})"  # Retorna el resultado

    def visitIntegral_expr(self, ctx):
        print("Calculando integral: ", ctx.getText())
        return "Integral Result"

    def visitAtom(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.ID():
            return ctx.ID().getText()
        return None

    def visitOp(self, ctx):
        left = self.visit(ctx.term(0))  # Obtiene el primer término
        right = self.visit(ctx.term(1))  # Obtiene el segundo término

        if ctx.PLUS():
            return left + right
        elif ctx.MINUS():
            return left - right
        elif ctx.MULT():
            return left * right
        elif ctx.DIV():
            return left / right
        elif ctx.EXP():
            return left ** right
        return None

    def visitTerm(self, ctx):
        return self.visit(ctx.getChild(0))  # Visita el primer hijo de 'term'

def main(file_path):
    # Abrir el archivo de entrada
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            expression = line.strip()
            print(f"\nProcesando línea {line_number}: {expression}")
            input_stream = InputStream(expression)
            
            lexer = FourierLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = FourierParser(stream)
            
            tree = parser.expr()
            evaluator = FourierEvaluator()
            result = evaluator.visit(tree)

            print("Resultado de la evaluación:", result)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        main(file_path)
    else:
        print("Por favor, proporciona la ruta del archivo de entrada.")

