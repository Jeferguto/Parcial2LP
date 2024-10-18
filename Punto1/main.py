import sys  # Importa el módulo sys para manejar argumentos de la línea de comandos
from antlr4 import *  # Importa todas las clases de ANTLR
from ComplexLexer import ComplexLexer  # Importa el lexer generado por ANTLR
from ComplexParser import ComplexParser  # Importa el parser generado por ANTLR
from ComplexVisitor import ComplexVisitor  # Importa el visitor generado por ANTLR

class ComplexEvaluator(ComplexVisitor):  # Define la clase ComplexEvaluator que hereda de ComplexVisitor
    
    def visitExpr(self, ctx):  # Método que visita la expresión
        return self.visit(ctx.complexExpr())  # Llama al método visit para la expresión compleja

    def visitRestaExpr(self, ctx):  # Método que visita las restas
        leftOperand = self.visit(ctx.complexExpr(0))  # Visita el primer operando
        rightOperand = self.visit(ctx.complexExpr(1))  # Visita el segundo operando
        return (leftOperand[0] - rightOperand[0], leftOperand[1] - rightOperand[1])  # Devuelve la resta de partes reales e imaginarias
        
    def visitSumaExpr(self, ctx):  # Método que visita las sumas
        leftOperand = self.visit(ctx.complexExpr(0))  # Visita el primer operando
        rightOperand = self.visit(ctx.complexExpr(1))  # Visita el segundo operando
        return (leftOperand[0] + rightOperand[0], leftOperand[1] + rightOperand[1])  # Devuelve la suma de partes reales e imaginarias

    def visitMultiplicacionExpr(self, ctx):  # Método que visita las multiplicaciones
        leftOperand = self.visit(ctx.complexExpr(0))  # Visita el primer operando
        rightOperand = self.visit(ctx.complexExpr(1))  # Visita el segundo operando
        # Cálculo de la multiplicación de números complejos
        realPart = leftOperand[0] * rightOperand[0] - leftOperand[1] * rightOperand[1]  # Parte real
        imaginaryPart = leftOperand[0] * rightOperand[1] + leftOperand[1] * rightOperand[0]  # Parte imaginaria
        return (realPart, imaginaryPart)  # Devuelve la parte real e imaginaria

    def visitDivisionExpr(self, ctx):  # Método que visita las divisiones
        leftOperand = self.visit(ctx.complexExpr(0))  # Visita el primer operando
        rightOperand = self.visit(ctx.complexExpr(1))  # Visita el segundo operando

        # Verifica si el denominador es cero
        if rightOperand[0] == 0 and rightOperand[1] == 0:
            print("Error: División por cero no permitida.")  # Imprime un error si se intenta dividir por cero
            return None
        
        # Cálculo de la división de números complejos
        denominator = rightOperand[0] ** 2 + rightOperand[1] ** 2  # Cálculo del denominador
        realPart = (leftOperand[0] * rightOperand[0] + leftOperand[1] * rightOperand[1]) / denominator  # Parte real
        imaginaryPart = (leftOperand[1] * rightOperand[0] - leftOperand[0] * rightOperand[1]) / denominator  # Parte imaginaria
        return (realPart, imaginaryPart)  # Devuelve la parte real e imaginaria

    def visitParentesisExpr(self, ctx):  # Método que visita expresiones entre paréntesis
        return self.visit(ctx.complexExpr())  # Visita la expresión compleja dentro de los paréntesis

    def visitRealConImaginarioExpr(self, ctx):  # Método que visita expresiones con parte real e imaginaria
        realPart = float(ctx.real().getText())  # Obtiene la parte real
        imaginaryPart = 0.0  # Inicializa la parte imaginaria a cero
        
        if ctx.signo():  # Si hay un signo presente
            sign = ctx.signo().getText()  # Obtiene el signo
            imaginaryStr = ctx.imaginary().real().getText()  # Obtiene la parte imaginaria
            imaginaryPart = float(imaginaryStr)  # Convierte a float
            if sign == '-':  # Si el signo es negativo
                imaginaryPart = -imaginaryPart  # Cambia la parte imaginaria a negativa
        else:
            if ctx.imaginary():  # Si solo hay parte imaginaria
                imaginaryStr = ctx.imaginary().real().getText()  # Obtiene la parte imaginaria
                imaginaryPart = float(imaginaryStr)  # Convierte a float
        
        return (realPart, imaginaryPart)  # Devuelve la parte real e imaginaria

    def visitSoloImaginarioExpr(self, ctx):  # Método que visita expresiones con solo parte imaginaria
        imaginaryStr = ctx.imaginary().real().getText()  # Obtiene la parte imaginaria
        imaginaryPart = float(imaginaryStr)  # Convierte a float
        return (0.0, imaginaryPart)  # Devuelve cero y la parte imaginaria

    def visitComplejoSimpleExpr(self, ctx):  # Método que visita expresiones complejas simples
        return self.visit(ctx.complejo())  # Visita la expresión compleja

def main():  # Función principal
    if len(sys.argv) < 2:  # Verifica si se han pasado suficientes argumentos
        print("Ingresar una operacion con numeros complejos. Ej -> \"(2 + 7i) + (3 - 4i)\"")  # Mensaje de ayuda
        return

    inputExpr = sys.argv[1]  # Obtiene la expresión compleja desde la línea de comandos
    inputStream = InputStream(inputExpr)  # Crea un flujo de entrada a partir de la expresión
    lexer = ComplexLexer(inputStream)  # Crea un lexer con el flujo de entrada
    tokenStream = CommonTokenStream(lexer)  # Crea un flujo de tokens a partir del lexer
    parser = ComplexParser(tokenStream)  # Crea un parser con el flujo de tokens
    tree = parser.expr()  # Analiza la expresión y genera un árbol de parseo

    evaluator = ComplexEvaluator()  # Crea un evaluador de expresiones complejas
    result = evaluator.visit(tree)  # Evalúa el árbol de parseo

    if result is None:  # Verifica si el resultado es None (en caso de error)
        print("No se pudo evaluar la expresión.")  # Mensaje de error
        return

    realPart, imaginaryPart = result  # Descompone el resultado en parte real e imaginaria
    print(f"Resultado: {realPart} + {imaginaryPart}i")  # Imprime el resultado

if __name__ == "__main__":  # Verifica si este archivo es el script principal
    main()  # Llama a la función principal

