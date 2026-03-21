# 4. String Formatting and f-Strings
# 1. Using  format() , create a sentence:
#   "My name is John and I am 25 years old."
#   by passing  "John"  and  25  as variables.
name = "John"
age = 25
text = "My name is {} and I am {} years old."
print(text.format(name, age))

# 2. Do the same using f-strings.
print(f"My name is {name} and I am {age} years old.")
