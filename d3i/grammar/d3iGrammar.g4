parser grammar d3iGrammar;
options { 
    tokenVocab=d3iLexer; 
    caseInsensitive = true;
}

d3
    : import_rule* domain* EOF
    ;

import_rule
    : DOCUMENT_LINE* 'import' qualifiedName
    ;

domain
    : directive* DOCUMENT_LINE* decorator* 'domain' IDENTIFIER '{' domain_element* '}'
    ;

    directive
        : DOCUMENT_LINE* IDENTIFIER qualifiedName
        ;
        
    domain_element
        : context
        ;
    
context
    :  DOCUMENT_LINE* decorator* 'context' IDENTIFIER '{' context_element* '}'
    ;

    context_element
        : enum
        | value_object
        | aggregate
        | view
        | repository
        | acl
        | service
        | interface
        ;

value_object
    : DOCUMENT_LINE* decorator* 'valueobject' IDENTIFIER inherits? '{' value_object_element* '}'
    ;

    value_object_element
        : value_object_member
        | enum
        | value_object
        ;
        
        value_object_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
            ;

event
    :  DOCUMENT_LINE* decorator* 'event' IDENTIFIER inherits? '{' event_element* '}'
    ;

    event_element
        : event_member
        | enum
        | value_object
        ;

    event_member
        : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
        ;
        
entity
    :  DOCUMENT_LINE* decorator* 'entity' IDENTIFIER inherits? '{' entity_element* '}'
    ;

    entity_element
        : entity_member
        | enum
        | value_object
        ;

        entity_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
            ;
        
aggregate
    :  DOCUMENT_LINE* decorator* 'aggregate' IDENTIFIER '{' aggregate_element* '}'
    ;

    aggregate_element
        : aggregate_entity
        | enum
        | value_object
        ;
        
        aggregate_entity
        :  'root'? entity
        ;

view
    :  DOCUMENT_LINE* decorator* 'view' IDENTIFIER inherits? '{' view_element* '}'
    ;

    view_element
        : view_member
        | enum
        | value_object
        ;

        view_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
            ;

repository
    : DOCUMENT_LINE* decorator* 'repository' IDENTIFIER ':' IDENTIFIER
    ;

service
    :  DOCUMENT_LINE* decorator* 'service' IDENTIFIER '{' service_element*  '}'
    ;

    service_element
        : operation
        | enum
        | value_object
        | event
        ;

interface
    :  DOCUMENT_LINE* decorator* 'interface' IDENTIFIER '{' interface_element*  '}'
    ;

    interface_element
        : operation
        | enum
        | value_object
        | event
        ;
    
operation
    : DOCUMENT_LINE* decorator* IDENTIFIER '(' (operation_param? (',' operation_param)*) ')' ((':' operation_return )? ('|' operation_return)*)
    ;

    operation_param
        : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
        ;

        operation_return
            : DOCUMENT_LINE* decorator* type
            ;


acl
    :  DOCUMENT_LINE* decorator* 'acl' IDENTIFIER '{' acl_element* '}'
    ;

    acl_element
        : enum
        | value_object
        | operation
        ;
       
type
    : primitive_type
    | reference_type
    | list_type
    | map_type
    ;
    
    primitive_type
        : 'integer'
        | 'number'
        | 'float'
        | 'date'
        | 'time'
        | 'dateTime'
        | 'string'
        | 'boolean'
        | 'bytes'
        | 'stream'
        | 'any'
        ;

    reference_type
        : qualifiedName
        | 'external' '[' STRING_LITERAL ']'
        ;

    list_type
        : 'list' '[' type ']'
        ;

    map_type
        : 'map' '[' type ',' type ']'
        ;
        
qualifiedName 
    : IDENTIFIER ('.' IDENTIFIER)* 
    ;

decorator
    : '@' IDENTIFIER
    | '@' IDENTIFIER '(' decorator_param (',' decorator_param)* ')' ;
    
    decorator_param
        : qualifiedName
        | INTEGER_CONSTANS
        | NUMBER_CONSTANS 
        | STRING_LITERAL
        ;

enum
    : DOCUMENT_LINE* decorator* 'enum' IDENTIFIER '{' enum_element? (',' enum_element)* '}'
    ;

    enum_element
        : DOCUMENT_LINE* decorator* IDENTIFIER
        ;

inherits
    : 'inherits' qualifiedName (',' qualifiedName)*
    ;