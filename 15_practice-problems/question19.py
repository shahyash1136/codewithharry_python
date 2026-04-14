"""
# 13. Second Largest Number

```text
Enter list: [10, 20, 5, 8]
Output: 10
```
"""

from typing import List


def parse_list(raw_values: List[int]):
    """
    The function check the raw list and raises the error if the list is empty or list contains a string in it.
    Args:
        raw_values(List(int)): The Raw list added by the user

    """
    if not raw_values:
        raise ValueError("List cannot be empty")

    if any(isinstance(value, str) for value in raw_values):
        raise ValueError("List cannot contain a string")


def check_second_largest_manually(raw_values: List[int]) -> int:
    """
    The function manually loops through the raw integer list and check and returns the second largest number from the list.
    Args:
        raw_values(List(int)): The Raw list added by the user
    Returns:
        int: Returns the second largest number from the list

    >>> check_second_largest_manually([10, 20, 5, 8])
    10
    >>> check_second_largest_manually([-10, -20, -5, -8])
    -8
    """
    parse_list(raw_values)
    if len(raw_values) < 2:
        raise ValueError("At least two elements required")

    largest = second_largest = float("-inf")

    for num in raw_values:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    if second_largest == float("-inf"):
        raise ValueError("No second largest value found")

    return second_largest


def check_second_largest(raw_values: List[int]) -> int:
    """
    The function checks the raw integer list and returns the second largest number from the list with the help of in build functions.
    Args:
        raw_values(List(int)): The Raw list added by the user
    Returns:
        int: Returns the second largest number from the list

    >>> check_second_largest([10, 20, 5, 8])
    10
    >>> check_second_largest([-10, -20, -5, -8])
    -8
    """
    parse_list(raw_values)

    unique = list(dict.fromkeys(raw_values))

    if len(unique) < 2:
        raise ValueError("At least two distinct values required")

    return sorted(unique)[-2]


def main() -> None:
    result_manually1 = check_second_largest_manually([10, 20, 5, 8])
    result_manually2 = check_second_largest_manually([-10, -20, -5, -8])
    result1 = check_second_largest([10, 20, 5, 8])
    result2 = check_second_largest([-10, -20, -5, -8])
    print(result_manually1)
    print(result_manually2)
    print(result1)
    print(result2)


if __name__ == "__main__":
    main()
