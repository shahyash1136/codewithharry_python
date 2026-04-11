"""
## 2. Even or Odd with Type Conversion

**Question:**
Take input as string, convert to integer, and check if number is even or odd.

```text
Enter number: 14
Output: Even
```
"""


def get_valid_number(prompt: str) -> int:
    while True:
        input_value = input(prompt).strip()
        try:
            return int(input_value)
        except ValueError:
            print("Please enter a valid integer")


def get_even_or_odd(number: int) -> str:
    """
    Determine whether a number is even or odd.

    Args:
        number (int): Input number

    Returns:
        str: "Even" or "Odd"
    """
    if number % 2 == 0:
        return "Even"
    return "Odd"


def main():
    number = get_valid_number("Enter a number: ")
    result = get_even_or_odd(number)
    print(result)


if __name__ == "__main__":
    main()
