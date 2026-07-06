import unittest
# Alias the dunder-prefixed helper so it is not name-mangled inside the class body.
from d3i.__main__ import __resolve_emitter as resolve_emitter, EMITTER_TARGETS, EMITTER_ALIASES


class TestCliEmitterTargets(unittest.TestCase):

    # --- supported targets resolve to a real emitter module -------------------

    def test_supported_backend_resolves(self):
        module, side = resolve_emitter("dotnet:backend")
        self.assertEqual(side, "backend")
        self.assertTrue(hasattr(module, "DoEmit"))

    def test_supported_client_resolves(self):
        module, side = resolve_emitter("typescript:client")
        self.assertEqual(side, "client")
        self.assertTrue(hasattr(module, "DoEmit"))

    def test_contract_proto_resolves(self):
        module, side = resolve_emitter("proto")
        self.assertEqual(side, "contract")
        self.assertTrue(hasattr(module, "DoEmit"))

    def test_contract_json_resolves(self):
        module, side = resolve_emitter("json")
        self.assertEqual(side, "contract")
        self.assertTrue(hasattr(module, "DoEmit"))

    def test_protobuf_alias_resolves_to_proto(self):
        module, side = resolve_emitter("protobuf")
        self.assertEqual(side, "contract")
        self.assertTrue(hasattr(module, "DoEmit"))

    # --- invalid targets (can never exist) ------------------------------------

    def test_invalid_typescript_backend(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("typescript:backend")
        msg = str(cm.exception)
        self.assertIn("not a valid target", msg)
        self.assertIn("client-only", msg)

    # --- planned targets (valid, not implemented yet) -------------------------

    def test_planned_dotnet_client(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("dotnet:client")
        self.assertIn("planned but not implemented", str(cm.exception))

    def test_planned_java_backend(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("java:backend")
        self.assertIn("planned but not implemented", str(cm.exception))

    def test_planned_rust_client(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("rust:client")
        self.assertIn("planned but not implemented", str(cm.exception))

    # --- bare language name needs a side --------------------------------------

    def test_bare_language_needs_side(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("dotnet")
        msg = str(cm.exception)
        self.assertIn("needs a side", msg)
        self.assertIn("dotnet:backend", msg)
        self.assertIn("dotnet:client", msg)

    def test_bare_typescript_excludes_invalid_backend(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("typescript")
        msg = str(cm.exception)
        self.assertIn("typescript:client", msg)
        self.assertNotIn("typescript:backend", msg)

    # --- unknown target -------------------------------------------------------

    def test_unknown_emitter(self):
        with self.assertRaises(SystemExit) as cm:
            resolve_emitter("bogus:x")
        self.assertIn("unknown emitter", str(cm.exception))

    # --- matrix consistency ---------------------------------------------------

    def test_matrix_statuses_are_valid(self):
        for key, (module, language, side, status, note) in EMITTER_TARGETS.items():
            self.assertIn(status, ("supported", "planned", "invalid"))
            # supported targets must name a module; others must not.
            if status == "supported":
                self.assertIsNotNone(module, f"{key} is supported but has no module")
            else:
                self.assertIsNone(module, f"{key} is {status} but names a module")

    def test_alias_targets_exist(self):
        for alias, target in EMITTER_ALIASES.items():
            self.assertIn(target, EMITTER_TARGETS)


if __name__ == "__main__":
    unittest.main()
