def newBalance(balance, monthlyInterest, minimumPayment):

    workingBalance = balance - minimumPayment

    workingBalance = workingBalance + (workingBalance * monthlyInterest)

    return round(workingBalance, 2)

def testMini(balance):

    count = 0
    while count < 12:
        count += 1
        balance = newBalance(balance, monthlyInterest, minimumPayment)

    return balance

balance = 33290
annualInterestRate = 0.2
monthlyInterest = annualInterestRate /12
minimumPayment = 0
testedBalance = balance


# count = 0
# while count < 12:
#     count += 1
#     balance = newBalance(balance, monthlyInterest, minimumPayment)

while testedBalance > 0:
    minimumPayment += 10
    testedBalance = testMini(balance)
    #print(testedBalance)

print("Lowest payment: "+ str(minimumPayment))
