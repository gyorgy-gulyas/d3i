import io
from d3i.elements.Elements import *
from d3i.Engine import Session
from d3i.emitters.dotnet_default.utils import *


def DoEmit(session: Session, output_dir: str):

    for domain in session.main.domains:
        domain_folder: str = utils.__create_folder__(output_dir, domain.name)
        for context in domain.contexts:
            context_folder: str = utils.__create_folder__(domain_folder, context.name)

            for enum in context.enums:
                enum_content: str = __emit_domain_enum__(domain, context, enum)
                utils.__create_cs_file__(context_folder, enum.name, enum_content)

            for value_object in context.value_objects:
                value_object_content: str = __emit_domain_value_objects__(domain, context, enum)
                utils.__create_cs_file__(context_folder, value_object.name, value_object_content)


def __emit_domain_enum__(domain: domain, context: context, enum: enum):
    buffer = io.StringIO()
    buffer.write(utils.fileHeader())
    buffer.write("\n")
    buffer.write(f"namespace {domain.name}.{context.name}")
    buffer.write("{")
    buffer.write(f"{utils.enumText(enum, indent=1)}")
    buffer.write("}")


def __emit_domain_value_objects__(domain: domain, context: context, value_object: value_object):
    buffer = io.StringIO()
    buffer.write(utils.fileHeader())
    buffer.write("\n")
    buffer.write(f"namespace {domain.name}.{context.name}")
    buffer.write("{")
    buffer.write(f"\t{utils.valueObjectText(value_object)}")
    buffer.write("}")
