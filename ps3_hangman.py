# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    print(len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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

    return "".join(listOfAllLetters)

def welcomeMessage(secretWord):

    secretLength = str(len(secretWord))
    welcomeMessage = "Welcome to the game, Hangman!\nI am thinking of a word that is "+ secretLength+" letters long.\n-------------"
    return welcomeMessage

def getLetter():

    """Gets a letter from the player as input"""

    letter = input("Please guess a letter:")
    letter = letter.lower()
    return letter

def showNumberOfGuesses(mistakesMade):

    numberOfGuesses = 8 - mistakesMade
    return numberOfGuesses

def hangman(secretWord, mistakesMade):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    numberOfGuesses = showNumberOfGuesses(mistakesMade)

    if numberOfGuesses > 0:

        #print number of guesses:
        print("You have "+str(numberOfGuesses) +" guesses left.")
        #print available letters:
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        #get a guess from the user:
        currentLetter = getLetter()
        showGuessed = getGuessedWord(secretWord, lettersGuessed)

        #check if letter is in lettersGuessed, if it is alert the user, show the guessed letters and the rest of the word and return:
        if currentLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + showGuessed)
        else:
            #Append good guess to list, show whether it's in the word, or update the mistakes:
            lettersGuessed.append(currentLetter)
            if currentLetter in secretWord:
                showGuessed = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: "+showGuessed)
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print("------------")
                    print("Congratulations, you won!")
                    playTime = False
                    return (playTime, mistakesMade)
            else:
                print("Oops! That letter is not in my word: "+showGuessed)
                print("------------")
                mistakesMade += 1
                playTime = True
                return (playTime, mistakesMade)

        print("------------")
        playTime = True
        return (playTime, mistakesMade)


    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        playTime = False
        return (playTime, mistakesMade)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
printOut = print(welcomeMessage(secretWord))

lettersGuessed = []
mistakesMade = 0
availableLetters = []
playTime = True

while playTime == True:
    (playTime, mistakesMade) = hangman(secretWord, mistakesMade)
