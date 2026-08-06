import unittest
from tests.dotnet_code_helper import *
from d3i.elements.Elements import *
from d3i.Engine import *


class TestEmitterDotnetDefault(unittest.TestCase):

    def setUp(self):
        #dotnet_code_helper.init_roslyn()
        pass

    def test_emitter_enum_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context CustomerContext {
        enum CustomerType{
            PrivatePerson,
            Company
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{
    enum CustomerType
    {
        PrivatePerson,
        Company,
    }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[0].fileName, "CustomerType.cs")
        

    def test_emitter_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context CustomerContext {
        composite WithAddress {
            city:string
            street:string
            country:string
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext{

        public interface IWithAddress
        {
                public string city { get; set; }
                public string street { get; set; }
                public string country { get; set; }
                public int zipCode { get; set; }
        }
}
"""
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IWithAddress.cs")
        print(result[0].content)

    def test_emitter_valueobject_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context CustomerContext {
        valueobject Address {
            city:string
            street:string
            country:string
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext{

        public class Address
        {
                public string city { get; set; }
                public string street { get; set; }
                public string country { get; set; }
                public int zipCode { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[0].fileName, "Address.cs")
        print(result[0].content)

    def test_emitter_valueobject_inheritance_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        composite WithAddress {
            city:string
            street:string
            country:string
            zipCode:integer
        }

        composite WithTypedAddress inherits WithAddress {
            enum AddressTypes {
                Headquarter,
                Site                                   
            }
            addressType:AddressTypes
        }

        valueobject PartnerAddress inherits WithTypedAddress {
            PartnerCode:string
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{
        public class PartnerAddress : ITypedWithAddress
        {
            #region IWithAddress
            public string city { get; set; }
            public string street { get; set; }
            public string country { get; set; }
            public int zipCode { get; set; }
            #endregion IWithAddress

            #region ITypedWithAddress
            enum AddressTypes
            {
                Headquarter,
                Site,                                   
            } 
            public AddressTypes addressType { get; set; }
            #endregion ITypedWithAddress

            public string PartnerCode { get; set; }
        }
}
"""
        self.assertEqual(3, len(result))
        self.assertEqual(result[0].fileName, "PartnerAddress.cs")
        print(result[0].content)

    def test_emitter_valueobject_inheritance_base_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        valueobject Address {
            city:string
            street:string
            country:string
            zipCode:integer
        }

        valueobject PartnerAddress inherits Address {
            PartnerCode:string
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext{

        public class PartnerAddress : Address
        {
            public string PartnerCode { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[1].fileName, "PartnerAddress.cs")
        print(result[1].content)

    def test_emitter_entity_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        aggregate CustomerAggregate {
            @decorator_entity
            entity Customer {
                @required
                name:string
                address:string
            }
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;
using PolyPersist.Net;
using PolyPersist.Net.Core;

namespace context_1.CustomerAggregate.somedomain
{

        public partial class Customer : Entity
        {
                public string name { get; set; }
                public string address { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[0].fileName, "Customer.cs")
        print(result[0].content)

    def test_emitter_entity_inheritance_base_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {

       aggregate CustomerAggregate {
            entity Partner {
                @required
                name:string
                address:string
            }
                                                
            @decorator_entity
            entity Customer inherits Partner {
                SelligPriceCategory:integer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;
using PolyPersist.Net;
using PolyPersist.Net.Core;

namespace somedomain.CustomerAggregate.context_1
{

        public partial class Customer : Partner
        {
            public int SelligPriceCategory { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[1].fileName, "Customer.cs")
        print(result[1].content)

    def test_emitter_entity_inheritance_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        composite Validable {
            isValid:string
        }

        aggregate CustomerAggregate {
            entity Partner inherits Validable {
                PartnerCode:string
            }
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{
        public class Partner : IValidable
        {
            #region IValidable
            public bool isValid { get; set; }
            #endregion IValidable

            public string PartnerCode { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[1].fileName, "Partner.cs")
        print(result[1].content)

    def test_emitter_view_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        view OrderView {
            @required
            customerName:string
            orderDate:date
            orderId:string
            orderedQuantity:number
            orderedItemId:string
            orderedItemName:string
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;
using PolyPersist.Net;
using PolyPersist.Net.Core;

namespace context_1.CustomerAggregate.somedomain
{
        public partial class OrderView : Entity
        {
                public string customerName { get; set; }
                public DateOnly orderDate { get; set; }
                public string orderId { get; set; }
                public decimal orderedQuantity { get; set; }
                public string orderedItemId { get; set; }
                public string orderedItemName { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[0].fileName, "OrderView.cs")
        print(result[0].content)

    def test_emitter_view_inheritance_base_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {

        view BaseView {
            @required
            customerName:string
            orderDate:date
            orderId:string
            orderedQuantity:number
        }
        view OrderItemView inherits BaseView {
            orderedItemId:string
            orderedItemName:string
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;
using PolyPersist.Net;
using PolyPersist.Net.Core;

namespace somedomain.CustomerAggregate.context_1
{
    public partial class OrderItemView : BaseView
    {
        public string orderedItemId { get; set; }
        public string orderedItemName { get; set; }
    }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[1].fileName, "OrderItemView.cs")
        print(result[1].content)

    def test_emitter_view_inheritance_composite_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        composite XmlSerializable {
            xmlValue:string
        }

        view OrderView inherits XmlSerializable {
            @required
            customerName:string
            orderDate:date
            orderId:string
            orderedQuantity:number
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{
    public partial class OrderView : Entity, IXmlSerializable
    {
        #region IXmlSerializable
        public string xmlValue { get; set; }
        #endregion IXmlSerializable

        public string customerName { get; set; }
        public DateOnly orderDate { get; set; }
        public string orderId { get; set; }
        public decimal orderedQuantity { get; set; }
    }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[1].fileName, "OrderView.cs")
        print(result[1].content)


    def test_emitter_aggregate_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        aggregate CustomerAggregate {
            root entity Customer {
                @id
                id:string
                name:string
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "Customer.cs")
        content = result[0].content
        self.assertIn("namespace WebShop.Orders.CustomerAggregate", content)
        self.assertIn("public partial class Customer : IEquatable<Customer>", content)
        self.assertIn("public string name { get; set; }", content)

    def test_emitter_service_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        service OrderService {
            command placeOrder( customerId:string ) : boolean
            query getOrder( id:string ) : string
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderService.cs")
        content = result[0].content
        self.assertIn("using ServiceKit.Net;", content)
        self.assertIn("public partial interface IOrderService", content)
        self.assertIn("Task<Response<bool>> placeOrder(CallingContext ctx, string customerId)", content)
        self.assertIn("Task<Response<string>> getOrder(CallingContext ctx, string id)", content)

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

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderIF_v1.cs")
        content = result[0].content
        self.assertIn("public partial interface IOrderIF_v1", content)
        self.assertIn("Task<Response<string>> getOrder(CallingContext ctx, string id)", content)

    def test_emitter_acl_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        acl OrderACL {
            query getData( id:string ) : string
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderACL.cs")
        content = result[0].content
        self.assertIn("public partial interface IOrderACL", content)
        self.assertIn("Task<Response<string>> getData(CallingContext ctx, string id)", content)

    def test_emitter_repository_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        repository OrderRepository {
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderRepository.cs")
        self.assertIn("public partial interface IOrderRepository", result[0].content)

    def test_emitter_dto_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        interface OrderIF version 1 {
            dto OrderDto {
                field:string
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderIF_v1.cs")
        content = result[0].content
        self.assertIn("public partial interface IOrderIF_v1", content)
        self.assertIn("public partial class OrderDto : IEquatable<OrderDto>", content)
        self.assertIn("public string field { get; set; }", content)

    def test_emitter_event_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        service OrderService {
            event OrderPlaced version 1 {
                orderId:string
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "IOrderService.cs")
        content = result[0].content
        self.assertIn("public partial class OrderPlaced_v1 : IEquatable<OrderPlaced_v1>", content)
        self.assertIn("public string orderId { get; set; }", content)

    def test_emitter_types_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        valueobject Types {
            listField: list[string]
            mapField: map[string, integer]
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        self.assertEqual(result[0].fileName, "Types.cs")
        content = result[0].content
        self.assertIn("public partial class Types : IEquatable<Types>", content)
        self.assertIn("public List<string> listField { get; set; }", content)
        self.assertIn("public Dictionary<string,int> mapField { get; set; }", content)


    def test_emitter_ref_ok(self):
        # a ref to another aggregate becomes a typed id: EntityId<X> from
        # PolyPersist.Net.Core (EntityId<Customer> != EntityId<Order>).
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        aggregate Order {
            root entity OrderHeader {
                customer: ref Customer
            }
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        header = next(f for f in result if f.fileName == "OrderHeader.cs")
        self.assertIn("using PolyPersist.Net.Core;", header.content)
        # ref targets the aggregate's ROOT entity (CustomerRoot), not the aggregate name
        self.assertIn("public EntityId<WebShop.Orders.Customer.CustomerRoot> customer { get; set; }", header.content)

    def test_emitter_optional_nullable_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        valueobject Contact {
            email:string
            @optional
            phone:string
            @optional
            age:integer
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        content = result[0].content
        # unmarked = required (non-nullable); @optional -> nullable
        self.assertIn("public string email { get; set; }", content)
        self.assertIn("public string? phone { get; set; }", content)
        self.assertIn("public int? age { get; set; }", content)

    def test_emitter_deprecated_gdpr_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        @deprecated( "use NewAddress, since 2.3" )
        valueobject Address {
            city:string
            @deprecated( "use zip" )
            zipCode:integer
            @gdpr
            email:string
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        self.assertEqual(1, len(result))
        content = result[0].content
        # @deprecated -> [Obsolete] on both the class and the field
        self.assertIn('[Obsolete("use NewAddress, since 2.3")]', content)
        self.assertIn('[Obsolete("use zip")]', content)
        # @gdpr is a marker only: it must not emit any attribute (exactly two [Obsolete]s)
        self.assertEqual(content.count("[Obsolete"), 2)

    def test_emitter_validate_ok(self):
        # a `validate` rule generates PolyPersist.IValidable.Validate with a guard per
        # rule; inlined composite rules and @optional null-guards are handled too.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain Shop {
    context C {
        composite WithZip {
            zipCode: string validate len(value) == 4
        }
        valueobject Order inherits WithZip {
            amount: number validate value > 0 AND value <= 1000
            @optional
            note: string validate len(value) <= 50
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        content = next(f for f in result if f.fileName == "Order.cs").content

        self.assertIn("using PolyPersist;", content)
        self.assertIn("using PolyPersist.Net.Common;", content)
        self.assertIn(", IValidable", content)
        self.assertIn("public virtual bool Validate( IList<IValidationError> errors )", content)
        # own rule: readable, negation folded into the operators, bare field names
        self.assertIn("if (amount <= 0 || amount > 1000)", content)
        # inlined composite rule (zipCode) lands in Order.Validate; string len -> .Length
        self.assertIn('MemberOfEntity = "zipCode"', content)
        self.assertIn("if ((zipCode?.Length ?? 0) != 4)", content)
        # @optional member is guarded by a null-check
        self.assertIn("note != null && (", content)

    def test_emitter_validate_base_class_chain(self):
        # a value object inheriting a validating base overrides the WALK and chains base into it;
        # `Validate` stays declared once, on the topmost validating class
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject Base {
            a: number validate value > 0
        }
        valueobject Derived inherits Base {
            b: number validate value > 0
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        base = next(f for f in result if f.fileName == "Base.cs").content
        derived = next(f for f in result if f.fileName == "Derived.cs").content

        # base: fresh IValidable, declares both the entry point and the walk
        self.assertIn("public virtual bool Validate( IList<IValidationError> errors )", base)
        self.assertIn("public virtual void ValidateInto( IList<IValidationError> errors, string pathPrefix )", base)
        # derived: overrides the WALK and chains base into it
        self.assertIn("public override void ValidateInto( IList<IValidationError> errors, string pathPrefix )", derived)
        self.assertIn("base.ValidateInto( errors, pathPrefix );", derived)
        self.assertIn("if (b <= 0)", derived)
        # the entry point is declared ONCE, on the topmost validating class
        self.assertNotIn("bool Validate(", derived)
        # IValidable is inherited (not re-listed)
        self.assertNotIn("IValidable", derived.split("class Derived")[1].split("{")[0])

    def test_emitter_validate_collection_len_count(self):
        # len() on a list/map maps to .Count (not .Length)
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain Shop {
    context C {
        valueobject Cart {
            items: list[string] validate len(value) <= 3
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        content = next(f for f in result if f.fileName == "Cart.cs").content
        self.assertIn("if ((items?.Count ?? 0) > 3)", content)

    def test_emitter_validate_negative_bounds(self):
        # negative numeric literals work in validate rules (ranges/comparisons)
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject Reading {
            temp: number validate value >= -273
            lon: number validate value IN -180..180
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        content = next(f for f in result if f.fileName == "Reading.cs").content
        self.assertIn("if (temp < -273)", content)
        self.assertIn("if (lon < -180 || lon > 180)", content)


class TestEmitterDotnetValidateCascade(unittest.TestCase):
    """
    A value object is self-validating, so a rule on it has to run wherever it is held. The bug this
    guards against was silent: OrderItem.Validate() was generated perfectly and never called, so an
    order with a zero-quantity item came back 200. The walk also has to say WHERE the failure is -
    two bad rows used to produce two identical errors, which a form cannot bind to anything.
    """

    def __emit(self, source: str):
        engine = Engine()
        session = Session(Source.CreateFromText(source))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())
        return {f.fileName: f.content for f in DotnetEmitter().Emit(session)}

    def test_validate_walks_into_a_held_value_object(self):
        files = self.__emit("""
domain Shop {
    context C {
        valueobject Address {
            country: string validate len(value) == 2
        }
        valueobject Customer {
            billing: Address
        }
    }
}
""")
        customer = files["Customer.cs"]
        # Customer declares no rule of its own, yet it validates - V12: it is the only entry point
        # the caller has, and without it the rule on the address never runs.
        self.assertIn(", IValidable", customer)
        self.assertIn("public virtual bool Validate( IList<IValidationError> errors )", customer)
        self.assertIn("ValidateInto( errors, string.Empty );", customer)
        self.assertIn('billing?.ValidateInto( errors, pathPrefix + "billing." );', customer)

    def test_validate_walks_into_a_list_and_numbers_the_path(self):
        files = self.__emit("""
domain Shop {
    context C {
        valueobject OrderItem {
            quantity: integer validate value > 0
        }
        valueobject Order {
            items: list[OrderItem]
        }
    }
}
""")
        order = files["Order.cs"]
        self.assertIn("for (int index = 0; index < items.Count; index++)", order)
        self.assertIn('items[index]?.ValidateInto( errors, $"{pathPrefix}items[{index}]." );', order)
        # a null list is not a crash
        self.assertIn("if (items != null)", order)

    def test_validate_walks_into_a_map_and_keys_the_path(self):
        files = self.__emit("""
domain Shop {
    context C {
        valueobject Price {
            amount: number validate value > 0
        }
        valueobject Catalog {
            prices: map[string,Price]
        }
    }
}
""")
        catalog = files["Catalog.cs"]
        self.assertIn("foreach (var pair in prices)", catalog)
        self.assertIn('pair.Value?.ValidateInto( errors, $"{pathPrefix}prices[{pair.Key}]." );', catalog)

    def test_an_own_rule_records_its_path(self):
        files = self.__emit("""
domain Shop {
    context C {
        valueobject Order {
            total: number validate value >= 0
        }
    }
}
""")
        self.assertIn('Path = pathPrefix + "total"', files["Order.cs"])

    def test_nothing_is_generated_for_a_class_that_holds_no_rule(self):
        # V2: the walk is decided at generation time, so a class of plain fields pays nothing
        files = self.__emit("""
domain Shop {
    context C {
        valueobject Plain {
            x: string
        }
        valueobject Holder {
            p: Plain
        }
    }
}
""")
        self.assertNotIn("ValidateInto", files["Plain.cs"])
        self.assertNotIn("ValidateInto", files["Holder.cs"])
        self.assertNotIn("IValidable", files["Holder.cs"])

    def test_a_self_referring_value_object_terminates(self):
        # V3: the TYPE graph is walked with a seen set, so a folder holding folders still emits
        files = self.__emit("""
domain D {
    context C {
        valueobject Folder {
            fname: string validate len(value) > 0
            subFolders: list[Folder]
        }
    }
}
""")
        folder = files["Folder.cs"]
        self.assertIn('subFolders[index]?.ValidateInto( errors, $"{pathPrefix}subFolders[{index}]." );', folder)

    def test_a_dto_holding_a_validating_dto_gets_an_entry_point(self):
        # V12: the shape the GUI posts is exactly the one that used to have no validator
        files = self.__emit("""
domain Shop {
    context C {
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
        content = files["IOrderIF_v1.cs"]
        self.assertIn("public virtual bool Validate( IList<IValidationError> errors )", content)
        self.assertIn('items[index]?.ValidateInto( errors, $"{pathPrefix}items[{index}]." );', content)

    def test_a_ref_is_not_walked_into(self):
        # `ref X` is an identity, not a nested object - there is nothing to validate on an id
        files = self.__emit("""
domain Shop {
    context C {
        aggregate Customer {
            root entity Account {
                id: string
                name: string validate len(value) > 0
            }
        }
        aggregate Order {
            root entity OrderHeader {
                customer: ref Customer
            }
        }
    }
}
""")
        self.assertNotIn("ValidateInto", files["OrderHeader.cs"])


class TestEmitterDotnetPrimitiveConversions(unittest.TestCase):
    """
    Clone and the gRPC mapping are built from EXPRESSIONS that the caller embeds in an assignment
    or a lambda. A branch that returned a statement, or nothing at all, produced C# that does not
    compile - and a branch copied from the outbound direction produced C# that compiles but loses
    the value on the way home.
    """

    # 'stream' is only legal in an operation signature, so it is exercised as a command parameter
    # rather than as a DTO member.
    _MODEL = """
domain WebShop {
    context Sales {
        @public_api( grpc )
        interface SalesIF version 1 {
            dto PayloadDTO {
                bag:any
                amount:integer
                ratio:float
                at:dateTime
                when:time
                raw:bytes
                text:string
            }
            command Pay( payload:PayloadDTO, blob:stream ) : PayloadDTO
        }
    }
}
"""

    def _emit(self):
        engine = Engine()
        session = Session(Source.CreateFromText(self._MODEL))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())
        result = DotnetEmitter().Emit(session)
        return next(f for f in result if f.fileName == "ISalesIF_v1.cs").content

    def test_grpc_mapping_has_no_stray_statement_terminator(self):
        content = self._emit()
        # integer/float used to come back as "x;\n", so the caller emitted "= x;\n;".
        self.assertNotIn(";\n\t\t\t\t;", content)
        self.assertNotIn("= ;", content)
        self.assertIn("result.Amount = @this.amount;", content)
        self.assertIn("result.amount = @from.Amount;", content)
        self.assertIn("result.Ratio = @this.ratio;", content)
        self.assertIn("result.ratio = @from.Ratio;", content)

    def test_grpc_mapping_converts_back_and_not_forward_again(self):
        content = self._emit()
        # outbound
        self.assertIn('result.When = @this.when.ToString("HH:mm:ss");', content)
        self.assertIn("result.Raw = @this.raw != null ? Google.Protobuf.ByteString.CopyFrom(@this.raw) : Google.Protobuf.ByteString.Empty;", content)
        self.assertIn("result.Bag = JsonSerializer.Serialize(@this.bag);", content)
        # inbound - each of these used to be a copy of the outbound expression
        self.assertIn("result.when = TimeOnly.Parse(@from.When, CultureInfo.InvariantCulture);", content)
        self.assertIn("result.raw = @from.Raw.ToByteArray();", content)
        self.assertIn("result.bag = JsonSerializer.Deserialize<object>(@from.Bag);", content)

    def test_grpc_datetime_is_made_utc_before_conversion(self):
        # Timestamp.FromDateTime throws on anything that is not DateTimeKind.Utc.
        content = self._emit()
        self.assertIn("Timestamp.FromDateTime(@this.at.ToUniversalTime());", content)

    def test_grpc_mapping_brings_the_usings_it_needs(self):
        content = self._emit()
        for using in ("using System.Globalization;", "using System.Text.Json;"):
            self.assertIn(using, content)

    def test_clone_copies_the_handle_for_any(self):
        # 'any' is object: there is no generic way to duplicate an arbitrary instance, so the clone
        # carries the reference over. What matters is that it is a single valid expression - this
        # branch used to emit nothing at all, producing "clone.bag = ;".
        content = self._emit()
        self.assertIn("clone.bag = bag;", content)
        self.assertNotIn("= ;", content)
        self.assertNotIn("temptemp", content)


class TestEmitterDotnetWorkflow(unittest.TestCase):
    # A workflow declares a SET of steps, not an order, so the body cannot be generated. What the
    # emitter produces is the saga guarantee: every step that declares a compensation records it,
    # and a failure rolls the lot back in reverse order.

    SOURCE = """
domain WebShop {
    context Orders {
        valueobject Money {
            amount:number
            currency:string
        }

        service Payments {
            event OrderPaid version 1 {
                orderId:string
            }
        }

        @retry( 3 )
        @timeout( "2m" )
        workflow FulfilOrder {
            @start
            command place( orderId:string, total:Money ) : string

            command cancel( reason:string )

            command approve( by:string ) : boolean

            query status( orderId:string ) : string

            eventhandler onPaid for event Payments.OrderPaid.v1

            step reserveStock( orderId:string, sku:string ) compensate releaseStock

            step releaseStock( orderId:string, sku:string )

            @retry( 1 )
            @timeout( "30s" )
            step chargeCard( orderId:string, total:Money ) : string compensate refundCard

            step refundCard( orderId:string, chargeId:string )

            step sendReceipt( orderId:string )

            enum Channel {
                Web,
                Store
            }
        }
    }
}
"""

    def __emit(self, source: str = None):
        engine = Engine()
        session = Session(Source.CreateFromText(source if source != None else self.SOURCE))
        engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        result = DotnetEmitter().Emit(session)
        return {code.fileName: code.content for code in result}

    def __file(self, name: str, source: str = None) -> str:
        files = self.__emit(source)
        self.assertIn(name, files)
        return files[name]

    def test_workflow_emits_four_files(self):
        files = self.__emit()
        for name in ("IFulfilOrderActivities.cs", "FulfilOrderWorkflow.cs", "FulfilOrderDefaults.cs", "FulfilOrderRegistration.cs"):
            self.assertIn(name, files)

    def test_every_step_becomes_an_activity(self):
        content = self.__file("IFulfilOrderActivities.cs")
        self.assertIn("public partial interface IFulfilOrderActivities", content)
        self.assertIn("[Activity]\n\t\tTask reserveStock(string orderId, string sku);", content)
        self.assertIn("[Activity]\n\t\tTask<string> chargeCard(string orderId, Money total);", content)
        self.assertIn("using Temporalio.Activities;", content)

    def test_the_start_command_is_the_workflow_run(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("[Workflow]\n\tpublic partial class FulfilOrderWorkflow", content)
        self.assertIn("[WorkflowRun]\n\t\tpublic async Task<string> place(string orderId, Money total)", content)

    def test_the_run_hands_the_failure_to_the_saga(self):
        # Without handing the failure over, a failing compensation would hide the real cause.
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("catch (Exception failure)", content)
        self.assertIn("await _saga.CompensateAsync(failure);", content)
        self.assertIn("throw;", content)

    def test_a_command_is_a_signal_without_a_return_and_an_update_with_one(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("[WorkflowSignal]\n\t\tpublic Task cancel(string reason) => OnCancel(reason);", content)
        self.assertIn("[WorkflowUpdate]\n\t\tpublic Task<bool> approve(string by) => OnApprove(by);", content)

    def test_a_query_is_synchronous(self):
        # A Temporal query may not await anything, so it is not a Task
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("[WorkflowQuery]\n\t\tpublic string status(string orderId) => OnStatus(orderId);", content)

    def test_an_eventhandler_is_a_signal(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("[WorkflowSignal]\n\t\tpublic Task onPaid(IPayments.OrderPaid_v1 @event) => HandleOnPaid(@event);", content)

    def test_the_developer_half_is_declared_but_not_written(self):
        # partial declarations with a return value MUST be implemented, so the compiler is what
        # tells the developer which bodies are missing
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("private partial Task<string> OnPlace(string orderId, Money total);", content)
        self.assertIn("private partial Task OnCancel(string reason);", content)
        self.assertIn("private partial Task<bool> OnApprove(string by);", content)
        self.assertIn("private partial string OnStatus(string orderId);", content)
        self.assertIn("private partial Task HandleOnPaid(IPayments.OrderPaid_v1 @event);", content)
        # the run body itself is never generated
        self.assertNotIn("private partial Task<string> OnPlace(string orderId, Money total)\n", content)

    def test_a_step_with_a_compensation_records_it(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("_saga.Push(nameof(reserveStock), () => Workflow.ExecuteActivityAsync(", content)
        self.assertIn("(IFulfilOrderActivities activities) => activities.releaseStock(orderId, sku),", content)

    def test_a_step_without_a_compensation_records_nothing(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        facade = content.split("public sealed partial class FulfilOrderSteps")[1]
        send_receipt = facade.split("public Task sendReceipt(string orderId)")[1]
        self.assertNotIn("_saga.Push", send_receipt)

    def test_the_compensation_arguments_are_bound_by_name_and_from_the_return(self):
        # refundCard( orderId, chargeId ): orderId comes from the forward parameter of the same name,
        # chargeId from what chargeCard returned
        content = self.__file("FulfilOrderWorkflow.cs")
        self.assertIn("var result = await Workflow.ExecuteActivityAsync(", content)
        self.assertIn("(IFulfilOrderActivities activities) => activities.refundCard(orderId, result),", content)
        self.assertIn("return result;", content)

    def test_a_step_decorator_overrides_the_workflow_default(self):
        content = self.__file("FulfilOrderDefaults.cs")
        self.assertIn('case "reserveStock":\n\t\t\t\t\toptions.ScheduleToCloseTimeout = TimeSpan.FromSeconds(120);', content)
        self.assertIn("options.RetryPolicy = new RetryPolicy { MaximumAttempts = 3 };", content)
        self.assertIn('case "chargeCard":\n\t\t\t\t\toptions.ScheduleToCloseTimeout = TimeSpan.FromSeconds(30);', content)
        self.assertIn("options.RetryPolicy = new RetryPolicy { MaximumAttempts = 1 };", content)

    def test_the_single_attempt_ceiling_stays_out_of_the_model(self):
        # @timeout is the whole business budget (ScheduleToClose); the ceiling of one attempt is
        # technical, so it is a generated default the developer can move
        content = self.__file("FulfilOrderDefaults.cs")
        self.assertIn("public static TimeSpan DefaultStartToCloseTimeout { get; set; } = TimeSpan.FromMinutes(1);", content)
        self.assertIn("StartToCloseTimeout = DefaultStartToCloseTimeout,", content)
        self.assertIn("static partial void Customize(string stepName, ActivityOptions options);", content)

    def test_durations_are_converted(self):
        source = self.SOURCE.replace('@timeout( "30s" )', '@timeout( "1h30m" )').replace('@timeout( "2m" )', '@timeout( "500ms" )')
        content = self.__file("FulfilOrderDefaults.cs", source)
        self.assertIn("TimeSpan.FromSeconds(5400)", content)
        self.assertIn("TimeSpan.FromMilliseconds(500)", content)

    def test_the_task_queue_is_derived_per_workflow(self):
        content = self.__file("FulfilOrderRegistration.cs")
        self.assertIn('public const string TaskQueue = "Orders.FulfilOrder";', content)
        self.assertIn("return registry.Register<FulfilOrderWorkflow>(taskQueue, typeof(IFulfilOrderActivities));", content)

    def test_types_declared_in_the_workflow_land_inside_the_class(self):
        content = self.__file("FulfilOrderWorkflow.cs")
        workflow_class = content.split("public partial class FulfilOrderWorkflow")[1].split("public sealed partial class")[0]
        self.assertIn("public enum Channel", workflow_class)

    SOURCE_WITHOUT_STEPS = """
domain WebShop {
    context Orders {
        workflow Approval {
            command start( orderId:string )
        }
    }
}
"""

    def test_a_workflow_without_steps_needs_no_activities(self):
        files = self.__emit(self.SOURCE_WITHOUT_STEPS)
        self.assertNotIn("IApprovalActivities.cs", files)
        self.assertNotIn("ApprovalDefaults.cs", files)
        self.assertIn("ApprovalWorkflow.cs", files)
        self.assertIn("ApprovalRegistration.cs", files)
        self.assertNotIn("public sealed partial class ApprovalSteps", files["ApprovalWorkflow.cs"])
        self.assertIn("return registry.Register<ApprovalWorkflow>(taskQueue);", files["ApprovalRegistration.cs"])

    def test_the_only_command_is_the_entry_point_without_a_decorator(self):
        files = self.__emit(self.SOURCE_WITHOUT_STEPS)
        self.assertIn("[WorkflowRun]\n\t\tpublic async Task start(string orderId)", files["ApprovalWorkflow.cs"])


class TestEmitterDotnetRefClone(unittest.TestCase):
    def test_a_ref_member_is_copied_not_cloned(self):
        # 'ref X' becomes EntityId<X>, a readonly record struct over a string. It is a VALUE, so the
        # assignment already copies it - and '?.Clone()' does not even compile on a struct, which is
        # what the reference branch used to emit for it.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain WebShop {
    context Orders {
        aggregate Customer {
            root entity CustomerAccount {
                name:string
            }
        }
        aggregate Order {
            root entity OrderHeader {
                customer:ref Customer
            }
        }
    }
}
"""))
        engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasDiagnostic())

        files = {code.fileName: code.content for code in DotnetEmitter().Emit(session)}
        content = files["OrderHeader.cs"]
        self.assertIn("clone.customer = customer;", content)
        self.assertNotIn("customer?.Clone()", content)


class TestEmitterDotnetCallingContext(unittest.TestCase):
    # The calling context is a plain per-request object: a service may hand it to background work
    # (the audit trail keeps a reference and reads the identity off it when the entry is written),
    # so a controller must not release it when the action returns.

    SOURCE = """
domain WebShop {
    context Orders {
        @public_api( rest, grpc, collection = "PublicApi" )
        interface OrderIF version 1 {
            query getOrder( id:string ) : string
        }
    }
}
"""

    def __controllers(self):
        engine = Engine()
        session = Session(Source.CreateFromText(self.SOURCE))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        result = DotnetEmitter().Emit(session)
        return {code.fileName: code.content for code in result if "Controller" in code.fileName}

    def test_controllers_build_the_context_without_a_pool(self):
        controllers = self.__controllers()
        self.assertIn("OrderIF_v1.RestController.cs", controllers)
        self.assertIn("OrderIF_v1.GrpcController.cs", controllers)
        self.assertIn("CallingContext.FromHttpContext( HttpContext, _logger );", controllers["OrderIF_v1.RestController.cs"])
        self.assertIn("CallingContext.FromGrpcContext( grpcContext, _logger );", controllers["OrderIF_v1.GrpcController.cs"])

    def test_the_grpc_controller_registers_itself(self):
        # the host maps the classes carrying [AutoRegisterGrpc]; without it the controller compiles,
        # the host starts, and the gRPC surface is simply not served
        controllers = self.__controllers()
        self.assertIn("[AutoRegisterGrpc]\n\tpublic class OrderIF_v1_GrpcController", controllers["OrderIF_v1.GrpcController.cs"])

    def test_no_controller_releases_the_context(self):
        for name, content in self.__controllers().items():
            self.assertNotIn("ReturnToPool", content, name)
            self.assertNotIn("PoolFrom", content, name)


class TestEmitterWorkflowIsBackendOnly(unittest.TestCase):
    # A workflow is not a transport surface, so only the .NET backend emits anything for it.

    SOURCE = """
domain WebShop {
    context Orders {
        workflow Approval {
            command start( orderId:string )
            step notify( orderId:string )
        }
    }
}
"""

    def __session(self):
        engine = Engine()
        session = Session(Source.CreateFromText(self.SOURCE))
        engine.Build(session)
        self.assertFalse(session.HasDiagnostic())
        return session

    def test_the_proto_emitter_ignores_workflows(self):
        from d3i.emitters.ProtoEmitter import ProtoEmitter
        self.assertEqual(0, len(ProtoEmitter().Emit(self.__session())))

    def test_the_typescript_emitter_ignores_workflows(self):
        from d3i.emitters.TypeScriptEmitter import TypeScriptEmitter
        self.assertEqual(0, len(TypeScriptEmitter().Emit(self.__session())))


class TestEmitterDotnetResponseShape(unittest.TestCase):
    """
    The status describes the ANSWER and the transport can carry exactly one, so it lives on the
    response; the errors are a list because a form with three bad fields is the ordinary case.
    The controller is also the only place that sees both worlds - PolyPersist raises exceptions,
    the wire speaks status + errors - and nobody owned that translation before, which is why a
    single bad field used to reach the caller as a 500.
    """

    SOURCE = """
domain Shop {
    context C {
        @internal_api( grpc, rest )
        interface OrderIF version 1 {
            dto OrderDTO {
                total: number validate value > 0
            }
            query getOrder( id:string ) : OrderDTO
            command cancel( id:string )
        }
    }
}
"""

    PUBLIC_SOURCE = SOURCE.replace("@internal_api( grpc, rest )", "@public_api( grpc, rest, collection = \"WebShopApi\" )")

    def __emit(self, source: str):
        engine = Engine()
        session = Session(Source.CreateFromText(source))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())
        return DotnetEmitter().Emit(session)

    def __files(self):
        return {f.fileName: f.content for f in self.__emit(self.SOURCE)}

    def test_the_grpc_controller_answers_with_a_status_and_every_error(self):
        content = self.__files()["OrderIF_v1.GrpcController.cs"]
        self.assertIn("_GrpcFailure_getOrder( response.Status, response.Errors );", content)
        self.assertIn("_GrpcFailure_cancel( response.Status, response.Errors );", content)
        self.assertIn("var failure = new OrderIF_v1_getOrderResponse() { Status = status.ToGrpc() };", content)
        self.assertIn("failure.Errors.Add( new ServiceKit.Protos.Error() {", content)
        # the one-per-error shape is gone
        self.assertNotIn("response.Error.Status", content)

    def test_the_grpc_controller_maps_polypersist_failures(self):
        content = self.__files()["OrderIF_v1.GrpcController.cs"]
        self.assertIn("var failure = _MapFailure( ex );", content)
        self.assertIn("ex is PolyPersist.Net.Common.ValidationExeption validationExeption", content)
        self.assertIn("Statuses.BadRequest, validationExeption.ValidationErrors.Select(", content)
        self.assertIn("Path = validationError.Path,", content)
        self.assertIn("ex is PolyPersist.Net.Common.NotFoundException", content)
        self.assertIn("return (Statuses.NotFound,", content)

    def test_the_rest_controller_answers_with_the_error_list(self):
        content = self.__files()["OrderIF_v1.RestController.cs"]
        self.assertIn("return StatusCode(response.Status.ToHttp(), response.Errors);", content)
        self.assertIn("return StatusCode(failure.Status.ToHttp(), failure.Errors);", content)
        # the documented failure body is a list, so a form learns about all its bad fields at once
        self.assertIn("typeof(IList<ServiceKit.Net.Error>)", content)
        self.assertNotIn("response.Error.Status.ToHttp()", content)

    def test_the_grpc_client_reads_the_status_not_the_oneof(self):
        content = self.__files()["OrderIF_v1.GrpcClient.cs"]
        self.assertIn("if( grpc_response.Status != ServiceKit.Protos.Statuses.Ok )", content)
        self.assertIn("grpc_response.Status.FromGrpc(), _FromGrpcErrors( grpc_response.Errors )", content)
        self.assertIn("private static ServiceKit.Net.Error[] _FromGrpcErrors( IEnumerable<ServiceKit.Protos.Error> errors )", content)
        # the value still travels in a oneof, so "no value" stays distinguishable from "default"
        self.assertIn("grpc_response.ResultCase == OrderIF_v1_getOrderResponse.ResultOneofCase.Value", content)
        self.assertNotIn("ResultOneofCase.Error", content)
        self.assertNotIn("ResultOneofCase.Success", content)

    def test_the_rest_client_reads_the_whole_error_list(self):
        content = self.__files()["OrderIF_v1.RestClient.cs"]
        self.assertIn("var errors = await response.Content.ReadFromJsonAsync<List<ServiceKit.Net.Error>>( _jsonOptions );", content)
        self.assertIn("response.StatusCode.FromHttp(), errors?.ToArray() ?? Array.Empty<ServiceKit.Net.Error>()", content)
        self.assertNotIn("ReadFromJsonAsync<Error>()", content)

    def test_the_public_clients_read_the_same_way(self):
        # the public (ApiClientKit) clients are a separate code path from the internal ones and
        # were the ones a careless bulk edit broke last time, so they get their own check
        public = [f for f in self.__emit(self.PUBLIC_SOURCE) if "ApiClientKit" in f.fullPath.replace("\\", "/")]
        by_name = {f.fileName: f.content for f in public}

        grpc = by_name["OrderIF_v1.GrpcClient.cs"]
        self.assertIn("if( grpc_response.Status != ServiceKit.Protos.Statuses.Ok )", grpc)
        self.assertIn("_FromGrpcErrors( grpc_response.Errors )", grpc)
        self.assertNotIn("ResultOneofCase.Error", grpc)

        rest = by_name["OrderIF_v1.RestClient.cs"]
        self.assertIn("ReadFromJsonAsync<List<ServiceKit.Net.Error>>( _jsonOptions );", rest)
        self.assertNotIn("ReadFromJsonAsync<Error>()", rest)


class TestEmitterDotnetRestClientCanCall(unittest.TestCase):
    """
    A generated client is only worth generating if it can reach the controller generated beside it.
    None of these were caught by reading the code: the client compiled, and every one of the three
    defects only showed up once something actually sent a request.
    """

    SOURCE = """
domain Shop {
    context C {
        @internal_api( grpc, rest )
        interface OrderIF version 1 {
            dto OrderDTO {
                @system_field id:string
                total: number
            }
            query getOrder( orderId:string ) : OrderDTO
            command setPrice( order:OrderDTO, price:number, at:date ) : OrderDTO
        }
    }
}
"""

    PUBLIC_SOURCE = SOURCE.replace("@internal_api( grpc, rest )", "@public_api( grpc, rest, collection = \"ShopApi\" )")

    def __emit(self, source: str):
        engine = Engine()
        session = Session(Source.CreateFromText(source))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())
        return {f.fileName: f.content for f in DotnetEmitter().Emit(session)}

    def test_the_clients_can_be_constructed(self):
        # a constructor with no modifier is private, so nobody outside could ever build one
        files = self.__emit(self.SOURCE)
        self.assertIn("public OrderIF_v1_RestClient( string serverAddress )", files["OrderIF_v1.RestClient.cs"])
        self.assertIn("public OrderIF_v1_GrpcClient( string serverAddress )", files["OrderIF_v1.GrpcClient.cs"])

    def test_the_route_is_not_escaped_as_a_whole(self):
        # escaping the whole url turns every separator into %2F and the request matches no route
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertNotIn("WebUtility.UrlEncode", content)
        self.assertIn("HttpMethod.Get, $\"/shop/c/orderif/v1/getorder/", content)

    def test_a_route_parameter_is_escaped_on_its_own(self):
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertIn("getorder/{Uri.EscapeDataString(orderId)}", content)

    def test_a_query_parameter_is_escaped_on_its_own(self):
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertIn("?price={Uri.EscapeDataString(price.ToString(CultureInfo.InvariantCulture))}", content)

    def test_a_date_query_parameter_is_valid_csharp(self):
        # the format and the culture were emitted without the comma between them
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertIn("at.ToString(\"yyyy-MM-dd\", CultureInfo.InvariantCulture)", content)
        self.assertNotIn("\" CultureInfo.InvariantCulture", content)

    def test_the_body_says_it_is_json(self):
        # without the media type the body goes out as text/plain and the controller answers 415
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertIn("new StringContent( JsonSerializer.Serialize<IOrderIF_v1.OrderDTO>( order, _jsonOptions ), Encoding.UTF8, \"application/json\" )", content)
        self.assertIn("using System.Text;", content)

    def test_the_client_speaks_the_hosts_json(self):
        # the host writes enums by name; a client on the default options fails on the first answer
        content = self.__emit(self.SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertIn("new JsonSerializerOptions( JsonSerializerDefaults.Web )", content)
        self.assertIn("Converters = { new JsonStringEnumConverter() },", content)
        self.assertIn("using System.Text.Json.Serialization;", content)
        self.assertIn("ReadFromJsonAsync<IOrderIF_v1.OrderDTO>( _jsonOptions )", content)
        self.assertIn("ReadFromJsonAsync<List<ServiceKit.Net.Error>>( _jsonOptions )", content)
        self.assertIn("JsonSerializer.Serialize<IOrderIF_v1.OrderDTO>( order, _jsonOptions )", content)

    def test_the_public_client_is_built_the_same_way(self):
        content = self.__emit(self.PUBLIC_SOURCE)["OrderIF_v1.RestClient.cs"]
        self.assertNotIn("WebUtility.UrlEncode", content)
        self.assertIn("getorder/{Uri.EscapeDataString(orderId)}", content)
        self.assertIn("Encoding.UTF8, \"application/json\" )", content)
        self.assertIn("Converters = { new JsonStringEnumConverter() },", content)
        self.assertIn("ReadFromJsonAsync<Shop.C.IOrderIF_v1.OrderDTO>( _jsonOptions )", content)

    def test_a_validator_reports_a_missing_value_instead_of_throwing(self):
        # a validator that throws turns a bad request into a 500, and the caller is told nothing
        # about the field that is actually wrong
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain Shop {
    context C {
        valueobject Address {
            country:string validate len(value) == 2
            email:string validate matches(email, "[^@]+@[^@]+")
            tags:list[string] validate len(value) <= 3
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        content = next(f for f in DotnetEmitter().Emit(session) if f.fileName == "Address.cs").content
        self.assertIn("if ((country?.Length ?? 0) != 2)", content)
        self.assertIn("if (!Regex.IsMatch(email ?? string.Empty, \"[^@]+@[^@]+\"))", content)
        self.assertIn("if ((tags?.Count ?? 0) > 3)", content)

    def test_an_unset_string_does_not_take_the_grpc_call_down(self):
        # protobuf throws on a null string field, so an id the caller has not got yet used to abort
        # the call inside the client before anything was sent
        content = self.__emit(self.SOURCE)["IOrderIF_v1.cs"]
        self.assertIn("result.Id = @this.id ?? string.Empty;", content)

    def test_a_system_field_stays_out_of_the_hash(self):
        # Equals and Clone already skip it; a hash that does not would put two equal instances in
        # different buckets and a dictionary would stop finding them
        content = self.__emit(self.SOURCE)["IOrderIF_v1.cs"]
        self.assertIn("hash.Add(total);", content)
        self.assertNotIn("hash.Add(id);", content)


if __name__ == "__main__":
    unittest.main()
