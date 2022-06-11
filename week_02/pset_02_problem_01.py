#  Problem 1 - Paying Debt off in a Year

"""A program that calculates the credit card balance after one year \
if a person only pays the minimum monthly payment required by the credit \
card company each month"""


def annual_remaining_balance(
        balance: int,
        annual_interest_rate: float,
        monthly_payment_rate: float) -> str:
    """Calculates statements on the monthly payment and remaining balance and \
    returns the remaining balance after 12 months
    """
    monthly_interest_rate = (annual_interest_rate) / 12.0

    for month in range(12):
        monthly_pay = balance * monthly_payment_rate
        unpaid_balance = balance - monthly_pay
        balance = unpaid_balance + monthly_interest_rate * unpaid_balance

    # For the grader(uses python 3.5) on edx use string concatenation
    # return "Remaining balance: " + str(round(balance, 2))
    return f"Remaining balance: {balance :.2f}"


# The line bellow is intended to be uncommented for the grader on edx.
# print(annual_remaining_balance(balance, annualInterestRate, monthlyPaymentRate))
