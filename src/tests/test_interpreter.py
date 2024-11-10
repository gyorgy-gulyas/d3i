import unittest
import d3i

class TestInterpreter(unittest.TestCase):

    def test_empty_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText( "")
        self.assertIsInstance( root, d3i)
        self.assertEqual(0, len(root.directives))
        self.assertEqual(0, len(root.domains))
    
    def test_directive_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText( "import somedomain")
        self.assertIsInstance( root, d3i)
        self.assertEqual(1, len(root.directives))
        directive: d3i.interpreter.directive = root.directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value, "somedomain")

if __name__ == "__main__":
    unittest.main()
