"""
## 7. Sum of Digits

**Question:**
Find sum of digits of a number.

**Example Input:**

```text
1234
```

**Example Output:**

```text
10
"""


def parse_number(prompt: str) -> int:
    """
    Prompts user for a positive integer with validation loop.
    Args:
        prompt (str): Message shown to user
    Returns:
        int: Validated positive integer
    """
    while True:
        input_value = input(prompt).strip()
        try:
            if not input_value:
                print("Input cannot be empty.")
                continue
            value = int(input_value)
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number")


def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits of a given number.
    Args:
        number(int): Input Number

    Returns:
        int: Sum of digits

    """
    total = sum(int(digit) for digit in str(number))
    return total


def main() -> None:
    number = parse_number("Enter a number: ")
    result = sum_of_digits(number)
    print(f"The sum of digits of {number} is: {result}")


if __name__ == "__main__":
    main()
