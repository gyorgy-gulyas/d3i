import unittest
import d3i
from d3i.linters import *


class TestLinterSemanticChecker(unittest.TestCase):

    def test_empty_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText(""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 0)

    def test_conflict_service_event_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service OrderService {
            event TheEvent {
            }
            event TheEvent {
            }
            event OtherEvent {
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(7,12)"]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):", "(5,12)"]))

    def test_conflict_interface_event_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface IOrderInterface {
            event TheEvent {
            }
            event TheEvent {
            }
            event OtherEvent {
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(7,12)"]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):", "(5,12)"]))

    def test_conflict_event_member_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service OrderService {
            event TheEvent {
                the_member:string
                the_member:number
                other_member:number
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("the_member" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(6,16):", "(7,16)"]))
        self.assertTrue("the_member" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,16):", "(6,16)"]))

    def test_conflict_context_enum_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        enum TheEnum {
            Value    
        }
        enum TheEnum {
            Value
        }
        enum OtherEnum {
            Value
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(7,8)"]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,8):", "(4,8)"]))

    def test_conflict_inner_enum_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        service OrderService { 
            enum TheEnum {
                Value    
            }
            enum TheEnum {
                Value
            }
            enum OtherEnum {
                Value
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(8,12)"]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(8,12):", "(5,12)"]))

    def test_conflict_enum_element_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        enum SomeEnum {
            TheValue,
            TheValue,
            OtherValue
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValue" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("TheValue" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_context_valueobject_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        valueobject TheValueObject {
        }
        valueobject TheValueObject {
        }
        valueobject OtherValueObject {
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_inner_valueobject_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        service OrderService { 
            valueobject TheValueObject {
            }
            valueobject TheValueObject {
            }
            valueobject OtherValueObject {
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(7,12)"]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):", "(5,12)"]))

    def test_conflict_valueobject_member_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        valueobject SomeValueobject {
            TheMember:string
            TheMember:number
            OtherMember:date
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheMember" in session.diagnostics[0].toText())
        self.assertTrue("(5,12)" in session.diagnostics[0].toText())
        self.assertTrue("TheMember" in session.diagnostics[1].toText())
        self.assertTrue("(6,12)" in session.diagnostics[1].toText())

    def test_conflict_entity_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        aggregate OrderAggregate {
            root entity TheEntity {
            }
            entity TheEntity {
            }
            entity OtherEntity {
            }
        }
        aggregate OrderAggregate2 {
            root entity TheEntity {
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 6)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEntity" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,17):", "(7,12)"]))
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(5,17):", "(13,17)"]))
        self.assertTrue("TheEntity" in session.diagnostics[2].toText())
        self.assertTrue(all(location in session.diagnostics[2].toText() for location in ["(7,12):", "(5,17)"]))
        self.assertTrue(all(location in session.diagnostics[3].toText() for location in ["(7,12):", "(13,17)"]))
        self.assertTrue("TheEntity" in session.diagnostics[4].toText())
        self.assertTrue(all(location in session.diagnostics[4].toText() for location in ["(13,17):", "(5,17)"]))
        self.assertTrue(all(location in session.diagnostics[5].toText() for location in ["(13,17):", "(7,12)"]))

    def test_conflict_entity_member_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        aggregate OrderAggregate {
            root entity TheEntity {
                TheMember:string
                TheMember:number
                OtherMember:date
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheMember" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(6,16):", "(7,16)"]))
        self.assertTrue("TheMember" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,16):", "(7,16)"]))

    def test_conflict_aggreaget_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        aggregate TheAggregate {
            root entity TheEntity1 {
                member:string
            }
        }
        aggregate TheAggregate {
            root entity TheEntity2 {
                member:string
            }
        }
        aggregate OtherAggregate {
            root entity TheEntity3 {
                member:string
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(9,8)"]))
        self.assertTrue("TheAggregate" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(9,8):", "(4,8)"]))

    def test_aggregate_no_root_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        aggregate OrderAggregate {
            entity TheEntity {
                TheMember:string
                OtherMember:date
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        x = session.diagnostics[0].toText()
        self.assertTrue("OrderAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8)", "There is no root"]))

    def test_aggregate_more_root_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        aggregate OrderAggregate {
            root entity TheEntity {
                TheMember:string
                OtherMember:date
            }
            root entity TheEntity2 {
                TheMember:number
                OtherMember:date
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        x = session.diagnostics[0].toText()
        self.assertTrue("OrderAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8)", "More than one root"]))

    def test_repository_unknown_reference_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        repository TheRepository : NotDefined
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheRepository" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8)", "NotDefined"]))

    def test_conflict_acl_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheAcl {
        }
        acl TheAcl {
        }
        acl OtherAcl {
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheAcl" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue("TheAcl" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):","(4,8)" ]))

    def test_conflict_acl_operation_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheAcl {
            TheOperation()
            TheOperation()
            OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(6,12)" ]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):","(5,12)" ]))

    def test_conflict_service_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        service TheService {
        }
        service TheService {
        }
        service OtherService {
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheService" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue("TheService" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):","(4,8)" ]))

    def test_conflict_service_operation_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheService {
            TheOperation()
            TheOperation()
            OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(6,12)" ]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):","(5,12)" ]))


    def test_conflict_interface_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface TheInterface {
        }
        interface TheInterface {
        }
        interface OtherInterface {
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheInterface" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue("TheInterface" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):","(4,8)" ]))


    def test_conflict_interface_operation_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheInterface {
            TheOperation()
            TheOperation()
            OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(6,12)" ]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):","(5,12)" ]))

if __name__ == "__main__":
    unittest.main()
