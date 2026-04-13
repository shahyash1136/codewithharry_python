"""
## 9. Character Frequency Counter
"""

from collections import Counter


def parse_string(prompt: str) -> str:
    """
    Prompts user for an alphabetic string with validation loop.

    Args:
        prompt (str): Message shown to user

    Returns:
        str: Validated lowercase alphabetic string
    """
    while True:
        raw = input(prompt).strip().lower()
        if not raw:
            print("Input cannot be empty.")
            continue
        if not raw.isalpha():
            print("Please enter alphabets only (no numbers or spaces).")
            continue
        return raw


def count_frequency_manual(characters: str) -> dict[str, int]:
    """
    Counts character frequency using manual dict approach.

    Args:
        characters (str): Input string

    Returns:
        dict[str, int]: Character frequency map

    >>> count_frequency_manual("apple")
    {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    """
    frequency = {}
    for char in characters:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def count_frequency_counter(characters: str) -> dict[str, int]:
    """
    Counts character frequency using collections.Counter.

    Args:
        characters (str): Input string

    Returns:
        dict[str, int]: Character frequency map

    >>> count_frequency_counter("apple")
    {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    >>> count_frequency_counter("banana")
    {'b': 1, 'a': 3, 'n': 2}
    """
    return dict(Counter(characters))


def main() -> None:
    value = parse_string("Enter a word: ")

    manual_result = count_frequency_manual(value)
    counter_result = count_frequency_counter(value)

    print(f"Manual  : {manual_result}")
    print(f"Counter : {counter_result}")


if __name__ == "__main__":
    main()
