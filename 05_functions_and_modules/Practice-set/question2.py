# 2. Function Arguments & Return Values
# 1. Write a function  full_name(first, last)  that takes first name and last name as parameters and returns a single string in the format  "First Last" .
def full_name(first, last):
    return first + " " + last


print(full_name("Yash", "Shah"))


# 2. Write a function  calculate_area(length, width=10)  that returns the area of a rectangle. Test it by calling the function with:
#     a. Both  length  and  width
#     b. Only  length  (use default width)
def calculate_area(length, width=10):
    area = width * length
    return area


print(calculate_area(2, 4))
print(calculate_area(2))
