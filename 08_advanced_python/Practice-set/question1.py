# 1. Decorators in Python
# 1. Write a decorator  logger  that prints  "Function is being called"  before the function runs. Use it to decorate a function  say_hello()  that prints "Hello!".
def logger(func):
    def wrapper():
        print("Function is being called")
        return func()

    return wrapper


@logger
def say_hello():
    print("Hello!")


say_hello()

# 2. Write a decorator  timer  that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


@timer
def sum_number():
    total = 0
    for i in range(1, 1_000_001):
        total += i
    return total
    
sum_number()


