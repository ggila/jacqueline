
class Ride(object):

    def __init__(self, a, b, x, y, s, f):
        self.start_position = (a, b)
        self.dest_position = (x, y)
        self.earlier_start = s
        self.latest_finish = f
