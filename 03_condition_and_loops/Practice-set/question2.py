# 2. Match Case Statements

# 1. Ask the user to enter a day number (1–7) and print the corresponding day of the week using  match case .
day = int(input("Enter a day number (1-7): "))

match day:
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case 1:
        print("Today is Sunday")
    case _:
        print("Your entered a wrong day")


# 2. Write a program using  match case  that simulates a simple calculator. Ask the user for two numbers and an operation (+, -, *, /). Perform the operation using  match case .
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
operator = input("Enter a opeartor from (+, -, *, /): ")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Please select a correct operator")
