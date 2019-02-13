def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here



    oddList = []

    if len(aTup) == 0:
        return tuple(oddList)

    oddList.append(aTup[0])


    count = 1

    while count < len(aTup):

        if count % 2 == 0:
            oddList.append(aTup[count])

        count += 1

    return tuple(oddList)


myOddTUp = oddTuples((15, 8, 19, 16, 2, 2))
print(myOddTUp)