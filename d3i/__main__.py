import argparse
import os
import json
from typing import Dict
import importlib.util
from pathlib import Path
from d3i.Engine import *
from d3i.linters.SemanticChecker import *

# Emitter capability matrix. Each key is a qualified target:
#   "<language>:<side>"  (side = backend | client), or a side-agnostic
#   contract emitter ("proto", "json").
# Value: (module, language, side, status, note)
#   module: importable module exposing DoEmit(...), or None if not implemented
#   status: "supported" (has an emitter) | "planned" (valid, not built yet)
#           | "invalid" (never valid)
#   note:   human-readable reason/hint (used in error messages)
EMITTER_TARGETS = {
    "dotnet:backend":     ("d3i.emitters.DotnetEmitter",     "dotnet",     "backend",  "supported", ""),
    "dotnet:client":      (None,                             "dotnet",     "client",   "planned",   "Blazor"),
    "typescript:client":  ("d3i.emitters.TypeScriptEmitter", "typescript", "client",   "supported", ""),
    "typescript:backend": (None,                             "typescript", "backend",  "invalid",   "TypeScript is client-only; there is no server runtime (Node is not supported)"),
    "java:backend":       (None,                             "java",       "backend",  "planned",   ""),
    "java:client":        (None,                             "java",       "client",   "planned",   ""),
    # Side-agnostic contract emitters (needed by every implementation).
    "proto":              ("d3i.emitters.ProtoEmitter",      "proto",      "contract", "supported", ""),
    "json":               ("d3i.emitters.JsonEmitter",       "json",       "contract", "supported", ""),
}

# Backward-compatible / convenience aliases for contract emitters.
EMITTER_ALIASES = {
    "protobuf": "proto",
}

# Adds CLI arguments to the parser
def __add_known_arguments(arg_parser: argparse.ArgumentParser):
    """
    Adds predefined command-line arguments to the argument parser.

    Parameters:
        arg_parser (argparse.ArgumentParser): The argument parser instance to configure.
    """
    arg_parser.add_argument("-p",
                            "--project-name",
                            help="optional project name",
                            required=False,
                            default=None)
    arg_parser.add_argument("-i",
                            "--input",
                            help="input .d3 file",
                            required=True)
    arg_parser.add_argument("-l",
                            "--linter",
                            help="used linter phyton file(s), if you specify multiple files, all liter will be called",
                            nargs='+',
                            default=[])
    arg_parser.add_argument("-e",
                            "--emitter",
                            help="emitter target(s) to run; you may specify multiple. Each is a qualified 'language:side' target (e.g. dotnet:backend, typescript:client), a side-agnostic contract emitter (proto, json), or a path to an external emitter .py file",
                            nargs='+',
                            default=[])
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
                            help="abort before emitting if any file or linter reports an error (default: enabled). Disable with --no-abort-on-error.",
                            default=True,
                            action=argparse.BooleanOptionalAction)
    arg_parser.add_argument("-aow",
                            "--abort-on-warning",
                            help="abort before emitting if any file or linter reports a warning (default: disabled). Enable with --abort-on-warning.",
                            default=False,
                            action=argparse.BooleanOptionalAction)
    arg_parser.add_argument("-c",
                            "--config-file",
                            help="path to a JSON configuration file. If omitted, the default configuration.json bundled in the d3i package is used." )

# Reads the configuration file and returns it as a dictionary
def __read_config_file(args, unknown_args) -> Dict[str, str]:
    """
    Reads configuration from a file (or default file) and merges any additional unknown CLI arguments.

    Parameters:
        args: Parsed known arguments.
        unknown_args (List[str]): Extra command-line arguments passed in key-value form.

    Returns:
        Dict[str, str]: Combined configuration dictionary.
    """
    # Use the provided config file or fallback to the default
    if (args.config_file != None):
        config_file = args.config_file
    else:
        config_file = os.path.join(Path(__file__).parent, "configuration.json")

    # Initialize an empty configuration dictionary
    configuration: Dict[str, str] = {}

    # If the input file exists, load the configuration
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            configuration = json.load(file)

    # Merge unknown args
    parsed_unknown = __parse_unknown_args(unknown_args)
    configuration.update(parsed_unknown)

    return configuration

def __parse_unknown_args(unknown_args: list[str]) -> Dict[str, object]:
    """
    Parses the unknow args.
    """
    config: Dict[str, object] = {}
    current_key = None

    for arg in unknown_args:
        if arg.startswith("--"):
            current_key = arg.lstrip("-")
            config[current_key] = True  # default to True if no value follows
        else:
            if current_key is None:
                continue
            # If the current key already has a value
            existing = config.get(current_key)
            if existing is True:
                config[current_key] = arg
            elif isinstance(existing, str):
                config[current_key] = [existing, arg]
            elif isinstance(existing, list):
                existing.append(arg)

    return config

# Parses the input files, creates a session, and returns it
def __parse_input_file(args, configuration: Dict[str, str]) -> Session:
    """
    Parses the input D3 file, creates an engine and session, and builds the AST.

    Parameters:
        args: Parsed CLI arguments.
        configuration (Dict[str, str]): Loaded configuration dictionary.

    Returns:
        Session: A parsed and built session instance.
    """
    engine = Engine(configuration)

    # Check if the input file exists, otherwise exit
    if not os.path.exists(args.input):
        exit(f"'{args.input}' file does not exist")

    # Create a session from the input file
    session = Session(Source.CreateFromFile(args.input), args.project_name)

    # Print info if verbose flag is set
    if (args.verbose):
        print(f"information: '{args.input}' file found, and added to sources")

    # Build the engine with the session
    root = engine.Build(session)

    return session

