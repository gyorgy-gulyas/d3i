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

    def test_conflict_service_event_fail(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain SomeDomain {
    context Order {
        service OrderService {
            event TheEvent version 1 {
            }
            event TheEvent version 1 {
            }
            event OtherEvent version 2{
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
        service OrderService {
            event TheEvent version 1 {
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
        session.PrintDiagnostics()
        self.assertEqual(len(session.diagnostics), 2)
        self.assertTrue("the_member" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(6,16):", "(7,16)"]))
        self.assertTrue("the_member" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,16):", "(6,16)"]))

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
        service TheService {
            eventhandler TheHandler for event NotDefinedEvent
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

if __name__ == "__main__":
    unittest.main()
