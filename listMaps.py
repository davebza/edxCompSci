def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def f(number):
    returnVal = abs(number)
    #return (returnVal)

testList = [1, -4, 8, -9]

y = (applyToEach(testList, f))
print(y)
