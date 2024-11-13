import unittest
import d3i


class TestInterpreter(unittest.TestCase):

    def tests_empty_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(0, len(root.directives))
        self.assertEqual(0, len(root.domains))

    def test_lines_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("""
import somedomain
  
  import somedomain
""",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        element: d3i.interpreter.base_element = root.directives[0]
        self.assertEqual(element.line, 2)
        self.assertEqual(element.column, 0)
        self.assertEqual(element.fileName, "internal string")

        element: d3i.interpreter.base_element = root.directives[1]
        self.assertEqual(element.line, 4)
        self.assertEqual(element.column, 2)
        self.assertEqual(element.fileName, "internal string")

    def test_directive_simple_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("import somedomain",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.directives))
        directive: d3i.interpreter.directive = root.directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value.getText(), "somedomain")

    def test_directive_qualified_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("import somedomain.subdomain.subdomain",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.directives))
        directive: d3i.interpreter.directive = root.directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value.getText(),
                         "somedomain.subdomain.subdomain")

    def test_decorator_simple_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("""
@simple
domain somedomain {}
""",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.domains))
        domain: d3i.interpreter.domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: d3i.interpreter.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")

    def test_decorator_multiple_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("""
@simple_1
@simple_2
domain somedomain {}
""",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.domains))
        domain: d3i.interpreter.domain = root.domains[0]
        self.assertEqual(2, len(domain.decorators))
        decorator: d3i.interpreter.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple_1")
        decorator: d3i.interpreter.decorator = domain.decorators[1]
        self.assertEqual(decorator.name, "simple_2")

    def test_decorator_complex_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText("""
@simple( "string", 1, 1.0, identifier.sub.sub )
domain somedomain {}
""",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.domains))
        domain: d3i.interpreter.domain = root.domains[0]
        self.assertEqual(1, len(domain.decorators))
        decorator: d3i.interpreter.decorator = domain.decorators[0]
        self.assertEqual(decorator.name, "simple")
        self.assertEqual(4, len(decorator.params))
        param: d3i.interpreter.decorator_param = decorator.params[0]
        self.assertEqual(
            param.kind, d3i.interpreter.decorator_param.Kind.String)
        self.assertEqual(param.value, "string")
        param: d3i.interpreter.decorator_param = decorator.params[1]
        self.assertEqual(
            param.kind, d3i.interpreter.decorator_param.Kind.Integer)
        self.assertEqual(param.value, 1)
        param: d3i.interpreter.decorator_param = decorator.params[2]
        self.assertEqual(
            param.kind, d3i.interpreter.decorator_param.Kind.Number)
        self.assertEqual(param.value, 1.0)
        param: d3i.interpreter.decorator_param = decorator.params[3]
        self.assertEqual(
            param.kind, d3i.interpreter.decorator_param.Kind.QualifiedName)
        self.assertEqual(param.value.getText(), "identifier.sub.sub")

    def test_context_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    @decorator
    context context_1 {
    }
    @decorator
    context context_2 {
    }
}
""",abortWhenError=True)
        self.assertIsInstance(root, d3i.interpreter.d3i)
        domain: d3i.interpreter.domain = root.domains[0]
        self.assertEqual(2, len(domain.contexts))
        context: d3i.interpreter.context = domain.contexts[0]
        self.assertEqual(context.name, "context_1")
        self.assertEqual(len(context.decorators), 1)
        context: d3i.interpreter.context = domain.contexts[1]
        self.assertEqual(context.name, "context_2")
        self.assertEqual(len(context.decorators), 1)

    def test_enum(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
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
""",abortWhenError=True)
        domain: d3i.interpreter.context = root.domains[0].contexts[0]
        enum: d3i.interpreter.enum = domain.enums[0]
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
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueObject Address {
            @required
            city:string
            street:string
            country:General.Country
            @required
            zipCode:integer
        }
    }
}
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        value_object: d3i.interpreter.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        member: d3i.interpreter.value_object_member = value_object.members[0]
        self.assertEqual(member.name, "city")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: d3i.interpreter.value_object_member = value_object.members[1]
        self.assertEqual(member.name, "street")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.String)
        member: d3i.interpreter.value_object_member = value_object.members[2]
        self.assertEqual(member.name, "country")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(),
                         "General.Country")
        member: d3i.interpreter.value_object_member = value_object.members[3]
        self.assertEqual(member.name, "zipCode")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.Integer)

    def test_value_object_inner_valueobject(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueObject Address {
            valueObject Inner{
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        value_object: d3i.interpreter.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        value_object_inner: d3i.interpreter.value_object = value_object.internal_value_objects[
            0]
        member: d3i.interpreter.value_object_member = value_object_inner.members[0]
        self.assertEqual(member.name, "inner_1")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.String)
        member: d3i.interpreter.value_object_member = value_object_inner.members[1]
        self.assertEqual(member.name, "inner_2")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.Integer)

    def test_value_object_inner_enum(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator_valueobject
        valueObject Address {
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        value_object: d3i.interpreter.value_object = context.value_objects[0]
        self.assertEqual(len(value_object.decorators), 1)
        self.assertEqual(value_object.name, "Address")
        self.assertEqual(len(value_object.members), 4)
        enum_inner: d3i.interpreter.enum = value_object.internal_enums[0]
        self.assertEqual(enum_inner.name, "InnerEnum")
        self.assertEqual(len(enum_inner.enum_elements), 2)

    def test_entity(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        entity: d3i.interpreter.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 2)
        member: d3i.interpreter.entity_member = entity.members[0]
        self.assertEqual(member.name, "name")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType,
                         d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(member.decorators[0].name, "required")
        member: d3i.interpreter.entity_member = entity.members[1]
        self.assertEqual(member.name, "address")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Address")

    def test_entity_inner_enum(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        entity: d3i.interpreter.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_enum: d3i.interpreter.enum = entity.internal_enums[0]
        self.assertEqual(inner_enum.name, "Kind")
        self.assertEqual(len(inner_enum.enum_elements), 2)

    def test_entity_inner_valueobject(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator_entity
        entity Customer {
            valueObject Credit {
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        entity: d3i.interpreter.entity = context.entities[0]
        self.assertEqual(len(entity.decorators), 1)
        self.assertEqual(entity.name, "Customer")
        self.assertEqual(len(entity.members), 3)
        inner_value_object: d3i.interpreter.value_object = entity.internal_value_objects[0]
        self.assertEqual(inner_value_object.name, "Credit")
        self.assertEqual(len(inner_value_object.members), 2)

    def test_aggregate(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        aggregate: d3i.interpreter.aggregate = context.aggregates[0]
        self.assertEqual(len(aggregate.internal_entities), 2)
        order_header:d3i.interpreter.aggregate_entity = aggregate.internal_entities[0]
        self.assertEqual(order_header.entity.name, "OrderHeader")
        self.assertEqual(order_header.isRoot, True)
        order_item:d3i.interpreter.aggregate_entity = aggregate.internal_entities[1]
        self.assertEqual(order_item.entity.name, "OrderItem")
        self.assertEqual(order_item.isRoot, False)
        
    def test_repository(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
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
""",abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        repository: d3i.interpreter.repository = context.repositories[0]
        self.assertEqual(repository.name, "orders")
        self.assertEqual(repository.element_name.getText(), "Order")
        repository: d3i.interpreter.repository = context.repositories[1]
        self.assertEqual(repository.name, "customers")
        self.assertEqual(repository.element_name.getText(), "Customer")

    def test_context_event(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator
        event OrderPlaced {
            valueObject EventData {
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
""", abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.context_events), 1)
        event: d3i.interpreter.event = context.context_events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.internal_enums), 1)
        self.assertEqual(len(event.internal_value_objects), 1)
        member:d3i.interpreter.event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType, d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(len(member.decorators), 0)
        member:d3i.interpreter.event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member:d3i.interpreter.event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")

    def test_domain_event(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context Empty {
    }
    @decorator
    event OrderPlaced {
        valueObject EventData {
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
""", abortWhenError=True)
        domain: d3i.interpreter.domain = root.domains[0]
        self.assertEqual(len(domain.domain_events), 1)
        event: d3i.interpreter.event = domain.domain_events[0]
        self.assertEqual(event.name, "OrderPlaced")
        self.assertEqual(len(event.members), 3)
        self.assertEqual(len(event.internal_enums), 1)
        self.assertEqual(len(event.internal_value_objects), 1)
        member:d3i.interpreter.event_member = event.members[0]
        self.assertEqual(member.name, "orderId")
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(member.type.PrimtiveType, d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(len(member.decorators), 0)
        member:d3i.interpreter.event_member = event.members[1]
        self.assertEqual(member.name, "importance")
        self.assertEqual(len(member.decorators), 0)
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "Importance")
        member:d3i.interpreter.event_member = event.members[2]
        self.assertEqual(member.name, "data")
        self.assertEqual(len(member.decorators), 1)
        self.assertEqual(member.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(member.type.reference_name.getText(), "EventData")


    def test_acl(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator
        acl CustomerACL {
            valueObject OrderData {
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
""", abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.acls), 1)
        acl: d3i.interpreter.acl = context.acls[0]
        self.assertEqual(acl.name, "CustomerACL")
        self.assertEqual(len(acl.methods), 1)
        self.assertEqual(len(acl.internal_enums), 1)
        self.assertEqual(len(acl.internal_value_objects), 1)
        method:d3i.interpreter.method = acl.methods[0]
        self.assertEqual(method.name, "getOrderData")
        self.assertEqual(len(method.decorators), 1)
        self.assertEqual(len(method.method_params), 1)
        method_param:d3i.interpreter.method_param = method.method_params[0]
        self.assertEqual(method_param.name, "customerId")
        self.assertEqual(method_param.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(method_param.type.PrimtiveType, d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(len(method_param.decorators), 1)
        self.assertEqual(method.return_type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(method.return_type.reference_name.getText(), "OrderData" )

    def test_service(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator
        service OrderService {
            valueObject OrderData {
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
""", abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.services), 1)
        service: d3i.interpreter.service = context.services[0]
        self.assertEqual(service.name, "OrderService")
        self.assertEqual(len(service.operations), 1)
        self.assertEqual(len(service.internal_enums), 1)
        self.assertEqual(len(service.internal_value_objects), 1)
        operation:d3i.interpreter.operation = service.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param:d3i.interpreter.operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(operation_param.type.PrimtiveType, d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return:d3i.interpreter.operation_return = operation.operation_returns[0]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderData" )
        operation_return:d3i.interpreter.operation_return = operation.operation_returns[1]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "ErrorNotFound" )

    def test_interface(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText(
            """
domain somedomain {
    context context_1 {
        @decorator
        interface OrderService {
            valueObject OrderDTO {
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
""", abortWhenError=True)
        context: d3i.interpreter.context = root.domains[0].contexts[0]
        self.assertEqual(len(context.interfaces), 1)
        interface: d3i.interpreter.interface = context.interfaces[0]
        self.assertEqual(interface.name, "OrderService")
        self.assertEqual(len(interface.operations), 1)
        self.assertEqual(len(interface.internal_enums), 1)
        self.assertEqual(len(interface.internal_value_objects), 1)
        operation:d3i.interpreter.operation = interface.operations[0]
        self.assertEqual(operation.name, "getOrder")
        self.assertEqual(len(operation.decorators), 1)
        self.assertEqual(len(operation.operation_params), 1)
        operation_param:d3i.interpreter.operation_param = operation.operation_params[0]
        self.assertEqual(operation_param.name, "orderId")
        self.assertEqual(operation_param.type.Kind, d3i.interpreter.type.Kind.Primitive)
        self.assertEqual(operation_param.type.PrimtiveType, d3i.interpreter.primitive_type.PrimtiveType.String)
        self.assertEqual(len(operation_param.decorators), 1)
        operation_return:d3i.interpreter.operation_return = operation.operation_returns[0]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "OrderDTO" )
        operation_return:d3i.interpreter.operation_return = operation.operation_returns[1]
        self.assertEqual(len(operation_return.decorators), 1)
        self.assertEqual(operation_return.type.Kind, d3i.interpreter.type.Kind.Reference)
        self.assertEqual(operation_return.type.reference_name.getText(), "ErrorNotFound" )

if __name__ == "__main__":
    unittest.main()
