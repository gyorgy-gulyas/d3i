// validation szabályok
// gdpr támogatás
// deprecated támogatása
// customizaton point like LSD
// event logging with destination
// interface logging with destination
// historized entity vagy audited
// Valamint: mely mezők változása érdekel audit szempontból: @audited status:string

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
    : DOCUMENT_LINE* decorator* 'domain' IDENTIFIER '{' domain_element* '}'   // Q12: directive removed
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
        | composite
        | aggregate
        | view
        | repository
        | acl
        | service
        | interface
        | workflow
        ;

value_object
    : DOCUMENT_LINE* decorator* 'valueobject' IDENTIFIER inherits? '{' value_object_element* '}'
    ;

    value_object_element
        : value_object_member
        | enum
        | value_object
        | operation      // Q1: value objects may expose pure query operations
        ;
        
        value_object_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type (VALIDATE validate_expr)?   // Q4
            ;

dto
    : DOCUMENT_LINE* decorator* 'dto' IDENTIFIER '{' dto_element* '}'
    ;

    dto_element
        : dto_member
        | enum
        | dto
        ;
        
        dto_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
            ;

composite
    : DOCUMENT_LINE* decorator* 'composite' IDENTIFIER inherits? '{' composite_element* '}'
    ;

    composite_element
        : composite_member
        | enum
        | value_object
        ;
        
        composite_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type (VALIDATE validate_expr)?   // Q4
            ;

event
    :  DOCUMENT_LINE* decorator* event_kind? 'event' IDENTIFIER 'version' INTEGER_CONSTANS inherits? '{' event_element* '}'
    ;

    // Q2: three explicit event kinds. No prefix (or 'domain') = domain event.
    event_kind
        : 'domain'
        | 'integration'
        | 'audit'
        ;

    event_element
        : event_member
        | enum
        ;

    event_member
        : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
        ;
        
eventhandler
    : DOCUMENT_LINE* decorator* 'eventhandler' IDENTIFIER 'for' 'event' qualifiedName
    ;

entity
    :  DOCUMENT_LINE* decorator* 'entity' IDENTIFIER inherits? '{' entity_element* '}'
    ;

    entity_element
        : entity_member
        | enum
        | value_object
        | operation      // Q1: entities (incl. aggregate root) may have command/query operations
        ;

        entity_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type (VALIDATE validate_expr)?   // Q4
            ;
        
aggregate
    :  DOCUMENT_LINE* decorator* 'eventsourced'? 'aggregate' IDENTIFIER '{' aggregate_element* '}'   // Q2: eventsourced marker
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
    :  DOCUMENT_LINE* decorator* 'view' IDENTIFIER view_projections? inherits? '{' view_element* '}'
    ;

    view_element
        : view_member
        | enum
        ;

        view_member
            : DOCUMENT_LINE* decorator* IDENTIFIER ':' type
            ;
    
    view_projections
        : 'projected' ':' qualifiedName (',' qualifiedName)*
        ;

repository
    : DOCUMENT_LINE* decorator* 'repository' IDENTIFIER '{' operation*  '}'
    ;

service
    :  DOCUMENT_LINE* decorator* 'service' IDENTIFIER '{' service_element*  '}'
    ;

    service_element
        : operation
        | enum
        | value_object
        | event
        | eventhandler
        ;

// Q3: workflow — first-class now, Temporal implementation later.
workflow
    :  DOCUMENT_LINE* decorator* 'workflow' IDENTIFIER '{' workflow_element*  '}'
    ;

    workflow_element
        : operation        // reuse command (start) / query (status)
        | step
        | eventhandler
        | enum
        | value_object
        ;

    // A step is a (Temporal) activity: a generated function that may declare the
    // step which compensates it (declarative saga pairing).
    step
        : DOCUMENT_LINE* decorator* 'step' IDENTIFIER '(' (operation_param? (',' operation_param)*) ')' (':' operation_return )? ('compensate' IDENTIFIER)?
        ;

interface
    :  DOCUMENT_LINE* decorator* 'interface' IDENTIFIER 'version' INTEGER_CONSTANS '{' interface_element*  '}'
    ;

    interface_element
        : operation
        | enum
        | dto
        | event
        ;
   
operation
    : DOCUMENT_LINE* decorator* ('command' | 'query' ) IDENTIFIER '(' (operation_param? (',' operation_param)*) ')' (':' operation_return )? emits_clause?
    ;

    // Q2: a command may declare the events it produces (the command records; the service publishes).
    emits_clause
        : 'emits' qualifiedName (',' qualifiedName)*
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
    | ref_type
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
        | 'i18nstring'
        | 'bytes'
        | 'stream'
        | 'any'
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

    // Q5: reference to another aggregate by identity (generates a typed id in codegen).
    ref_type
        : REF qualifiedName
        ;

qualifiedName
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

// Q4: small, lintable validate expression sublanguage.
// `value` is the field itself; a bare IDENTIFIER may reference a sibling field.
validate_expr
    : validate_or
    ;

    validate_or
        : validate_and (OR validate_and)*
        ;

    validate_and
        : validate_unary (AND validate_unary)*
        ;

    validate_unary
        : NOT validate_unary
        | validate_predicate
        ;

    validate_predicate
        : validate_term (( LT | LE | GT | GE | EQ | NEQ ) validate_term)?
        | validate_term IN validate_range
        | validate_term IN validate_set
        | validate_term BETWEEN validate_term AND validate_term
        ;

    validate_range
        : validate_term DOTDOT validate_term
        ;

    validate_set
        : '{' validate_term (',' validate_term)* '}'
        ;

    validate_term
        : IDENTIFIER '(' (validate_term (',' validate_term)*)? ')'   // function call: len(...), matches(...)
        | IDENTIFIER                                                 // 'value' or a sibling field
        | INTEGER_CONSTANS
        | NUMBER_CONSTANS
        | STRING_LITERAL
        | '(' validate_expr ')'
        ;

decorator
    : '@' IDENTIFIER
    | '@' IDENTIFIER '(' decorator_param (',' decorator_param)* ')' ;
    
    decorator_param
        : IDENTIFIER '=' ( qualifiedName | INTEGER_CONSTANS | NUMBER_CONSTANS | STRING_LITERAL )   // named:      name = value
        | qualifiedName                                                                            // positional: identifier / dotted name
        | INTEGER_CONSTANS                                                                          // positional: integer
        | NUMBER_CONSTANS                                                                           // positional: number
        | STRING_LITERAL                                                                            // positional: string
        ;

enum
    : DOCUMENT_LINE* decorator* 'enum' IDENTIFIER '{' enum_element? (',' enum_element)* ','? '}'
    ;

    enum_element
        : DOCUMENT_LINE* decorator* IDENTIFIER
        ;

inherits
    : 'inherits' qualifiedName (',' qualifiedName)*
    ;