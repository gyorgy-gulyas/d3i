import d3i
import argparse
import os
import importlib.util
from pathlib import Path

arg_parser = argparse.ArgumentParser(
    description="This program processes d3i files and produces results according to the specified emitter.")

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
arg_parser.add_argument("-aoe",
                        "--abort-on-error",
                        help="when any file has a syntax erro, or any of the linter reports error, then no emitter called and the executing is aborted",
                        action="store_true")
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

args = arg_parser.parse_args()

if (len(args.input) == 0):
    print("at least on input must be specified, use -h to see help.")

#region process inputs
engine = d3i.Engine()
session = d3i.Session()
for input in args.input:
    if os.path.exists(input) == False:
          exit(f"'{input}' file does not exist")
    else:
        session.AddSource(d3i.Source.CreateFromFile( input ))
        if(args.verbose):
            print(f"information: '{input}' file found, and added to sources")

if(args.verbose):
    print( f"information: {len(session.sources)} file will be processed")
root = engine.Build(session)

if(session.HasErrror() == True):
    session.PrintErrors()
    if(args.abort_on_error):
        exit( "abort on error is enabled, process is aborted")
else:
    if(args.verbose):
        print( f"information: no error found in build")
#endregion process inputs

#region linting
for linter_file in args.linter:
    spec = importlib.util.spec_from_file_location(Path(linter_file).stem, linter_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.DoLint( session )

if(session.HasErrror() == True):
    session.PrintErrors()
    if(args.abort_on_error):
        exit( "abort on error is enabled, prcess is aborted")
#endregion process inputs

#region emitting
for emitter_file in args.emitter:
    spec = importlib.util.spec_from_file_location(Path(emitter_file).stem, emitter_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(module.DoEmit( session, args.output_dir ))

if(session.HasErrror() == True):
    session.PrintErrors()
    if(args.abort_on_error):
        exit( "abort on error is enabled, process is aborted")
#endregion process inputs
