import sys  # Importa el módulo sys para acceder a argumentos de línea de comandos
from antlr4 import *  # Importa las funcionalidades de ANTLR
from IterableLexer import IterableLexer  # Importa el lexer generado
from IterableParser import IterableParser  # Importa el parser generado
from IterableVisitor import IterableVisitor  # Importa el visitor generado

# Definición de funciones predefinidas


def square(x):
    return x **1/2  # Devuelve el cuadrado de x

def double(x):
    return x * 2  # Devuelve el doble de x

def increment(x):
    return x + 1  # Devuelve x incrementado en 1

def isEven(x):
    return x % 2 == 0  # Devuelve True si x es par

def isOdd(x):
    return x % 2 != 0  # Devuelve True si x es impar

def greaterThanTen(x):
    return x > 15  # Devuelve True si x es mayor que 15 (cuidado con el valor límite)

# Evaluador de las expresiones
class IterableEvaluator(IterableVisitor):
    def visitMapExpr(self, ctx):
        function_name = ctx.ID().getText()  # Obtiene el nombre de la función desde el contexto
        iterable = eval(ctx.iterable().getText())  # Evalúa el iterable desde el contexto

        if function_name in globals():  # Verifica si la función está definida
            function = globals()[function_name]  # Obtiene la función definida
            result = list(map(function, iterable))  # Usa map para aplicar la función al iterable
            return result  # Devuelve el resultado
        return None  # Si la función no está definida, devuelve None

    def visitFilterExpr(self, ctx):
        function_name = ctx.ID().getText()  # Obtiene el nombre de la función desde el contexto
        iterable = eval(ctx.iterable().getText())  # Evalúa el iterable desde el contexto

        if function_name in globals():  # Verifica si la función está definida
            function = globals()[function_name]  # Obtiene la función definida
            result = list(filter(function, iterable))  # Usa filter para aplicar la función al iterable
            return result  # Devuelve el resultado
        return None  # Si la función no está definida, devuelve None

# Función principal para procesar la entrada
def main():
    input_stream = InputStream(sys.argv[1])  # Lee la expresión de entrada desde los argumentos de línea de comandos
    lexer = IterableLexer(input_stream)  # Crea el lexer
    stream = CommonTokenStream(lexer)  # Crea el stream de tokens
    parser = IterableParser(stream)  # Crea el parser
    tree = parser.start()  # Genera el árbol sintáctico a partir de la entrada

    evaluator = IterableEvaluator()  # Crea una instancia del evaluador
    result = evaluator.visit(tree)  # Visita el árbol y evalúa la expresión

    # Imprimir el resultado de la evaluación con un mensaje descriptivo
    function_name = tree.children[0].ID().getText()  # Obtiene el nombre de la función del árbol

    if isinstance(result, list):  # Verifica si el resultado es una lista
        if function_name == 'isEven':
            print(f"Resultado: Los pares son {result}")  # Imprime los pares encontrados
        elif function_name == 'isOdd':
            print(f"Resultado: Los impares son {result}")  # Imprime los impares encontrados
        elif function_name == 'greaterThanTen':
            print(f"Resultado: Los números mayores a X son {result}")  # Imprime los números mayores a X
        elif function_name == 'square':
            print(f"Resultado: Los cuadrados son {result}")  # Imprime los cuadrados
        elif function_name == 'double':
            print(f"Resultado: Los dobles son {result}")  # Imprime los dobles
        elif function_name == 'increment':
            print(f"Resultado: Los incrementos son {result}")  # Imprime los incrementos
    else:
        print("Resultado: No se encontraron resultados.")  # Mensaje si no se encontraron resultados

if __name__ == "__main__":
    main()  # Llama a la función principal para ejecutar el programa

