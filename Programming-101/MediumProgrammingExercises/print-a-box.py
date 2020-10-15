height = input('Height?\n')
width = input('Width?\n')

height = int(height)
width = int(width)

#print top row
print(' * ' * width)

#print walls
walls = ' * ' + '   ' * (width-2) + ' * '

for x in range(height-2):
    print(walls)
# print bottom row

print(' * ' * width)
