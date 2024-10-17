grammar Complex;

// Punto de entrada de la gramática
expr: complexExpr EOF;  // Define que una expresión completa termina con el final de la entrada

// Expresión compleja con operadores + y -
complexExpr
    : complexExpr '+' complexExpr   #SumaExpr  // Suma de dos expresiones complejas
    | complexExpr '-' complexExpr   #RestaExpr // Resta de dos expresiones complejas
    | '(' complexExpr ')'           #ParentesisExpr // Expresión compleja entre paréntesis
    | complejo                      #ComplejoSimpleExpr // Número complejo simple
    ;

// Definición de un número complejo (real, imaginario o ambos)
complejo
    : real (signo imaginary)?       #RealConImaginarioExpr // Parte real con o sin parte imaginaria
    | imaginary                     #SoloImaginarioExpr    // Solo parte imaginaria
    ;

// Un número real puede ser entero o decimal
real
    : INT                           // Definición de número entero
    | FLOAT                         // Definición de número decimal
    ;

// Parte imaginaria: número real seguido de 'i'
imaginary
    : real 'i'
    ;

// Definimos un signo opcional para la parte imaginaria
signo
    : '+'
    | '-'
    ;

// Definiciones del lexer para identificar tokens
INT   : [0-9]+;                     // Números enteros
FLOAT : [0-9]+ '.' [0-9]+;          // Números decimales
PLUS  : '+';                        // Operador de suma
MINUS : '-';                        // Operador de resta
LPAREN: '(';                        // Paréntesis izquierdo
RPAREN: ')';                        // Paréntesis derecho
WS    : [ \t\r\n]+ -> skip;         // Ignorar espacios en blanco

