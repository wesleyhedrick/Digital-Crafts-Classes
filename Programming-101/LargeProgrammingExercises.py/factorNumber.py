dividend = int(input('Give me a number, and I\'ll give you all it\'s factors.\n'))
divisor = 1
halfwaypoint = dividend / 2 + 1

while divisor < halfwaypoint:
    if dividend % divisor == 0: 
        print(divisor)
    divisor += 1



