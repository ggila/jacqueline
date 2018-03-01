
from reader import readSubject

STEP_COUNT, rides, cars = readSubject()

step = 0
while step < STEP_COUNT:
    for car in cars:
        if car.isAvailable(step):
            car.findRide(rides)
