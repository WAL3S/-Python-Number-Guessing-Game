import random

#a simple number guessing game program where the computer has a number in mind and the user has to guess the number

join = input('welcome to the number guessing game, want to play? (Yes/No)\n')

if join.lower() == 'yes':
    
    random_int = random.randint(1, 10)
    stay_or_leave = 'yes'

    while stay_or_leave.lower() != 'no':
        
        guess = int(input('start guessing!\n'))

        if guess == random_int: 
            stay_or_leave = input(f'you guessed the right number, the number was {random_int}, would you like to play again? (Yes/No)\n')

            if stay_or_leave.lower() == 'yes':
                random_int = random.randint(1, 10)
                continue
            else :
                break

     


