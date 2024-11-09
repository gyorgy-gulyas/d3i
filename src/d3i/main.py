from interpreter.Parser import Parser

parser = Parser()
parser.ParseText( """
domain Valami {
    @hello
    context Hello {
        @hello
        enum Days {
            @hello
            Monday,
            @hello
            Thuesday    
        }
    }
}
domain Valami {
}
                 """)
parser.PrintTree()
parser.BuildElementTree()
