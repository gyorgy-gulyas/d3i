import unittest
import d3i
from d3i.emitters.DotnetEmmiter import *


class TestEmitterDotnetDefault(unittest.TestCase):

    def test_empty_ok(self):
        engine = d3i.Engine()
        session = d3i.Session()
        session.AddSource(d3i.Source.CreateFromText(""))
        root = engine.Build(session)
        emitter = DotnetEmmiter()



if __name__ == "__main__":
    unittest.main()
