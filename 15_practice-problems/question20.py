"""
# 14. Sum All Even Numbers

```text
Enter list: [1,2,3,4,5,6]
Output: 12
```
"""


def parse_list(raw_values: list[int | float]):
    """
    The function check the raw list and raises the error if the list is empty or list contains a string in it.
    Args:
        raw_values(list(int)): List given by the user.

    """
    if not raw_values:
        raise ValueError("List cannot be empty")

    if any(isinstance(value, str | float) for value in raw_values):
        raise ValueError("List cannot contain a string or a float value")


def get_sum_of_even_numbers_manually(raw_values: list[int]) -> int:
    """
    The function takes a raw list from the user takes all the even numbers and adds them manually.
    Args:
        raw_values(list[int]) : List given by the user.
    Returns:
        int: Returns the sum of all even numbers

    >>> get_sum_of_even_numbers_manually([1, 2, 3, 4, 5, 6])
    12
    >>> get_sum_of_even_numbers_manually([1, 2.5, "3", 4, 5, 6])
    ValueError: List cannot contain a string or a float value
    """

    parse_list(raw_values)
    total = 0
    for value in raw_values:
        if value % 2 == 0:
            total += value

    return total


def get_sum_of_even_numbers(raw_values: list[int]) -> int:
    """
    The function takes a raw list from the user takes all the even numbers and adds them with the help of in build functions.
    Args:
        raw_values(list[int]) : List given by the user.
    Returns:
        int: Returns the sum of all even numbers

    >>> get_sum_of_even_numbers([1, 2, 3, 4, 5, 6])
    12
    >>> get_sum_of_even_numbers([1, 2.5, "3", 4, 5, 6])
    ValueError: List cannot contain a string or a float value
    """

    parse_list(raw_values)

    return sum([value for value in raw_values if value % 2 == 0])


def main() -> None:
    user_input_lists = [[1, 2, 3, 4, 5, 6], [2, 32, 45, 54, 62]]

    for idx, lst in enumerate(user_input_lists, 1):
        print(f"\nList {idx}: {lst}")
        print(f"Built-in: {get_sum_of_even_numbers(lst)}")
        print(f"Manual: {get_sum_of_even_numbers_manually(lst)}")


if __name__ == "__main__":
    main()
