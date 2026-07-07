import unittest
from d3i.emitters.ProtoEmitter import *
from d3i.elements.Elements import *
from d3i.Engine import *


class TestEmitterProto(unittest.TestCase):

    def test_emitter_interface_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        interface OrderIF version 1 {
            query getOrder( id:string ) : string
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = ProtoEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "OrderIF_v1.proto")
        content = result[0].content
        self.assertIn('syntax = "proto3";', content)
        self.assertIn("service OrderIF_v1 {", content)
        self.assertIn("rpc getOrder(OrderIF_v1_getOrderRequest) returns (OrderIF_v1_getOrderResponse);", content)
        self.assertIn("message OrderIF_v1_getOrderRequest {", content)
        self.assertIn("string id = 1;", content)
        self.assertIn("message OrderIF_v1_getOrderResponse {", content)
        self.assertIn("oneof result {", content)

    def test_emitter_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        composite WithAddress {
            enum AddressType {
                Home,
                Work
            }
            city:string
            zipCode:integer
            addressType:AddressType
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = ProtoEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "WithAddress.proto")
        content = result[0].content
        self.assertIn("message WithAddress {", content)
        self.assertIn("enum AddressType {", content)
        self.assertIn("string city = 1;", content)
        self.assertIn("int32 zipCode = 2;", content)
        self.assertIn("AddressType addressType = 3;", content)

    def test_emitter_dto_enum_list_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        interface OrderIF version 1 {
            enum Status {
                New,
                Done
            }
            dto OrderDto {
                id:string
                tags: list[string]
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = ProtoEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "OrderIF_v1.proto")
        content = result[0].content
        self.assertIn("enum Status {", content)
        self.assertIn("Status_New = 0;", content)
        self.assertIn("message OrderDto {", content)
        self.assertIn("string id = 1;", content)
        self.assertIn("repeated string tags = 2;", content)


    def test_emitter_ref_ok(self):
        # a ref is the referenced aggregate's id, emitted as a string on the wire.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        interface OrderIF version 1 {
            dto OrderDto {
                c: ref Customer
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = ProtoEmitter().Emit(session)
        content = result[0].content
        self.assertIn("message OrderDto {", content)
        # a ref is the referenced aggregate's id -> string on the wire
        self.assertIn("string c = 1;", content)


if __name__ == "__main__":
    unittest.main()
