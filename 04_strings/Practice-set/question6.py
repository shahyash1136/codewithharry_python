# 6. Bonus Questions
# 1. Write a program that counts how many vowels are in a given string.
def count_vowels(input_string):
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1
    vowels = 'aeiou'
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count

user_input = input("Enter a string to count the vowels: ")
vowel_count = count_vowels(user_input)
print(f"The number of vowels in the given string is: {vowel_count}")

# 2. Take a user input string and check if it is a palindrome (same forwards and backwards).
text = input("Enter a text to check if its a palindrome?: ").lower()

if text == text[::-1]:
    print("The given word is Palindrome")
else:
    print("The given word is not a Palindrome")
