from typing import Dict
from d3i.elements.Elements import *
from d3i.emitters.dotnet_emmiter.DotnetEmmiter import *
from d3i.Engine import Session


class ModelEmmiter(DotnetEmmiter):
    def __init__(self, output_dir: str = "./", configuration: Dict[str, str] = {}):
        super().__init__(output_dir, configuration)

    def Emit(self, session: Session) -> Dict[str, str]:
        result: Dict[str, str] = {}

        for domain in session.main.domains:
            for context in domain.contexts:

                content = self.__beginContext(domain, context)
                fileName = self.__get_context_model_filename(domain, context, context.name)

                for enum in context.enums:
                    content += self.enumText(enum)

                for value_object in context.value_objects:
                    content += self.valueObjectText(value_object)

                content += self.__endContext(domain, context)
                result[fileName] = content

        return result

    def __get_context_model_filename(self, domain: domain, context: context, name: str) -> str:

        if (self.configuration.createFolderStructure == True):
            return os.path.join(domain.name, context.name, context.name + ".cs")
        else:
            return name + ".cs"

    def __beginContext(self, domain, context):
        buffer = io.StringIO()
        buffer.write(self.beginFile())
        buffer.write("\n")
        buffer.write(f"namespace {domain.name}.{context.name}\n")
        buffer.write("{\n")
        return buffer.getvalue()

    def __endContext(self, domain, context):
        buffer = io.StringIO()
        buffer.write("}")
        buffer.write(self.endFile())
        return buffer.getvalue()
