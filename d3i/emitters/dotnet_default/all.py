from d3i.elements.Elements import *
from d3i.Engine import Session
import importlib.util
from pathlib import Path


def DoEmit(session: Session, output_dir: str):
    current_dir: str = Path(__file__).stem

    __do_emit__(session, output_dir, current_dir, "models.py")

    def __do_emit__(session: Session, output_dir: str, current_dir: str, module_file:str):
        spec = importlib.util.spec_from_file_location(current_dir, module_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.DoEmit(session, output_dir)
