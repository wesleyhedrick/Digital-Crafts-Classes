height = input('How tall is the triangle?\n')
height = int(height)
stars = 1
counter = height - 1 
space = ' '*counter

while height > 0:
    print(space, '*'*stars)
    counter -= 1
    space = ' '*counter
    height -= 1
    stars +=2


# counter = 3
# space = ' '*counter
# print(space, '*')

# counter = 2
# space = ' '*counter
# print(space, '*')

# counter = 1
# space = ' '*counter
# print(space, '*')

# counter = 3
# space = ' '*counter
# print(space, '*')