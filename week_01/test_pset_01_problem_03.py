"""Multiple test of the same definition with various string inputs"""

from pset_01_problem_03 import longest_substring


def test_01():
    """Test with a given string"""
    assert longest_substring(
        "fhiaehyvdjzjrwaqguxgii") == "Longest substring in alphabetical order is : aehy"


def test_02():
    """Test with a given string"""
    assert longest_substring(
        "fhiaehyvdjzjrwaqguxgii") == "Longest substring in alphabetical order is : aehy"


def test_03():
    """Test with a given string"""
    assert longest_substring(
        "midlqbmggcuicrnpwowft") == "Longest substring in alphabetical order is : dlq"


def test_04():
    """Test with a given string"""
    assert longest_substring(
        "kiwyuidhasyztfetziiivar") == "Longest substring in alphabetical order is : asyz"


def test_05():
    """Test with a given string"""
    assert longest_substring(
        "eojfarapyicidcewaqthzp") == "Longest substring in alphabetical order is : apy"


def test_06():
    """Test with a given string"""
    assert longest_substring(
        "mklwfnsrkakjnhuaopxylci") == "Longest substring in alphabetical order is : aopxy"


def test_07():
    """Test with a given string"""
    assert longest_substring(
        "oqigvmyctvkbnugxwjbb") == "Longest substring in alphabetical order is : ctv"


def test_08():
    """Test with a given string"""
    assert longest_substring(
        "cfmcnjmzovhbqfngvz") == "Longest substring in alphabetical order is : cfm"


def test_09():
    """Test with a given string"""
    assert longest_substring(
        "abcdefghijklmnopqrstuvwxyz") == "Longest substring in alphabetical order is : abcdefghijklmnopqrstuvwxyz"


def test_10():
    """Test with a given string"""
    assert longest_substring(
        "qpgouyrmqrgvq") == "Longest substring in alphabetical order is : gouy"


def test_11():
    """Test with a given string"""
    assert longest_substring(
        "eypjdfdhpaai") == "Longest substring in alphabetical order is : dhp"


def test_12():
    """Test with a given string"""
    assert longest_substring(
        "njwwndbugrfealxurhce") == "Longest substring in alphabetical order is : jww"


def test_13():
    """Test with a given string"""
    assert longest_substring(
        "zyxwvutsrqponmlkjihgfedcba") == "Longest substring in alphabetical order is : z"


def test_14():
    """Test with a given string"""
    assert longest_substring(
        "sdbepvclczxkpjaosmqxgn") == "Longest substring in alphabetical order is : bepv"


def test_15():
    """Test with a given string"""
    assert longest_substring(
        "khgjngbgsxrdtcfjmlnocegi") == "Longest substring in alphabetical order is : bgsx"


def test_16():
    """Test with a given string"""
    assert longest_substring(
        "uqfkcnmaijvnumyykvgsuen") == "Longest substring in alphabetical order is : aijv"


def test_17():
    """Test with a given string"""
    assert longest_substring(
        "        vmpegktggfghrothavmoxgv") == "Longest substring in alphabetical order is : egkt"


def test_18():
    """Test with a given string"""
    assert longest_substring(
        "        dalmmzjazuxuwgrbuedybu") == "Longest substring in alphabetical order is : almmz"


def test_19():
    """Test with a given string"""
    assert longest_substring(
        "uadncmpxkan") == "Longest substring in alphabetical order is : cmpx"


def test_20():
    """Test with a given string"""
    assert longest_substring(
        "sbuxegkmkhrasrcd") == "Longest substring in alphabetical order is : egkm"


def test_21():
    """Test with a given string"""
    assert longest_substring(
        "kozrqmkhcptqaihref") == "Longest substring in alphabetical order is : koz"
