grammar Complex;

// Punto de entrada de la gramática
expr: complexExpr EOF;  // Define que una expresión completa termina con el final de la entrada

// Expresión compleja con operadores +, -, * y /
complexExpr
    : complexExpr '+' complexExpr   #SumaExpr
    | complexExpr '-' complexExpr   #RestaExpr
    | complexExpr '*' complexExpr   #MultiplicacionExpr // Multiplicación de dos expresiones complejas
    | complexExpr '/' complexExpr   #DivisionExpr // División de dos expresiones complejas
    | '(' complexExpr ')'           #ParentesisExpr
    | complejo                      #ComplejoSimpleExpr
    ;

// Definición de un número complejo (real, imaginario o ambos)
complejo
    : real (signo imaginary)?       #RealConImaginarioExpr
    | imaginary                     #SoloImaginarioExpr
    ;

// Un número real puede ser entero o decimal
real
    : INT
    | FLOAT
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
INT   : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]+;
PLUS  : '+';
MINUS : '-';
MULT  : '*';
DIV   : '/';
LPAREN: '(';
RPAREN: ')';
WS    : [ \t\r\n]+ -> skip;