# Checks for errors in the session and exits if conditions are met
def __check_errors(session: Session, args, action: str):
    """
    Checks for diagnostics (errors and warnings) and handles abort conditions based on CLI flags.

    Parameters:
        session (Session): The session object containing diagnostics.
        args: Parsed CLI arguments.
        action (str): The current processing phase (e.g., "parsing", "linting", "emitting").
    """
    # If there are diagnostics (errors or warnings), print them
    if (session.HasDiagnostic() == True):
        session.PrintDiagnostics()

        # Abort if any error occurs and abort-on-error is set
        if (session.HasAnyError() == True and args.abort_on_error):
            exit("abort on error is enabled, process is aborted")

        # Abort if any warning occurs and abort-on-warning is set
        if (session.HasAnyWarning() == True and args.abort_on_warning):
            exit("abort on warning is enabled, process is aborted")
    else:
        # Print info if verbose flag is set and no errors/warnings found
        if (args.verbose):
            print(f"information: no error found in {action}")

# Calls the linters specified in the arguments
def __call_linters(session: Session, args, configuration: Dict[str, str]):
    """
    Calls the built-in semantic checker and any additional linter modules.

    Parameters:
        session (Session): The session to analyze.
        args: Parsed CLI arguments.
        configuration (Dict[str, str]): Loaded configuration dictionary.
    """
    # Call the default semantic checker linter
    if (args.verbose):
        print(f"information: calling 'SemanticChecker")
    defaultChecker = SemanticChecker(session)
    session.main.visit(defaultChecker, None)

    # Execute additional linters specified in the arguments
    for linter_file in args.linter:
        spec = importlib.util.spec_from_file_location(Path(linter_file).stem, linter_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if (args.verbose):
            print(f"information: calling linter:'{linter_file}'")
        module.DoLint(session, configuration)

# Resolves a CLI emitter argument against the capability matrix.
def __resolve_emitter(emitter_name: str):
    """
    Resolves a CLI emitter argument to (imported module, side), or exits with a
    helpful message. Accepts a qualified "language:side" target, a side-agnostic
    contract emitter (proto/json), or a path to an external emitter .py file.

    Two distinct error classes are reported:
      - invalid: the target can never exist (e.g. typescript:backend);
      - planned: the target is valid but not implemented yet (e.g. dotnet:client).
    """
    key = EMITTER_ALIASES.get(emitter_name, emitter_name)

    if key in EMITTER_TARGETS:
        module_path, language, side, status, note = EMITTER_TARGETS[key]
        if status == "supported":
            return importlib.import_module(module_path), side
        if status == "planned":
            suffix = f" ({note})" if note else ""
            exit(f"error: the {language} {side} emitter{suffix} is planned but not implemented yet.")
        if status == "invalid":
            exit(f"error: '{emitter_name}' is not a valid target - {note}.")

    # A bare language name without a side: suggest the valid qualified forms.
    suggestions = sorted(
        k for k, v in EMITTER_TARGETS.items()
        if k.startswith(emitter_name + ":") and v[3] != "invalid"
    )
    if suggestions:
        exit(f"error: '{emitter_name}' needs a side - use one of: {', '.join(suggestions)}")

    # An external emitter given as a path to a .py file.
    if os.path.exists(emitter_name):
        spec = importlib.util.spec_from_file_location(Path(emitter_name).stem, emitter_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module, "external"

    known = ", ".join(sorted(EMITTER_TARGETS))
    exit(f"unknown emitter '{emitter_name}': not a known target ({known}) and no such file")


# Calls the emitters specified in the arguments
def __call_emiters(session: Session, args, configuration: Dict[str, str]):
    """
    Resolves & validates every requested emitter up front (fail fast), then runs them.
    """
    if (len(args.emitter) == 0):
        return

    resolved = []  # list of (name, module, side)
    for emitter_name in args.emitter:
        module, side = __resolve_emitter(emitter_name)
        resolved.append((emitter_name, module, side))

    # Warn if only the shared contract is being generated (no backend/client target).
    if all(side == "contract" for (_name, _module, side) in resolved):
        print("warning: only contract emitters (proto/json) were requested - these "
              "generate the shared wire contract and are usually run alongside a "
              "backend or client target.")

    for emitter_name, module, side in resolved:
        if (args.verbose):
            print(f"information: calling emitter:'{emitter_name}'")
        module.DoEmit(session, args.output_dir, configuration)

# Main function to run the script
def main():
    """
    Main function to process input files and call linters and emitters.
    This function orchestrates argument parsing, configuration loading,
    session creation, validation, linting, emitting, and error checking.
    """
    # Create argument parser and add known arguments
    arg_parser = argparse.ArgumentParser(description="This program processes d3i files and produces results according to the specified emitter.")
    __add_known_arguments(arg_parser)

    # Parse known arguments and unknown arguments (-i/--input is required, argparse enforces it)
    args, unknown_args = arg_parser.parse_known_args()

    # Read configuration file and parse input files
    configuration = __read_config_file(args, unknown_args)
    session: Session = __parse_input_file(args, configuration)
    __check_errors(session, args, "parsing")

    # Run linters on the session
    __call_linters(session, args, configuration)
    __check_errors(session, args, "linting")

    # Run emitters on the session
    __call_emiters(session, args, configuration)
    __check_errors(session, args, "emitting")


if __name__ == "__main__":
    main()

