import os
import shutil
import glob

os.system("java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./parser -Dlanguage=Python3 ./parser/grammar/d3iLexer.g4")
os.system("java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./parser -Dlanguage=Python3 ./parser/grammar/d3iGrammar.g4")

source_directory = './parser'
destination_directory = './parser/grammar'
wildcards = ['*.interp', '*.tokens']

files_to_move = []
for pattern in wildcards:
    files_to_move.extend(glob.glob(os.path.join(source_directory, pattern)))

for file_path in files_to_move:
    destination_file = os.path.join(destination_directory, os.path.basename(file_path))

    if os.path.exists(destination_file):
        os.remove(destination_file)

    shutil.move(file_path, destination_directory)
