grammar Fourier;

// Reglas léxicas
INT         : [0-9]+ ;
FLOAT       : [0-9]+ '.' [0-9]* ;
ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
WS          : [ \t\r\n]+ -> skip ;
PLUS        : '+' ;
MINUS       : '-' ;
MULT        : '*' ;
DIV         : '/' ;
EXP         : '^' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
INTEGRAL    : '∫' ;
DELTA       : 'δ' ;
SINC        : 'sinc' ;
PI          : 'π' ;
FOURIER     : 'F' ;
INVFOURIER  : 'F^-1' ;
UNITSTEP    : 'H' ;
E           : 'e' ;
J           : 'j' ;

// Reglas sintácticas
expr        : term (op term)* ;

op          : PLUS
            | MINUS
            | MULT
            | DIV
            | EXP ;

term        : func_expr
            | integral_expr
            | atom ;

func_expr   : FOURIER LPAREN expr RPAREN
            | INVFOURIER LPAREN expr RPAREN ;

integral_expr : INTEGRAL expr ('dt' | 'dw') ;

atom        : ID
            | INT
            | FLOAT
            | LPAREN expr RPAREN
            | func_call ;

func_call   : SINC LPAREN expr RPAREN
            | DELTA LPAREN expr RPAREN
            | UNITSTEP LPAREN expr RPAREN ;

