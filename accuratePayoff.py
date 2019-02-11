def newBalance(balance, monthlyInterest, minimumPayment):

    workingBalance = balance - minimumPayment
    workingBalance = workingBalance + (workingBalance * monthlyInterest)

    return workingBalance

def testMini(balance):

    count = 0
    while count < 12:
        count += 1
        balance = newBalance(balance, monthlyInterest, minimumPayment)

    return balance

# Values:

balance = 320000
annualInterestRate = 0.2
expectedAnswer = 29157.09
monthlyInterest = annualInterestRate /12

lowerBound = balance / 12
upperBound = (balance * (1+monthlyInterest)**12)/12


print(f"Lower: {lowerBound}")
print(f"Upper: {upperBound}")

minimumPayment = upperBound/2
testedBalance = balance
count = 0

print(f"Minimum: {minimumPayment}")
testedBalance = testMini(balance)
print(f"New balance: {testedBalance}")

if expectedAnswer == minimumPayment:
    print("Hey")
else:
    print("No!")

print(count)