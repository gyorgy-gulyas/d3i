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

    def test_same_name_domain_event_fail(self):
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
        self.assertTrue("(3,4)" in session.diagnostics[0].toText())
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue("(5,4)" in session.diagnostics[1].toText())

    def test_same_name_context_event_fail(self):
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
        self.assertTrue("(4,8)" in session.diagnostics[0].toText())
        self.assertTrue("TheEvent" in session.diagnostics[1].toText())
        self.assertTrue("(6,8)" in session.diagnostics[1].toText())

    def test_same_name_event_member_fail(self):
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
        self.assertTrue("(4,8)" in session.diagnostics[0].toText())
        self.assertTrue("the_member" in session.diagnostics[1].toText())
        self.assertTrue("(5,8)" in session.diagnostics[1].toText())

    def test_same_name_context_enum_fail(self):
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
        self.assertTrue("(4,8)" in session.diagnostics[0].toText())
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue("(7,8)" in session.diagnostics[1].toText())


    def test_same_name_inner_enum_fail(self):
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
        self.assertTrue("(5,12)" in session.diagnostics[0].toText())
        self.assertTrue("TheEnum" in session.diagnostics[1].toText())
        self.assertTrue("(8,12)" in session.diagnostics[1].toText())

    def test_same_name_enum_element_fail(self):
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
        self.assertTrue("(5,12)" in session.diagnostics[0].toText())
        self.assertTrue("TheValue" in session.diagnostics[1].toText())
        self.assertTrue("(6,12)" in session.diagnostics[1].toText())

if __name__ == "__main__":
    unittest.main()
