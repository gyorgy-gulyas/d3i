import unittest
import d3i
from d3i.emitters import *


class TestBuild(unittest.TestCase):

    def test_empty_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText(""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        self.assertEqual(0, len(root.domains))

    def test_lines_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        element: d3i.base_element = root.domains[0]
        self.assertEqual(element.line, 2)
        self.assertEqual(element.column, 0)
        self.assertEqual(element.fileName, "internal string")

    def test_directive_qualified_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
import somedomain.subdomain.subdomain
domain somedomain{
}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        self.assertEqual(1, len(root.domains[0].directives))
        directive: d3i.directive = root.domains[0].directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value.getText(), "somedomain.subdomain.subdomain")

    def test_decorator_simple_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
@simple
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        self.assertEqual(1, len(root.domains))
        domain: d3i.domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: d3i.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")

    def test_decorator_multiple_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
@simple_1
@simple_2
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        self.assertEqual(1, len(root.domains))
        domain: d3i.domain = root.domains[0]
        self.assertEqual(2, len(domain.decorators))
        decorator: d3i.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple_1")
        decorator: d3i.decorator = domain.decorators[1]
        self.assertEqual(decorator.name, "simple_2")

    def test_decorator_complex_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
@simple( "string", 1, 3.14, identifier.sub.sub )
domain somedomain {}
"""))
        root = engine.Build(session)
        self.assertIsInstance(root, d3i.d3)
        self.assertEqual(1, len(root.domains))
        domain: d3i.domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: d3i.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")
        self.assertEqual(4, len(decorator.params))
        param: d3i.decorator_param = decorator.params[0]
        self.assertEqual(param.kind, d3i.decorator_param.Kind.String)
        self.assertEqual(param.value, "string")
        param: d3i.decorator_param = decorator.params[1]
        self.assertEqual(param.kind, d3i.decorator_param.Kind.Integer)
        self.assertEqual(param.value, 1)
        param: d3i.decorator_param = decorator.params[2]
        self.assertEqual(param.kind, d3i.decorator_param.Kind.Number)
        self.assertEqual(param.value, Decimal('3.14'))
        param: d3i.decorator_param = decorator.params[3]
        self.assertEqual(param.kind, d3i.decorator_param.Kind.QualifiedName)
        self.assertEqual(param.value.getText(), "identifier.sub.sub")

    def test_context_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        self.assertIsInstance(root, d3i.d3)
        domain: d3i.domain = root.domains[0]
        self.assertEqual(2, len(domain.contexts))
        context: d3i.context = domain.contexts[0]
        self.assertEqual(context.name, "context_1")
        self.assertEqual(len(context.decorators), 1)
        context: d3i.context = domain.contexts[1]
        self.assertEqual(context.name, "context_2")
        self.assertEqual(len(context.decorators), 1)

    def test_enum(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        domain: d3i.context = root.domains[0].contexts[0]
        enum: d3i.enum = domain.enums[0]
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
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        context: d3i.context = root.domains[0].contexts[0]
        value_object: d3i.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        member: d3i.value_object_member = value_object.members[0]
        self.assertEqual(member.name, "city")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: d3i.value_object_member = value_object.members[1]
        self.assertEqual(member.name, "street")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        member: d3i.value_object_member = value_object.members[2]
        self.assertEqual(member.name, "country")
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "General.Country")
        member: d3i.value_object_member = value_object.members[3]
        self.assertEqual(member.name, "zipCode")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.Integer)

    def test_value_object_inner_valueobject(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        context: d3i.context = root.domains[0].contexts[0]
        value_object: d3i.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        value_object_inner: d3i.value_object = value_object.internal_value_objects[0]
        member: d3i.value_object_member = value_object_inner.members[0]
        self.assertEqual(member.name, "inner_1")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        member: d3i.value_object_member = value_object_inner.members[1]
        self.assertEqual(member.name, "inner_2")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.Integer)

    def test_value_object_inner_enum(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        context: d3i.context = root.domains[0].contexts[0]
        value_object: d3i.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        enum_inner: d3i.enum = value_object.internal_enums[0]
        self.assertEqual(enum_inner.name, "InnerEnum")
        self.assertEqual(len(enum_inner.enum_elements), 2)

    def test_entity(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator_entity
        entity Customer {
            @required
            name:string
            address:Address
        }
    }
}
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        entity: d3i.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 2)
        member: d3i.entity_member = entity.members[0]
        self.assertEqual(member.name, "name")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: d3i.entity_member = entity.members[1]
        self.assertEqual(member.name, "address")
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Address")

    def test_entity_inner_enum(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
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
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        entity: d3i.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_enum: d3i.enum = entity.internal_enums[0]
        self.assertEqual(inner_enum.name, "Kind")
        self.assertEqual(len(inner_enum.enum_elements), 2)

    def test_entity_inner_valueobject(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
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
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        entity: d3i.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_value_object: d3i.value_object = entity.internal_value_objects[0]
        self.assertEqual(inner_value_object.name, "Credit")
        self.assertEqual(len(inner_value_object.members), 2)

    def test_aggregate(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        context: d3i.context = root.domains[0].contexts[0]
        aggregate: d3i.aggregate = context.aggregates[0]
        self.assertEqual(len(aggregate.internal_entities), 2)
        order_header: d3i.aggregate_entity = aggregate.internal_entities[0]
        self.assertEqual(order_header.entity.name, "OrderHeader")
        self.assertEqual(order_header.isRoot, True)
        order_item: d3i.aggregate_entity = aggregate.internal_entities[1]
        self.assertEqual(order_item.entity.name, "OrderItem")
        self.assertEqual(order_item.isRoot, False)

    def test_repository(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
        entity Customer {
            @required
            name:string
            address:Address
        }

        repository orders:Order
        repository customers:Customer
    }
}
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        repository: d3i.repository = context.repositories[0]
        self.assertEqual(repository.name, "orders")
        self.assertEqual(repository.element_name.getText(), "Order")
        repository: d3i.repository = context.repositories[1]
        self.assertEqual(repository.name, "customers")
        self.assertEqual(repository.element_name.getText(), "Customer")

    def test_service_event(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        service OrderService{
            event OrderPlaced {
                valueobject EventData {
                    data_1:string
                    data_1:string
                }
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
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.services[0].events), 1)
        event: d3i.event = context.services[0].events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.internal_enums), 1)
        self.assertEqual(len(event.internal_value_objects), 1)
        member: d3i.event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(member.decorators), 0)
        member: d3i.event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member: d3i.event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")

    def test_inerface_event(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        interface IOrderService{
            event OrderPlaced {
                valueobject EventData {
                    data_1:string
                    data_1:string
                }
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
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.interfaces[0].events), 1)
        event: d3i.event = context.interfaces[0].events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.internal_enums), 1)
        self.assertEqual(len(event.internal_value_objects), 1)
        member: d3i.event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(member.decorators), 0)
        member: d3i.event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member: d3i.event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")


    def test_acl(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
            getOrderData( @fromBody customerId: string ): OrderData
        }
    }
}
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.acls), 1)
        acl: d3i.acl = context.acls[0]
        self.assertEqual(acl.name, "CustomerACL")
        self.assertEqual(len(acl.operations), 1)
        self.assertEqual(len(acl.internal_enums), 1)
        self.assertEqual(len(acl.internal_value_objects), 1)
        operation: d3i.operation = acl.operations[0]
        self.assertEqual(operation.name, "getOrderData")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: d3i.operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "customerId")
        self.assertEqual(operation_param.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        self.assertEqual(operation.operation_returns[0].type.kind, d3i.type.Kind.Reference)
        self.assertEqual(operation.operation_returns[0].type.reference_name.getText(), "OrderData")

    def test_service(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
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
            getOrder( @fromBody orderId: string )
                : @status(200) OrderData
                | @status(404) ErrorNotFound
        }
    }
}
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.services), 1)
        service: d3i.service = context.services[0]
        self.assertEqual(service.name, "OrderService")
        self.assertEqual(len(service.operations), 1)
        self.assertEqual(len(service.internal_enums), 1)
        self.assertEqual(len(service.internal_value_objects), 1)
        operation: d3i.operation = service.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: d3i.operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return: d3i.operation_return = operation.operation_returns[0]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderData")
        operation_return: d3i.operation_return = operation.operation_returns[1]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "ErrorNotFound")

    def test_interface(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        interface OrderService {
            valueobject OrderDTO {
                name:string
                kind:CustomerKind
                Address:string
            }
            enum CustomerKind {
                PrivatePerson,
                Company
            }
          
            @verb("get")
            getOrder( @fromBody orderId: string )
                : @status(200) OrderDTO
                | @status(404) ErrorNotFound
        }
    }
}
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.interfaces), 1)
        interface: d3i.interface = context.interfaces[0]
        self.assertEqual(interface.name, "OrderService")
        self.assertEqual(len(interface.operations), 1)
        self.assertEqual(len(interface.internal_enums), 1)
        self.assertEqual(len(interface.internal_value_objects), 1)
        operation: d3i.operation = interface.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param: d3i.operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(operation_param.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return: d3i.operation_return = operation.operation_returns[0]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderDTO")
        operation_return: d3i.operation_return = operation.operation_returns[1]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "ErrorNotFound")


def test_context_event(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain somedomain {
    context context_1 {
        @decorator
        event OrderPlaced {
            valueobject EventData {
                data_1:string
                data_1:string
            }
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
"""))
        root = engine.Build(session)
        context: d3i.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.context_events), 1)
        event: d3i.event = context.context_events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.internal_enums), 1)
        self.assertEqual(len(event.internal_value_objects), 1)
        member: d3i.event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.kind, d3i.type.Kind.Primitive)
        self.assertEqual(member.type.primtiveKind, d3i.primitive_type.PrimtiveKind.String)
        self.assertEqual(len(member.decorators), 0)
        member: d3i.event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member: d3i.event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.kind, d3i.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")

if __name__ == "__main__":
    unittest.main()
