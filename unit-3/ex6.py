''' 6. Write a program to perform file and directory 
operations using os and sys modules. '''

import os
import sys

# 1. System Operations (sys)
print("Python Version:", sys.version)
print("Script Name:", sys.argv[0])

# 2. Directory Operations (os)
print("Current Directory:", os.getcwd())

# Create a folder
folder = "my_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created.")

# 3. File Operations (os)
file_path = os.path.join(folder, "test.txt")

# Create and write to a file
with open(file_path, "w") as f:
    f.write("Hello World")
print("File created inside folder.")

# List everything inside the folder
print("Folder Contents:", os.listdir(folder))


''' OUTPUT :
        Python Version: 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]
        Script Name: d:\Tushar-4053\PYTHON\UNITS\unit-3\ex6.py
        Current Directory: D:\Tushar-4053\PYTHON\UNITS\unit-3
        File created inside folder.
        Folder Contents: ['test.txt']
'''