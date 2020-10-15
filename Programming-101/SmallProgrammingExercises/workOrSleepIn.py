day = int(input('Give me a number between 0 and 6.\n'))
dayArray = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if day == 0:
    print('Get ready for church')
elif day > 0 and day < 6: 
    print('Get ready for the grind!')
else: 
    print('Sleep in, bra.')