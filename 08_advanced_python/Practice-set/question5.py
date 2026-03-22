# 5. Exception Handling and Custom Errors
# 1. Write a program that asks the user to enter a number and handles:
#     a. ValueError  if the input is not a number
#     b. ZeroDivisionError  if you try to divide by zero
# 2.Create a custom exception  NegativeNumberError  and raise it when the user enters a negative number.


class NegativeNumberError(Exception):
    pass


while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")
        print(f"The division is {a / b}")
    except ValueError:
        print("Please don't perform bad typecasts")
    except ZeroDivisionError:
        print("Hey don't divide by 0")
    except NegativeNumberError as e:
        print(e)
    except Exception as e:
        print("Unknown error", e)
