# ### 1. Student Information Formatter
# **Question:**
# Write a program that takes a student's name and age as input and prints a formatted sentence.

# **Example Output:**
# ```text
# Enter name: John
# Enter age: 22
# Output: John is 22 years old.
# ```

# ---


def get_valid_name():
    while True:
        name = input("Enter name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: ").strip())
            if age > 0 or age < 120:
                return age
            print("Age must be greater than 0 or less then 120.")
        except ValueError:
            print("Enter a valid number.")


name = get_valid_name()
age = get_valid_age()

print(f"{name} is {age} years old.")
