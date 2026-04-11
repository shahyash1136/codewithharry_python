"""
## 3. Largest of Three Numbers

**Question:**
Take three numbers and print the largest.

```text
Enter three numbers: 5 12 8
Output: 12
```
"""


from typing import List


def get_valid_numbers(prompt: str) -> List[int]:
    while True:
        values = input(prompt).strip()
        try:
            numbers = [int(v) for v in values.replace(",", " ").split()]
            if not numbers:
                print("Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("Please enter numbers only.")


def get_largest_number(numbers: List[int]) -> int:
    """
    Returns the largest number from a list.

    Args:
        numbers (List[int]): List of integers

    Returns:
        int: Largest number
    """
    return max(numbers)


def main():
    numbers = get_valid_numbers("Enter numbers (space or comma separated): ")
    result = get_largest_number(numbers)
    print(f"Largest number is {result}")


if __name__ == "__main__":
    main()
