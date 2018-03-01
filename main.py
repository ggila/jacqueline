from utils import read_subject, write_result

for f in ["subject/a_example.in", "subject/b_should_be_easy.in", "subject/c_no_hurry.in", "subject/d_metropolis.in", "subject/e_high_bonus.in"]:
    STEP_COUNT, BONUS, rides, cars = read_subject(f)
    step = 0
    print f, STEP_COUNT, len(cars), len(rides)
    while step < STEP_COUNT:
        if step % 100 == 0:
            print step
        for car in cars:
            if car.available(step):
                r = car.findRide(rides, step, STEP_COUNT)
                if r is not None:
                    rides.remove(r)
        step += 1
    write_result(f, cars)
