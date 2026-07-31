import argparse
import json
import os
import tempfile
import unittest

from d3i.Engine import *
from d3i.emitters.JsonEmitter import DoEmit as JsonDoEmit, JsonEmitter
# Alias the dunder-prefixed helper so it is not name-mangled inside the class body.
from d3i.__main__ import __call_linters as call_linters


class TestExternalLinterCall(unittest.TestCase):
    """
    An external linter is loaded from a .py file and called by convention. The convention is the
    one the built-in SemanticChecker.DoLint declares and the one every emitter's DoEmit follows:
    (session, output_dir, configuration).
    """

    def test_external_linter_is_called_with_the_documented_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            linter_path = os.path.join(tmp, "recording_linter.py")
            record_path = os.path.join(tmp, "record.json").replace("\\", "\\\\")
            with open(linter_path, "w", encoding="utf-8") as file:
                file.write(
                    "import json\n"
                    "def DoLint(session, output_dir, configuration):\n"
                    f"    with open(r'{record_path}', 'w') as f:\n"
                    "        json.dump({'output_dir': output_dir, 'configuration': configuration}, f)\n"
                )

            engine = Engine()
            session = Session(Source.CreateFromText("domain D { }"))
            engine.Build(session)

            args = argparse.Namespace(verbose=False, linter=[linter_path], output_dir=tmp)
            # Calling this with two arguments raised a TypeError before every external linter ran.
            call_linters(session, args, {"key": "value"})

            with open(os.path.join(tmp, "record.json"), encoding="utf-8") as file:
                record = json.load(file)
            self.assertEqual(tmp, record["output_dir"])
            self.assertEqual({"key": "value"}, record["configuration"])


class TestJsonEmitterConfiguration(unittest.TestCase):
    """
    The JSON emitter's options are documented under a 'json.' prefix. It used to CHECK for the
    prefixed key but READ the bare one, so setting a documented option raised a KeyError instead
    of taking effect.
    """

    def _emit_with(self, configuration):
        engine = Engine()
        session = Session(Source.CreateFromText("domain D { }"))
        engine.Build(session)

        with tempfile.TemporaryDirectory() as tmp:
            JsonDoEmit(session, tmp, configuration)
            with open(os.path.join(tmp, "main.json"), encoding="utf-8") as file:
                return file.read()

    def test_default_configuration_is_indented_by_four(self):
        content = self._emit_with({})
        self.assertIn('\n    "$type"', content)

    def test_json_indent_is_honoured(self):
        content = self._emit_with({"json.indent": 2})
        self.assertIn('\n  "$type"', content)
        self.assertNotIn('\n    "$type"', content)

    def test_json_sort_keys_is_honoured(self):
        # Declaration order at the root is $type, imports, domains; sorted it is domains, imports.
        content = self._emit_with({"json.sort_keys": True})
        self.assertLess(content.index('"domains"'), content.index('"imports"'))

    def test_a_string_false_turns_the_option_off(self):
        # Configuration values arrive as strings from the command line, and bool("False") is True,
        # so a string has to be read by its content rather than its truthiness.
        content = self._emit_with({"json.sort_keys": "False"})
        self.assertLess(content.index('"imports"'), content.index('"domains"'))


class TestJsonEmitterInterfaces(unittest.TestCase):

    def test_an_interface_is_listed_under_interfaces_not_services(self):
        engine = Engine()
        session = Session(Source.CreateFromText("""
domain D {
    context C {
        service TheService {
        }
        interface TheInterface version 1 {
        }
    }
}
"""))
        engine.Build(session)
        self.assertFalse(session.HasAnyError())

        model = json.loads(JsonEmitter(withLocation=False).Emit(session))
        context = model["domains"][0]["contexts"][0]

        self.assertEqual(["TheService"], [s["name"] for s in context["services"]])
        self.assertEqual(["TheInterface"], [i["name"] for i in context["interfaces"]])


if __name__ == "__main__":
    unittest.main()
