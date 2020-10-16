import random

secret_number = random.randint(1,10)

print('I am thinking of a number between 1 and 10.')
the_game_must_go_on = True

while the_game_must_go_on:
    user_guess = int(input('What\'s the number?\n'))   
    if user_guess == secret_number:
        print(f'We have a psychic in the house! It\'s {secret_number}!')
        the_game_must_go_on = False
    elif user_guess > secret_number: 
        print('You\'re out over your skis a bit. Try again.')
    else:
        print('Think bigger...')


    





