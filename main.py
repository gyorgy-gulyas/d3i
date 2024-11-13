import d3i

parser = d3i.interpreter.Parser()
d3i = parser.ParseText( """
domain somedomain {
    context context_1 {
        valuessbject Address {
        }
    }
}
""")
parser.PrintTree()
print(d3i)
