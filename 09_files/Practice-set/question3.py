# 3. OS and Shutil Modules
# 1. Use the  os  module to:
#   a. Print the current working directory
import os

curdir = os.getcwd()
print(curdir)
#   b. List all files and folders in the current directory
a = os.listdir(".")
print(a)
#   c. Create a new folder  my_folder
os.mkdir("09_files/Practice-set/my_folder")

# 2. Use the  shutil  module to:
import shutil

#   a. Copy a file from one folder to another
shutil.copy("09_files/Practice-set/notes.txt", "09_files/Practice-set/my_folder")
#   b. Move a file to a new folder
shutil.move("09_files/Practice-set/tasks.txt", "09_files/Practice-set/my_folder")
#   c. Delete a file (careful: irreversible!)
os.remove("09_files/Practice-set/notes.txt")
