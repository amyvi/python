# This is a basic python exercise - //GUESS THE NUMBER //
# Using simple if and else if statements
# There are no error handling included

import random

name = input('Hello, what is your name?')
print('Hi', name,  'we are going to play a guessing game! I am thinking of nunmber between 1-20')
randomNumber = random.randint(1, 20)

for guessNumberOfTimes in range(1, 7):
    guess = int(input('Take a guess'))

    if guess > randomNumber:
        print('Your guess is too high!')
    elif guess < randomNumber:
        print('Your guess is too low!')
    else:
        break


if guess == randomNumber:
    print('Yehey! You got it right, ', name,  'You guessed my number in' + str(guessNumberOfTimes) + 'guesses')
else:
    print('Nope. The correct number was ' + str(randomNumber))

