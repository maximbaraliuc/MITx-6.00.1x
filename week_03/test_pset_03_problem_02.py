"""Test the correct output for  Problem 2 - Getting the User's Guess. \
Number of tests: 6."""

from pset_03_hangman import getGuessedWord


def test_case_01():
    """Check which letters in a string are matched by a list of letters"""
    word = "apple"
    letters = ['e', 'i', 'k', 'p', 'r', 's']
    assert getGuessedWord(word, letters) == '_ pp_ e'


def test_case_02():
    """Check which letters in a string are matched by a list of letters"""
    word = "durian"
    letters = ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']
    assert getGuessedWord(word, letters) == 'durian'


def test_case_03():
    """Check which letters in a string are matched by a list of letters"""
    word = "mangosteen"
    letters = ['g', 'k', 'c', 'a', 'd', 'm', 'r', 'i', 'v', 'b']
    assert getGuessedWord(word, letters) == 'ma_ g_ _ _ _ _ _ '


def test_case_04():
    """Check which letters in a string are matched by a list of letters"""
    word = "broccoli"
    letters = ['x', 'c', 'o', 'i', 'b', 'v', 'u', 'j', 'f', 'w']
    assert getGuessedWord(word, letters) == 'b_ occo_ i'


def test_case_05():
    """Check which letters in a string are matched by a list of letters"""
    word = "lettuce"
    letters = []
    assert getGuessedWord(word, letters) == '_ _ _ _ _ _ _ '


def test_case_06():
    """Check which letters in a string are matched by a list of letters"""
    word = "banana"
    letters = ['y', 'i', 's', 'a', 'h', 'c', 'x', 'r', 'n', 'o']
    assert getGuessedWord(word, letters) == '_ anana'
