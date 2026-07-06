from __future__ import annotations
import unittest
from d3i.Engine import *

class TestBuild(unittest.TestCase):

    def test_empty_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(0, len(root.domains))

    def test_lines_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        element: base_element = root.domains[0]
        self.assertEqual(element.line, 2)
        self.assertEqual(element.column, 0)
        self.assertEqual(element.fileName, "internal string")

    def test_document_lines_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
#doc line 1
#doc line 2
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        domain: domain = root.domains[0]
        self.assertEqual(2, len(domain.document_lines))
        self.assertEqual(domain.document_lines[0], "doc line 1")
        self.assertEqual(domain.document_lines[1], "doc line 2")


    def test_import_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
import somedomain.subdomain.subdomain
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(1, len(root.imports))
        _import: import_ = root.imports[0]
        self.assertEqual(_import.name, "somedomain.subdomain.subdomain")


    def test_directive_qualified_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
resources somedomain.subdomain.subdomain
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(1, len(root.domains[0].directives))
        directive: directive = root.domains[0].directives[0]
        self.assertEqual(directive.keyword, "resources")
        self.assertEqual(directive.value.getText(), "somedomain.subdomain.subdomain")

    def test_decorator_simple_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
@simple
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(1, len(root.domains))
        domain: domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")

    def test_decorator_multiple_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
@simple_1
@simple_2
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(1, len(root.domains))
        domain: domain = root.domains[0]
        self.assertEqual(2, len(domain.decorators))
        decorator: decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple_1")
        decorator: decorator = domain.decorators[1]
        self.assertEqual(decorator.name, "simple_2")

    def test_decorator_complex_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
