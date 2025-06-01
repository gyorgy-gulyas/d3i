lexer grammar d3iLexer;

channels { COMMENT_CHANNEL }

options { 
    caseInsensitive = true;
}
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
PIPE : '|' ;

// declaration keywords

ACL : 'acl' ;
AGGREGATE : 'aggregate' ;
CONTEXT : 'context' ;
DOMAIN : 'domain' ;
ENTITY : 'entity' ;
ENUM : 'enum' ;
EVENT : 'event' ;
IMPORT : 'import' ;
INTERFACE : 'interface' ;
REPOSITORY : 'repository' ;
SERVICE : 'service' ;
TRAIT : 'trait' ;
VALUEOBJECT : 'valueobject' ;
VIEW : 'view' ;

// qualifier keywords
ROOT : 'root' ;
INHERITS : 'inherits' ;

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
STREAM: 'stream';
ANY: 'any';
LIST : 'list' ;
MAP : 'map' ;
EXTERNAL : 'external' ;

// constans
INTEGER_CONSTANS : [0-9]+ ;
NUMBER_CONSTANS : [0-9]+'.'[0-9]+ ;
STRING_LITERAL: '"' .*? '"';

// syntax controllers
IDENTIFIER: [a-z][a-z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;

DOCUMENT_LINE: '#' ~[\r\n]*;
LINE_COMMENT : '//' ~[\r\n]* -> channel(COMMENT_CHANNEL);
BLOCK_COMMENT : '/*' .*? '*/' -> channel(COMMENT_CHANNEL);
