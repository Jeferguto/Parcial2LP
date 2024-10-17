import sys
from antlr4 import *
from ComplexLexer import ComplexLexer  # Importa el lexer generado
from ComplexParser import ComplexParser  # Importa el parser generado
from ComplexVisitor import ComplexVisitor  # Importa el visitor generado

# Definición de la clase que evaluará las expresiones complejas
class ComplexEvaluator(ComplexVisitor):
    
    # Visita la expresión raíz y delega a la expresión compleja
    def visitExpr(self, ctx):
        return self.visit(ctx.complexExpr())

    # Maneja la resta de dos expresiones complejas
    def visitRestaExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))  # Operando izquierdo
        rightOperand = self.visit(ctx.complexExpr(1))  # Operando derecho
        return (leftOperand[0] - rightOperand[0], leftOperand[1] - rightOperand[1])
        
    
    # Maneja la suma de dos expresiones complejas
    def visitSumaExpr(self, ctx):
        leftOperand = self.visit(ctx.complexExpr(0))  # Obtiene el operando izquierdo
        rightOperand = self.visit(ctx.complexExpr(1))  # Obtiene el operando derecho
        return (leftOperand[0] + rightOperand[0], leftOperand[1] + rightOperand[1])

    # Maneja las expresiones entre paréntesis
    def visitParentesisExpr(self, ctx):
        return self.visit(ctx.complexExpr())

    # Maneja la expresión que tiene tanto parte real como imaginaria
    def visitRealConImaginarioExpr(self, ctx):
        realPart = float(ctx.real().getText())  # Convierte la parte real a flotante
        imaginaryPart = 0.0  # Inicializa la parte imaginaria en 0
        
        # Si hay un signo y una parte imaginaria, ajusta la parte imaginaria
        if ctx.signo():
            sign = ctx.signo().getText()  # Obtiene el signo de la parte imaginaria
            imaginaryStr = ctx.imaginary().real().getText()  # Obtiene el valor de la parte imaginaria
            imaginaryPart = float(imaginaryStr)
            if sign == '-':
                imaginaryPart = -imaginaryPart
        else:
            # Si no hay signo, verifica si hay una parte imaginaria
            if ctx.imaginary():
                imaginaryStr = ctx.imaginary().real().getText()
                imaginaryPart = float(imaginaryStr)
        
        return (realPart, imaginaryPart)

    # Maneja las expresiones que solo contienen parte imaginaria
    def visitSoloImaginarioExpr(self, ctx):
        imaginaryStr = ctx.imaginary().real().getText()  # Obtiene la parte imaginaria
        imaginaryPart = float(imaginaryStr)
        return (0.0, imaginaryPart)

    # Maneja la visita a un número complejo simple
    def visitComplejoSimpleExpr(self, ctx):
        return self.visit(ctx.complejo())

# Función principal para ejecutar el programa
def main():
    # Verifica que se haya ingresado una expresión como argumento
    if len(sys.argv) < 2:
        print("Ingresar una operacion con numeros complejos. Ej -> \"(2 + 7i) + (3 - 4i)\"")
        return

    inputExpr = sys.argv[1]  # Obtiene la expresión ingresada
    inputStream = InputStream(inputExpr)  # Convierte la expresión en un stream de entrada
    lexer = ComplexLexer(inputStream)  # Genera los tokens usando el lexer
    tokenStream = CommonTokenStream(lexer)  # Crea el stream de tokens
    parser = ComplexParser(tokenStream)  # Pasa el stream de tokens al parser
    tree = parser.expr()  # Genera el árbol sintáctico

    evaluator = ComplexEvaluator()  # Crea una instancia del evaluador
    result = evaluator.visit(tree)  # Visita el árbol para evaluar la expresión

    # Si no se pudo evaluar, muestra un mensaje de error
    if result is None:
        print("No se pudo evaluar la expresión.")
        return

    realPart, imaginaryPart = result  # Desempaqueta el resultado en parte real e imaginaria
    
    # Si ambas partes son 0, la expresión no contiene números complejos
    if realPart == 0 and imaginaryPart == 0:
        print("Esta expresión no contiene números complejos.")
    else:
        # Muestra el resultado formateado
        if imaginaryPart >= 0:
            print(f"Resultado: {realPart} + {imaginaryPart}i")
        else:
            print(f"Resultado: {realPart} - {abs(imaginaryPart)}i")

# Inicia el programa si se ejecuta como script
if __name__ == '__main__':
    main()

