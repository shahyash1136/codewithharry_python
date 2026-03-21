# 6. Variable Scope and Docstrings
# 1. Write a function increment() that increments a counter each time it is called.
def increment():
    counter = 0
    counter += 1
    return counter


print(increment())
print(increment())
print(increment())
print(increment())
print(increment())
print(increment())
print(increment())


# 2. Write a function  multiply(a, b)  that has a proper docstring explaining what it does. Then use  help(multiply)  to display the docstring.
def multiply(a, b):
    """
    Multiplies two numbers a and b and returns the result.

    Parameters:
    a (int or float): The first number to multiply.
    b (int or float): The second number to multiply.

    Returns:
    int or float: The product of a and b.
    """
    return a * b


help(multiply)
