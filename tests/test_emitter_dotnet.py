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
        self.assertTrue(1, len(result))
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

        valueobject PartnerAddress inherits WithAddress {
            PartnerCode:string
        }
    }
}
"""))
        root = engine.Build(session)
        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{
        public class PartnerAddress : IWithAddress
        {
            #region IWithAddress
            public string city { get; set; }
            public string street { get; set; }
            public string country { get; set; }
            public int zipCode { get; set; }
            #endregion IWithAddress

            public string PartnerCode { get; set; }
        }
}
"""
        self.assertTrue(1, len(result))
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

    def test_emitter_acl_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        acl CustomerACL {
            valueobject OrderData {
                name:string
                kind:CustomerKind
                Address:string
            }
            enum CustomerKind {
                PrivatePerson,
                Company
            }
          
            #getting order data based on customer id    
            @verb("get")
            getOrderData( @fromBody customerId: string )
                : #order data when any found for given customer
                  @status(200) OrderData
                | #error message when any bussines logig error is occured
                  #for example: customer not found
                  @status(401) Error

            #delete order based on orderId 
            @verb("post")
            deleteOrder( orderId: string )
        }
    }
}
"""))
        root = engine.Build(session)
        emitter = DotnetEmitter()
        result = emitter.Emit(session)
        expected = """
"""
        self.assertEqual(result[0].fileName, "ICustomerACL.cs")
        self.assertEqual(result[1].fileName, "CustomerACL.proto")
        self.assertEqual(result[2].fileName, "CustomerACLGrpcController.cs")
        print(result[0].content)
        #print(result[1].content)
        print(result[2].content)



if __name__ == "__main__":
    unittest.main()
