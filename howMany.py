def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here

    count = 0

    for key in aDict:
        current = aDict.get(key)
        count += len(current)

    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    currentBiggest = 0
    count = 0
    currentKey = ""

    for key in aDict:
        current = aDict.get(key)
        count = len(current)
        if count > currentBiggest:
            currentBiggest = count
            currentKey = key

    return currentKey


