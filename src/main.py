from parser.d3iParser import d3iParser

parser = d3iParser()
parser.ParseText( """
domain Valami {
}
                 domain Valami {
}
                 """)
parser.PrintTree()
parser.BuildElementTree()
