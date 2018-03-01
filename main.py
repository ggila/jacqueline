from reader import readSubject

subject = "input/a_example.in"

STEP_COUNT, BONUS, rides, cars = readSubject(subject)

step = 0
while step < STEP_COUNT:
    for car in cars:
        if car.isAvailable(step):
            car.findRide(rides)
