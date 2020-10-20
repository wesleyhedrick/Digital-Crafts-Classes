# Functions

**encapsulation**

## Defining a Function
- def keyword
- name of function
- parameters
- executing section

## Importance of return in a function
- It is important to make your functions return *something* because it makes your program easier to debug
- You can have only *one* return in a function
    - but the single return can be a return of multiple values if it is in a list, tuple, or other multivalue item.
- python exits the function after the return statement
- if there is no return statement python implicitly returns None

## Parameters and Arguments
- In common parlance they are interchangeable. 
- Technically parameters refers to the items in the function's definition while
- arguments refers to the counterparts of parameters. Arguments are the items supplied by the user. 
- def add(a, b): return a + b. Parameters: a and b. Arguments: 2 and 3 when the user calls the function


## Scope
- Python does not normally allow functions to modify global variables