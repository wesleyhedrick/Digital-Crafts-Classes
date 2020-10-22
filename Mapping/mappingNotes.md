#Mapping

## Dictionaries
- key, value pairs
- keys separated from values by ":"
- key/value pairs separated from other key/value pairs by ","


## Writing and Retrieving Data
- Three ways to retrieve data from a dictionary
    - dictionary[keyname] - retrieves value for the key
    - dictionary.get(keyname) - retrieves value for the key
    - dictionary.values() - returns all values of a dict

- in operator 
- not in operator

- Update Dictionary
    - dictionary[keyname] = value
    **if the key exists, the above will update. If not, it will create new key/value pair**

- Iterating over a Dictionary
for key, value in dictionary.items():
    print(f'{key}{value}')

- Delete with del keyword

## Saving to a File

with open() as file:
    file.read()


## Pickle
- a python module that encodes python variables to be stored in a file
- It can also decode the info for use in a file
- Two main pickle methods
    - .dump()
        - with open('file.txt', 'wb') as f:
            pickle.dump()
    - .load()
        - with open('file.txt', 'rb') as f:
            pickle.load()

## JSON
- Javascript Object Notation 
- json module can be used to serialize and deserialize data just like pickle
  - **main difference** is that you don't open file in binary

