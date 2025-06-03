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
        expected = """"""
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
        expected = """"""
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
        expected = """"""
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
            private_member:external["java.util.map.HashMap<>"]
        }
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)

        expected = """"""
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
        expected = """"""
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
        expected = """"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))

    def tests_repository_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext {
        @storage( "mongo" )
        repository orders:Order
    }
}
"""))
        engine.Build(session)

        jsonEmmiter = JsonEmitter()
        result = jsonEmmiter.Emit(session)
        expected = """"""
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
        expected = """"""
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
        expected = """"""
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
        expected = """"""
        diff = jsondiff.diff(result, expected, syntax='symmetric')
        self.assertEqual(0, len(diff))


if __name__ == "__main__":
    unittest.main()
