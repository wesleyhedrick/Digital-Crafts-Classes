# n to m
start_num = int(input('Give me a starting number.'))
finish_num = int(input('Give me an ending number.'))

beginner = start_num
terminator = finish_num+1

while beginner < terminator:
    print(beginner)
    beginner += 1