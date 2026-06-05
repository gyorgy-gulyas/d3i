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
EQUAL : '=' ;

// declaration keywords
ACL : 'acl' ;
AGGREGATE : 'aggregate' ;
CONTEXT : 'context' ;
COMPOSITE : 'composite' ;
DOMAIN : 'domain' ;
ENTITY : 'entity' ;
ENUM : 'enum' ;
EVENT : 'event' ;
EVENTHANDLER : 'eventhandler' ;
IMPORT : 'import' ;
INTERFACE : 'interface' ;
REPOSITORY : 'repository' ;
SERVICE : 'service' ;
VALUEOBJECT : 'valueobject' ;
DTO : 'dto' ;
VIEW : 'view' ;

// qualifier keywords
ROOT : 'root' ;
INHERITS : 'inherits' ;
VERSION : 'version' ;
FOR : 'for' ;
PROJECTED: 'projected' ;
COMMAND : 'command' ;
QUERY : 'query' ;

// built-in types
INTEGER : 'integer' ;
NUMBER : 'number' ;
FLOAT : 'float' ;
DATE : 'date' ;
TIME : 'time' ;
DATETIME : 'dateTime' ;
STRING : 'string' ;
I18NSTRING : 'i18nstring' ;
BOOLEAN : 'boolean' ;
BYTES : 'bytes' ;
STREAM: 'stream';
ANY: 'any';
LIST : 'list' ;
MAP : 'map' ;

// constans
INTEGER_CONSTANS : [0-9]+ ;
NUMBER_CONSTANS : [0-9]+'.'[0-9]+ ;
STRING_LITERAL: '"' .*? '"';

// syntax controllers
IDENTIFIER: [a-z][a-z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
BOM : '\uFEFF' -> skip ;

DOCUMENT_LINE: '#' ~[\r\n]*;
LINE_COMMENT : '//' ~[\r\n]* -> channel(COMMENT_CHANNEL);
BLOCK_COMMENT : '/*' .*? '*/' -> channel(COMMENT_CHANNEL);
