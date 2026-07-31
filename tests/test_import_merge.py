from __future__ import annotations
import os
import tempfile
import unittest

from d3i.Engine import *
from d3i.linters.SemanticChecker import SemanticChecker


class TestImportMerge(unittest.TestCase):
    """
    Imports are resolved from the importing file's directory and the imported d3s are folded into
    the main one. Building from a string cannot exercise any of that - the import path never
    resolves - so every test here writes real files to a temporary directory and builds from disk.
    """

    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        self.addCleanup(self._dir.cleanup)

    def _write(self, relative_path: str, content: str) -> str:
        path = os.path.join(self._dir.name, relative_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        return path

    def _build(self, main_path: str) -> tuple[Session, d3]:
        engine = Engine()
        session = Session(Source.CreateFromFile(main_path))
        root = engine.Build(session)
        return session, root

    def _build_ok(self, main_path: str) -> tuple[Session, d3]:
        session, root = self._build(main_path)
        self.assertFalse(session.HasAnyError(),
                         "\n".join(d.toText() for d in session.diagnostics))
        return session, root

    def test_import_merges_into_an_existing_context(self):
        # The interesting case: both files describe the SAME domain and context, so the imported
        # elements have to be folded in one by one rather than appended as a whole context.
        self._write("base.d3", """
domain Shop {
    context Sales {
        enum Currency {
            HUF,
            EUR
        }
        valueobject Money {
            amount:integer
        }
        composite Audited {
            createdBy:string
        }
    }
}
""")
        main = self._write("main.d3", """
import base
domain Shop {
    context Sales {
        valueobject Price {
            net:integer
        }
    }
}
""")
        _session, root = self._build_ok(main)

        self.assertEqual(1, len(root.domains), "the same domain from two files stays one domain")
        context = root.domains[0].contexts[0]
        self.assertEqual(1, len(root.domains[0].contexts), "the same context stays one context")

        self.assertEqual(["Money", "Price"], sorted(v.name for v in context.value_objects))
        self.assertEqual(["Currency"], [e.name for e in context.enums])
        self.assertEqual(["Audited"], [c.name for c in context.composites])

        # A merged element must be re-parented, otherwise name resolution walks back into the file
        # it came from and cannot see anything the main file declares.
        merged = next(v for v in context.value_objects if v.name == "Money")
        self.assertIs(context, merged.parent)

    def test_import_adds_a_whole_new_domain(self):
        self._write("catalog.d3", """
domain Catalog {
    context Products {
        valueobject Sku {
            code:string
        }
    }
}
""")
        main = self._write("main.d3", """
import catalog
domain Shop {
    context Sales {
    }
}
""")
        _session, root = self._build_ok(main)

        self.assertEqual(["Catalog", "Shop"], sorted(d.name for d in root.domains))
        catalog = next(d for d in root.domains if d.name == "Catalog")
        self.assertIs(root, catalog.parent)

    def test_import_adds_a_whole_new_context_to_an_existing_domain(self):
        self._write("billing.d3", """
domain Shop {
    context Billing {
        valueobject Invoice {
            total:integer
        }
    }
}
""")
        main = self._write("main.d3", """
import billing
domain Shop {
    context Sales {
    }
}
""")
        _session, root = self._build_ok(main)

        self.assertEqual(1, len(root.domains))
        self.assertEqual(["Billing", "Sales"], sorted(c.name for c in root.domains[0].contexts))

    def test_dotted_import_resolves_to_a_subdirectory(self):
        self._write(os.path.join("shop", "sales", "base.d3"), """
domain Shop {
    context Sales {
        valueobject Money {
            amount:integer
        }
    }
}
""")
        main = self._write("main.d3", """
import shop.sales.base
domain Shop {
    context Sales {
    }
}
""")
        session, root = self._build_ok(main)

        self.assertEqual(["Money"], [v.name for v in root.domains[0].contexts[0].value_objects])
        self.assertEqual(2, len(session.all), "the main file and the imported one")

    def test_a_type_declared_in_an_imported_file_resolves_after_merging(self):
        # The payoff of merging: the main file may name a type it never declared. If the merge is
        # broken, this fails in the linter rather than silently producing a half-built model.
        self._write("base.d3", """
domain Shop {
    context Sales {
        valueobject Address {
            city:string
        }
    }
}
""")
        main = self._write("main.d3", """
import base
domain Shop {
    context Sales {
        valueobject Customer {
            name:string
            address:Address
        }
    }
}
""")
        session, root = self._build_ok(main)

        session.main.visit(SemanticChecker(session), None)
        self.assertFalse(session.HasAnyError(),
                         "\n".join(d.toText() for d in session.diagnostics))

    def test_the_same_import_reached_twice_is_processed_once(self):
        self._write("shared.d3", """
domain Shop {
    context Sales {
        valueobject Money {
            amount:integer
        }
    }
}
""")
        self._write("left.d3", """
import shared
domain Shop {
    context Sales {
    }
}
""")
        self._write("right.d3", """
import shared
domain Shop {
    context Sales {
    }
}
""")
        main = self._write("main.d3", """
import left
import right
domain Shop {
    context Sales {
    }
}
""")
        session, root = self._build_ok(main)

        self.assertEqual(4, len(session.all), "main + left + right + shared, the last one only once")
        self.assertEqual(["Money"], [v.name for v in root.domains[0].contexts[0].value_objects],
                         "a diamond import must not merge the shared file twice")

    def test_missing_import_reports_an_error(self):
        main = self._write("main.d3", """
import nosuchfile
domain Shop {
}
""")
        session, _root = self._build(main)

        self.assertTrue(session.HasAnyError())
        self.assertIn("nosuchfile", " ".join(d.message for d in session.diagnostics))

    def test_import_element_keeps_a_reference_to_the_imported_d3(self):
        self._write("base.d3", """
domain Shop {
}
""")
        main = self._write("main.d3", """
import base
domain Shop {
}
""")
        _session, root = self._build_ok(main)

        self.assertEqual(1, len(root.imports))
        self.assertEqual("base", root.imports[0].name)
        self.assertIsInstance(root.imports[0].d3, d3)


if __name__ == "__main__":
    unittest.main()
