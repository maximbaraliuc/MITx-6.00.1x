""" Problem set 01 - Problem 3

Assume "s" is a string of lower case characters.

Write a program that prints the longest substring of "s" in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head. """

s = 'azcbobobegghakl'  # Longest substring in alphabetical order is: beggh
s = 'abcbcd'  # Longest substring in alphabetical order is: abc
# s = 'zzcaisxes'  # Longest substring in alphabetical order is: aisx
# s = 'jwnkynbeqnevcsbhwbdi'  # Longest substring in alphabetical order is: beq
# s = 'yijduigpkuccmbnlnnsz'  # Longest substring in alphabetical order is: lnnsz
# s = 'xnwkjtqoxqmorzk'  # Longest substring in alphabetical order is: morz


abc = "abcdefghijklmnopqrstuvwxyz"
temporary_string = ""
stored_string = ""
abc_index = 0

for char in s:
    if len(temporary_string) != 0:
        if char < abc[abc_index]:
            #  Check the strings lengths
            if len(stored_string) < len(temporary_string):
                stored_string = temporary_string
            # Reset everything
            temporary_string = ""
            abc_index = 0
        else:
            for i in range(abc_index, len(abc)):
                if char == abc[i]:
                    temporary_string += char
                    abc_index = i
                    break

    if len(temporary_string) == 0:
        # Loop through ABC to find a match
        for i in range(len(abc)):
            if char == abc[i]:
                abc_index = i
                temporary_string += char
                break

        # if abc_index == len(abc)-1:
        #     # Check the strings lengths
        #     if len(stored_string) < len(temporary_string):
        #         stored_string = temporary_string
        #     # Reset everything
        #     temporary_string = ""
        #     abc_index = 0
        #     break

if len(stored_string) < len(temporary_string):
    stored_string = temporary_string


print("Longest substring in alphabetical order is:", stored_string)


# check if code is not generate errors related to "len(abc))".
