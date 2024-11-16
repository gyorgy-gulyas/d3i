import d3i

parser = d3i.elements.Parser()
d3i = parser.ParseText( """
domain somedomain {
    context context_1 {
        valueObject Address {
        }
    }
}
""")
parser.PrintTree()
print(d3i)
