"""Test the correct output for Problem 3 - Printing Out all Available Letters . \
Number of tests: 6."""

from pset_03_hangman import getAvailableLetters


def test_case_01():
    """Check which letters in a string have not
      yet been guessed."""
    letters = ['e', 'i', 'k', 'p', 'r', 's']
    assert getAvailableLetters(letters) == 'abcdfghjlmnoqtuvwxyz'


def test_case_02():
    """Check which letters in a string have not
      yet been guessed."""
    letters = []
    assert getAvailableLetters(letters) == 'abcdefghijklmnopqrstuvwxyz'


def test_case_03():
    """Check which letters in a string have not
      yet been guessed."""
    letters = ['c', 'a', 'p', 'g', 'n', 'u', 'y', 's', 'h', 't', 'r']
    assert getAvailableLetters(letters) == 'bdefijklmoqvwxz'


def test_case_04():
    """Check which letters in a string have not
      yet been guessed."""
    letters = ['h', 'k', 'l', 'r', 'a', 'd', 'o', 'z']
    assert getAvailableLetters(letters) == 'bcefgijmnpqstuvwxy'


def test_case_05():
    """Check which letters in a string have not
      yet been guessed."""
    letters = ['v', 'w', 'k', 'i', 'l', 's', 'z', 'd', 'c', 'j', 'h', 'p']
    assert getAvailableLetters(letters) == 'abefgmnoqrtuxy'


def test_case_06():
    """Check which letters in a string have not
      yet been guessed."""
    letters = ['g', 'p', 'k', 'h', 'm', 'z', 'y']
    assert getAvailableLetters(letters) == 'abcdefijlnoqrstuvwx'
