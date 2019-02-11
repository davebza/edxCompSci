balance = 320000
annualInterestRate = 0.2
expectedAnswer = 29157.09

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

monthlyInterest = annualInterestRate /12
lowerBound = balance / 12
upperBound = (balance * (1+monthlyInterest)**12)/12
print(f"Upper {upperBound}")

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

if expectedAnswer == minimumPayment:
    print("Hey")
else:
    print("No!")