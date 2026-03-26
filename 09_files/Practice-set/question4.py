# 4. Creating Command Line Utilities


# 2 Write a command-line utility  search_word.py  that takes two arguments:
#   a. A filename
#   b. A word to search and prints how many times the word appears in the file.
# import argparse

# parser = argparse.ArgumentParser(
#     description="A word search to print how many times the word appears in the file"
# )
# parser.add_argument("filename", help="The file to process")
# parser.add_argument("word", help="A word to search in the file")

# args = parser.parse_args()

# try:
#     with open(args.filename, "r") as file:
#         wordSum = sum(1 for args.word in file)
#         print(wordSum)

# except FileNotFoundError:
#     print("File not found")

import sys


def search_word(word, string):
    return string.count(word)


if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename) as f:
        string = f.read()
        n = search_word(word, string)
        print(f"There are {n} occurences of {word} in the file {filename}")
