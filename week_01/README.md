# Problem set 01

## Problem 1

Assume `s` is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string `s`. Valid vowels are: `'a', 'e', 'i', 'o'`, and `'u'`. For example, if `s = 'azcbobobegghakl'`, your program should print:

    Number of vowels: 5

## Solution

```python
vowels_counter = 0
for char in s:
    if char in "aeiou":
        vowels_counter += 1
print("Number of vowels:", vowels_counter)
```

## Problem 2

Assume `s` is a string of lower case characters.

Write a program that prints the number of times the string `'bob'` occurs in `s`. For example, if `s = 'azcbobobegghakl'`, then your program should print

    Number of times bob occurs is: 2

## Solution

```python
counter = 0
for i in range(len(s)):
    if s[i:i+len("bob")] == "bob":
        counter += 1
print("Number of times bob occurs is:", counter)
```

## Problem 3

Assume `s` is a string of lower case characters.

Write a program that prints the longest substring of `s` in which the letters occur in alphabetical order. For example, if `s = 'azcbobobegghakl'`, then your program should print

    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`, then your program should print

    Longest substring in alphabetical order is: abc

:memo: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

## Solution

```python
import string


def longest_substring(s: str) -> str:
    """Returns the longest substring in alphabetical order
    """

    abc = string.ascii_lowercase
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

    return f"Longest substring in alphabetical order is : {final_str}"
```
