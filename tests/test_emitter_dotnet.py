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
        # Q13: @deprecated -> [Obsolete] on both the class and the field
        self.assertIn('[Obsolete("use NewAddress, since 2.3")]', content)
        self.assertIn('[Obsolete("use zip")]', content)
        # @gdpr is a marker only: it must not emit any attribute (exactly two [Obsolete]s)
        self.assertEqual(content.count("[Obsolete"), 2)


if __name__ == "__main__":
    unittest.main()
