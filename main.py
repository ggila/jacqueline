
step = 0
while step < STEP_COUNT:
    for car in cars:
        car.update()
        if car.isAvailable():
            car.findRide(rides, step)
