def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    listOfSecretLetters = list(secretWord)
    outputList = []

    for letter in listOfSecretLetters:
        if letter in lettersGuessed:
            outputList.append(letter)
        else:
            outputList.append("_")

    outputString = " ".join(outputList)
    return outputString