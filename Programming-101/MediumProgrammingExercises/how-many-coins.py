coin_count = 0
print(f'You have {0} coins.')
coins = input('Do you want one? (y/n)\n')
carryonwithgame = True

while carryonwithgame: 
    if coins == 'y':
        coin_count += 1
        print(f'You now have {coin_count} coins.')
        coins = input('Do you want another?\n')
    else:
        carryonwithgame = False
        print('You don\t want anymore? Okay, bye')
