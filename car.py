from distance import getDistance

class Car(object):

    def __init__(self):
        self.position = (0, 0)
        self.historic = []
        self.notAvailableFor = -1

    def available(self, step):
        return step >= self.notAvailableFor
    
    def findRide(self, rides, step, STEP_COUNT):
        for r in rides:
            if not r.available:
                continue
            timetodo = r.isDoable(self, step, STEP_COUNT)
            if timetodo != -1:
                self.assign(r, timetodo)
                return

    def assign(self, r, timetodo):
        self.notAvailableFor = timetodo
        self.historic.append(r.number)
        self.position = r.dest_position
        r.available = False

    
