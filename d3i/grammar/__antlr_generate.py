import os
import shutil
import glob


# A saját Java JDK bin könyvtárad helye
java_bin_path = r"C:/java/bin"
env = os.environ.copy()
env["PATH"] = java_bin_path + os.pathsep + env["PATH"]


os.system("C:/java/bin/java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./d3i/grammar -Dlanguage=Python3 ./d3i/grammar/d3iLexer.g4")
os.system("C:/java/bin/java -jar ./tools/antlr/antlr-4.13.2-complete.jar -o ./d3i/grammar -Dlanguage=Python3 ./d3i/grammar/d3iGrammar.g4 -visitor")

source_directory = './d3i/grammar'
destination_directory = './d3i/grammar/.antlr'
wildcards = ['*.interp', '*.tokens']

files_to_move = []
for pattern in wildcards:
    files_to_move.extend(glob.glob(os.path.join(source_directory, pattern)))

for file_path in files_to_move:
    destination_file = os.path.join(destination_directory, os.path.basename(file_path))

    if os.path.exists(destination_file):
        os.remove(destination_file)

    shutil.move(file_path, destination_directory)

