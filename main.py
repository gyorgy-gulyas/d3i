import d3i
import argparse
import os

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
                        help="when the any of the linter reports error, then no emitter called",
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
                        default=["./"])

args = arg_parser.parse_args()

if (len(args.input) == 0):
    print("at least on input must be specified, use -h to see help.")


engine = d3i.Engine()
session = d3i.Session()

for input in args.input:
    if os.path.exists(input) == False:
          exit(f"'{input}' file does not exist")
    else:
        session.AddSource(d3i.Source.CreateFromFile( input ))

root = engine.Build(session)
print(root)

# parser = d3i.elements.Parser()
# d3i = parser.ParseText( """
# domain somedomain {
#    context context_1 {
#        valueObject Address {
#        }
#    }
# }""")
# parser.PrintTree()
# print(d3i)
