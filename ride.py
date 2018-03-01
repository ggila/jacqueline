from distance import getDistance

class Ride(object):

    def __init__(self, a, b, x, y, s, f):
        self.start_position = (a, b)
        self.dest_position = (x, y)
        self.earlier_start = s
        self.latest_finish = f

    def isDoable(self, car, step, STEP_COUNT):
        timeToGetCar = getDistance(self.start_position - car.position)
        if step + timeToGetCar < earlier_start:
            return False
        timeToTravel = getDistance(self.start_position - self.dest_position)
        if step + timeToGetCar + timeToTravel < latest_finish:
            return False
        if step + timeToGetCar + timeToTravel < STEP_COUNT:
            return False
        return True
