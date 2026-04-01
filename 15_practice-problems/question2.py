# ### 2. Celsius to Fahrenheit Converter
# **Question:**
# Convert Celsius temperature to Fahrenheit.

# **Example Output:**
# ```text
# Enter Celsius: 25
# Output: 77.0 Fahrenheit
# Formula (c * 1.8) + 32
# ```


def get_valid_num(prompt):
    while True:
        number = input(prompt).strip()
        try:
            return float(number)
        except ValueError:
            print("Please enter a valid number.")


def celsius_to_fahrenheit():
    celsius_temp = get_valid_num("Enter temperature in Celsius: ")
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    return fahrenheit_temp


temp = celsius_to_fahrenheit()
print(f"The temperature is {temp:.2f} Fahrenheit.")
