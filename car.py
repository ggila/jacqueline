

class Car(object):

    def __init__(self):
        self.available = True
        self.position = (0, 0)
        self.historic = []

    def isAvailable(self):
        return self.available

    def update(self):
        if self.available == False:
            self.notAvailableFor -= 1
        if self.notAvailableFor <= 0:
            self.available = True
    
    def findRide(self, rides, step, STEP_COUNT):
        for r in rides:
            if r.isDoable(self.position, step, STEP_COUNT):
                self.assign(r)

    def assign(r):
        self.available = False
        self.notAvailableFor = getDistance(r.start_position - r.dest_position)
        self.historic.append(r.number)

    
