# 1. Write a small script  count_lines.py  that takes a filename as input and prints. how many lines are in the file.
# Example usage:
# python count_lines.py tasks.txt
# # Output: Number of lines: 4
import argparse

parser = argparse.ArgumentParser(description="A simple command-line utility.")
parser.add_argument("filename", help="The file to process.")

args = parser.parse_args()

try:
    with open(args.filename, "r") as file:
        lines = sum(1 for line in file)
        print(f"Number of lines: {lines}")
except FileNotFoundError:
    print("File not found")
