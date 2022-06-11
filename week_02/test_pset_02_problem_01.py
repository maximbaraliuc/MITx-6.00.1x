"""Two test cases for an account annual balance check"""

from pset_02_problem_01 import annual_remaining_balance


def test_case_01():
    """Checks the annual balance with given parameters"""

    balance = 42
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    assert annual_remaining_balance(
        balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 31.38"


def test_case_02():
    """Checks the annual balance with given parameters"""

    balance = 484
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    assert annual_remaining_balance(
        balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 361.61"


def test_case_03():
    """Checks the annual balance with given parameters"""

    balance = 298
    annualInterestRate = 0.18
    monthlyPaymentRate = 0.08
    assert annual_remaining_balance(
        balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 131.00"


def test_case_04():
    """Checks the annual balance with given parameters"""

    balance = 303
    annualInterestRate = 0.15
    monthlyPaymentRate = 0.06
    assert annual_remaining_balance(
        balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 167.39"


def test_case_05():
    """Checks the annual balance with given parameters"""

    balance = 250
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    assert annual_remaining_balance(
        balance, annualInterestRate, monthlyPaymentRate) == "Remaining balance: 186.78"
