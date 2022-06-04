""" Problem set 01 - Problem 2

Assume "s" is a string of lower case characters.

Write a program that prints the number of times the string "bob" occurs in "s". For example, if s = "azcbobobegghakl", then your program should print

Number of times bob occurs is: 2 """


# The s and "bob" are already declared in the problem "grader" on edx webplatform.

s = "azcbobobegghakl"
test_string = "bob"

counter = 0
for i in range(len(s)):
    if s[i:i+len("bob")] == "bob":
        counter += 1
print("Number of times bob occurs is:", counter)
