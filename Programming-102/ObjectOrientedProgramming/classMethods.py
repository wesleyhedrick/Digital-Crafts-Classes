class Vehicle:
    def __init__(self, category, top_speed, acceleration, wheels = 4):
        self.category = category
        self.wheels = wheels
        self.speed = 0
        self.top_speed = top_speed
        self.position = 0
        self.acceleration = acceleration


    def move(self):
        self.position += self.speed
    
    def accelerate(self):
        if self.speed <= self.top_speed:
            self.speed += self.acceleration
        self.move()
        



myMoto = Vehicle('Motorcycle', 200, 100 )
myCar = Vehicle('BMW', 150, 65)
myTank = Vehicle('Sherman', 45, 20)
myTruck = Vehicle('Peterbilt', 100, 20)
myPogo = Vehicle('JomJom', 3, 3)

raceTime = int(input('How long is the race?'))
race = 0


while race < raceTime:
    myMoto.accelerate()
    myCar.accelerate()
    myTank.accelerate()
    myTruck.accelerate()
    myPogo.accelerate()
    race += 1

print(f'{myMoto.category} - {myMoto.position}')
print(f'{myCar.category} - {myCar.position}')
print(f'{myTank.category} - {myTank.position}')
print(f'{myTruck.category} - {myTruck.position}')
print(f'{myPogo.category} - {myPogo.position}')




