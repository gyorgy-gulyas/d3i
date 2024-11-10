import d3i

parser = d3i.interpreter.Parser()
d3i = parser.ParseText( """
import hello
                 """)
parser.PrintTree()
print(d3i)
