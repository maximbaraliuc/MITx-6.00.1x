#  Problem 2 - Paying Debt off in a Year

"""A program that calculates the minimum fixed monthly (constant) payment \
needed in order pay off a credit card balance within 12 months. \
Monthly pay should be divisible by 10$"""


def min_monthly_payment(balance: int, annual_interest_rate: float) -> str:
    """Return the lowest monthly payment that will pay off all debt in under \
    12 months"""

    monthly_interest_rate = (annual_interest_rate) / 12.0

    # Set a min for the constant of monthly pay
    monthly_pay = balance // 120 * 10
    current_balance = balance

    while current_balance > 0:
        # Modify or reset the starting point variables
        current_balance = balance
        monthly_pay += 10

        # Simulate one year of payments
        for _ in range(12):
            unpaid_balance = current_balance - monthly_pay
            current_balance = unpaid_balance + monthly_interest_rate * unpaid_balance

    # For the grader(uses python 3.5) on edx use string concatenation
    return "Lowest Payment: " + str(monthly_pay)
    # return f"Lowest Payment: {monthly_pay}"


# The line bellow is intended to be uncommented for the grader on edx.
# print(min_monthly_payment(balance, annualInterestRate))
