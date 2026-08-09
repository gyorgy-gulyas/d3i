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
INTEGRATION : 'integration' ;
AUDIT : 'audit' ;
// An audit fact is a RECORD, not an event: nothing reacts to it, it is kept as evidence. Calling it
// an event would promise a behaviour that does not exist - see D3I-35.
RECORD : 'record' ;
// Names the internal fact a published contract is translated from.
FROM : 'from' ;
EVENTSOURCED : 'eventsourced' ;
EMITS : 'emits' ;
WORKFLOW : 'workflow' ;
STEP : 'step' ;
COMPENSATE : 'compensate' ;
// validate sublanguage keywords / operators
VALIDATE : 'validate' ;
REF : 'ref' ;
AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
IN : 'in' ;
BETWEEN : 'between' ;
LE : '<=' ;
GE : '>=' ;
NEQ : '!=' ;
EQ : '==' ;
LT : '<' ;
GT : '>' ;
DOTDOT : '..' ;
MINUS : '-' ;   // negative numeric literals in validate expressions

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

// A version, where a name is REFERENCED: `OrderIF#1`. The declaration still says the readable
// `version 1` - a different position does not have to look the same.
//
// The token carries its digits rather than being a bare '#', and that is what resolves the clash
// with the documentation line below: both start with '#', ANTLR takes the longest match, so a bare
// '#' would always lose to a comment running to the end of the line.
VERSION_REF : '#' [0-9]+ ;

// The first character after '#' may not be a digit, so `#1` cannot open a comment. That is the
// entire cost of using '#' for versions, and it is a rule a reader can hold: write `# 1. step`,
// not `#1. step`.
DOCUMENT_LINE: '#' (~[0-9\r\n] ~[\r\n]*)?;
LINE_COMMENT : '//' ~[\r\n]* -> channel(COMMENT_CHANNEL);
BLOCK_COMMENT : '/*' .*? '*/' -> channel(COMMENT_CHANNEL);
