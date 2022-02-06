# Continued Python Files for Games at Chapter 2
# Boulder Parchment Shears (remake of  Rock, Paper, Scissors)

import random

print('Boulder, Parchment, Scissors')

variablePlays = {
    "b": "Boulder",
    "p": "Parchment",
    "s": "Scissors",
}

wins = 0
losses = 0
ties = 0

# main game loop...
while True:

    # Stands for rock paper scissors, created list for random.choice to run from
    BPS = ['b', 'p', 's']
    computerChoice = random.choice(BPS)
    # Could have used numerical values...

    # print(wins, ' Wins, ', losses, ' Losses,', ties, ', Ties')
    # improvement
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    playerChoice = input('Enter your move (b)oulder, (p)archment, (s)hears, or (q)uit: ', )

    if playerChoice == 'q':
        break

    elif playerChoice == 'b':
        print('\nYou chose boulder!')
        print('Boulder VERSUS...', end =" ")
    elif playerChoice == 'p':
        print('\nYou chose parchment!')
        print('Parchment VERSUS...', end =" ")
    elif playerChoice == 's':
        print('\nYou chose shears!')
        print('Shears VERSUS...', end =" ")

    if playerChoice == computerChoice:
        print('the computers choice:', variablePlays[computerChoice])
        print('\nIts a Tie!')
        ties = ties + 1

    # Conditions of winning

    elif playerChoice == 'p' and computerChoice == 'b':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Win!')
        wins = wins + 1
    elif playerChoice == 's' and computerChoice == 'p':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Win!')
        wins = wins + 1
    elif playerChoice == 'b' and computerChoice == 's':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Win!')
        wins = wins + 1

    # Transitions to losing conditions

    elif playerChoice == 'p' and computerChoice == 's':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Lose!')
        losses = losses + 1
    elif playerChoice == 's' and computerChoice == 'b':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Lose!')
        losses = losses + 1
    elif playerChoice == 'b' and computerChoice == 'p':
        print('the computers choice:', variablePlays[computerChoice])
        print('\nYou Lose!')
        losses = losses + 1

print('Your', wins, ' Wins, ', losses, ' Losses,', ties, ', Ties')
