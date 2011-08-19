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
    
    # Multiplication by a constant
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    
    # Division by a constant
    def __div__(self, other):
        return Point(self.x / other, self.y / other)
    
    def __repr__(self):
        return 'Point(%i, %i)' % (self.x, self.y)
        
class RGB:
    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b
        
    def toTuple(self):
        return (self.r, self.g, self.b)
    
    def __add__(self, other):
        return RGB(self.r + other.r, self.g + other.g, self.b + other.b)
    
    def __sub__(self, other):
        return RGB(self.r - other.r, self.g - other.g, self.b - other.b)
    
    # Multiplication by a constant
    def __mul__(self, other):
        return RGB(self.r * other, self.g * other, self.b * other)
    
    # Division by a constant
    def __div__(self, other):
        return RGB(self.r / other, self.g / other, self.b / other)
    
    def __repr__(self):
        return 'RGB(%i, %i, %i)' % (self.r, self.g, self.b)

    def distSquared(self, other):
        return (self.r-other.r)**2+(self.g-other.g)**2+(self.b-other.b)**2

class Move:
    def __init__(self, point1, point2, score):
        self.point1 = point1
        self.point2 = point2
        self.score = score
    def pointTuple(self):
        return (self.point1, self.point2)
