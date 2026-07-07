import unittest
from d3i.emitters.TypeScriptEmitter import *
from d3i.elements.Elements import *
from d3i.Engine import *


# The TypeScript emitter only generates client code for interfaces that are
# published on REST via @public_api( rest, collection = "..." ). Everything else
# (enums, value objects, composites, aggregates, services) emits nothing.
class TestEmitterTypeScript(unittest.TestCase):

    SOURCE = """
domain WebShop {
    context Orders {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto OrderDto {
                id:string
                amount:integer
            }
            query getOrder( id:string ) : OrderDto
        }
    }
}
"""

    def test_emitter_non_rest_interface_emits_nothing(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        interface OrderIF version 1 {
            query getOrder( id:string ) : string
        }
        valueobject Address {
            city:string
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = TypeScriptEmitter().Emit(session)
        self.assertEqual(0, len(result))

    def test_emitter_rest_interface_types_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(self.SOURCE))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = TypeScriptEmitter().Emit(session)
        self.assertEqual(2, len(result))

        types = next(f for f in result if f.fileName == "OrderIF_v1.ts")
        self.assertIn("export interface OrderDto {", types.content)
        self.assertIn("id:string;", types.content)
        self.assertIn("amount:number;", types.content)

    def test_emitter_rest_interface_client_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(self.SOURCE))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = TypeScriptEmitter().Emit(session)
        client = next(f for f in result if f.fileName == "OrderIF_v1.RestClient.ts")
        content = client.content
        self.assertIn("export const OrderIF = {", content)
        self.assertIn("V1: {", content)
        self.assertIn("async getOrder(id: string): Promise<OrderIF_v1.OrderDto>", content)
        self.assertIn("rest.axios.get", content)


    def test_emitter_ref_ok(self):
        # a ref is the referenced aggregate's id, emitted as a string on the wire.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        @public_api( rest, collection = "PublicApi" )
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

        result = TypeScriptEmitter().Emit(session)
        types = next(f for f in result if f.fileName == "OrderIF_v1.ts")
        self.assertIn("export interface OrderDto {", types.content)
        # a ref is the referenced aggregate's id -> string on the wire
        self.assertIn("c:string;", types.content)


if __name__ == "__main__":
    unittest.main()
