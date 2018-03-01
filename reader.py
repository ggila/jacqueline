from car import Car
from ride import Ride

def readSubject(subject):
    rides = []
    cars = []
    STEP_COUNT = 0
    BONUS = 0
    with open(subject, "r") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                constants = line.split()
                STEP_COUNT = int(constants[5])
                BONUS = int(constants[4])
                cars = [Car]*int(constants[2])
            else:
                ride = Ride(*line.split())
                rides.append(ride)
    return STEP_COUNT, BONUS, rides, cars
