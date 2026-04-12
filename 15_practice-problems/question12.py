"""
## 6. Multiplication Table

**Question:**
Print multiplication table of a given number till 10.

**Example Input:**

```text
4
```

**Example Output:**

```text
4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
```
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
                print("Input connot be empty.")
                continue
            value = int(input_value)
            if value <= 0:
                print("Please enter only positive integer.")
            return value
        except ValueError:
            print("Please enter a whole number")


def generate_multiplication_table(number: int, limit: int = 10) -> str:
    """
    Generate the multiplication table of a given number.

    Args:
        number (int): Input number
        limit (int): Range limit (default is 10)

    Returns:
        str: Formatted multiplication table
    """
    table_lines = [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]
    return "\n".join(table_lines)


def main():
    number = parse_number("Enter a number: ")
    result = generate_multiplication_table(number)
    print(result)


if __name__ == "__main__":
    main()
