import unittest
import d3i

class TestInterpreter(unittest.TestCase):

    def tests_empty_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText( "")
        self.assertIsInstance( root, d3i.interpreter.d3i)
        self.assertEqual(0, len(root.directives))
        self.assertEqual(0, len(root.domains))
    
    def test_directive_simple_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText( "import somedomain")
        self.assertIsInstance( root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.directives))
        directive: d3i.interpreter.directive = root.directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value.getText(), "somedomain")

    def test_directive_qualified_ok(self):
        parser = d3i.interpreter.Parser()
        root = parser.ParseText( "import somedomain.subdomain.subdomain")
        self.assertIsInstance( root, d3i.interpreter.d3i)
        self.assertEqual(1, len(root.directives))
        directive: d3i.interpreter.directive = root.directives[0]
        self.assertEqual(directive.keyword, "import")
        self.assertEqual(directive.value.getText(), "somedomain.subdomain.subdomain")

if __name__ == "__main__":
    unittest.main()
