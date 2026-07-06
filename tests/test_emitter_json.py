import unittest
import jsondiff
from d3i.Engine import *
from d3i.emitters.JsonEmitter import *


class TestEmitterJson(unittest.TestCase):

    def test_empty_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": []
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_decorators_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
@without_params
@with_params( "string", 1, 3.14, identifier.sub.sub )
domain somedomain{
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "somedomain",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "without_params",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 2,
                        "column": 0
                    }
                },
                {
                    "$type": "d3i.decorator",
                    "name": "with_params",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.String",
                            "value": "string",
                            "location": {
                                "fileName": "internal string",
                                "line": 3,
                                "column": 14
                            }
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "1",
                            "location": {
                                "fileName": "internal string",
                                "line": 3,
                                "column": 24
                            }
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Number",
                            "value": "3.14",
                            "location": {
                                "fileName": "internal string",
                                "line": 3,
                                "column": 27
                            }
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.QualifiedName",
                            "value": "identifier.sub.sub",
                            "location": {
                                "fileName": "internal string",
                                "line": 3,
                                "column": 33
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 0
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_domain_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_directives_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
using PartnerContext
namespace somedomain.subdomain.subsubdomain
                                                    
domain SomeDomain {
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "using",
                    "value": [
                        "PartnerContext"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 2,
                        "column": 0
                    }
                },
                {
                    "$type": "d3i.directive",
                    "keyword": "namespace",
                    "value": [
                        "somedomain",
                        "subdomain",
                        "subsubdomain"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 0
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_context_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    @context_decorator
    context OrderContext {
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [
                        {
                            "$type": "d3i.decorator",
                            "name": "context_decorator",
                            "params": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 3,
                                "column": 4
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_enum_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @enum_decorator  
        @enum_decorator_with_param( "decorator_value")
        enum CustomerType {
            @value( 1 )
            PrivatePerson,
            @value( 2 )
            Company
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [
                        {
                            "$type": "d3i.enum",
                            "name": "CustomerType",
                            "enum_elements": [
                                {
                                    "$type": "d3i.enum_element",
                                    "value": "PrivatePerson",
                                    "document_lines": [],
                                    "decorators": [
                                        {
                                            "$type": "d3i.decorator",
                                            "name": "value",
                                            "params": [
                                                {
                                                    "$type": "d3i.decorator_param",
                                                    "kind": "Kind.Integer",
                                                    "value": "1",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 7,
                                                        "column": 20
                                                    }
                                                }
                                            ],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 7,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.enum_element",
                                    "value": "Company",
                                    "document_lines": [],
                                    "decorators": [
                                        {
                                            "$type": "d3i.decorator",
                                            "name": "value",
                                            "params": [
                                                {
                                                    "$type": "d3i.decorator_param",
                                                    "kind": "Kind.Integer",
                                                    "value": "2",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 9,
                                                        "column": 20
                                                    }
                                                }
                                            ],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 9,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "enum_decorator",
                                    "params": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "enum_decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 5,
                                                "column": 36
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_value_object_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decorator  
        @decorator_with_param( "decorator_value")
        valueObject PartnerAddress {
            enum PartnerType{
                Customer,    
                PrivatePerson
            }
            valueobject internal_valueobject{
                data_1:string    
                data_2:date
            }

            @sample_decorator( "listOfContries" )
            country:Country
            @max_length( 100 )
            address:string
            zipCode:integer
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)

        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [
                        {
                            "$type": "d3i.value_object",
                            "name": "PartnerAddress",
                            "inherits": [],
                            "members": [
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "country",
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "Country",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 17,
                                            "column": 20
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [
                                        {
                                            "$type": "d3i.decorator",
                                            "name": "sample_decorator",
                                            "params": [
                                                {
                                                    "$type": "d3i.decorator_param",
                                                    "kind": "Kind.String",
                                                    "value": "listOfContries",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 16,
                                                        "column": 31
                                                    }
                                                }
                                            ],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 16,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 16,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 19,
                                            "column": 20
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [
                                        {
                                            "$type": "d3i.decorator",
                                            "name": "max_length",
                                            "params": [
                                                {
                                                    "$type": "d3i.decorator_param",
                                                    "kind": "Kind.Integer",
                                                    "value": "100",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 18,
                                                        "column": 25
                                                    }
                                                }
                                            ],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 18,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 18,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "zipCode",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 20,
                                            "column": 20
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 20,
                                        "column": 12
                                    }
                                }
                            ],
                            "operations": [],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "Customer",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                }
                            ],
                            "value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "internal_valueobject",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data_1",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 23
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data_2",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Date",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 13,
                                                    "column": 23
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 13,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 11,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 5,
                                                "column": 31
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_aggregate_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decorator  
        @decorator_with_param( "decorator_value")
        aggregate OrderAggregate {
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject PartnerAddress{
                country:Country
                address:string
                zipCode:integer
            }

            root entity OrderHeader{
                id:string    
                address:PartnerAddress
                partnerType:PartnerType
            }
                                                    
             entity OrderItem{
                order_id:string    
                item:string
                quantity:number
            }
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [
                        {
                            "$type": "d3i.aggregate",
                            "name": "OrderAggregate",
                            "eventsourced": "False",
                            "internal_entities": [
                                {
                                    "$type": "d3i.aggregate_entity",
                                    "isRoot": "True",
                                    "entity": {
                                        "$type": "d3i.entity",
                                        "name": "OrderHeader",
                                        "inherits": [],
                                        "members": [
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "id",
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 18,
                                                        "column": 19
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 18,
                                                    "column": 16
                                                }
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "address",
                                                "type": {
                                                    "$type": "d3i.reference_type",
                                                    "kind": "Kind.Reference",
                                                    "reference_name": "PartnerAddress",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 19,
                                                        "column": 24
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 19,
                                                    "column": 16
                                                }
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "partnerType",
                                                "type": {
                                                    "$type": "d3i.reference_type",
                                                    "kind": "Kind.Reference",
                                                    "reference_name": "PartnerType",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 20,
                                                        "column": 28
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 20,
                                                    "column": 16
                                                }
                                            }
                                        ],
                                        "operations": [],
                                        "enums": [],
                                        "value_objects": [],
                                        "document_lines": [],
                                        "decorators": [],
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 17,
                                            "column": 17
                                        }
                                    },
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 17,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.aggregate_entity",
                                    "isRoot": "False",
                                    "entity": {
                                        "$type": "d3i.entity",
                                        "name": "OrderItem",
                                        "inherits": [],
                                        "members": [
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "order_id",
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 24,
                                                        "column": 25
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 24,
                                                    "column": 16
                                                }
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "item",
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 25,
                                                        "column": 21
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 25,
                                                    "column": 16
                                                }
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "quantity",
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.Number",
                                                    "location": {
                                                        "fileName": "internal string",
                                                        "line": 26,
                                                        "column": 25
                                                    }
                                                },
                                                "document_lines": [],
                                                "decorators": [],
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 26,
                                                    "column": 16
                                                }
                                            }
                                        ],
                                        "operations": [],
                                        "enums": [],
                                        "value_objects": [],
                                        "document_lines": [],
                                        "decorators": [],
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 23,
                                            "column": 13
                                        }
                                    },
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 23,
                                        "column": 13
                                    }
                                }
                            ],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "Customer",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                }
                            ],
                            "value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "PartnerAddress",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "country",
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "Country",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 24
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "address",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 13,
                                                    "column": 24
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 13,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "zipCode",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Integer",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 14,
                                                    "column": 24
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 14,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 11,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 5,
                                                "column": 31
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_view_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decorator  
        @decorator_with_param( "decorator_value")
        view OrderView {
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject PartnerAddress{
                country:Country
                address:string
                zipCode:integer
            }

            id:string    
            address:PartnerAddress
            partnerType:PartnerType
            product:string
            quantity:number
        }
    }
}
"""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [
                        {
                            "$type": "d3i.view",
                            "name": "OrderView",
                            "inherits": [],
                            "members": [],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "Customer",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 5,
                                                "column": 31
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [
                        {
                            "$type": "d3i.value_object",
                            "name": "PartnerAddress",
                            "inherits": [],
                            "members": [
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "country",
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "Country",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 12,
                                            "column": 24
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 12,
                                        "column": 16
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 13,
                                            "column": 24
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 13,
                                        "column": 16
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "zipCode",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 14,
                                            "column": 24
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 14,
                                        "column": 16
                                    }
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 11,
                                "column": 12
                            }
                        }
                    ],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        },
        {
            "$type": "d3i.domain",
            "name": null,
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "id",
                    "value": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 17,
                        "column": 12
                    }
                },
                {
                    "$type": "d3i.directive",
                    "keyword": "address",
                    "value": [
                        "PartnerAddress"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 18,
                        "column": 12
                    }
                },
                {
                    "$type": "d3i.directive",
                    "keyword": "partnerType",
                    "value": [
                        "PartnerType"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 19,
                        "column": 12
                    }
                },
                {
                    "$type": "d3i.directive",
                    "keyword": "product",
                    "value": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 20,
                        "column": 12
                    }
                },
                {
                    "$type": "d3i.directive",
                    "keyword": "quantity",
                    "value": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 21,
                        "column": 12
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 17,
                "column": 12
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_repository_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @storage( "mongo" )
        repository orders {
            query getById( id:string ) : string
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [
                        {
                            "$type": "d3i.repository",
                            "name": "orders",
                            "operations": [
                                {
                                    "$type": "d3i.operation",
                                    "name": "getById",
                                    "kind": "Kind.Query",
                                    "emits": [],
                                    "operation_params": [
                                        {
                                            "$type": "d3i.operation_param",
                                            "name": "id",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 6,
                                                    "column": 30
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 27
                                            }
                                        }
                                    ],
                                    "operation_return": {
                                        "$type": "d3i.operation_return",
                                        "type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 41
                                            }
                                        },
                                        "document_lines": [],
                                        "decorators": [],
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 6,
                                            "column": 41
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 6,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "storage",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "mongo",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 4,
                                                "column": 18
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_acl_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decoration( "value" )
        acl partnerACL{
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject PartnerData {
                address:string
                type:PartnerType
            }

            @post
            getPartnerData( @required partnerId: string ) : PartnerData
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [
                        {
                            "$type": "d3i.acl",
                            "name": "partnerACL",
                            "operations": [],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "Customer",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 7,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 6,
                                        "column": 12
                                    }
                                }
                            ],
                            "value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "PartnerData",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "address",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 11,
                                                    "column": 24
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 11,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "type",
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "PartnerType",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 21
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 10,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decoration",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 4,
                                                "column": 21
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        },
        {
            "$type": "d3i.domain",
            "name": "partnerId",
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "post",
                    "value": [
                        "getPartnerData"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 15,
                        "column": 13
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "required",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 16,
                        "column": 28
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 15,
                "column": 13
            }
        },
        {
            "$type": "d3i.domain",
            "name": null,
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "PartnerData",
                    "value": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 16,
                        "column": 60
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 16,
                "column": 60
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_service_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decoration( "value" )
        service OrderService {
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject OrderData {
                address:string
                type:PartnerType
            }
            event OrderPlaced {
                orderId:string
            }

            @post
            getOrder( @required orderId: string ) 
                : @status(200) OrderData
                | @status(404) ErrorNotFound

            @put
            closeAllOrder()
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [
                        {
                            "$type": "d3i.service",
                            "name": "OrderService",
                            "operations": [],
                            "events": [
                                {
                                    "$type": "d3i.event",
                                    "name": "OrderPlaced",
                                    "version": "None",
                                    "kind": "Kind.Domain",
                                    "inherits": [],
                                    "members": [],
                                    "enums": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 14,
                                        "column": 12
                                    }
                                }
                            ],
                            "eventhandlers": [],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "Customer",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 7,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 6,
                                        "column": 12
                                    }
                                }
                            ],
                            "value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "OrderData",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "address",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 11,
                                                    "column": 24
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 11,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "type",
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "PartnerType",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 21
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 10,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decoration",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 4,
                                                "column": 21
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        },
        {
            "$type": "d3i.domain",
            "name": "getOrder",
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "orderId",
                    "value": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 15,
                        "column": 16
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "post",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 18,
                        "column": 12
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 15,
                "column": 16
            }
        },
        {
            "$type": "d3i.domain",
            "name": "orderId",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "required",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 19,
                        "column": 22
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 19,
                "column": 22
            }
        },
        {
            "$type": "d3i.domain",
            "name": "OrderData",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "status",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "200",
                            "location": {
                                "fileName": "internal string",
                                "line": 20,
                                "column": 26
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 20,
                        "column": 18
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 20,
                "column": 18
            }
        },
        {
            "$type": "d3i.domain",
            "name": "ErrorNotFound",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "closeAllOrder",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [
                        {
                            "$type": "d3i.decorator",
                            "name": "put",
                            "params": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 23,
                                "column": 12
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 23,
                        "column": 12
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "status",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "404",
                            "location": {
                                "fileName": "internal string",
                                "line": 21,
                                "column": 26
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 21,
                        "column": 18
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 21,
                "column": 18
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_interface_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decoration( "value" )
        interface OrderInterface {
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject OrderData {
                address:string
                type:PartnerType
            }
            event OrderPlaced {
                orderId:string
            }

            @post
            getOrder( @required orderId: string ) 
                : @status(200) OrderData
                | @status(404) ErrorNotFound

            @put
            closeAllOrder()
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [
                        {
                            "$type": "d3i.interface",
                            "name": "OrderInterface",
                            "version": "None",
                            "operations": [],
                            "events": [],
                            "enums": [],
                            "dtos": [],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decoration",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "value",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 4,
                                                "column": 21
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 4,
                                        "column": 8
                                    }
                                }
                            ],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [
                        {
                            "$type": "d3i.enum",
                            "name": "PartnerType",
                            "enum_elements": [
                                {
                                    "$type": "d3i.enum_element",
                                    "value": "Customer",
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 16
                                    }
                                },
                                {
                                    "$type": "d3i.enum_element",
                                    "value": "PrivatePerson",
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 8,
                                        "column": 16
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 6,
                                "column": 12
                            }
                        }
                    ],
                    "value_objects": [
                        {
                            "$type": "d3i.value_object",
                            "name": "OrderData",
                            "inherits": [],
                            "members": [
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 11,
                                            "column": 24
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 11,
                                        "column": 16
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "type",
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "PartnerType",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 12,
                                            "column": 21
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 12,
                                        "column": 16
                                    }
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 10,
                                "column": 12
                            }
                        }
                    ],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        },
        {
            "$type": "d3i.domain",
            "name": "getOrder",
            "directives": [
                {
                    "$type": "d3i.directive",
                    "keyword": "OrderPlaced",
                    "value": [
                        "orderId"
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 14,
                        "column": 18
                    }
                }
            ],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "post",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 18,
                        "column": 12
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 14,
                "column": 18
            }
        },
        {
            "$type": "d3i.domain",
            "name": "orderId",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "required",
                    "params": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 19,
                        "column": 22
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 19,
                "column": 22
            }
        },
        {
            "$type": "d3i.domain",
            "name": "OrderData",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "status",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "200",
                            "location": {
                                "fileName": "internal string",
                                "line": 20,
                                "column": 26
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 20,
                        "column": 18
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 20,
                "column": 18
            }
        },
        {
            "$type": "d3i.domain",
            "name": "ErrorNotFound",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "closeAllOrder",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [
                        {
                            "$type": "d3i.decorator",
                            "name": "put",
                            "params": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 23,
                                "column": 12
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 23,
                        "column": 12
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "status",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "404",
                            "location": {
                                "fileName": "internal string",
                                "line": 21,
                                "column": 26
                            }
                        }
                    ],
                    "location": {
                        "fileName": "internal string",
                        "line": 21,
                        "column": 18
                    }
                }
            ],
            "location": {
                "fileName": "internal string",
                "line": 21,
                "column": 18
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))


    def tests_import_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
import some.other.module
domain SomeDomain {
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [
        {
            "$type": "d3i.import_",
            "name": "some.other.module",
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 3,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        composite Base {
            enum Kind {
                A,
                B
            }
            valueobject Inner {
                data:string
            }
            common:string
            count:integer
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "Order",
                    "entities": [],
                    "composites": [
                        {
                            "$type": "d3i.composite",
                            "name": "Base",
                            "inherits": [],
                            "members": [
                                {
                                    "$type": "d3i.composite_member",
                                    "name": "common",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 12,
                                            "column": 19
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 12,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.composite_member",
                                    "name": "count",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 13,
                                            "column": 18
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 13,
                                        "column": 12
                                    }
                                }
                            ],
                            "enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "Kind",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "A",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "B",
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 7,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 12
                                    }
                                }
                            ],
                            "value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "Inner",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 10,
                                                    "column": 21
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 10,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 9,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_dto_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface TheInterface version 1 {
            dto TheDto {
                field:string
                amount:integer
            }
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "Order",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [
                        {
                            "$type": "d3i.interface",
                            "name": "TheInterface",
                            "version": "1",
                            "operations": [],
                            "events": [],
                            "enums": [],
                            "dtos": [
                                {
                                    "$type": "d3i.dto",
                                    "name": "TheDto",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.dto_member",
                                            "name": "field",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 6,
                                                    "column": 22
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.dto_member",
                                            "name": "amount",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Integer",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 7,
                                                    "column": 23
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 7,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "enums": [],
                                    "dtos": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 12
                                    }
                                }
                            ],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_event_eventhandler_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            event TheEvent version 1 {
                data:string
            }
            eventhandler TheHandler for event TheEvent
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "Order",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [
                        {
                            "$type": "d3i.service",
                            "name": "TheService",
                            "operations": [],
                            "events": [
                                {
                                    "$type": "d3i.event",
                                    "name": "TheEvent",
                                    "version": "1",
                                    "kind": "Kind.Domain",
                                    "inherits": [],
                                    "members": [
                                        {
                                            "$type": "d3i.event_member",
                                            "name": "data",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 6,
                                                    "column": 21
                                                }
                                            },
                                            "document_lines": [],
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "enums": [],
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 12
                                    }
                                }
                            ],
                            "eventhandlers": [
                                {
                                    "$type": "d3i.eventhandler",
                                    "name": "TheHandler",
                                    "handled_event": "TheEvent",
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 8,
                                        "column": 12
                                    }
                                }
                            ],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_types_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Types {
            listField: list[string]
            mapField: map[string, integer]
            refField: some.Reference
            primitiveField: boolean
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "Order",
                    "entities": [],
                    "composites": [],
                    "aggregates": [],
                    "views": [],
                    "repositories": [],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [
                        {
                            "$type": "d3i.value_object",
                            "name": "Types",
                            "inherits": [],
                            "members": [
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "listField",
                                    "type": {
                                        "$type": "d3i.list_type",
                                        "kind": "Kind.List",
                                        "item_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 5,
                                                "column": 28
                                            }
                                        },
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 5,
                                            "column": 23
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 5,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "mapField",
                                    "type": {
                                        "$type": "d3i.map_type",
                                        "kind": "Kind.Map",
                                        "key_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 26
                                            }
                                        },
                                        "value_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.Integer",
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 6,
                                                "column": 34
                                            }
                                        },
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 6,
                                            "column": 22
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 6,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "refField",
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "some.Reference",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 7,
                                            "column": 22
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "primitiveField",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Boolean",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 8,
                                            "column": 28
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 8,
                                        "column": 12
                                    }
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": [],
                            "location": {
                                "fileName": "internal string",
                                "line": 4,
                                "column": 8
                            }
                        }
                    ],
                    "document_lines": [],
                    "decorators": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": [],
            "location": {
                "fileName": "internal string",
                "line": 2,
                "column": 0
            }
        }
    ]
}"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))


if __name__ == "__main__":
    unittest.main()
