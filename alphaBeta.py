x = 276566
epsilon = 0.01
numberOfGuesses = 0

low = 1.0
high = x

answer = (high + low)/2.0

while abs(answer ** 3 - x) >= epsilon:

    print('low = ' + str(low) + ' high = '+ str(high) + ' answer = ' + str(answer))
    numberOfGuesses += 1

    if answer ** 3 < x:
        low = answer
    else:
        high = answer
    answer = (high + low)/2.0

print(f'The number of guesses was {numberOfGuesses} and the square root of {x} is close to {answer}')
