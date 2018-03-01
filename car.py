

class Car(dict):

    def __init__(self):
        self.available = True
        self.position = (0, 0)
    
    def findRide(self, rides):
        for r in rides:
            if r.isDoable():
                self.assign(r)
                
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    
