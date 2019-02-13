monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
epsilon = 0.01

# Keep testing new payment values until the balance is +/- lowestBalance
while abs(balance) > epsilon:
    # Reset balance:
    balance = originalBalance
    # Calculate a new monthly payment:
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test this guess:
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds in light of this:
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment

# When the while loop terminates, we know we have our answer!
print("Lowest Payment:", round(payment, 2))