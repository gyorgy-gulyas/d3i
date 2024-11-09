import unittest
import d3i.interpreter as d3i

class TestInterpreter(unittest.TestCase):

    def test_empty_ok(self):
        parser = d3i.Parser()
        root:d3i = parser.ParseText( "")
        self.assertIsInstance( root, d3i)
        self.assertEqual(0, len(root.directives))
        self.assertEqual(0, len(root.domains))
    
    def test_directive_ok(self):
        parser = d3i.Parser()
        root:d3i = parser.ParseText( "import somedomain")
        self.assertIsInstance( root, d3i)
        self.assertEqual(1, len(root.directives))
        directives: d3i.directive = root.directives[0]

if __name__ == "__main__":
    unittest.main()
