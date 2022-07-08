# Problem set 05

- [**Introduction**](#introduction)
- [**Problem 01**](#problem-1---build-the-shift-dictionary-and-apply-shift)
- [**Problem 02**](#problem-2---plaintextmessage)
- [**Problem 03**](#problem-3---ciphertextmessage)
- [**Problem 04**](#problem-4---decrypt-a-story)

## Introduction

Encryption is the process of obscuring information to make it unreadable without special knowledge. For centuries, people have devised schemes to encrypt messages - some better than others - but the advent of the computer and the Internet revolutionized the field. These days, it's hard not to encounter some sort of encryption, whether you are buying something online or logging into a shared computer system. Encryption lets you share information with other trusted people, without fear of disclosure.

A cipher is an algorithm for performing encryption (and the reverse, decryption). The original information is called plaintext. After it is encrypted, it is called ciphertext. The ciphertext message contains all the information of the plaintext message, but it is not in a format readable by a human or computer without the proper mechanism to decrypt it; it should resemble random gibberish to those for whom it is not intended.

A cipher usually depends on a piece of auxiliary information, called a key. The key is incorporated into the encryption process; the same plaintext encrypted with two different keys should have two different ciphertexts. Without the key, it should be difficult to decrypt the resulting ciphertext into readable plaintext.

This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher. Some vocabulary to get you started on this problem:

- _Encryption_ - the process of obscuring or encoding messages to make them unreadable until they are decrypted
- _Decryption_ - making encrypted messages readable again by decoding them
- _Cipher_ - algorithm for performing encryption and decryption
- _Plaintext_ - the original message
- _Ciphertext_ - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish.

**The Caesar Cipher**

The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet). Here is what the whole alphabet looks like shifted three spots to the right:

`Original: a b c d e f g h i j k l m n o p q r s t u v w x y z`

`3-shift: d e f g h i j k l m n o p q r s t u v w x y z a b c`

Using the above key, we can quickly translate the message "happy" to "kdssb" (note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c).

**Note!!** We are using the English alphabet for this problem - that is, the following letters in the following order:

```python
>>> import string
>>> print string.ascii_lowercase
>>> abcdefghijklmnopqrstuvwxyz
```

We will treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to "A", then the same lowercase letter should map to "a". Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a corresponding ciphertext with a comma in the same position.

```markdown
| plaintext       | shift     | ciphertext      |
| --------------- | --------- | --------------- |
| 'abcdef'        | 2         | 'cdefgh'        |
| 'Hello, World!' | 5         | 'Mjqqt, Btwqi!' |
| ''              | any value | ''              |
```

We implemented for you two helper functions: `load_words `and `is_word`. You may use these in your solution and you do not need to understand them completely, but should read the associated comments. You should read and understand the helper code in the rest of the file and use it to guide your solutions.

**Getting Started**

To get started, download the [ps6.zip](https://courses.edx.org/assets/courseware/v1/a3239690f87a97bb3be2e75b0917bf38/asset-v1:MITx+6.00.1x+2T2022+type@asset+block/ps6.zip) file. Extract it to your working directory. The files inside are:

- ps6.py - a file containing three classes that you will have to implement.
- words.txt - a file containing valid English words (should be in the same folder as your ps6..py file).
- story.txt - a file containing an encrypted message that you will have to decode (should be in the same folder as your ps6..py file).

This will be your first experience coding with classes! We will have a `Message` class with two subclasses `PlaintextMessage` and `CiphertextMessage` .

[**^ go up**](#problem-set-05)

## Problem 1 - Build the Shift Dictionary and Apply Shift

The `Message` class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

In the next two questions, you will fill in the methods of the `Message` class found in `ps6.py` according to the specifications in the docstrings. The methods in the `Message` class already filled in are:

- `__init__(self, text)`
- The getter method `get_message_text(self)`
- The getter method `get_valid_words(self)`, notice that this one returns a copy of `self.valid_words` to prevent someone from mutating the original list.

In this problem, you will fill in two methods:

1. Fill in the `build_shift_dict(self, shift)` method of the `Message` class. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

   If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by `string.ascii_lowercase` and `string.ascii_uppercase`:

   ```python
   >>> import string
   >>> print(string.ascii_lowercase)
   abcdefghijklmnopqrstuvwxyz
   >>> print(string.ascii_uppercase)
   ABCDEFGHIJKLMNOPQRSTUVWXYZ
   ```

   A reminder from the introduction page - characters such as the space character, commas, periods, exclamation points, etc will _not_ be encrypted by this cipher - basically, all the characters within `string.punctuation`, plus the space (`' '`) and all numerical characters (0 - 9) found in `string.digits`.

2. Fill in the `apply_shift(self, shift)` method of the `Message` class. You may find it easier to use `build_shift_dict(self, shift)`. Remember that spaces and punctuation should not be changed by the cipher.

Paste your implementation of the `Message` class in the box below.

## Solution

```python
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''

        # Create lower and uppercase alphabet strings and apply a shift to it
        abc_low = string.ascii_lowercase
        abc_up = string.ascii_uppercase
        abc_low_shift = abc_low[shift:] + abc_low[: shift]
        abc_up_shift = abc_up[shift:] + abc_up[: shift]

        dict_low = {}
        dict_up = {}

        # In case if the shift number is bigger than the abc
        if shift >= 26:
            shift = shift % 26

        # Apply the the shift and unify the upper lower in a dictionary
        for a, b in zip(abc_low, abc_low_shift):
            dict_low[a] = b

        for a, b in zip(abc_up, abc_up_shift):
            dict_up[a] = b

        dict_low.update(dict_up)
        # print(dict_low)

        return dict_low

    def apply_shift(self, shift):
        '''
            Applies the Caesar Cipher to self.message_text with the input shift.
            Creates a new string that is self.message_text shifted down the
            alphabet by some number of characters determined by the input shift

            shift (integer): the shift with which to encrypt the message.
            0 <= shift < 26

            Returns: the message text (string) in which every character is shifted
                down the alphabet by the input shift
            '''

        shift_dict = self.build_shift_dict(shift)
        abc_ABC = string.ascii_letters
        message_shift = ""

        for char in self.message_text:
            if char in abc_ABC:
                message_shift += shift_dict[char]
            else:
                message_shift += char

        return message_shift
```

[**^ go up**](#problem-set-05)

## Problem 2 - PlaintextMessage

For this problem, the graders will use our implementation of the `Message` class, so don't worry if you did not get the previous parts correct.

`PlaintextMessage` is a subclass of `Message` and has methods to encode a string using a specified shift value. Our class will always create an encoded version of the message, and will have methods for changing the encoding.

Implement the methods in the class `PlaintextMessage` according to the specifications in ps6.py. The methods you should fill in are:

- `__init__(self, text, shift)`: Use the parent class constructor to make your code more concise.
- The getter method `get_shift(self)`
- The getter method `get_encrypting_dict(self)`: This should return a COPY of `self.encrypting_dict` to prevent someone from mutating the original dictionary.
- The getter method `get_message_text_encrypted(self)`
- `change_shift(self, shift)`: Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.

Paste your implementation of the entire `PlaintextMessage` class in the box below.

## Solution

```python
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
```

[**^ go up**](#problem-set-05)

## Problem 3 - CiphertextMessage

For this problem, the graders will use our implementation of the `Message` and `PlaintextMessage` classes, so don't worry if you did not get the previous parts correct.

Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. If `message` is the encrypted message, and `s` is the shift used to encrypt the message, then `apply_shift(message, 26-s)` gives you the original plaintext message. Do you see why?

The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift! We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher! A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

Fill in the methods in the class `CiphertextMessage` according to the specifications in ps6.py. The methods you should fill in are:

- `__init__(self, text)`: Use the parent class constructor to make your code more concise.
- `decrypt_message(self)`: You may find the helper function `is_word(wordlist, word)` and the string [method `split()`](https://docs.python.org/3/library/stdtypes.html#str.split) useful. Note that `is_word` will ignore punctuation and other special characters when considering whether a word is valid.

**Hints**

**Using string.split**

You may find the function `string.split` useful for dividing the text up into words.

```python
>>> 'Hello world!'.split('o')
['Hell', ' w', 'rld!']
>>> '6.00.1x is pretty fun'.split(' ')
['6.00.1x', 'is', 'pretty', 'fun']
```

Paste your implementation of the entire `CiphertextMessage` class in the box below.

## Solution

```python
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        final_count = 0
        current_count = 0

        best_shift = 0
        best_message = ""

        for shift in range(26):
            current_count = 0

            # Generate a shifted dictionary and apply to decipher
            self.shift = shift
            self.encrypting_dict = self.build_shift_dict(self.shift)
            message_text = self.apply_shift(self.shift)

            # Split the deciphered text into words
            words = message_text.split(" ")

            for word in words:
                if is_word(self.valid_words, word):
                    current_count += 1

            # Choose the version with most valid words
            if final_count <= current_count:
                final_count = current_count
                best_shift = shift
                best_message = message_text

        return (best_shift, best_message)
```

[**^ go up**](#problem-set-05)
​

## Problem 4 - Decrypt a Story

For this problem, the graders will use our implementation of the `Message`, `PlaintextMessage`, and `CiphertextMessage` classes, so don't worry if you did not get the previous parts correct.

Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function `get_story_string()` that returns the encrypted version of the story as a string. Create a `CiphertextMessage` object using the story string and use `decrypt_message` to return the appropriate shift value and unencrypted story string.

Paste your function `decrypt_story()` in the box below.

## Solution

```python
def decrypt_story():
    story = get_story_string()
    story_cipher = CiphertextMessage(story)
    return story_cipher.decrypt_message()

```

[**^ go up**](#problem-set-05)
