""" Problem set 01 - Problem 1

Assume "s" is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string "s". Valid vowels are: "a", "e", "i", "o", and "u". For example, if s = "azcbobobegghakl", your program should print:

Number of vowels: 5 """

s = input("Enter some text...")
# vowels = "aeiou"

vowels_counter = 0
for char in s:
    if char in "aeiou":
        vowels_counter += 1

print("Number of vowels:", vowels_counter)
