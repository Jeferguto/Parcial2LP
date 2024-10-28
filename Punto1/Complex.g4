grammar Complex;  // Define el nombre de la gramática

// Punto de entrada de la gramática
expr: complexExpr EOF;  // Define que una expresión completa termina con el final de la entrada

// Expresión compleja con operadores +, -, * y /
complexExpr
    : complexExpr '+' complexExpr   #SumaExpr        // Suma de dos expresiones complejas
    | complexExpr '-' complexExpr   #RestaExpr       // Resta de dos expresiones complejas
    | complexExpr '*' complexExpr   #MultiplicacionExpr // Multiplicación de dos expresiones complejas
    | complexExpr '/' complexExpr   #DivisionExpr    // División de dos expresiones complejas
    | '(' complexExpr ')'           #ParentesisExpr  // Expresión entre paréntesis
    | complejo                      #ComplejoSimpleExpr // Una expresión compleja simple
    ;

// Definición de un número complejo (real, imaginario o ambos)
complejo
    : real (signo imaginary)?       #RealConImaginarioExpr // Parte real y opcionalmente parte imaginaria
    | imaginary                     #SoloImaginarioExpr // Solo parte imaginaria
    ;

// Un número real puede ser entero o decimal
real
    : INT                            // Un número entero
    | FLOAT                          // Un número decimal
    ;

// Parte imaginaria: número real seguido de 'i'
imaginary
    : real 'i'                      // Define que la parte imaginaria es un número seguido de 'i'
    ;

// Definimos un signo opcional para la parte imaginaria
signo
    : '+'                           // Signo positivo
    | '-'                           // Signo negativo
    ;

// Definiciones del lexer para identificar tokens
INT   : [0-9]+;                    // Define un token para números enteros
FLOAT : [0-9]+ '.' [0-9]+;         // Define un token para números decimales
PLUS  : '+';                       // Define un token para el símbolo +
MINUS : '-';                       // Define un token para el símbolo -
MULT  : '*';                       // Define un token para el símbolo *
DIV   : '/';                       // Define un token para el símbolo /
LPAREN: '(';                       // Define un token para el símbolo de apertura (
RPAREN: ')';                       // Define un token para el símbolo de cierre )
WS    : [ \t\r\n]+ -> skip;        // Define que los espacios en blanco se deben ignorar

