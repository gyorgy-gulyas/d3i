import unittest
import d3i
from d3i.linters import *


class TestLinterSemanticChecker(unittest.TestCase):

    def test_empty_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText(""))
        root = engine.Build(session)

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 0)

    def test_conflict_domain_event_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    event TheEvent {
    }
    event TheEvent {
    }
    event OtherEvent {
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(3,4):","(5,4)" ]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(5,4):","(3,4)" ]))

    def test_conflict_context_event_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    context OrderContext{
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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEvent" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):","(4,8)" ]))

    def test_conflict_event_member_fail(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain SomeDomain {
    event TheEvent {
        the_member:string
        the_member:number
        other_member:number
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("the_member" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(5,8)" ]))
        self.assertTrue("the_member" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(5,8):","(4,8)" ]))

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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(7,8)" ]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,8):","(4,8)" ]))

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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEnum" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(8,12)" ]))
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(8,12):","(5,12)" ]))

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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValue" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(6,12)" ]))
        self.assertTrue("TheValue" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,12):","(5,12)" ]))

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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(6,8):","(4,8)" ]))

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

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 2)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheValueObject" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(5,12):","(7,12)" ]))
        self.assertTrue("TheValueObject" in session.diagnostics[1].toText())
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(7,12):","(5,12)" ]))

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

        self.assertFalse(session.HasErrror())
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
        entity TheEntity {
        }
        entity TheEntity {
        }
        entity OtherEntity {
        }
        aggregate OrderAggregate {
            entity TheEntity {
            }
        }
    }
}
"""))
        root = engine.Build(session)

        self.assertFalse(session.HasErrror())
        checker = SemanticChecker(session)
        data = root.visit(checker, None)
        self.assertEqual(len(session.diagnostics), 6)
        x = session.diagnostics[0].toText()
        self.assertTrue("TheEntity" in session.diagnostics[0].toText())
        self.assertTrue(all(location in session.diagnostics[0].toText() for location in ["(4,8):","(6,8)" ]))
        self.assertTrue(all(location in session.diagnostics[1].toText() for location in ["(4,8):","(11,12)" ]))
        self.assertTrue("TheEntity" in session.diagnostics[2].toText())
        self.assertTrue(all(location in session.diagnostics[2].toText() for location in ["(6,8):","(4,8)" ]))
        self.assertTrue(all(location in session.diagnostics[3].toText() for location in ["(6,8):","(11,12)" ]))
        self.assertTrue("TheEntity" in session.diagnostics[4].toText())
        self.assertTrue(all(location in session.diagnostics[4].toText() for location in ["(11,12):","(4,8)" ]))
        self.assertTrue(all(location in session.diagnostics[5].toText() for location in ["(11,12):","(6,8)" ]))


if __name__ == "__main__":
    unittest.main()
