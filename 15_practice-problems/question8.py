"""
# 1. Number Sign Checker

**Question:** Check whether number is positive, negative or zero.

```text
Enter number: -7
Output: Negative
```
"""


def get_valid_number(prompt: str) -> int:
    while True:
        input_value = input(prompt).strip()
        try:
            return int(input_value)
        except ValueError:
            print("Please enter a valid number")


def get_number_sign(number: int) -> str:
    """
    Determines whether a number is positive, negative, or zero.

    Args:
        number (int): Input number

    Returns:
        str: "Positive", "Negative", or "Zero"
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"


def main():
    number = get_valid_number("Enter a number: ")
    result = get_number_sign(number)
    print(result)


if __name__ == "__main__":
    main()
