from os import path
from car import Car
from ride import Ride


def read_subject(subject):
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
                cars = [Car()]*int(constants[2])
            else:
                integers = [int(elt) for elt in line.split()]
                integers.append(i-1)
                ride = Ride(*integers)
                rides.append(ride)
    return STEP_COUNT, BONUS, rides, cars

def write_result(subject, cars):
    result = path.basename(subject)
    result = path.splitext(result)[0]+".out"
    result = path.join("results", result)
    all_lines = []
    for car in cars:
        line = [len(car.historic)] + car.historic
        line = map(str, line)
        all_lines.append(" ".join(line))
    with open(result, "w") as f:
        f.write("\n".join(all_lines))
        f.write("\n")
