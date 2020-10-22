class Vehicle:
    def __init__(a, b, c=4):
        a.category = b
        a.wheels = c


myMoto = Vehicle('Motorcycle', 2)
myCar = Vehicle('BMW')
myTank = Vehicle('Sherman', 42)
myTruck = Vehicle('Peterbilt', 18)
myPogo = Vehicle('JomJom', 0)


print(myMoto.category)
print(myMoto.wheels)

print(myCar.category)
print(myCar.wheels)

print(myTank.category)
print(myTank.wheels)

print(myTruck.category)
print(myTruck.wheels)

print(myPogo.category)
print(myPogo.wheels)