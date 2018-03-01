from reader import readSubject

for f in ["subject/a_example.in", "subject/b_should_be_easy.in", "subject/c_no_hurry.in", "subject/d_metropolis.in", "subject/e_high_bonus.in"]:
    STEP_COUNT, BONUS, rides, cars = readSubject(f)
    step = 0
    while step < STEP_COUNT:
        for car in cars:
            car.update()
            if car.isAvailable(step):
                car.findRide(rides)
