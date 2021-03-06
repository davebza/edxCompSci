def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    listOfSecretLetters = list(set(secretWord))

    for letter in lettersGuessed:
        if letter in listOfSecretLetters:
            index = listOfSecretLetters.index(letter)
            listOfSecretLetters.pop(index)

    if len(listOfSecretLetters) == 0:
        return True
    elif len(listOfSecretLetters) > 0:
        return False
