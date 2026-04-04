"""
### 6. Reverse String Without Slicing
Question:
Reverse a string without using slicing.
"""


def reverse_string(text: str) -> str:
    return "".join(reversed(text))


def validate_string(prompt: str) -> str:
    while True:
        input_value = input(prompt).strip()

        if not input_value:
            print("Input cannot be empty")
            continue

        if input_value.isdigit():
            print("Input value cannot be a number")
            continue

        return input_value


def main():
    input_value = validate_string("Enter a string to reverse: ")
    reversed_value = reverse_string(input_value)
    print(reversed_value)


if __name__ == "__main__":
    main()
