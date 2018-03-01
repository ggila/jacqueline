from utils import read_subject, write_result

for f in ["subject/a_example.in"]:
#, "subject/b_should_be_easy.in", "subject/c_no_hurry.in", "subject/d_metropolis.in", "subject/e_high_bonus.in"]:
    STEP_COUNT, BONUS, rides, cars = read_subject(f)
    step = 0
    print STEP_COUNT
    while step < STEP_COUNT:
        for car in cars:
            car.update()
            if car.isAvailable():
                car.findRide(rides, step, STEP_COUNT)
        step += 1
    print "writing"
    
    write_result(f, cars)
