def calculateMonthlyMinimumPayment(lastMonthBalance):

    paymentDue = lastMonthBalance * monthlyPaymentRate
    #print(f"The minimum payment for this month is {paymentDue}")

    return paymentDue

def newBalance(balance, monthlyInterestRate):

    paymentToRemove = calculateMonthlyMinimumPayment(balance)
    #print(f"removing monthly minimum: {paymentToRemove}")
    workingBalance = balance - paymentToRemove
    #print(f"Balance is now: {workingBalance}")
    returnBalance = workingBalance + (workingBalance * monthlyInterestRate)

    return returnBalance

def monthlyCalculations(balance, monthlyInterestRate):

    balance = newBalance(balance, monthlyInterestRate)

    return round(balance, 2)

#initial values:

# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
numberOfMonths = 12
totalPaid = 0

# Begin Calcs:

count = 0

while count < numberOfMonths:

    count+= 1
    balance = round(monthlyCalculations(balance, monthlyInterestRate), 2)

print("Remaining balance: " + str(balance))
