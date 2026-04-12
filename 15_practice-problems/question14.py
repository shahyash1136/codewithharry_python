"""
## 8. Palindrome Number

**Question:**
Check whether a number is palindrome.

**Example Input:**

```text
121
```

**Example Output:**

```text
Palindrome
```
"""


def parse_number(prompt: str) -> int:
    """
    Prompts user for a non-negative integer with validation loop.
    Args:
        prompt (str): Message shown to user
    Returns:
        int: Validated non-negative integer
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Input cannot be empty.")
            continue
        try:
            value = int(raw)
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print(f"'{raw}' is not a valid number. Please enter a whole number.")


def palindrome_checker(number: int) -> bool:
    """
    Checks whether a given number is a palindrome or not.
    Args:
        number (int): Input number
    Returns:
        bool: True if palindrome, False otherwise

    >>> palindrome_checker(121)
    True
    >>> palindrome_checker(2566)
    False
    >>> palindrome_checker(0)
    True
    >>> palindrome_checker(1)
    True
    """
    return str(number) == str(number)[::-1]


def main() -> None:
    number = parse_number("Enter a number to check if it's a palindrome: ")
    result = palindrome_checker(number)
    print("Palindrome" if result else "Not a Palindrome")


if __name__ == "__main__":
    main()
