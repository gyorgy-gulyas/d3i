parser grammar d3iGrammar;
options { 
    tokenVocab=d3iLexer; 
    caseInsensitive = true;
}

d3i
    : domain* EOF
    ;

domain
    : directive* decorator* 'domain' IDENTIFIER '{' domain_element* '}'
    ;

    directive
        : IDENTIFIER qualifiedName
        ;
        
    domain_element
        : context
        | event;
    
context
    :  decorator* 'context' IDENTIFIER '{' context_element* '}'
    ;

    context_element
        : enum
        | value_object
        | entity
        | aggregate
        | repository
        | event
        | acl
        | service
        | interface
        ;

value_object
    : decorator* 'valueobject' IDENTIFIER '{' value_object_element* '}'
    ;

    value_object_element
        : value_object_member
        | enum
        | value_object
        ;
        
        value_object_member
            : decorator* IDENTIFIER ':' type
            ;

event
    :  decorator* 'event' IDENTIFIER '{' event_element* '}'
    ;

    event_element
        : event_member
        | enum
        | value_object
        ;

    event_member
        : decorator* IDENTIFIER ':' type
        ;
        
entity
    :  decorator* 'entity' IDENTIFIER '{' entity_element* '}'
    ;

    entity_element
        : entity_member
        | enum
        | value_object
        ;

        entity_member
            : decorator* IDENTIFIER ':' type
            ;
        
aggregate
    :  decorator* 'aggregate' IDENTIFIER '{' aggregate_element* '}'
    ;

    aggregate_element
        : aggregate_entity
        | enum
        | value_object
        ;
        
        aggregate_entity
        :  'root'? entity
        ;

repository
    : decorator* 'repository' IDENTIFIER ':' qualifiedName
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
    : decorator* IDENTIFIER '(' (operation_param? (',' operation_param)*) ')' ((':' operation_return )? ('|' operation_return)*)
    ;

    operation_param
        : decorator* IDENTIFIER ':' type
        ;

        operation_return
            : decorator* type
            ;


acl
    :  decorator* 'acl' IDENTIFIER '{' acl_element* '}'
    ;

    acl_element
        : enum
        | value_object
        | method
        ;
        
        method
            : decorator* IDENTIFIER '(' (method_param? (',' method_param)*) ')' ':' type
            ;

            method_param
                : decorator* IDENTIFIER ':' type
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
        ;

    reference_type
        : qualifiedName
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
    : decorator* 'enum' IDENTIFIER '{' enum_element? (',' enum_element)* '}'
    ;

    enum_element
        : decorator* IDENTIFIER
        ;