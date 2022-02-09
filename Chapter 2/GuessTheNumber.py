# Continued Python Files for Games at Chapter 2
# Guess The Number

import random

randomNumber = random.randint(1, 20)

print("I am thinking of a number between 1 and 20: ", randomNumber)

numGuesses = 1
userGuess = 0

while userGuess != randomNumber:
    userGuess = int(input("Take a guess: "))
    print(userGuess)

    if userGuess < randomNumber:
        print("Your guess is low.")
    elif userGuess > randomNumber:
        print("Your guess is too high")

    elif userGuess == randomNumber:
        print("Good job! You guessed my number in ", numGuesses, "guesses!")
        break

    numGuesses = numGuesses + 1

