import random

print('\n\t\t***Guess The Random number Game***\n\t\t\t(1 to 100)')

# Generates the random number within the given range
guess = random.randint(1, 100)
chances = 9

# This While loop exits when all chances are finished
while chances:
    userGuess = int(input('Guess the number : '))
    if userGuess == guess:
        print('Wow GREAT! You have guessed the number...')
        break
    if userGuess > guess:
        print('The Number is Lesser than the Number you entered')
    elif userGuess < guess:
        print('The Number is Greater than the Number you entered')

    print(f'You have still {chances-1}')

    if chances == 1:
        print(f'The Number is {guess}')

    chances -= 1
