"""
# 11. Find Largest in List

```text
Enter list: [4, 9, 2, 11]
Output: 11
```
"""


def largest_in_list_manual(numbers: list) -> int:
    """
    The function finds the largest number manually by looping through the list

    Args:
        numbers (list): List given by user

    Returns:
        int: Return the largest number in form of number

    >>> largest_in_list_manual([-10, -5, -3, -6, -5])
    -3
    >>> largest_in_list_manual([4, 9, 2, 11])
    11
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    largest_number = numbers[0]
    for num in numbers:
        if largest_number < num:
            largest_number = num
    return largest_number


def largest_in_list(numbers: list) -> int:
    """
    The function finds the largest number with in build max function

    Args:
        numbers (list): List given by user

    Returns:
        int: Return the largest number in form of number

    >>> largest_in_list([-10, -5, -3, -6, -5])
    -3
    >>> largest_in_list([4, 9, 2, 11])
    11
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


def main() -> None:
    list_arr1 = [2, 5, -3, 6, 10]
    list_arr2 = [-10, -5, -3, -6, -5]
    list_arr3 = [4, 9, 2, 11]
    largest_result1 = largest_in_list(list_arr1)
    largest_result2 = largest_in_list(list_arr2)
    largest_result3 = largest_in_list(list_arr3)
    manual_result1 = largest_in_list_manual(list_arr1)
    manual_result2 = largest_in_list_manual(list_arr2)
    manual_result3 = largest_in_list_manual(list_arr3)
    print(f"Manual Result 1 = {manual_result1}")
    print(f"Largest Result 1 = {largest_result1}")
    print(f"Manual Result 2 = {manual_result2}")
    print(f"Largest Result 2 = {largest_result2}")
    print(f"Manual Result 3 = {manual_result3}")
    print(f"Largest Result 3 = {largest_result3}")


if __name__ == "__main__":
    main()
