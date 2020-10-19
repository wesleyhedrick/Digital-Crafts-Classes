thingsAroundMe = ['monitor', 'fire', 'Ariel', 'Yeti', 'iPhone']
inputPrompt = f'Here\'s a list of my favorite things: {favoriteThingsString}'
print(inputPrompt)

user_choice = int(input('Which item is your favorite? (Choose a number)'))
print(f'You chose {thingsAroundMe[user_choice]}! Good choice!')
    