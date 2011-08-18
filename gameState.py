class Gem:
    def __init__(self, color, status):
        self.color = color
        self.status = status

class Board:
    def __init__(self):
        self.board = []

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def toTuple(self):
        return (self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return 'Point(%i, %i)' % (self.x, self.y)