# 7. Bonus Challenges
# 1. Write a recursive function  fibonacci(n)  that prints the first  n  Fibonacci numbers.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# 2. Write a function  safe_divide(a, b)  that returns the result of  a / b , but returns  "Cannot divide by zero"  if  b  is  0 .
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
