# 2. Read, Write, and Append Files
# 1. Write a program that writes three lines of text to a file  tasks.txt .

file = open("09_files/Practice-set/tasks.txt", "w")
file.write("My name is Yash Shah.\nI'm a UI developer.\nWho is trying to learn python.")
file.close()

# 2. Open  tasks.txt  in append mode and add a new line  "Task Completed!" .
f = open("09_files/Practice-set/tasks.txt", "a")
f.write("\nTask Completed!")
f.close()

# 3. Read the file and print all lines as a list using  readlines() .
f = open("09_files/Practice-set/tasks.txt", "r")
content = f.read()
print(content)
f.close()
