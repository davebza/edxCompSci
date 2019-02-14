import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    #Get a list of all possible letters:
    allLetters = string.ascii_lowercase
    listOfAllLetters = list(allLetters)

    #compare letters in lettersGuessed, and if the letter has been guessed, remove it from all letters:

    for letter in lettersGuessed:
        if letter in listOfAllLetters:
            listOfAllLetters.remove(letter)

    return listOfAllLetters


