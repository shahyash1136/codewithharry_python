# 5. Dictionaries and Dictionary Methods
# 1. Create a dictionary  student = {"name": "John", "age": 20, "grade": "A"} and:

student = {"name": "John", "age": 20, "grade": "A"}
#     a. Print the value of  "name" .
print(student["name"])

#     b. Change  "grade"  to  "A+" .
student["grade"] = "A+"
print(student)

#     c. Add a new key  "city"  with value  "Delhi" .
student["city"] = "Delhi"
print(student)

# 2. Create a dictionary of three friends and their phone numbers. Use:
friends = {"a": "1234567890", "b": "987654321", "c": "6549871203"}
#     a. keys()  to get all names
print(friends.keys())
#     b. values()  to get all numbers
print(friends.values())
#     c. items()  to loop over key-value pairs and print them
for key,value in student.items():
    print(f"{key} = {value}")
