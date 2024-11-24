import d3i
import argparse
import os
import json
from typing import Dict
import importlib.util
from pathlib import Path


def __add_known_arguments__():
    arg_parser.add_argument("-i",
                            "--input",
                            help="input d3 file(s), multiple files may be necessary if a domain is described in multiple files, or if you want to process multiple domains at once ",
                            nargs='+',
                            default=[])
    arg_parser.add_argument("-l",
                            "--linter",
                            help="used linter phyton file(s), if you specify multiple files, all liter will be called from the files",
                            nargs='+',
                            default=[])
    arg_parser.add_argument("-e",
                            "--emitter",
                            help="used emmitter file, if you specify multiple files, all emitter will be called",
                            nargs='+',
                            default=["./d3i/emitter/JsonEmitter.py"])
    arg_parser.add_argument("-o",
                            "--output-dir",
                            help="output directory",
                            type=str,
                            default="./")
    arg_parser.add_argument("-v",
                            "--verbose",
                            help="detailed output",
                            action="store_true")
    arg_parser.add_argument("-aoe",
                            "--abort-on-error",
                            help="when any file has a any error, or any of the linter reports an error, then no emitter called and the executing is aborted",
                            action="store_true")
    arg_parser.add_argument("-aow",
                            "--abort-on-warning",
                            help="when any file has a any warinig, or any of the linter reports a warining, then no emitter called and the executing is aborted",
                            action="store_true")
    arg_parser.add_argument("-c",
                            "--config-file",
                            help="define the configuration in json format. If the option is present, then the default ./configuration.json will be used",
                            action="store_true")


def __read_config_file__(args, unknown_args) -> Dict[str, str]:
    if (args.config_file != None):
        config_file = args.config_file
    else:
        config_file = os.path.join(Path(__file__).stem, "configuration.json")

    configuration: Dict[str, str] = {}
    with open(config_file, "r") as file:
        configuration = json.load(file)

    for i in range(0, len(unknown_args), 2):
        if i + 1 < len(unknown_args):
            configuration[unknown_args[i]] = unknown_args[i + 1]

    return configuration


def __parse_input_files__(args) -> d3i.Session:
    engine = d3i.Engine()
    session = d3i.Session()
    for input in args.input:
        if os.path.exists(input) == False:
            exit(f"'{input}' file does not exist")
        else:
            session.AddSource(d3i.Source.CreateFromFile(input))
            if (args.verbose):
                print(f"information: '{input}' file found, and added to sources")

    if (args.verbose):
        print(f"information: {len(session.sources)} file will be processed")
    root = engine.Build(session)

    return session


def __check_errors__(session: d3i.Session, args):
    if (session.HasDiagnostic() == True):
        session.PrintDiagnostics()
        if (session.HasAnyError() == True and args.abort_on_error):
            exit("abort on error is enabled, process is aborted")
        if (session.HasAnyWarning() == True and args.abort_on_warinig):
            exit("abort on warning is enabled, process is aborted")
    else:
        if (args.verbose):
            print(f"information: no error found in build")


def __call_linters__(session: d3i.Session, args):
    for linter_file in args.linter:
        spec = importlib.util.spec_from_file_location(Path(linter_file).stem, linter_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.DoLint(session, configuration)


def __call_emiters__(session: d3i.Session, args):
    for emitter_file in args.emitter:
        spec = importlib.util.spec_from_file_location(Path(emitter_file).stem, emitter_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.DoEmit(session, args.output_dir, configuration)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="This program processes d3i files and produces results according to the specified emitter.")

    __add_known_arguments__(arg_parser)
    args, unknown_args = arg_parser.parse_known_args()
    if (len(args.input) == 0):
        print("at least on input must be specified, use -h to see help.")

    # parse
    configuration = __read_config_file__(args)
    session: d3i.Session = __parse_input_files__(args)
    __check_errors__(session, args)

    # linting
    __call_linters__(session, args)
    __check_errors__(session, args)

    # emmiting
    __call_emiters__(session, args)
    __check_errors__(session, args)
