# 1. Introduction to Lists
# 1. Create a list  fruits = ["apple", "banana", "cherry"] .
#     a. Print the first fruit.
#     b. Replace  "banana"  with  "orange" .
#     c. Print the length of the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))


# 2. Create a list of numbers from  1  to  10 .
#     a. Print the first three numbers using slicing.
#     b. Print the last three numbers using slicing.
number = []
for i in range(1,11):
    number.append(i)

print(number[:3])
print(number[-3:])