@simple( "string", 1, 3.14, identifier.sub.sub )
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        self.assertEqual(1, len(root.domains))
        domain: domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")
        self.assertEqual(4, len(decorator.params))
        param: decorator_param = decorator.params[0]
        self.assertEqual(param.kind, decorator_param.Kind.String)
        self.assertEqual(param.value, "string")
        param: decorator_param = decorator.params[1]
        self.assertEqual(param.kind, decorator_param.Kind.Integer)
        self.assertEqual(param.value, 1)
        param: decorator_param = decorator.params[2]
        self.assertEqual(param.kind, decorator_param.Kind.Number)
        self.assertEqual(param.value, Decimal('3.14'))
        param: decorator_param = decorator.params[3]
        self.assertEqual(param.kind, decorator_param.Kind.QualifiedName)
        self.assertEqual(param.value.getText(), "identifier.sub.sub")

    def test_context_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    @decorator
    context context_1 {
    }
    @decorator
    context context_2 {
    }
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3)
        domain: domain = root.domains[0]
        self.assertEqual(2, len(domain.contexts))
        context: context = domain.contexts[0]
        self.assertEqual(context.name, "context_1")
        self.assertEqual(len(context.decorators), 1)
        context: context = domain.contexts[1]
        self.assertEqual(context.name, "context_2")
        self.assertEqual(len(context.decorators), 1)

    def test_enum(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_enum
        enum WeekDays{
            @first
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            @last
            Friday
        }
    }
}
"""))
        root = engine.Build(session)
        domain: context = root.domains[0].contexts[0]
        enum: enum = domain.enums[0]
        self.assertEqual(enum.name, "WeekDays")
        self.assertEqual(len(enum.decorators), 1)
        self.assertEqual(len(enum.enum_elements), 5)
        self.assertEqual(enum.enum_elements[0].value, "Monday")
        self.assertEqual(enum.enum_elements[1].value, "Tuesday")
        self.assertEqual(enum.enum_elements[2].value, "Wednesday")
        self.assertEqual(enum.enum_elements[3].value, "Thursday")
        self.assertEqual(enum.enum_elements[4].value, "Friday")
        self.assertEqual(enum.enum_elements[0].decorators[0].name, "first")
        self.assertEqual(enum.enum_elements[4].decorators[0].name, "last")

    def test_value_object(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueobject Address {
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        value_object: value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        member: value_object_member = value_object.members[0]
        self.assertEqual(member.name, "city")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: value_object_member = value_object.members[1]
        self.assertEqual(member.name, "street")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        member: value_object_member = value_object.members[2]
        self.assertEqual(member.name, "country")
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "General.Country")
        member: value_object_member = value_object.members[3]
        self.assertEqual(member.name, "zipCode")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)

    def test_value_object_inner_valueobject(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueobject Address {
            valueobject Inner{
                inner_1:string
                inner_2:integer
            }
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        value_object: value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        value_object_inner: value_object = value_object.value_objects[0]
        member: value_object_member = value_object_inner.members[0]
        self.assertEqual(member.name, "inner_1")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        member: value_object_member = value_object_inner.members[1]
        self.assertEqual(member.name, "inner_2")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)

    def test_value_object_inner_enum(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueobject Address {
            enum InnerEnum{
                Value1,
                Value2
            }
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        value_object: value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        enum_inner: enum = value_object.enums[0]
        self.assertEqual(enum_inner.name, "InnerEnum")
        self.assertEqual(len(enum_inner.enum_elements), 2)

    def test_composite(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_composite
        composite WithAddress {
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        composite: composite = context.composites[0]
        self.assertEqual(len(composite.decorators), 1)
        self.assertEqual(composite.name, "WithAddress")
        self.assertEqual(len(composite.members), 4)
        member: composite_member = composite.members[0]
        self.assertEqual(member.name, "city")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: composite_member = composite.members[1]
        self.assertEqual(member.name, "street")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        member: composite_member = composite.members[2]
        self.assertEqual(member.name, "country")
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "General.Country")
        member: composite_member = composite.members[3]
        self.assertEqual(member.name, "zipCode")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)

    def test_composite_inner_valueobject(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_composite
        composite WithAddress {
            valueobject Inner{
                inner_1:string
                inner_2:integer
            }
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        composite: composite = context.composites[0]
        self.assertEqual(len(composite.decorators), 1)
        self.assertEqual(composite.name, "WithAddress")
        self.assertEqual(len(composite.members), 4)
        value_object_inner: value_object = composite.value_objects[0]
        member: value_object_member = value_object_inner.members[0]
        self.assertEqual(member.name, "inner_1")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        member: value_object_member = value_object_inner.members[1]
        self.assertEqual(member.name, "inner_2")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)

    def test_composite_inner_enum(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_composite
        composite WithAddress {
            enum InnerEnum{
                Value1,
                Value2
            }
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        composite: composite = context.composites[0]
        self.assertEqual(len(composite.decorators), 1)
        self.assertEqual(composite.name, "WithAddress")
        self.assertEqual(len(composite.members), 4)
        enum_inner: enum = composite.enums[0]
        self.assertEqual(enum_inner.name, "InnerEnum")
        self.assertEqual(len(enum_inner.enum_elements), 2)

    def test_entity(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        aggregate CustomerAggregate {
            @decorator_entity
            entity Customer {
                @required
                name:string
                address:Address
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[0].internal_entities[0].entity
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 2)
        member: entity_member = entity.members[0]
        self.assertEqual(member.name, "name")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: entity_member = entity.members[1]
        self.assertEqual(member.name, "address")
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Address")

    def test_entity_inner_enum(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        aggregate CutomerAggregate{    
            @decorator_entity
            entity Customer {
                enum Kind{
                    PrivatePerson,
                    Company
                }
                @required
                name:string
                address:Address
                kind:Kind
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[0].internal_entities[0].entity
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_enum: enum = entity.enums[0]
        self.assertEqual(inner_enum.name, "Kind")
        self.assertEqual(len(inner_enum.enum_elements), 2)

    def test_entity_inner_valueobject(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        aggregate CusometAggregate { 
            @decorator_entity
            entity Customer {
                valueobject Credit {
                    limit:decimal
                    currency:Currency
                }
                @required
                name:string
                address:Address
                kind:Kind
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[0].internal_entities[0].entity
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_value_object: value_object = entity.value_objects[0]
        self.assertEqual(inner_value_object.name, "Credit")
        self.assertEqual(len(inner_value_object.members), 2)

    def test_entity_inheritance_base_entity(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        aggregate Base {
            entity Object {
                @required
                HumanReadableKey:string
            }
        }

        aggregate CustomerAggregate {
            @decorator_entity
            entity Partner {
                @required
                name:string
                address:Address
            }

            @decorator_entity
            entity Customer inherits Partner, Base.Object {
                @required
                discountCategory:integer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[1].internal_entities[1].entity
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 1)
        member: entity_member = entity.members[0]
        self.assertEqual(member.name, "discountCategory")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)
        self.assertEqual(member.decorators[0].name, "required")
        self.assertEqual(len(entity.inherits), 2)
        base_entity_name:qualified_name = entity.inherits[0]
        self.assertEqual(base_entity_name.getText(), "Partner" )
        base_entity_name = entity.inherits[1]
        self.assertEqual(base_entity_name.getText(), "Base.Object" )

    
    def test_entity_inheritance_base_composit(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        composite Object {
            @required
            HumanReadableKey:string
        }

        aggregate CustomerAggregate {
            @decorator_entity
            entity Partner {
                @required
                name:string
                address:Address
            }

            @decorator_entity
            entity Customer inherits Partner, Object {
                @required
                discountCategory:integer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[0].internal_entities[1].entity
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 1)
        member: entity_member = entity.members[0]
        self.assertEqual(member.name, "discountCategory")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.Integer)
        self.assertEqual(member.decorators[0].name, "required")
        self.assertEqual(len(entity.inherits), 2)
        base_entity_name:qualified_name = entity.inherits[0]
        self.assertEqual(base_entity_name.getText(), "Partner" )
        base_entity_name = entity.inherits[1]
        self.assertEqual(base_entity_name.getText(), "Object" )

    def test_aggregate(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_aggregate
        aggregate Order {
            root entity OrderHeader {
                deadline:date
                customer:Customer
                lines:list[OrderItem]
            }
            entity OrderItem {
                quantity:decimal
                product:string
                price:decimal
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        aggregate: aggregate = context.aggregates[0]
        self.assertEqual(len(aggregate.internal_entities), 2)
        order_header: aggregate_entity = aggregate.internal_entities[0]
        self.assertEqual(order_header.entity.name, "OrderHeader")
        self.assertEqual(order_header.isRoot, True)
        order_item: aggregate_entity = aggregate.internal_entities[1]
        self.assertEqual(order_item.entity.name, "OrderItem")
        self.assertEqual(order_item.isRoot, False)

    def test_view(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_view
        view CustomerView {
            @required
            name:string
            address:Address
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        view: view = context.views[0]
        self.assertEqual(len(view.decorators), 1)
        self.assertEqual(view.name, "CustomerView")
        self.assertEqual(len(view.members), 2)
        member: view_member = view.members[0]
        self.assertEqual(member.name, "name")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: view_member = view.members[1]
        self.assertEqual(member.name, "address")
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Address")

    def test_view_inner_enum(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_view
        view CustomerView {
            enum Kind{
                PrivatePerson,
                Company
            }
            @required
            name:string
            address:Address
            kind:Kind
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        view: view = context.views[0]
        self.assertEqual(len(view.decorators), 1)
        self.assertEqual(view.name, "CustomerView")
        self.assertEqual(len(view.members), 3)
        inner_enum: enum = view.enums[0]
        self.assertEqual(inner_enum.name, "Kind")
        self.assertEqual(len(inner_enum.enum_elements), 2)

    def test_repository(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        aggregate Order {
            root entity OrderHeader {
                deadline:date
                customer:Customer
                lines:list[OrderItem]
            }
            entity OrderItem {
                quantity:decimal
                product:string
                price:decimal
            }
        }
        repository orders {
            query getById( id:string ) : string
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        repository: repository = context.repositories[0]
        self.assertEqual(repository.name, "orders")
        self.assertEqual(len(repository.operations), 1)
        self.assertEqual(repository.operations[0].name, "getById")

    def test_service_event_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        service OrderService {
            event OrderPlaced version 1 {
                enum Importance {
                    High,
                    Normal,
                    Low
                }

                orderId:string
                importance:Importance
                @decorator_data
                data:string
            }
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()

        context: context = root.domains[0].contexts[0]
        self.assertEqual(len(context.services[0].events), 1)
        event: event = context.services[0].events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(event.version, 1)
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.enums), 1)
        member: event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(len(member.decorators), 0)
        member: event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member: event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.kind, type.Kind.Primitive)

    def test_inerface_event(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        interface IOrderService version 1{
            event OrderPlaced version 2 {
                enum Importance {
                    High,
                    Normal,
                    Low
                }

                orderId:string
                importance:Importance
                @decorator_data
                data:EventData
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        self.assertEqual(len(context.interfaces[0].events), 1)
        event: event = context.interfaces[0].events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(event.version, 2 )
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.enums), 1)
        member: event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(len(member.decorators), 0)
        member: event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member: event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.kind, type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")


    def test_acl(self):
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
          
            @verb("get")
            query getOrderData( @fromBody customerId: string ): OrderData
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        self.assertEqual(len(context.acls), 1)
        acl: acl = context.acls[0]
        self.assertEqual(acl.name, "CustomerACL")
        self.assertEqual(len(acl.operations), 1)
        self.assertEqual(len(acl.enums), 1)
        self.assertEqual(len(acl.value_objects), 1)
        operation: operation = acl.operations[0]
        self.assertEqual(operation.name, "getOrderData")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "customerId")
        self.assertEqual(operation_param.type.kind, type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        self.assertEqual(operation.operation_return.type.kind, type.Kind.Reference)
        self.assertEqual(operation.operation_return.type.reference_name.getText(), "OrderData")

    def test_service(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        service OrderService {
            valueobject OrderData {
                name:string
                kind:CustomerKind
                Address:string
            }
            enum CustomerKind {
                PrivatePerson,
                Company
            }
          
            @verb("get")
            query getOrder( @fromBody orderId: string )
                : @status(200) OrderData
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        self.assertEqual(len(context.services), 1)
        service: service = context.services[0]
        self.assertEqual(service.name, "OrderService")
        self.assertEqual(len(service.operations), 1)
        self.assertEqual(len(service.enums), 1)
        self.assertEqual(len(service.value_objects), 1)
        operation: operation = service.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.kind, type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return: operation_return = operation.operation_return
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderData")

    def test_interface(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        interface OrderService version 2 {
            dto OrderDTO {
                name:string
                kind:CustomerKind
                Address:string
            }
            enum CustomerKind {
                PrivatePerson,
                Company
            }
          
            @verb("get")
            query getOrder( @fromBody orderId: string )
                : @status(200) OrderDTO
                | @status(404) ErrorNotFound
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        self.assertEqual(len(context.interfaces), 1)
        interface: interface = context.interfaces[0]
        self.assertEqual(interface.name, "OrderService")
        self.assertEqual(interface.version, 2)
        self.assertEqual(len(interface.operations), 1)
        self.assertEqual(len(interface.enums), 1)
        self.assertEqual(len(interface.dtos), 1)
        operation: operation = interface.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.kind, type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return: operation_return = operation.operation_return
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderDTO")


    def test_dto(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface TheInterface version 1 {
            dto TheDto {
                enum Kind {
                    A,
                    B
                }
                field:string
                amount:integer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        interface: interface = context.interfaces[0]
        self.assertEqual(len(interface.dtos), 1)
        dto: dto = interface.dtos[0]
        self.assertEqual(dto.name, "TheDto")
        self.assertEqual(len(dto.members), 2)
        self.assertEqual(dto.members[0].name, "field")
        self.assertEqual(dto.members[0].type.kind, type.Kind.Primitive)
        self.assertEqual(dto.members[0].type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(dto.members[1].name, "amount")
        self.assertEqual(dto.members[1].type.primtiveKind, primitive_type.PrimtiveKind.Integer)
        self.assertEqual(len(dto.enums), 1)
        self.assertEqual(dto.enums[0].name, "Kind")

    def test_list_type(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject TheValueObject {
            data: list[ string ]
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        member = context.value_objects[0].members[0]
        self.assertEqual(member.name, "data")
        self.assertEqual(member.type.kind, type.Kind.List)
        self.assertEqual(member.type.item_type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.item_type.primtiveKind, primitive_type.PrimtiveKind.String)

    def test_map_type(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject TheValueObject {
            data: map[ string, integer ]
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        member = context.value_objects[0].members[0]
        self.assertEqual(member.name, "data")
        self.assertEqual(member.type.kind, type.Kind.Map)
        self.assertEqual(member.type.key_type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.key_type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(member.type.value_type.kind, type.Kind.Primitive)
        self.assertEqual(member.type.value_type.primtiveKind, primitive_type.PrimtiveKind.Integer)

    def test_view_projection(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        view TheView projected: SomeEntity {
            field:string
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        view: view = context.views[0]
        self.assertEqual(view.name, "TheView")
        self.assertEqual(len(view.view_projections), 1)
        self.assertEqual(view.view_projections[0].getText(), "SomeEntity")

    def test_value_object_inheritance(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Derived inherits Base {
            field:string
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        value_object: value_object = context.value_objects[0]
        self.assertEqual(value_object.name, "Derived")
        self.assertEqual(len(value_object.inherits), 1)
        self.assertEqual(value_object.inherits[0].getText(), "Base")

    def test_composite_inheritance(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        composite Derived inherits Base {
            field:string
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        composite: composite = context.composites[0]
        self.assertEqual(composite.name, "Derived")
        self.assertEqual(len(composite.inherits), 1)
        self.assertEqual(composite.inherits[0].getText(), "Base")

    def test_view_inheritance(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        view Derived inherits Base {
            field:string
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        view: view = context.views[0]
        self.assertEqual(view.name, "Derived")
        self.assertEqual(len(view.inherits), 1)
        self.assertEqual(view.inherits[0].getText(), "Base")

    def test_eventhandler(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            eventhandler TheHandler for event SomeEvent
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        service: service = context.services[0]
        self.assertEqual(len(service.eventhandlers), 1)
        self.assertEqual(service.eventhandlers[0].name, "TheHandler")
        self.assertEqual(service.eventhandlers[0].handledEvent.getText(), "SomeEvent")

    def test_operation_command_query(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            command doIt( x:string ) : boolean
            query getIt( id:integer ) : SomeType
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        service: service = context.services[0]
        self.assertEqual(len(service.operations), 2)

        command: operation = service.operations[0]
        self.assertEqual(command.kind, operation.Kind.Command)
        self.assertEqual(command.name, "doIt")
        self.assertEqual(command.operation_params[0].name, "x")
        self.assertEqual(command.operation_params[0].type.primtiveKind, primitive_type.PrimtiveKind.String)
        self.assertEqual(command.operation_return.type.kind, type.Kind.Primitive)
        self.assertEqual(command.operation_return.type.primtiveKind, primitive_type.PrimtiveKind.Boolean)

        query: operation = service.operations[1]
        self.assertEqual(query.kind, operation.Kind.Query)
        self.assertEqual(query.name, "getIt")
        self.assertEqual(query.operation_params[0].type.primtiveKind, primitive_type.PrimtiveKind.Integer)
        self.assertEqual(query.operation_return.type.kind, type.Kind.Reference)
        self.assertEqual(query.operation_return.type.reference_name.getText(), "SomeType")


    def test_value_object_operation(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money {
            amount:number
            currency:string
            query isPositive() : boolean
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        value_object: value_object = context.value_objects[0]
        self.assertEqual(len(value_object.operations), 1)
        self.assertEqual(value_object.operations[0].kind, operation.Kind.Query)
        self.assertEqual(value_object.operations[0].name, "isPositive")

    def test_entity_operation(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        aggregate OrderAggregate {
            root entity OrderHeader {
                total:number
                command applyDiscount( percent:number )
                query isOverdue() : boolean
            }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        entity: entity = context.aggregates[0].internal_entities[0].entity
        self.assertEqual(len(entity.operations), 2)
        self.assertEqual(entity.operations[0].kind, operation.Kind.Command)
        self.assertEqual(entity.operations[0].name, "applyDiscount")
        self.assertEqual(entity.operations[1].kind, operation.Kind.Query)
        self.assertEqual(entity.operations[1].name, "isOverdue")


    def test_event_kinds(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            event Plain version 1 { x:number }
            domain event Created version 1 { x:number }
            integration event Shipped version 1 { x:number }
            audit event Logged version 1 { who:string }
        }
    }
}
"""))
        root = engine.Build(session)
        service = root.domains[0].contexts[0].services[0]
        self.assertEqual(len(service.events), 4)
        self.assertEqual(service.events[0].kind, event.Kind.Domain)
        self.assertEqual(service.events[1].kind, event.Kind.Domain)
        self.assertEqual(service.events[2].kind, event.Kind.Integration)
        self.assertEqual(service.events[3].kind, event.Kind.Audit)

    def test_eventsourced_aggregate(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        eventsourced aggregate Account {
            root entity AccountRoot { balance:number }
        }
        aggregate Plain {
            root entity PlainRoot { x:number }
        }
    }
}
"""))
        root = engine.Build(session)
        context: context = root.domains[0].contexts[0]
        self.assertEqual(context.aggregates[0].eventsourced, True)
        self.assertEqual(context.aggregates[1].eventsourced, False)

    def test_command_emits(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        aggregate OrderAggregate {
            root entity OrderHeader {
                total:number
                command place() emits Placed, AuditLogged
            }
        }
    }
}
"""))
        root = engine.Build(session)
        entity: entity = root.domains[0].contexts[0].aggregates[0].internal_entities[0].entity
        command: operation = entity.operations[0]
        self.assertEqual(command.name, "place")
        self.assertEqual(len(command.emits), 2)
        self.assertEqual(command.emits[0].getText(), "Placed")
        self.assertEqual(command.emits[1].getText(), "AuditLogged")


if __name__ == "__main__":
    unittest.main()
