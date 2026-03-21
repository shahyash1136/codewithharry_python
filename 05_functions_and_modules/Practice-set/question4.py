# 4. Recursion in Python
# 1. Write a recursive function  factorial(n)  that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))

"""
fact(3)
3 * fact(2)
3 * 2 * fact(1)
3 * 2 * 1
"""


# 2. Write a recursive function  sum_of_digits(n)  that returns the sum of all digits of a given number.


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


# sum of digits of 7532 is same as:
# 2 (last digit) + sum of digits of 753
print(sum_of_digits(7532))
