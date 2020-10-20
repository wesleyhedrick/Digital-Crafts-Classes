# Carbs, Fats, Proteins

# myShoppingList = [['Ramen', 'All-Bran'],['Peanut Butter', 'Avocado'],['Chicken', 'Steak']]

myShoppingList = [
    ['Carbs', ['Ramen', 'All-Bran']], 
    ['Fat',['Peanut Butter', 'Avocado']], 
    ['Protein',['Chicken', 'Steak']]
]

print(myShoppingList[0][1][0])

for enum, item in enumerate(myShoppingList):
    print(f'{enum+1}. {item[0]}')
    for fdnum, food in enumerate(item[1]):
        print(f'   {fdnum+1}. {food}')
    
