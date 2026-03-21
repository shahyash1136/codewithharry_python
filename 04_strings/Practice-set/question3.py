# 3. String Methods and Functions
# 1. Take the string  " i love python programming "  and:
#     a. Remove extra spaces from both ends
#     b. Convert it to title case
#     c. Count how many times  "o"  appears
text = " i love python programming "
print(text.strip())
print(text.title())
print(text.count("o"))

# 2. Check if the string  "123abc"  is alphanumeric.
text = "123abc"
print(text.isalnum())