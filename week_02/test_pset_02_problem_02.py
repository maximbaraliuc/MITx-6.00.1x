"""Three test cases with usual parameters"""
from pset_02_problem_02 import min_monthly_payment


def test_case_01():
    """Test with parameters with values in usual range"""

    balance: int = 3329
    annualInterestRate: float = 0.2
    assert min_monthly_payment(
        balance, annualInterestRate) == "Lowest Payment: 310"


def test_case_02():
    """Test with parameters with values in usual range"""

    balance = 4773
    annualInterestRate = 0.2
    assert min_monthly_payment(
        balance, annualInterestRate) == "Lowest Payment: 440"


def test_case_03():
    """Test with parameters with values in usual range"""

    balance = 3926
    annualInterestRate = 0.2
    assert min_monthly_payment(
        balance, annualInterestRate) == "Lowest Payment: 360"
