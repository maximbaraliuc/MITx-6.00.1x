"""Two test cases with usual parameters"""
from pset_02_problem_03 import min_monthly_payment


def test_case_01():
    """Test with parameters with values in usual range"""

    balance: int = 320000
    annualInterestRate: float = 0.2

    assert min_monthly_payment(
        balance, annualInterestRate) == "Lowest Payment: 29157.09"


def test_case_02():
    """Test with parameters with values in usual range"""

    balance = 999999
    annualInterestRate = 0.18

    assert min_monthly_payment(
        balance, annualInterestRate) == "Lowest Payment: 90325.03"
