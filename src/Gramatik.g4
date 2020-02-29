grammar Gramatik;


start : expr EOF #startRule;
expr : 
	SYMBOL #simbol
	| NUMBER #numar
	| SYMBOL INTR #maybe
	| expr expr #concat
	| expr OR expr #sau
	| ANYTHING #anything
	| SYMBOL AST #star
	| SYMBOL PLS #plus
	| SYMBOL acco #range
	| PARPD interval PARPI #interv
	| PARD expr PARI #paranteze
	| PARPD interval PARPI AST #intervAdvanced
	| PARD expr PARI AST #parantAst
	| PARD expr PARI PLS #parantPls
	| PARD expr PARI INTR #parantMaybe
;

acco :  ACD inacco ACI ;
inacco : 
	 VIRG NUMBER #caz1
	| NUMBER VIRG #caz2
	| NUMBER VIRG NUMBER #caz3 
	| NUMBER #caz4
	;
interval : interval SYMBOL | interval NUMBER | interval SYMBOL MINUS SYMBOL | SYMBOL MINUS SYMBOL 
	| interval NUMBER MINUS NUMBER | NUMBER MINUS NUMBER | SYMBOL | NUMBER ;


PARD : '(' ;
PARI : ')' ;
PARPD : '[' ;
PARPI : ']' ;
AST : '*' ;
PLS : '+' ;
INTR : '?' ;
ACD : '{' ;
ACI : '}' ;
MINUS : '-' ;
VIRG : ',' ;
OR : '|' ;

ANYTHING : '.' ;
NUMBER : [0-9]+ ;
SYMBOL: [a-z] | [A-Z] ;            
WS : [ \t\r\n]+ -> skip ;