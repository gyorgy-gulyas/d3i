import unittest
import d3i
from d3i.emitter import *
import jsondiff

class TestEmitterJson(unittest.TestCase):

    def tests_empty_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText(""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = '{\n    "$type": "d3i.d3",\n    "domains": []\n}'
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_decorators_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
@without_params
@with_params( "string", 1, 3.14, identifier.sub.sub )
domain somedomain{
}
"""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "somedomain",
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
            "directives": [],
            "contexts": [],
            "domain_events": [],
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
}
"""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [],
            "contexts": [],
            "domain_events": [],
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
using PartnerContext
namespace somedomain.subdomain.subsubdomain
                                                    
domain SomeDomain {
}
"""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [
                {
                    "$type": "d3i.directive",
                    "decorators": [],
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
                    "decorators": [],
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    @context_decorator
    context OrderContext {
    }
}
"""))
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
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
                    "enums": [],
                    "value_objects": [],
                    "entities": [],
                    "aggregates": [],
                    "repositories": [],
                    "acls": [],
                    "context_events": [],
                    "services": [],
                    "interfaces": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        root = engine.Build(session)

        jsonEmmiter = JsonEmitter()
        data = root.visit(jsonEmmiter, None)
        result = json.dumps(data, indent=4)
        expected = """{
    "$type": "d3i.d3",
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "decorators": [],
                    "enums": [
                        {
                            "$type": "d3i.enum",
                            "name": "CustomerType",
                            "enum_elements": [
                                {
                                    "$type": "d3i.enum_element",
                                    "name": "PrivatePerson",
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
                                    "name": "Company",
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
                    "entities": [],
                    "aggregates": [],
                    "repositories": [],
                    "acls": [],
                    "context_events": [],
                    "services": [],
                    "interfaces": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
            zipCode:ineger
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
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "decorators": [],
                    "enums": [],
                    "value_objects": [
                        {
                            "$type": "d3i.value_object",
                            "name": "PartnerAddress",
                            "members": [
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "country",
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
                                    },
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "Country",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 17,
                                            "column": 20
                                        }
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "address",
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
                                    },
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 19,
                                            "column": 20
                                        }
                                    }
                                },
                                {
                                    "$type": "d3i.value_object_member",
                                    "name": "zipCode",
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 20,
                                        "column": 12
                                    },
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "ineger",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 20,
                                            "column": 20
                                        }
                                    }
                                }
                            ],
                            "internal_enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "name": "Customer",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "name": "PrivatePerson",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                }
                            ],
                            "internal_value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "internal_valueobject",
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data_1",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            },
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 23
                                                }
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "data_2",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 13,
                                                "column": 16
                                            },
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.Date",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 13,
                                                    "column": 23
                                                }
                                            }
                                        }
                                    ],
                                    "internal_enums": [],
                                    "internal_value_objects": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 11,
                                        "column": 12
                                    }
                                }
                            ],
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
                    "entities": [],
                    "aggregates": [],
                    "repositories": [],
                    "acls": [],
                    "context_events": [],
                    "services": [],
                    "interfaces": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
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

    def tests_entity_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @decorator  
        @decorator_with_param( "decorator_value")
        entity Partner {
            enum PartnerType {
                Customer,    
                PrivatePerson
            }
            valueobject PartnerAddress{
                country:Country
                address:string
                zipCode:ineger
            }

            @unique
            id:string
            @max_length( 100 )
            name:string
            address:PartnerAddress
            type:PartnerType
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
    "domains": [
        {
            "$type": "d3i.domain",
            "name": "SomeDomain",
            "decorators": [],
            "directives": [],
            "contexts": [
                {
                    "$type": "d3i.context",
                    "name": "OrderContext",
                    "decorators": [],
                    "enums": [],
                    "value_objects": [],
                    "entities": [
                        {
                            "$type": "d3i.entity",
                            "name": "Partner",
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
                                            "column": 15
                                        }
                                    },
                                    "decorators": [
                                        {
                                            "$type": "d3i.decorator",
                                            "name": "unique",
                                            "params": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 17,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 17,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.entity_member",
                                    "name": "name",
                                    "type": {
                                        "$type": "d3i.primitive_type",
                                        "kind": "Kind.Primitive",
                                        "primtiveKind": "PrimtiveKind.String",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 20,
                                            "column": 17
                                        }
                                    },
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
                                                        "line": 19,
                                                        "column": 25
                                                    }
                                                }
                                            ],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 19,
                                                "column": 12
                                            }
                                        }
                                    ],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 19,
                                        "column": 12
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
                                            "line": 21,
                                            "column": 20
                                        }
                                    },
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 21,
                                        "column": 12
                                    }
                                },
                                {
                                    "$type": "d3i.entity_member",
                                    "name": "type",
                                    "type": {
                                        "$type": "d3i.reference_type",
                                        "kind": "Kind.Reference",
                                        "reference_name": "PartnerType",
                                        "location": {
                                            "fileName": "internal string",
                                            "line": 22,
                                            "column": 17
                                        }
                                    },
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 22,
                                        "column": 12
                                    }
                                }
                            ],
                            "internal_enums": [
                                {
                                    "$type": "d3i.enum",
                                    "name": "PartnerType",
                                    "enum_elements": [
                                        {
                                            "$type": "d3i.enum_element",
                                            "name": "Customer",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 8,
                                                "column": 16
                                            }
                                        },
                                        {
                                            "$type": "d3i.enum_element",
                                            "name": "PrivatePerson",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 9,
                                                "column": 16
                                            }
                                        }
                                    ],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 7,
                                        "column": 12
                                    }
                                }
                            ],
                            "internal_value_objects": [
                                {
                                    "$type": "d3i.value_object",
                                    "name": "PartnerAddress",
                                    "members": [
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "country",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 12,
                                                "column": 16
                                            },
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "Country",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 12,
                                                    "column": 24
                                                }
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "address",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 13,
                                                "column": 16
                                            },
                                            "type": {
                                                "$type": "d3i.primitive_type",
                                                "kind": "Kind.Primitive",
                                                "primtiveKind": "PrimtiveKind.String",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 13,
                                                    "column": 24
                                                }
                                            }
                                        },
                                        {
                                            "$type": "d3i.value_object_member",
                                            "name": "zipCode",
                                            "decorators": [],
                                            "location": {
                                                "fileName": "internal string",
                                                "line": 14,
                                                "column": 16
                                            },
                                            "type": {
                                                "$type": "d3i.reference_type",
                                                "kind": "Kind.Reference",
                                                "reference_name": "ineger",
                                                "location": {
                                                    "fileName": "internal string",
                                                    "line": 14,
                                                    "column": 24
                                                }
                                            }
                                        }
                                    ],
                                    "internal_enums": [],
                                    "internal_value_objects": [],
                                    "decorators": [],
                                    "location": {
                                        "fileName": "internal string",
                                        "line": 11,
                                        "column": 12
                                    }
                                }
                            ],
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
                    "aggregates": [],
                    "repositories": [],
                    "acls": [],
                    "context_events": [],
                    "services": [],
                    "interfaces": [],
                    "location": {
                        "fileName": "internal string",
                        "line": 3,
                        "column": 4
                    }
                }
            ],
            "domain_events": [],
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
