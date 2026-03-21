# 1. If-Else Conditional Statements

# 1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
num1 = int(input("Enter a number: "))

if num1 > 0:
    print("Number is positive")
elif num1 < 0:
    print("Number is negative")
else:
    print("Number is 0")

# 2. Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible vote")
else:
    print("You are not eligible to vote")

# 3. Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.
num2 = int(input("Enter a number: "))

if num2 % 2 == 0:
    print("The number is even")
else:
    print("The is number is odd")
