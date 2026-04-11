"""
## 4. Reverse a String

**Question:**
Reverse a string without using built-in reverse methods.

```text
Enter string: python
Output: nohtyp
```
"""


def reverse_string(string: str) -> str:
    """
    Reverse a string without using built-in reverse methods or slicing.

    Args:
        string (str): Input string

    Returns:
        str: Reversed string
    """
    reversed_chars = []
    for i in range(len(string) - 1, -1, -1):
        reversed_chars.append(string[i])
    return "".join(reversed_chars)


def main():
    string_input = input("Enter a string: ")
    result = reverse_string(string_input)
    print(result)


if __name__ == "__main__":
    main()
