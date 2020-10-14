my_num = input('Give me a number')

try: 
    my_num = int(my_num)
    print(100/my_num)
except:
    print('something is wrong')