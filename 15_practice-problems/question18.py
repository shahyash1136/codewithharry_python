"""
# 12. Remove Duplicates from List

```text
Enter list: [1,2,2,3,4,4]
Output: [1,2,3,4]
```
"""

from typing import Any


def remove_duplicates_manually(raw_values: list[Any]) -> list[Any]:
    """
    The function takes the raw list from the user and check if its empty or not and then removes the duplicate values from the raw list by manually looping through the raw list

    Args:
        raw_values(list): The list given by the user to remove duplicates

    Returns:
        list[any]: Return the distinct list to the user

    >>> remove_duplicates_manually([1, 2, 2, 3, 4, 4])
    [1,2,3,4]
    >>> remove_duplicates_manually(["raj", "sham", "sham", "raj", "john", "max"])
    ["raj", "sham", "john", "max"]

    """
    if not raw_values:
        raise ValueError("List cannot be empty")

    seen = set()
    result = []

    for value in raw_values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


def remove_duplicates(raw_values: list[Any]) -> list[Any]:
    """
    The function takes the raw list from the user and check if its empty or not and then removes the duplicate values from the raw list with the help of in build dict.fromkeys() function

    Args:
        raw_values(list): The list given by the user to remove duplicates

    Returns:
        list[any]: Return the distinct list to the user

    >>> remove_duplicates([1, 2, 2, 3, 4, 4])
    [1,2,3,4]
    >>> remove_duplicates(["raj", "sham", "sham", "raj", "john", "max"])
    ["raj", "sham", "john", "max"]

    """
    if not raw_values:
        raise ValueError("List cannot be empty")

    return list(dict.fromkeys(raw_values))


def main() -> None:
    list1 = [1, 2, 2, 3, 4, 4]
    list2 = ["raj", "sham", "sham", "raj", "john", "max"]
    result1 = remove_duplicates(list1)
    result2 = remove_duplicates(list2)
    manual_result1 = remove_duplicates_manually(list1)
    manual_result2 = remove_duplicates_manually(list2)
    print(f"Remove Duplicates : {result1}")
    print(f"Remove Duplicates Manually: {manual_result1}")
    print(f"Remove Duplicates : {result2}")
    print(f"Remove Duplicates Manually : {manual_result2}")


if __name__ == "__main__":
    main()
