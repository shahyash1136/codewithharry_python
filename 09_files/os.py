import os

a = os.listdir("dir")
print(a)
print(os.getcwd())  # gets current working dictory
print(os.path.exists("dir")) # Test whether a path exists for the directory

# os.remove("sample.txt") # use to remove file
# os.rmdir("dir/sub") # used to remove empty dir