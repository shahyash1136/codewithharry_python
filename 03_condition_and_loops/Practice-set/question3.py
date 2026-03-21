# 3. For Loops

# 1. Print numbers from 1 to 10 using a  for  loop.
for i in range(1, 11):
    print(i)


# 2. Print the multiplication table of a number (entered by user).
num1 = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num1} X {i} = {num1*i}")


# 3. Calculate the sum of all numbers from 1 to 100 using a  for  loop.
sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# 4. Print the following pattern using a  for  loop:
# *
# **
# ***
# ****
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
