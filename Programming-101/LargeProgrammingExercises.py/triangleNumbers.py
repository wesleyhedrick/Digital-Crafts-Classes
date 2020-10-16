counter = 1 #1 #2 #3 #4
triangle_number = 1 #3 #6 #10 #15
incrementer = 2 #3 #4 #5 #6
print(f'Triangle number 1: {triangle_number}')

while counter < 5:
    triangle_number += incrementer
    print(f'Triangle Number {counter + 1}: {triangle_number}')
    incrementer += 1
    counter += 1