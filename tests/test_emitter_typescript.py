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

    def test_emitter_dto_validation_ok(self):
        # a DTO's own validate rules generate a client-side validator function
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto CreateOrder {
                amount: number validate value > 0 AND value <= 1000
                email: string validate matches(value, "^.+@.+$")
                tags: list[string] validate len(value) <= 3
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = TypeScriptEmitter().Emit(session)
        content = next(f for f in result if f.fileName == "OrderIF_v1.ts").content

        # the shared error shape + the validator function
        self.assertIn("export interface ValidationError {", content)
        self.assertIn("export function validateCreateOrder( dto: CreateOrder ): ValidationError[] {", content)
        # readable, negated conditions with dto. access. `amount` is a `number`, which is typed
        # Decimal here - TypeScript will not compare a Decimal with a literal, so it is read as a
        # number first (which also works on the plain JSON number that really arrives).
        self.assertIn("if (Number(dto.amount) <= 0 || Number(dto.amount) > 1000)", content)
        self.assertIn('if (!new RegExp("^.+@.+$").test(dto.email))', content)
        # len on a list -> .length
        self.assertIn("if (dto.tags.length > 3)", content)
        self.assertIn('memberOfEntity: "amount"', content)
        self.assertIn("return errors;", content)
        # the entry point starts the walk with an empty path; the walk is what records the errors
        self.assertIn("validateCreateOrderInto( dto, \"\", errors );", content)
        self.assertIn("export function validateCreateOrderInto( dto: CreateOrder, pathPrefix: string, errors: ValidationError[] ): void {", content)
        self.assertIn('path: pathPrefix + "amount"', content)


class TestEmitterTypeScriptQueryParams(unittest.TestCase):

    def test_a_numeric_query_param_is_inside_the_interpolation(self):
        # a stray '$' put the name outside the template hole - `${$price.toString()}` - so the
        # generated client did not compile for any operation with a numeric query parameter
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto OrderItemDTO {
                quantity: integer
            }
            command setPrice( orderItem: OrderItemDTO, price: number ) : OrderItemDTO
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        content = next(f for f in TypeScriptEmitter().Emit(session) if f.fileName == "OrderIF_v1.RestClient.ts").content
        self.assertIn("price=${price.toString()}", content)
        self.assertNotIn("${$price", content)


class TestEmitterTypeScriptValidateCascade(unittest.TestCase):
    """
    The client side has the same job as the server: a rule declared on a dto has to run wherever
    that dto is held, and the error has to say WHERE it is so a form can mark the right control.
    """

    def __content(self, source: str, fileName: str = "OrderIF_v1.ts") -> str:
        engine = Engine()
        session = Session(Source.CreateFromText(source))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())
        return next(f for f in TypeScriptEmitter().Emit(session) if f.fileName == fileName).content

    def test_the_walk_descends_into_lists_and_numbers_the_path(self):
        content = self.__content("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto OrderItemDTO {
                quantity: integer validate value > 0
            }
            dto OrderDTO {
                items: list[OrderItemDTO]
            }
        }
    }
}
""")
        # V12: OrderDTO has no rule of its own, and it is exactly the shape the form posts
        self.assertIn("export function validateOrderDTO( dto: OrderDTO ): ValidationError[] {", content)
        self.assertIn("dto.items.forEach( (item, index) => { if (item != null) validateOrderItemDTOInto( item, `${pathPrefix}items[${index}].`, errors ); } );", content)

    def test_the_walk_descends_into_a_held_dto_and_a_map(self):
        content = self.__content("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto AddressDTO {
                country: string validate len(value) == 2
            }
            dto CustomerDTO {
                billing: AddressDTO
                addresses: map[string,AddressDTO]
            }
        }
    }
}
""")
        self.assertIn('validateAddressDTOInto( dto.billing, pathPrefix + "billing.", errors );', content)
        self.assertIn("Object.entries( dto.addresses ).forEach( ([key, value]) => { if (value != null) validateAddressDTOInto( value, `${pathPrefix}addresses[${key}].`, errors ); } );", content)
        # a map is a Record; `Dictionary` is not a TypeScript type and the branch that emitted it
        # also crashed the emitter, so no dto with a map member had ever been generated
        self.assertIn("addresses:Record<string,AddressDTO>;", content)

    def test_a_nested_dto_is_walked_through_its_namespace(self):
        # a nested dto's validator is emitted inside its parent's namespace, so only the LAST
        # segment of the name becomes the function
        content = self.__content("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto OrderDTO {
                dto CustomerDataDTO {
                    email: string validate matches(value, "@")
                }
                customer: CustomerDataDTO
            }
        }
    }
}
""")
        self.assertIn('OrderDTO.validateCustomerDataDTOInto( dto.customer, pathPrefix + "customer.", errors );', content)

    def test_a_dto_that_holds_no_rule_gets_no_validator(self):
        content = self.__content("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto PlainDTO {
                x: string
            }
            dto HolderDTO {
                p: PlainDTO
            }
        }
    }
}
""")
        self.assertNotIn("validatePlainDTO", content)
        self.assertNotIn("validateHolderDTO", content)
        self.assertNotIn("export interface ValidationError", content)

    def test_a_self_referring_dto_terminates(self):
        content = self.__content("""
domain Shop {
    context C {
        @public_api( rest, collection = "PublicApi" )
        interface OrderIF version 1 {
            dto FolderDTO {
                fname: string validate len(value) > 0
                subFolders: list[FolderDTO]
            }
        }
    }
}
""")
        self.assertIn("dto.subFolders.forEach( (item, index) => { if (item != null) validateFolderDTOInto( item, `${pathPrefix}subFolders[${index}].`, errors ); } );", content)


if __name__ == "__main__":
    unittest.main()
