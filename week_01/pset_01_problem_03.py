""" Problem set 01 - Problem 3
Assume "s" is a string of lower case characters.
Write a program that prints the longest substring of "s" in which the letters
occur in alphabetical order. For example, if s = "azcbobobegghakl", then your
program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = "abcbcd",
then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart.
If you"ve spent more than a few hours on this problem, we suggest that you
move on to a different part of the course. If you have time, come back to this
problem after you"ve had a break and cleared your head. """

s = "azcbobobegghakl"
# ============================================================================


abc = "abcdefghijklmnopqrstuvwxyz"
final_str = ""
current_str = ""
current_ind = 0

for char in s:
    # If the current letter breaks the alphabetical order, reset the counters
    if char < abc[current_ind]:
        current_str = ""
        current_ind = 0

    # Find a match and its properties,  add it to the temp string
    for ind, letter in enumerate(abc):
        if char == letter:
            current_ind = ind
            current_str += letter
            break

    # Save the final_str if needed
    if len(final_str) < len(current_str):
        final_str = current_str

print("Longest substring in alphabetical order is:", final_str)
