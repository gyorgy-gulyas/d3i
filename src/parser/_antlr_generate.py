import os
import shutil
import glob

os.system("java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./src/parser -Dlanguage=Python3 ./src/parser/grammar/d3iLexer.g4")
os.system("java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./src/parser -Dlanguage=Python3 ./src/parser/grammar/d3iGrammar.g4 -visitor")

source_directory = './src/parser'
destination_directory = './src/parser/grammar'
wildcards = ['*.interp', '*.tokens']

files_to_move = []
for pattern in wildcards:
    files_to_move.extend(glob.glob(os.path.join(source_directory, pattern)))

for file_path in files_to_move:
    destination_file = os.path.join(destination_directory, os.path.basename(file_path))

    if os.path.exists(destination_file):
        os.remove(destination_file)

    shutil.move(file_path, destination_directory)
