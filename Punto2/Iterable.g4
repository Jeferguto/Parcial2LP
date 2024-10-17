grammar Iterable;  // Define la gramática llamada Iterable

start
    : mapExpr | filterExpr  // La regla de inicio puede ser una expresión de mapa o una expresión de filtro
    ;

mapExpr
    : 'MAP' '(' ID ',' iterable ')'  // Define una expresión de mapa que comienza con 'MAP', seguido de un identificador y un iterable
    ;

filterExpr
    : 'FILTER' '(' ID ',' iterable ')'  // Define una expresión de filtro que comienza con 'FILTER', seguido de un identificador y un iterable
    ;

iterable
    : '[' (NUMBER (',' NUMBER)*)? ']'  // Define un iterable como una lista de números, opcionalmente separados por comas
    ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]*  // Define un identificador que comienza con una letra o guion bajo, seguido de letras, números o guiones bajos
    ;

NUMBER
    : [0-9]+  // Define un número como una secuencia de dígitos
    ;

WS
    : [ \t\r\n]+ -> skip  // Ignora espacios en blanco, tabulaciones y saltos de línea
    ;

