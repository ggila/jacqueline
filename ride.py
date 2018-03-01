from distance import getDistance

class Ride(object):

    def __init__(self, a, b, x, y, s, f):
        self.start_position = (a, b)
        self.dest_position = (x, y)
        self.earlier_start = s
        self.latest_finish = f

    def isDoable(self, car, step):
        timeToGetCar = getDistance(self.start_position - self.dest_position)
        if step + timeToGetCar < earlier_start:
            return False
        timeToTrave = getDistance(self.start_position - self.dest_position)
        return 
