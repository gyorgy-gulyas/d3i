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

if __name__ == "__main__":
    unittest.main()
