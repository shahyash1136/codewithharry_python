"""
### 7. Character Frequency Counter
**Question:**
Count frequency of each character.

**Example Output:**
```text
Input: apple
Output: {'a':1,'p':2,'l':1,'e':1}
```
"""


def validate_string(prompt: str):
    while True:
        input_value = input(prompt).strip()

        if not input_value:
            print("Input cannot be empty")
            continue

        if input_value.isdigit():
            print("Input value cannot be a number")
            continue

        return input_value


def character_frequency(text):
    frequency = {}

    for char in text:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    return frequency


def main():
    user_input = validate_string("Enter a character: ")
    response_output = character_frequency(user_input)
    print(response_output)


if __name__ == "__main__":
    main()
