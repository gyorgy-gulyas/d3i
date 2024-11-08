from parser.d3iParser import d3iParser

parser = d3iParser()
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
