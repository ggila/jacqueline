

class Car(dict):

    def __init__(self):
        self.available = True
        self.position = (0, 0)

    def isAvailable(self):
        if not self.notAvailableFor:
            self.available = True
        return self.availbale

    def update(self):
        if self.isAvailable() == False:
            self.notAvailableFor -= 1
    
    def findRide(self, rides, step):
        for r in rides:
            if r.isDoable(self.position, step):
                self.assign(r)
                
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    
