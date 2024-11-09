from d3i.interpreter.Parser import Parser

parser = Parser()
d3i = parser.ParseText( """
domain Valami {
}
domain Valami {
}
                 """)
parser.PrintTree()
print(d3i)
