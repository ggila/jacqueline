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

    def isDoable(self, rides, car, step, STEP_COUNT):
        timeToGetCar = getDistance(self.start_position, car.position)
        diffdatestart = self.earlier_start - step - timeToGetCar 
        if diffdatestart > 0:
            timeToGetCar += diffdatestart
        timeToTravel = self.duration
        if step > self.latest_finish or timeToTravel + step  > STEP_COUNT:
            rides.remove(self)
            return -1
        if step + timeToGetCar + timeToTravel > min(self.latest_finish, STEP_COUNT):
            return -1
        return step + timeToGetCar + timeToTravel
