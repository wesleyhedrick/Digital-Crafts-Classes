#Print a Square II
square_size = input('How big a square should I print?\n')
square_size = int(square_size)
starList = []

for i in range(square_size):
    starList.append('*')

square_width = ' '.join(starList)

for x in range(square_size):
    print(square_width)


better_square = input('How big a square should I print?\n')
better_square = int(better_square)

height = better_square
width = better_square

for x in range(height):
    print(" * " * width)


