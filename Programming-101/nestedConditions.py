pet_name = input('What is your pet\'s name?\n')

if len(pet_name) <= 3:
    print('That name is too short.')
elif len(pet_name) > 3:
    if pet_name == 'Shadow':
        print('El Gato Diablo!')
    elif pet_name == 'Daisy':
        print('Good dog!')
    else:
        print(f'Awwww! Sweet {pet_name}!')
