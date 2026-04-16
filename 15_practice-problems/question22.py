"""
# 16. Rotate List Left by 1

```text
Enter list: [1,2,3,4]
Output: [2,3,4,1]
```
"""

from typing import Any


def rotate_list(raw_list: list[Any], number: int = 1) -> list[Any]:
    """
    The function rotates the list given by the user from left by n times.
    Args:
        raw_list(list[Any]): Raw list given by the user
        number(int): Number to rotate the list from left
    Returns:
        list[Any]: Returns the modified list
    >>> rotate_list([1, 2, 3, 4], 1)
    [2, 3, 4, 1]
    >>> rotate_list([1, 2, 3, 4], 2)
    [3, 4, 1, 2]
    >>> rotate_list([1, 2, 3, 4], 4)
    [1, 2, 3, 4]
    """
    if not raw_list:
        raise ValueError("List cannot be empty")

    if number < 0:
        raise ValueError("number must be non-negative")

    rotate = number % len(raw_list)

    return raw_list[rotate:] + raw_list[:rotate]


def main() -> None:
    test_cases = [
        ([1, 2, 3, 4], 1),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4], 6),
        ([1, 2, 3, 4], 0),
    ]
    for lst, n in test_cases:
        print(f"rotate_list({lst}, {n}) → {rotate_list(lst, n)}")


if __name__ == "__main__":
    main()
