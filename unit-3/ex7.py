''' 7. Write a program to copy move and delete files 
using shutil module. '''

import os
import shutil

with open("test.txt", "w") as f:
    f.write("Hello")

shutil.copy("test.txt", "copy.txt")
print("Copied!")

os.mkdir("my_folder")
shutil.move("copy.txt", "my_folder/moved.txt")
print("Moved!")

shutil.rmtree("my_folder")
print("Deleted!")

os.remove("test.txt")


''' OUTPUT :
        Copied!
        Moved!
        Deleted!
'''