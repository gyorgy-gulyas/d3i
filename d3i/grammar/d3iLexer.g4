lexer grammar d3iLexer;

channels { COMMENT_CHANNEL }

// syntax elements
DOT : '.' ;
COMMA : ',' ;
SEMI : ':' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
LBARCKET : '[' ;
RBRACKET : ']' ;
AT : '@' ;
ARROW : '=>' ;


// declaration keywords
DOMAIN : 'domain' ;
CONTEXT : 'context' ;
EVENT : 'event' ;
ENTITY : 'entity' ;
AGGREGATE : 'aggregate' ;
SERVICE : 'service' ;
INTERFACE : 'interface' ;
ACL : 'acl' ;
VALUEOBJECT : 'valueObject' ;
ENUM : 'enum' ;
REPOSITORY : 'repository' ;

// qualifier keywords
ROOT : 'root' ;
OR : 'or' ;

// built-in types
INTEGER : 'integer' ;
NUMBER : 'number' ;
FLOAT : 'float' ;
DATE : 'date' ;
TIME : 'time' ;
DATETIME : 'dateTime' ;
STRING : 'string' ;
BOOLEAN : 'boolean' ;
BYTES : 'bytes' ;
LIST : 'list' ;
MAP : 'map' ;

// constans
INTEGER_CONSTANS : [0-9]+ ;
NUMBER_CONSTANS : [0-9]+'.'[0-9]+ ;
STRING_LITERAL: '"' .*? '"';

// syntax controllers
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;



LINE_COMMENT : '//' ~[\r\n]* -> channel(COMMENT_CHANNEL);
BLOCK_COMMENT : '/*' .*? '*/' -> channel(COMMENT_CHANNEL);
