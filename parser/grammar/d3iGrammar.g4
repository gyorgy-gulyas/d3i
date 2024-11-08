parser grammar d3iGrammar;
options { 
    tokenVocab=d3iLexer; 
    caseInsensitive = true;
}

d3i
    : directive* domain* EOF
    ;

directive
    : IDENTIFIER qualifiedName
    ;

domain
    : decorator* 'domain' IDENTIFIER '{' domain_element* '}'
    ;

    domain_element
        : context
        | event;
    
context
    :  decorator* 'context' IDENTIFIER '{' context_element* '}'
    ;

    context_element
        : entity
        | enum
        | value_object
        | aggregate
        | repository
        | acl
        | event
        | service
        | interface
        ;

value_object
    : decorator* 'valueObject' IDENTIFIER '{' value_object_member* '}'
    ;

    value_object_member
        : decorator* IDENTIFIER ':' type
        | enum
        | value_object
        ;
        
event
    :  decorator* 'event' IDENTIFIER '{' event_member* '}'
    ;

    event_member
        : decorator* IDENTIFIER ':' type
        | enum
        | value_object
        ;
        
entity
    :  decorator* 'entity' IDENTIFIER '{' entity_member* '}'
    ;

    entity_member
        : decorator* IDENTIFIER ':' type
        | enum
        | value_object
        ;
        
aggregate
    :  decorator* 'aggregate' IDENTIFIER '{' aggregate_element* '}'
    ;

    aggregate_element
        :  'root'? entity
        | enum
        | value_object
        ;

repository
    : decorator* 'repository' IDENTIFIER ':' IDENTIFIER
    ;

service
    :  decorator* 'service' IDENTIFIER '{' service_element*  '}'
    ;

    service_element
        : operation
        | enum
        | value_object
        ;

interface
    :  decorator* 'interface' IDENTIFIER '{' interface_element*  '}'
    ;

    interface_element
        : operation
        | enum
        | value_object
        ;
    
operation
    : decorator* IDENTIFIER '(' operation_param? (',' operation_param)* ')' operation_return?
    ;

    operation_param
        : decorator* IDENTIFIER ':' type
        ;

    operation_return
        : ':' decorator* type ('|' decorator* type)*
        ;

acl
    :  decorator* 'acl' IDENTIFIER '{' acl_element* '}'
    ;

    acl_element
        : enum
        | value_object
        | acl_function
        ;
        
        acl_function
            : decorator* IDENTIFIER '(' acl_function_param? (',' acl_function_param)* ')' ':' type
            ;

            acl_function_param
                : decorator* IDENTIFIER ':' type
                ;
type
    : primitive_type
    | reference_type
    | container_type
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
        ;

    reference_type
        : qualifiedName
        ;

    container_type
        : 'list' '[' type ',' type ']'
        | 'map' '[' type ',' type ']'
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
    : decorator* 'enum' IDENTIFIER '{' enum_element (',' enum_element)* '}'
    ;

    enum_element
        : decorator* IDENTIFIER
        ;