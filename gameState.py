class Gem:
    def __init__(self, color, status, point):
        self.color = color
        self.status = status
        self.point = point
    
    def __repr__(self):
        return 'Gem(%s, %s, %s)' % (self.color, self.status, self.point)

class GameState:
    def __init__(self):
        self.gameOver = False
        self.board = []
        
        self.level = 0
        self.score = 0
        self.percentComplete = 0

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