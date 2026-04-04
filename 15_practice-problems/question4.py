"""
### 4. Fibonacci Series
**Question:**
Print first N Fibonacci numbers.

**Example Output:**
```text
Enter N: 6
Output: 0 1 1 2 3 5
```
"""


def is_valid_number(prompt):
    while True:
        number = input(prompt)
        try:
            if int(number) < 0:
                print("The number cannot be a negative number")
                continue
            return int(number)
        except ValueError:
            print("Enter a valid number")


def fibonacci_series(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_series(num - 2) + fibonacci_series(num - 1)


def fibonacciNumber(n):
    ans = []
    for i in range(n):
        ans.append(fibonacci_series(i))
    return ans


def main():
    number = is_valid_number("Enter Nth number to get its Fibonacci Series: ")
    res = fibonacciNumber(number)
    for num in res:
        print(num, end=" ")


if __name__ == "__main__":
    main()
