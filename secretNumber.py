import math

print("PLease think of a number between 0 and 100")

low = 0
high = 100

computerGuess = math.floor((high + low) / 2.0)

endGame = False

while not endGame:

    print(f"Is your guess {computerGuess}?")

    userAnswer = input("Enter 'h' if this is too high. Enter 'l' if this is too low, and enter 'c' to show it is correct:")

    if userAnswer == "h":
        high = computerGuess
        computerGuess = math.floor((high + low) / 2.0)


    elif userAnswer == "l":
        low = computerGuess
        computerGuess = math.floor((high + low) / 2.0)


    elif userAnswer == "c":
        print(f"Game over. Your guess was {computerGuess}.")
        endGame = True

    else:
        print("I don't understand your input. Try again.")








