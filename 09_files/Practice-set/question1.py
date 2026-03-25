# 1. File I/O Basics
# 1. Create a text file  notes.txt  using Python and write  "Learning Python is fun!"  into it.
file = open("09_files/Practice-set/notes.txt", "w")
file.write("Learning Python is fun!")
file.close()

# 2. Open  notes.txt , read its content, and print it to the console.
f = open("09_files/Practice-set/notes.txt", "r")
content = f.read()
print(content)
f.close()
