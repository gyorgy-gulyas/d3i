import unittest
from d3i.Engine import *
from d3i.linters.SemanticChecker import *


class TestLinterSemanticChecker(unittest.TestCase):

    def test_empty_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText(""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 0)

    def test_conflict_context_event_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        event TheEvent {
        }
        event TheEvent {
        }
        event OtherEvent {
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_interface_event_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface IOrderInterface version 1 {
            event TheEvent version 1 {
            }
            event TheEvent version 1 {
            }
            event OtherEvent version 2 {
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(7,12)"]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):", "(5,12)"]))

    def test_conflict_event_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        event TheEvent {
            the_member:string
            the_member:number
            other_member:number
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("the_member" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("the_member" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_context_enum_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(7,8)"]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,8):", "(4,8)"]))

    def test_conflict_inner_enum_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(8,12)"]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(8,12):", "(5,12)"]))

    def test_conflict_enum_element_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheValue" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("TheValue" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_context_valueobject_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_inner_valueobject_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(7,12)"]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):", "(5,12)"]))

    def test_conflict_valueobject_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheMember" in session.diagnostics[0].toText())
        self.assertTrue("(5,12)" in session.diagnostics[0].toText())
        self.assertTrue("TheMember" in session.diagnostics[1].toText())
        self.assertTrue("(6,12)" in session.diagnostics[1].toText())

    def test_conflict_entity_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 6)
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
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheMember" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(6,16):", "(7,16)"]))
        self.assertTrue("TheMember" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,16):", "(7,16)"]))

    def test_conflict_aggregate_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(9,8)"]))
        self.assertTrue("TheAggregate" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(9,8):", "(4,8)"]))

    def test_conflict_all_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        enum TheName { }
        valueobject TheName { }
        aggregate TheName { root entity TheEntity{}}
        view TheName { }
        repository TheName {}
        acl TheName {}
        service TheName {}
        interface TheName version 1 {}
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 56)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]

        self.assertTrue(any(all(x in s for x in ["TheName", "(4,8):", "(5,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(4,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(5,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(5,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(6,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(6,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(7,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(7,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(8,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(8,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(9,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(10,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(9,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(10,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(10,8):', '(11,8)']) for s in messages))

        self.assertTrue(any(all(x in s for x in ["TheName", "(11,8):", "(4,8)"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(5,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(6,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(7,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(8,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(9,8)']) for s in messages))
        self.assertTrue(any(all(x in s for x in ['TheName', '(11,8):', '(10,8)']) for s in messages))

    def test_aggregate_no_root_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("OrderAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8)", "There is no root"]))

    def test_aggregate_more_root_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("OrderAggregate" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8)", "More than one root"]))

    def test_conflict_acl_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheAcl" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheAcl" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_acl_operation_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheAcl {
            command TheOperation()
            command TheOperation()
            command OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_service_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheService" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheService" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_service_operation_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        acl TheService {
            command TheOperation()
            command TheOperation()
            command OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_interface_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface TheInterface version 1 {
        }
        interface TheInterface version 1 {
        }
        interface OtherInterface version 2 {
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheInterface" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):", "(6,8)"]))
        self.assertTrue("TheInterface" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):", "(4,8)"]))

    def test_conflict_interface_operation_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface TheInterface version 1 {
            command TheOperation()
            command TheOperation()
            command OtherOperation()
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("TheOperation" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):", "(6,12)"]))
        self.assertTrue("TheOperation" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):", "(5,12)"]))

    def test_conflict_operation_param_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface TheInterface version 1 {
            command TheOperation1( param: string )
            command TheOperation2( already: string, already: string, other: integer)
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("already" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(6,35):", "(6,52)"]))
        self.assertTrue("already" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,52):", "(6,35)"]))

    def test_reference_type_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
        interface TheInterface version 1 {
        }
        interface TheInterface version 2 {
            dto dto_out{
                dto dto_inner{
                    enum enum_inner{
                    }    
                }    
            }    
            enum enum_out{
            }    
            event event_out version 1 {
            }    
            event event_out version 2{
                enum enum_inner {
                }    
            }    
        }

        service TheService {
            valueobject vo_out{
                valueobject vo_inner{
                    enum enum_inner{
                    }    
                }    
            }    
            enum enum_out{
            }    
        }
        service OtherService {
            valueobject vo_out{
                valueobject vo_inner{
                    enum enum_inner{
                    }    
                }

                member_0: TheInterface.v2.event_out.v2.enum_inner
                member_1: vo_inner
                member_2: vo_inner.enum_inner
                member_3: enum_out
                member_4: TheService.vo_out.vo_inner.enum_inner
            }    
            enum enum_out{
            }    
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 0)

    def test_inheritence_wrong_type_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
            aggregate Order {
                root entity TheEntity inherits TheInterface.TheEvent{
                }    
            }
            valueobject TheValueObject inherits Order.TheEntity{
            }                                                    
            interface TheInterface version 1 {
                event TheEvent version 1 inherits TheValueObject{
            }    
        }
    }
}
"""))
        root = engine.Build(session)
        session.PrintDiagnostics()
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 3)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]

        self.assertTrue(any(all(x in s for x in ["TheInterface.TheEvent", "(5,47):"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ["Order.TheEntity", "(8,48):"]) for s in messages))
        self.assertTrue(any(all(x in s for x in ["TheValueObject", "(11,50):"]) for s in messages))

    def test_conflict_dto_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface TheInterface version 1 {
            dto TheDto { }
            dto TheDto { }
            dto OtherDto { }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]
        self.assertTrue(all("TheDto" in s and "conflicts" in s for s in messages))

    def test_conflict_dto_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface TheInterface version 1 {
            dto TheDto {
                member:string
                member:integer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]
        self.assertTrue(all("member" in s and "conflicts" in s for s in messages))

    def test_conflict_composite_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        composite TheComposite { }
        composite TheComposite { }
        composite OtherComposite { }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]
        self.assertTrue(all("TheComposite" in s and "conflicts" in s for s in messages))

    def test_conflict_composite_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        composite TheComposite {
            member:string
            member:integer
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]
        self.assertTrue(all("member" in s and "conflicts" in s for s in messages))

    def test_conflict_repository_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        repository TheRepository { }
        repository TheRepository { }
        repository OtherRepository { }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        messages = [diagnostic.toText() for diagnostic in session.diagnostics]
        self.assertTrue(all("TheRepository" in s and "already exists" in s for s in messages))

    def test_inheritance_not_found_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject TheValueObject inherits NotDefined { }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("NotDefined" in session.diagnostics[0].toText())
        self.assertTrue("inheritance is not found" in session.diagnostics[0].toText())

    def test_eventhandler_unknown_event_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        eventhandler TheHandler for event NotDefinedEvent
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("NotDefinedEvent" in session.diagnostics[0].toText())
        self.assertTrue("handled event" in session.diagnostics[0].toText())

    def test_view_projection_unknown_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        view TheView projected: NotDefined { }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("NotDefined" in session.diagnostics[0].toText())
        self.assertTrue("projection is not found" in session.diagnostics[0].toText())

    def test_invalid_list_type_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject TheValueObject {
            data: list[ list[ string ] ]
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("list can only contain" in session.diagnostics[0].toText())

    def test_conflict_view_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        view TheView {
            member:string
            member:integer
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue(all("member" in s.toText() and "conflicts" in s.toText() for s in session.diagnostics))

    def test_any_on_field_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Bag {
            data: any
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'any' type is not allowed on a domain model field" in session.diagnostics[0].toText())

    def test_stream_on_field_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Bag {
            data: stream
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'stream' type is not allowed on a field" in session.diagnostics[0].toText())

    def test_stream_on_dto_member_fail(self):
        # A DTO is a transferred VALUE, not a channel: a file belongs in the operation's signature,
        # and what a DTO can carry about it is a reference or its metadata.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface OrderIF version 1 {
            dto UploadDto {
                content: stream
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'stream' type is not allowed on a field" in session.diagnostics[0].toText())

    def test_stream_in_a_list_on_a_dto_member_fail(self):
        # The list/map wrapper must not hide the stream from the rule.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface OrderIF version 1 {
            dto UploadDto {
                contents: list[stream]
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'stream' type is not allowed on a field" in session.diagnostics[0].toText())

    def test_stream_on_event_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        event Uploaded {
            content: stream
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'stream' type is not allowed on a field" in session.diagnostics[0].toText())

    def test_any_on_dto_member_ok(self):
        # A DTO is the boundary: 'any' stays allowed there, only 'stream' is refused.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        interface OrderIF version 1 {
            dto BagDto {
                data: any
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 0)

    def test_any_stream_in_operation_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            command send( payload:any ) : stream
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 0)

    def test_bare_aggregate_reference_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        aggregate OrderAggregate {
            root entity OrderHeader {
                customer: Customer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must be referenced by identity" in session.diagnostics[0].toText())
        self.assertTrue("ref Customer" in session.diagnostics[0].toText())

    def test_ref_to_non_aggregate_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money { amount:number }
        aggregate OrderAggregate {
            root entity OrderHeader {
                price: ref Money
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("may only reference an aggregate" in session.diagnostics[0].toText())

    def test_workflow_unknown_compensate_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        workflow OrderSaga {
            command start( orderId:string )
            step reserveStock( orderId:string ) compensate nonExistentStep
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("nonExistentStep" in session.diagnostics[0].toText())
        self.assertTrue("is not found in workflow" in session.diagnostics[0].toText())

    def test_query_emits_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service TheService {
            query getIt( id:string ) : string emits SomeEvent
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("getIt" in session.diagnostics[0].toText())
        self.assertTrue("cannot emit events" in session.diagnostics[0].toText())

    def test_valueobject_command_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money {
            amount:number
            command setAmount( value:number )
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("setAmount" in session.diagnostics[0].toText())
        self.assertTrue("cannot be a command" in session.diagnostics[0].toText())

    def test_invalid_map_type_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject TheValueObject {
            data: map[ string, list[ string ] ]
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("Value of map can only contain" in session.diagnostics[0].toText())

    def test_interface_surface_valueobject_member_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money { amount:number }
        interface OrderIF version 1 {
            dto OrderDto {
                total: Money
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("may only expose dto, enum and primitive" in session.diagnostics[0].toText())
        self.assertTrue("Money" in session.diagnostics[0].toText())

    def test_interface_surface_operation_param_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        valueobject Money { amount:number }
        interface OrderIF version 1 {
            query convert( m: Money ) : string
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("may only expose dto, enum and primitive" in session.diagnostics[0].toText())

    def test_interface_surface_ok(self):
        # dto/enum/primitive members and a ref (string on the wire) are all allowed.
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        aggregate Customer {
            root entity CustomerRoot { id:string }
        }
        interface OrderIF version 1 {
            enum Status { New, Done }
            dto Line { sku:string }
            dto OrderDto {
                id: string
                status: Status
                line: Line
                owner: ref Customer
            }
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())

        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 0)

    def test_validate_ok(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            start: number
            end: number validate value > start
            name: string validate len(value) <= 10 AND matches(value, "^a")
            grade: integer validate value IN 1..5
        }
    }
}
"""))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError())
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 0)

    def test_validate_unknown_identifier_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            x: number validate value > nope
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("nope" in session.diagnostics[0].toText())
        self.assertTrue("not 'value' nor a sibling field" in session.diagnostics[0].toText())

    def test_validate_unknown_function_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            x: string validate size(value) > 0
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("Unknown function 'size'" in session.diagnostics[0].toText())

    def test_validate_type_mismatch_fail(self):
        # you cannot order-compare a string ( `> 0` needs a number/date )
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            name: string validate value > 0
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("needs ordered values" in session.diagnostics[0].toText())

    def test_validate_len_on_number_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            n: integer validate len(value) > 0
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'len'" in session.diagnostics[0].toText())
        self.assertTrue("string or a list/map" in session.diagnostics[0].toText())

    def test_validate_dto_type_mismatch_fail(self):
        # DTO validate is type-checked too: `> 0` on a string dto member is an error
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        interface OrderIF version 1 {
            dto CreateOrder {
                name: string validate value > 0
            }
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("needs ordered values" in session.diagnostics[0].toText())

    def test_validate_not_boolean_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        valueobject V {
            x: number validate 5
        }
    }
}
"""))
        root = engine.Build(session)
        checker = SemanticChecker(session)
        root.visit(checker, None)
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must be a boolean condition" in session.diagnostics[0].toText())

    # ------------------------------------------------------------------
    # workflow rules — L1 (@start), L3/L4 (compensation), L5 (step surface),
    # L6/L7 (@retry/@timeout), L8 (ignored compensation return)
    # ------------------------------------------------------------------

    def __lint(self, source: str):
        engine = Engine()
        session = Session(Source.CreateFromText(source))
        root = engine.Build(session)
        self.assertFalse(session.HasAnyError(), "the source must parse before it can be linted")
        root.visit(SemanticChecker(session), None)
        session.PrintDiagnostics()
        return session

    def __wrap(self, workflow_body: str) -> str:
        return """
domain SomeDomain {
    context Order {
        enum Currency { HUF, EUR }
        valueobject Money { amount:number }
        composite Auditable { createdAt:dateTime }
        aggregate OrderAggregate {
            root entity OrderHeader { id:string }
        }
        workflow OrderSaga {
%s
        }
    }
}
""" % workflow_body

    def test_workflow_single_command_is_implicit_start_ok(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            query status( orderId:string ) : string
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_workflow_no_command_fail(self):
        session = self.__lint(self.__wrap("""
            step reserveStock( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("has no command" in session.diagnostics[0].toText())

    def test_workflow_many_commands_without_start_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            command cancel( reason:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("none is marked with '@start'" in session.diagnostics[0].toText())
        self.assertTrue("'place', 'cancel'" in session.diagnostics[0].toText())

    def test_workflow_many_commands_with_start_ok(self):
        session = self.__lint(self.__wrap("""
            @start
            command place( orderId:string )
            command cancel( reason:string )
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_workflow_two_starts_fail(self):
        session = self.__lint(self.__wrap("""
            @start
            command place( orderId:string )
            @start
            command replace( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("only one '@start' command" in session.diagnostics[0].toText())
        self.assertTrue("'place'" in session.diagnostics[0].toText())

    def test_workflow_start_on_query_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @start
            query status( orderId:string ) : string
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("may only mark a command" in session.diagnostics[0].toText())

    def test_compensation_binding_ok(self):
        # orderId binds by name+type, chargeId by the unambiguous return type
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( orderId:string, amount:number ) : string compensate refundCard
            step refundCard( orderId:string, chargeId:string )
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_compensation_unbindable_param_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( orderId:string, amount:number ) : string compensate refundCard
            step refundCard( orderId:string, reasonCode:integer )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'reasonCode'" in session.diagnostics[0].toText())
        self.assertTrue("cannot be bound" in session.diagnostics[0].toText())

    def test_compensation_without_return_unbindable_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step reserveStock( orderId:string ) compensate releaseStock
            step releaseStock( orderId:string, sku:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'sku'" in session.diagnostics[0].toText())
        self.assertTrue("returns nothing" in session.diagnostics[0].toText())

    def test_compensation_name_matches_but_type_differs_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step reserveStock( orderId:string ) compensate releaseStock
            step releaseStock( orderId:integer )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("but a different type" in session.diagnostics[0].toText())

    def test_compensation_ambiguous_return_binding_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( amount:number ) : string compensate refundCard
            step refundCard( chargeId:string, receiptId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("could all be bound to the return value" in session.diagnostics[0].toText())
        self.assertTrue("'chargeId', 'receiptId'" in session.diagnostics[0].toText())

    def test_compensation_binds_value_object_by_name_ok(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( price:Money ) compensate refundCard
            step refundCard( price:Money )
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_nested_compensation_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( orderId:string ) compensate refundCard
            step refundCard( orderId:string ) compensate notifyFailure
            step notifyFailure( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("cannot declare a 'compensate' of its own" in session.diagnostics[0].toText())

    def test_compensation_return_is_ignored_warning(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step chargeCard( orderId:string ) compensate refundCard
            step refundCard( orderId:string ) : boolean
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertEqual(session.diagnostics[0].severity, Diagnostic.Severity.Warning)
        self.assertTrue("is ignored" in session.diagnostics[0].toText())

    def test_step_surface_allowed_types_ok(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step charge( price:Money, currency:Currency, order: ref OrderAggregate, tags:list[string], meta:map[string,integer] ) : Money
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_step_stream_param_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step upload( content:stream )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'stream' type is not allowed in a step signature" in session.diagnostics[0].toText())
        self.assertTrue("the parameter 'content'" in session.diagnostics[0].toText())

    def test_step_any_return_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step callExternal( id:string ) : any
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'any' type is not allowed in a step signature" in session.diagnostics[0].toText())
        self.assertTrue("the return value" in session.diagnostics[0].toText())

    def test_step_any_inside_list_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step callExternal( payloads:list[any] )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("'any' type is not allowed in a step signature" in session.diagnostics[0].toText())

    def test_command_may_still_take_stream_and_any_ok(self):
        # W11/W13 narrow the step only; the command/query surface is untouched (Q10).
        session = self.__lint(self.__wrap("""
            command place( content:stream, extra:any )
"""))
        self.assertEqual(len(session.diagnostics), 0)

    def test_step_composite_param_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            step writeAuditTrail( entry:Auditable )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("may only carry enum, value object" in session.diagnostics[0].toText())
        self.assertTrue("composite" in session.diagnostics[0].toText())

    def test_retry_and_timeout_ok(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        @retry( 3 )
        @timeout( "2m" )
        workflow OrderSaga {
            command place( orderId:string )
            @retry( 1 )
            @timeout( "1h30m" )
            step sendReceipt( orderId:string )
            @timeout( "500ms" )
            step ping( orderId:string )
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 0)

    def test_retry_zero_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @retry( 0 )
            step charge( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must be at least 1" in session.diagnostics[0].toText())

    def test_retry_non_integer_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @retry( "3" )
            step charge( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("takes exactly one integer argument" in session.diagnostics[0].toText())

    def test_workflow_retry_invalid_fail(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        @retry( 0 )
        workflow OrderSaga {
            command place( orderId:string )
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("workflow 'OrderSaga'" in session.diagnostics[0].toText())
        self.assertTrue("must be at least 1" in session.diagnostics[0].toText())

    def test_timeout_not_a_duration_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @timeout( "5 minutes" )
            step charge( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("is not a duration" in session.diagnostics[0].toText())

    def test_timeout_zero_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @timeout( "0s" )
            step charge( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("is zero" in session.diagnostics[0].toText())

    def test_timeout_non_string_fail(self):
        session = self.__lint(self.__wrap("""
            command place( orderId:string )
            @timeout( 5 )
            step charge( orderId:string )
"""))
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("takes exactly one string argument" in session.diagnostics[0].toText())

    # ---- D3I-50: a version is a promise, and a promise needs someone to make it to -------------

    def test_an_eventsourced_aggregate_event_must_be_versioned(self):
        # The fact stays in the stream longer than the code that wrote it, so the code that reads it
        # back will be newer than the code that produced it - the same compatibility problem as with
        # a foreign team, only against your own past.
        session = self.__lint("""
domain SomeDomain {
    context Order {
        eventsourced aggregate Account {
            root entity AccountHeader {
                @partitionKey
                accountId:string
                command open( owner:string ) emits Opened
            }
            event Opened { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must declare a version" in session.diagnostics[0].toText())
        self.assertTrue("eventsourced" in session.diagnostics[0].toText())

    def test_an_eventsourced_aggregate_event_with_a_version_is_ok(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        eventsourced aggregate Account {
            root entity AccountHeader {
                @partitionKey
                accountId:string
                command open( owner:string ) emits Opened.v1
            }
            event Opened version 1 { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 0)

    def test_an_internal_event_must_not_be_versioned(self):
        # Its consumers ship in the same deployment unit and move with it, so breaking the shape is
        # a compile error. A version would promise a stability nobody is keeping.
        session = self.__lint("""
domain SomeDomain {
    context Order {
        event DailyClosingCompleted version 1 { orderCount:number }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must not declare a version" in session.diagnostics[0].toText())

    def test_an_internal_event_without_a_version_is_ok(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        event DailyClosingCompleted { orderCount:number }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 0)

    def test_an_event_of_a_plain_aggregate_must_not_be_versioned(self):
        # Not eventsourced: the fact is a passing message, not a stored one.
        session = self.__lint("""
domain SomeDomain {
    context Order {
        aggregate Account {
            root entity AccountHeader {
                @partitionKey
                accountId:string
                command open( owner:string ) emits Opened.v1
            }
            event Opened version 1 { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must not declare a version" in session.diagnostics[0].toText())

    def test_a_published_event_must_be_versioned(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        interface OrderIF version 1 {
            event OrderPlaced { orderId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("must declare a version" in session.diagnostics[0].toText())
        self.assertTrue("another team reads it" in session.diagnostics[0].toText())

    def test_an_integration_event_must_be_versioned_wherever_it_is(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        integration event Shipped { orderId:string }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("contract with somebody outside" in session.diagnostics[0].toText())

    def test_an_audit_event_must_be_versioned(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        audit event Exported { orderId:string }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("kept for years" in session.diagnostics[0].toText())

    # ---- D3I-50: the ordering scope -----------------------------------------------------------

    def test_a_recording_root_without_a_partition_key_is_warned_about(self):
        # Not fatal - the generated Record simply asks for the key - but it is almost always a
        # mistyped decorator, and finding that out from a compiler error in hand-written code is a
        # bad way to find it out. Note the deliberate typo below.
        session = self.__lint("""
domain SomeDomain {
    context Order {
        aggregate Account {
            root entity AccountHeader {
                @partitonKey
                accountId:string
                command open( owner:string ) emits Opened
            }
            event Opened { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("no member is marked" in session.diagnostics[0].toText())
        self.assertEqual(Diagnostic.Severity.Warning, session.diagnostics[0].severity)

    def test_an_eventsourced_root_without_a_partition_key_is_an_error(self):
        # An eventsourced aggregate IS its stream, and a stream without a key cannot be read back.
        session = self.__lint("""
domain SomeDomain {
    context Order {
        eventsourced aggregate Account {
            root entity AccountHeader {
                accountId:string
                command open( owner:string ) emits Opened.v1
            }
            event Opened version 1 { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("cannot be read back without it" in session.diagnostics[0].toText())
        self.assertEqual(Diagnostic.Severity.Error, session.diagnostics[0].severity)

    def test_a_root_that_records_nothing_needs_no_partition_key(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        aggregate Account {
            root entity AccountHeader { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 0)

    def test_two_partition_keys_on_a_root_is_an_error(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        aggregate Account {
            root entity AccountHeader {
                @partitionKey
                accountId:string
                @partitionKey
                tenantId:string
                command open( owner:string ) emits Opened
            }
            event Opened { accountId:string }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("More than one member" in session.diagnostics[0].toText())
        self.assertTrue("ordered against one thing" in session.diagnostics[0].toText())

    def test_a_partition_key_on_a_non_root_entity_has_no_effect(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        aggregate Account {
            root entity AccountHeader { accountId:string }
            entity AccountLine {
                @partitionKey
                lineId:string
            }
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("has no effect" in session.diagnostics[0].toText())
        self.assertEqual(Diagnostic.Severity.Warning, session.diagnostics[0].severity)

    def test_two_partition_keys_on_an_event_is_an_error(self):
        session = self.__lint("""
domain SomeDomain {
    context Order {
        event DailyClosingCompleted {
            @partitionKey
            businessDay:date
            @partitionKey
            region:string
        }
    }
}
""")
        self.assertEqual(len(session.diagnostics), 1)
        self.assertTrue("More than one member" in session.diagnostics[0].toText())


if __name__ == "__main__":
    unittest.main()
