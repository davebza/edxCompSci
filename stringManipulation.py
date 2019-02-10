def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if len(aStr) == 0:
        return False

    if len(aStr) == 1:
        if char == aStr[0]:
            return True
        else:
            return False

    mid = int(len(aStr)/2)

    if char == aStr[mid]:
        return True
    elif char > aStr[mid]:
        aStr = aStr[mid:]
        return isIn(char, aStr)
    else:
        aStr = aStr[:mid]
        return isIn(char, aStr)



# y = isIn("a", "abcdef")
# print(y)

y = isIn('c', 'ccehprruvy')
print(y)


