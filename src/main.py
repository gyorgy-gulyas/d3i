from antlr4 import *
from parser.d3iParser import d3iParser

parser = d3iParser()
parser.ParseText( """
    import Valami
    import Valami1.Valami2
                    """)
#parser.PrintTree()
parser.BuildElementTree()
