import unittest
import json
from d3i.Engine import *
from d3i.emitters.JsonEmitter import *


class TestEmitterJson(unittest.TestCase):

    def test_empty_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": []
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

    def tests_decorators_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
@without_params
@with_params( "string", 1, 3.14, identifier.sub.sub )
domain somedomain{
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "somedomain",
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": [
                {
                    "$type": "d3i.decorator",
                    "name": "without_params",
                    "params": []
                },
                {
                    "$type": "d3i.decorator",
                    "name": "with_params",
                    "params": [
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.String",
                            "value": "string"
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Integer",
                            "value": "1"
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.Number",
                            "value": "3.14"
                        },
                        {
                            "$type": "d3i.decorator_param",
                            "kind": "Kind.QualifiedName",
                            "value": "identifier.sub.sub"
                        }
                    ]
                }
            ]
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

    def tests_domain_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                            "params": []
                        }
                    ]
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                                    "value": "1"
                                                }
                                            ]
                                        }
                                    ]
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
                                                    "value": "2"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "enum_decorator",
                                    "params": []
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "enum_decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)

        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "Country"
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
                                                    "value": "listOfContries"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String"
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
                                                    "value": "100"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "zipCode",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer"
                                    },
                                    "document_lines": [],
                                    "decorators": []
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data_2",
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Date"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": []
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "address",
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.reference_type",
                                                    "kind": "Kind.Reference",
                                                    "reference_name": "PartnerAddress"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "partnerType",
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.reference_type",
                                                    "kind": "Kind.Reference",
                                                    "reference_name": "PartnerType"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            }
                                        ],
                                        "operations": [],
                                        "enums": [],
                                        "value_objects": [],
                                        "document_lines": [],
                                        "decorators": []
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
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "item",
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.String"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            },
                                            {
                                                "$type": "d3i.entity_member",
                                                "name": "quantity",
                                                "validate": null,
                                                "type": {
                                                    "$type": "d3i.primitive_type",
                                                    "kind": "Kind.Primitive",
                                                    "primtiveKind": "PrimtiveKind.Number"
                                                },
                                                "document_lines": [],
                                                "decorators": []
                                            }
                                        ],
                                        "operations": [],
                                        "enums": [],
                                        "value_objects": [],
                                        "document_lines": [],
                                        "decorators": []
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "Country"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "address",
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "zipCode",
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Integer"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": []
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value"
                                        }
                                    ]
                                }
                            ]
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
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": [
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator",
                                    "params": []
                                },
                                {
                                    "$type": "d3i.decorator",
                                    "name": "decorator_with_param",
                                    "params": [
                                        {
                                            "$type": "d3i.decorator_param",
                                            "kind": "Kind.String",
                                            "value": "decorator_value"
                                        }
                                    ]
                                }
                            ]
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
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "Country"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "zipCode",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": []
                        }
                    ],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operation_return": {
                                        "$type": "d3i.operation_return",
                                        "type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String"
                                        },
                                        "document_lines": [],
                                        "decorators": []
                                    },
                                    "document_lines": [],
                                    "decorators": []
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
                                            "value": "mongo"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "acls": [],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "type",
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "PartnerType"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "services": [],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                    "decorators": []
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "PrivatePerson",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "type",
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "PartnerType"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                            "value": "value"
                                        }
                                    ]
                                }
                            ]
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
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.enum_element",
                                    "value": "PrivatePerson",
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": []
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
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "type",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "PartnerType"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": []
                        }
                    ],
                    "document_lines": [],
                    "decorators": []
                },
                {
                    "$type": "d3i.context",
                    "name": "getOrder",
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
                            "name": "post",
                            "params": []
                        },
                        {
                            "$type": "d3i.decorator",
                            "name": "required",
                            "params": []
                        },
                        {
                            "$type": "d3i.decorator",
                            "name": "status",
                            "params": [
                                {
                                    "$type": "d3i.decorator_param",
                                    "kind": "Kind.Integer",
                                    "value": "200"
                                }
                            ]
                        },
                        {
                            "$type": "d3i.decorator",
                            "name": "status",
                            "params": [
                                {
                                    "$type": "d3i.decorator_param",
                                    "kind": "Kind.Integer",
                                    "value": "404"
                                }
                            ]
                        },
                        {
                            "$type": "d3i.decorator",
                            "name": "put",
                            "params": []
                        }
                    ]
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))


    def tests_import_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
