number = int(input('What number are you thinking of?\n'))

secretNumber = 10

if number > secretNumber:
    print('Oooh! That\'s too high.')

elif number < secretNumber:
    print('Too low')

else:
    print('That\'s what I was thinking of! You are a mensch!')
