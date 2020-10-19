# Sequences
- Definition - data type that can store more than one value
    - Lists, tuples, ranges

- Accessing data inside a sequence with **indeces** and **loops**
    - Ex: myList[3] will grab the fourth item in the list
    - Negative indeces are valid and start from the end of the list
    - Slicing myList[1,3] will grab 2nd and 3rd items.
        - myList[1:]
        - myList[:3]
    - Looping 
        - while
        - for 
            - for x in myList:
                do something to x

- Replacing items in a list
    - myList[1] = "new data"
- Deleting items from a list
    - **del** keyword 
    - **del** myList[3]

- Combining Lists
    - Concatenation = myList = [1,2,3] + [4,5]
    - Extend = myList.extend([6,7])
        - myCats = ['Pandora', 'Ariel']
        - myList.extend(myCats)


# Strings
- You can access items in a string with indeces just like in lists
- myString = "abcdedf"
- myString[3] returns "d"
- Convert strings to lists with **list** keyword
    - myStringList = list(myString)
    - 


# Nuggets 
- Lists are mutable items
- access the index of a list in a for-in loop by using enumerate().
    - for number, things in enumerate(thingsList):
        print(f'{number}: {things}')


