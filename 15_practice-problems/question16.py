"""
## 10. Prime Number Checker

**Question:**
Check if number is prime.

**Example Input:**

```text
17
```

**Example Output:**

```text
Prime
```
"""


def parse_number(prompt: str) -> int:
    """
    Prompts user for a non-negative integer with validation loop.

    Args:
        prompt (str): Message shown to the user.

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
                print("Please enter only non-negative values.")
                continue
            return value
        except ValueError:
            print(f"'{raw}' is not a valid number. Please enter a whole number.")


def is_prime(number: int) -> bool:
    """
    Checks if a given number is prime.

    Args:
        number (int): Non-negative integer to check.

    Returns:
        bool: True if prime, False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(1)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    """
    if number <= 1:
        return False
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            return False
    return True


def main() -> None:
    number = parse_number("Enter a number: ")
    result = is_prime(number)
    print("Prime" if result else "Not Prime")


if __name__ == "__main__":
    main()
