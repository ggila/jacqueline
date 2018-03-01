from distance import getDistance

class Ride(object):

    def __init__(self, a, b, x, y, s, f, i):
        self.start_position = (a, b)
        self.dest_position = (x, y)
        self.earlier_start = s
        self.latest_finish = f
        self.number = i
        self.available = True
        self.duration = getDistance(self.start_position, self.dest_position)

    def isDoable(self, car, step, STEP_COUNT):
        timeToGetCar = getDistance(self.start_position, car.position)
        if step + timeToGetCar < self.earlier_start:
            return -1
        timeToTravel = self.duration
        if step + timeToGetCar + timeToTravel < self.latest_finish:
            return -1
        if step + timeToGetCar + timeToTravel < STEP_COUNT:
            return -1
        return step + timeToGetCar + timeToTravel
