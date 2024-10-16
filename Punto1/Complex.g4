grammar Complex;

// Punto de entrada
expr: complexExpr EOF;

// Expresión compleja con operadores + y -
complexExpr
    : complexExpr '+' complexExpr #Suma
    | complexExpr '-' complexExpr #Resta
    | '(' complexExpr ')'          #Parentesis
    | complejo                     #ComplejoSimple
    ;

// Un número complejo tiene una parte real, una imaginaria o ambas
complejo
    : real (signo imaginary)?      #RealConImaginario
    | imaginary                    #SoloImaginario
    ;

// Un número real puede ser entero o decimal
real
    : INT
    | FLOAT
    ;

// La parte imaginaria es un número real seguido de 'i'
imaginary
    : real 'i'
    ;

// Definimos un signo opcional para la parte imaginaria
signo
    : '+'
    | '-'
    ;

// Reglas del Lexer
INT   : [0-9]+;                     // Números enteros
FLOAT : [0-9]+ '.' [0-9]+;          // Números decimales
PLUS  : '+';                        // Operador suma
MINUS : '-';                        // Operador resta
LPAREN: '(';                        // Paréntesis izquierdo
RPAREN: ')';                        // Paréntesis derecho
WS    : [ \t\r\n]+ -> skip;         // Espacios en blanco ignorados

