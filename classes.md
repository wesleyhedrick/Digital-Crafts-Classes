# Classes

## Creating a Class
class Person:
    pass

## Instantiating a Class
clint = Person()

## the __init__ function
- you must have an __init__ in your class, it runs everytime the class is instantiated.
- class Cat:
    def __init__:
        print('I am a new cat.')
**__init__ and __str__ are two examples of auto functions**


## You can add all sorts of things to a class
- class Mob:
    def__init__(self, name, size, color, health = 10, ):
        self.name = name
        self.size = size 
        self.color = color

## Class methods can return values outside the class
## A method is really just a function that lives inside a class

## Class Inheritance
- class Mob: 
    pass

- class Hero(Mob):
    pass


- this is kind of like saying Hero = Mob BUT not exactly
- it doesn't equal it but it copies all its functionality

## Super
- call a function from my parent even though I overwrote it


# Walking through a class

- below is a small piece of code with a class, the creation of an instance of the class, a use of the instance, and the creation of another instance of the class.

class Pet:
    def __init__(self, name, fullness=50, happiness=50):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = 5
        self.mopiness = 5

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

ariel = Pet('Ariel')
ariel.eat_food()

pandora = Pet('Pandora')
ariel.get_love()
pandora.be_alive()



1. Creating a class
- all classes must have an __init__ function.
    - the double underscores on either side of init are special in a python class. When python sees these this construction __init__ it knows to run the function automatically every time a new instance of the class is created.
    - this is important because __init__ does not run on instances only on instantiation. 


