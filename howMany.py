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




