# Problem 3 - Using Bisection Search to Make the Program Faster

"""Using BISECTION SEARCH the program calculates the minimum fixed and \
constant monthly payment needed in order pay off a credit card balance within \
12 months."""


def min_monthly_payment(balance: float, annual_interest_rate: float) -> str:
    """Return the lowest monthly payment to the cent (0.01$) that will \
    pay off all debt in under 12 months - using bisection search"""

    monthly_interest_rate = (annual_interest_rate) / 12.0
    original_balance = balance
    # Set the lower and upper bound for bisection search
    monthly_pay_low = balance / 12
    monthly_pay_up = (balance*(1 + monthly_interest_rate)**12)/12.0

    # Till the result doesn't differ less than a cent
    while abs(balance) > 0.01:
        # Reinitialize or reset the starting point variables
        balance = original_balance
        monthly_pay = (monthly_pay_low + monthly_pay_up) / 2.0

        # Simulate one year of payments
        for _ in range(12):
            unpaid_balance = balance - monthly_pay
            balance = unpaid_balance + monthly_interest_rate * unpaid_balance

        if balance < 0:
            monthly_pay_up = monthly_pay
        else:
            monthly_pay_low = monthly_pay

    # For the grader(uses python 3.5) on edx use string concatenation
    # return "Lowest Payment: " + str(round(monthly_pay, 2))
    return f"Lowest Payment: {monthly_pay :.2f}"


# The line bellow is intended to be uncommented for the grader on edx.
# print(min_monthly_payment(balance, annualInterestRate))
