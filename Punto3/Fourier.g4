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
LBRACKET    : '[' ;    
RBRACKET    : ']' ;    
INTEGRAL    : '∫' ;
DELTA       : 'δ' ;
SINC        : 'sinc' ;
PI          : 'π' ;
FOURIER     : 'F' ;
INVFOURIER  : 'F^-1' ;
UNITSTEP    : 'H' ; // Cambiado para que coincida
E           : 'e' ;
J           : 'j' ;
ARROW       : '→' ; // Flecha

// Reglas sintácticas
assign      : ID '=' expr;  

expr        : term (op term)* ;

op          : PLUS
            | MINUS
            | MULT
            | DIV
            | EXP ;

term        : func_expr
            | integral_expr
            | atom ;

func_expr   : FOURIER LBRACKET expr RBRACKET    
            | INVFOURIER LBRACKET expr RBRACKET 
            | ID LPAREN expr RPAREN;  

integral_expr : INTEGRAL expr ('dt' | 'dw') ;

atom        : ID
            | INT
            | FLOAT
            | MINUS atom 
            | LPAREN expr RPAREN
            | func_call 
            | J atom ; 

func_call   : SINC LPAREN expr RPAREN
            | DELTA LPAREN expr RPAREN
            | UNITSTEP LPAREN expr RPAREN ;

mapping_expr : expr ARROW expr; // Para manejar expresiones de la forma "A → B"