import some.other.module
domain SomeDomain {
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [
        {
            "$type": "d3i.import_",
            "name": "some.other.module",
            "document_lines": [],
            "decorators": []
        }
    ],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "contexts": [],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.composite_member",
                                    "name": "count",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Integer"
                                    },
                                    "document_lines": [],
                                    "decorators": []
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
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "value": "B",
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "document_lines": [],
                                    "decorators": []
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
                                            "validate": null,
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "operations": [],
                                    "enums": [],
                                    "value_objects": [],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": []
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
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        },
                                        {
                                            "$type": "d3i.dto_member",
                                            "name": "amount",
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Integer"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "enums": [],
                                    "dtos": [],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "document_lines": [],
                            "decorators": []
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                                "primtiveKind": "PrimtiveKind.String"
                                            },
                                            "document_lines": [],
                                            "decorators": []
                                        }
                                    ],
                                    "enums": [],
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "eventhandlers": [
                                {
                                    "$type": "d3i.eventhandler",
                                    "name": "TheHandler",
                                    "handled_event": "TheEvent",
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": []
                        }
                    ],
                    "interfaces": [],
                    "workflows": [],
                    "enums": [],
                    "value_objects": [],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))

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

        jsonEmmiter = JsonEmitter(withLocation=False)
        result = jsonEmmiter.Emit(session)
        expected = """{
    "$type": "d3i.d3",
    "imports": [],
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
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
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.list_type",
                                        "kind": "Kind.List",
                                        "item_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String"
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "mapField",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.map_type",
                                        "kind": "Kind.Map",
                                        "key_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.String"
                                        },
                                        "value_type": {
                                            "$type": "d3i.primitive_type",
                                            "kind": "Kind.Primitive",
                                            "primtiveKind": "PrimtiveKind.Integer"
                                        }
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "refField",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "some.Reference"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "primitiveField",
                                    "validate": null,
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.Boolean"
                                    },
                                    "document_lines": [],
                                    "decorators": []
                                }
                            ],
                            "operations": [],
                            "enums": [],
                            "value_objects": [],
                            "document_lines": [],
                            "decorators": []
                        }
                    ],
                    "document_lines": [],
                    "decorators": []
                }
            ],
            "domain_events": [],
            "document_lines": [],
            "decorators": []
        }
    ]
}"""
        self.assertEqual(json.loads(result), json.loads(expected))


    def tests_new_constructs_serialize_ok(self):
        # Covers JSON serialization of the Q1-Q5 constructs that no other snapshot
        # populates: workflow/step (+compensate), ref type, integration/audit event
        # kinds, eventsourced aggregate, populated emits, validate, and a
        # value-object query operation.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money {
            amount:number validate value >= 0
            query isPositive() : boolean
        }
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        eventsourced aggregate OrderAggregate {
            root entity OrderHeader {
                customer: ref Customer
                command place() emits Placed
            }
        }
        service TheService {
            integration event Shipped version 1 { x:number }
            audit event Logged version 1 { who:string }
        }
        workflow OrderSaga {
            step reserveStock( id:string ) compensate releaseStock
            step releaseStock( id:string )
        }
    }
}
"""))
        engine.Build(session)
        result = JsonEmitter(withLocation=False).Emit(session)

        self.assertIn('"$type": "d3i.workflow"', result)
        self.assertIn('"$type": "d3i.step"', result)
        self.assertIn('"compensate": "releaseStock"', result)
        self.assertIn('"$type": "d3i.ref_type"', result)
        self.assertIn('"kind": "Kind.Integration"', result)
        self.assertIn('"kind": "Kind.Audit"', result)
        self.assertIn('"eventsourced": "True"', result)
        self.assertIn('"Placed"', result)
        self.assertIn('"validate": "value>=0"', result)
        self.assertIn('"name": "isPositive"', result)


if __name__ == "__main__":
    unittest.main()
