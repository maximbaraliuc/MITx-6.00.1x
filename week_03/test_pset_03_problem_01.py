"""Test the correct output for  Problem 1 - Is the Word Guessed. \
Number of tests: 6."""

from pset_03_hangman import isWordGuessed


def test_case_01():
    """Check if the letters in a string are matched by a list of letters"""
    word = "apple"
    letters = ['a', 'e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(word, letters) is False


def test_case_02():
    """Check if the letters in a string are matched by a list of letters"""
    word = "durian"
    letters = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
    assert isWordGuessed(word, letters) is True


def test_case_03():
    """Check if the letters in a string are matched by a list of letters"""
    word = "grapefruit"
    letters = ['t', 'h', 'n', 'f', 'r', 'x', 'w', 'c', 'b', 'p']
    assert isWordGuessed(word, letters) is False


def test_case_04():
    """Check if the letters in a string are matched by a list of letters"""
    word = "carrot"
    letters = ['w', 'm', 'j', 'u', 'c', 'x', 'q', 'o', 'i', 'r']
    assert isWordGuessed(word, letters) is False


def test_case_05():
    """Check if the letters in a string are matched by a list of letters"""
    word = "pineapple"
    letters = []
    assert isWordGuessed(word, letters) is False


def test_case_06():
    """Check if the letters in a string are matched by a list of letters"""
    word = "carrot"
    letters = ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']
    assert isWordGuessed(word, letters) is True
