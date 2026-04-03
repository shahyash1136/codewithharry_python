"""
### 3. Prime Number Checker
**Question:**
Check whether a given number is prime.

**Example Output:**
```text
Enter number: 7
Output: Prime Number
```
"""


def is_valid_num(prompt):
    while True:
        number = input(prompt)
        try:
            return int(number)
        except ValueError:
            print("Please enter a valid number")


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    number = is_valid_num("Enter a number: ")
    if is_prime(number):
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is not a Prime Number")


if __name__ == "__main__":
    main()
