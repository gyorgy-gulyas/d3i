import unittest
import d3i
from tests.dotnet_code_helper import *
from d3i.emitters.dotnet_emmiter.ModelEmitter import *


class TestEmitterDotnetDefault(unittest.TestCase):

    def setUp(self):
        dotnet_code_helper.init_roslyn()

    def test_modelemitter_enum_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText("""
domain WebShop {
    context CustomerContext {
        enum CustomerType{
            PrivatePerson,
            Company
        }
    }
}
"""))
        root = engine.Build(session)
        emitter = ModelEmmiter()
        result = emitter.Emit(session)
        expected = """
using System;
using System.Collections.Generic;

namespace WebShop.CustomerContext
{l
    enum CustomerType
    {
        PrivatePerson,
        Company,
    }
}
"""
        self.assertTrue(1, len(result))
        self.assertEqual(result[0].fileName, "CustomerContext.cs")
        equal, index, diff_part_1, diff_part_2 = dotnet_code_helper.compare_and_extract_diff(expected, result[0].content)
        self.assertTrue(equal)
        compiled, errors, assembly = dotnet_code_helper.compile_debug(result, dotnet_code_helper.assembly_name())
        self.assertTrue(compiled)

        print(result)

    
if __name__ == "__main__":
    unittest.main()
