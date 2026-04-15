"""
# 15. Separate Even and Odd

```text
Enter list: [1,2,3,4,5]
Output:
Even: [2,4]
Odd: [1,3,5]
```
"""


def parse_list(raw_values: list[int]) -> None:
    """
    The function check the raw list and raises the error if the list is empty or list contains a string in it.
    Args:
        raw_values(list(int)): List given by the user.
    """
    if not raw_values:
        raise ValueError("List cannot be empty")

    if any(isinstance(value, str | float) for value in raw_values):
        raise ValueError("List cannot contain a string or a float value")


def get_even_odd_numbers_manually(raw_values: list[int]) -> tuple[list[int], list[int]]:
    """
    The function takes a raw list from the user and loops through it to give the odd and even numbers.
    Args:
        raw_values(list(int)): List given by the user.
    Returns:
        tuple[list[int], list[int]]: Returns Odd and Even List to the user

    >>> get_even_odd_numbers_manually([1,2,3,4,5])
    Even : [2, 4]
    Odd : [1, 3, 5]
    """
    parse_list(raw_values)
    even = []
    odd = []
    for value in raw_values:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)

    return even, odd


def get_even_odd_numbers(raw_values: list[int]) -> tuple[list[int], list[int]]:
    """
    The function takes a raw list from the user and filters the value to give the odd and even numbers.
    Args:
        raw_values(list(int)): List given by the user.
    Returns:
        tuple[list[int], list[int]]: Returns Odd and Even List to the user

    >>> get_even_odd_numbers([1,2,3,4,5])
    Even : [2, 4]
    Odd : [1, 3, 5]
    """
    parse_list(raw_values)
    odd = filter(lambda value: value % 2 != 0, raw_values)
    even = [value for value in raw_values if value % 2 == 0]

    return even, list(odd)


def main() -> None:
    user_input_lists = [[1, 2, 3, 4, 5, 6], [2, 32, 45, 54, 62]]

    result = get_even_odd_numbers(user_input_lists[0])
    even, odd = result
    print(f"Even : {even}")
    print(f"Odd : {odd}")

    result_manual = get_even_odd_numbers(user_input_lists[1])
    even, odd = result_manual
    print(f"Even Manually: {even}")
    print(f"Odd  Manually: {odd}")


if __name__ == "__main__":
    main()
