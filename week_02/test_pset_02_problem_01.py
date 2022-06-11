"""Two test cases for an account annual balance check"""

from pset_02_problem_01 import annual_remaining_balance


def test_case_01():
    """Checks the annual balance with given parameters"""
    assert annual_remaining_balance(
        42, 0.2, 0.04) == "Remaining balance: 31.38"


def test_case_02():
    """Checks the annual balance with given parameters"""
    assert annual_remaining_balance(
        484, 0.2, 0.04) == "Remaining balance: 361.61"
