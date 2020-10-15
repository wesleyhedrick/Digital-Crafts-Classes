#Prompt user for his name
name = input('What is your name?\n')

print(f'Hello {name}')

#Print name in all caps

name = input('What is your name?').upper()
length = len(name)

print(f'Hello {name}')
print((f'Your name has {length} letters in it.').upper())


#Madlib
print('Let\'s do a madlib.')
noun1 = input('Give me a noun.\n')
name = input('Give me a funny name.\n')
noun2 = input('Give me another noun.\n')
verb = input('Give me an exciting verb.\n')
nounplural = input('Give me a noun in the plural.\n')
time = input('Give me a length of time like \'four days\' or \'two minutes\' or \'3 years.\'\n')

content = f'''There once was {noun1} named {name}. 
He lived on top of a {noun2} 
and {verb} {nounplural} {time}.'''

print(content)

#Day of the Week
day = int(input('Give me a number between 0 and 6.\n'))

dayArray = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print('You must be thinking of ' + dayArray[day])

#Work or Sleep In?
day = int(input('Give me a number between 0 and 6.\n'))
dayArray = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if day == 0:
    print('Get ready for church')
elif day > 0 and day < 6: 
    print('Get ready for the grind!')
else: 
    print('Sleep in, bra.')

#Celsius to Fahrenheit
cels = int(input('What celsius temp do you want to convert?'))

fahr = cels*(9/5) + 32

print(f'{cels} degrees Celsius equals {fahr} degrees Fahrenheit.')

# Looping from 1 to 10

counter = 1

while counter < 11:
    print(counter)
    counter += 1

# n to m
start_num = int(input('Give me a starting number.'))
finish_num = int(input('Give me an ending number.'))

beginner = start_num
terminator = finish_num+1

while beginner < terminator:
    print(beginner)
    beginner += 1

#Print a square

for x in range(5):
    print('*****')

#Print a Square II
square_size = input('How big a square shall I print?')
starArray = []

for i in range(square_size):
    starArray.append('*')

square_width = ''.join(starArray)


for x in range(square_size):
    print(squarewidth)


