""" Problem set 01 - Problem 3
Assume "s" is a string of lower case characters.
Write a program that prints the longest substring of "s" in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head. """

abc = "abcdefghijklmnopqrstuvwxyz"
final_str = ""
current_str = ""
current_ind = 0

for char in s:
    # If the current letter breaks the alphabetical order, reset the counters
    if char < abc[current_ind]:
        current_str = ""
        current_ind = 0

    # When a the current_str contains letters add one more if in alphabetical order
    if len(current_str) != 0:
        for i in range(current_ind, len(abc)):
            if char == abc[i]:
                current_str += char
                current_ind = i
                break
    # A new current_str check, loop the ABC to find the first match character.
    else:
        for i in range(len(abc)):
            if char == abc[i]:
                current_ind = i
                current_str += char
                break

    # Save the final_str if needed
    if len(final_str) < len(current_str):
        final_str = current_str

print("Longest substring in alphabetical order is:", final_str)
