## Drill 2
# Moves files from a specified folder to another folder

import os
import shutil

print("Remember, in python, you must use double backslashes \\\\ to avoid escape chars.") 
src = raw_input("\nGive path to source folder: ")
dst = raw_input("\nGive path to destination folder: ")
if (src == 't' and dst == 't'):
    src = 'H:\\Python27\\Python stuff\\Python Drills\\PythonDrill_2\\Folder A\\'
    dst = 'H:\\Python27\\Python stuff\\Python Drills\\PythonDrill_2\\Folder B\\'
source_folder = os.listdir(src)
for f in source_folder:
    shutil.move(src + f, dst)
    print("Moved file " + f + "\nFrom - " + src + "\nTo - " + dst)
