# Represents a Gem on the board
class Gem:
    def __init__(self, color, status, point):
        self.color = color
        self.status = status
        self.point = point
    
    def __repr__(self):
        return 'Gem(%s, %s, %s)' % (self.color, self.status, self.point)

# Represents the state of the game, including the board, score, and level
class GameState:
    def __init__(self, boardDim):
        self.gameOver = False
        self.boardDim = boardDim
        
        self.board = Board(boardDim)
        
        self.level = 0
        self.score = 0
        self.percentComplete = 0
    
    # Updates the board to reflect the given move and adds to the total score
    def makeMove(self, move):
        self.score += self.board.makeMove(move)
    
    # Returns the current level
    def getLevel(self):
        return self.level
    
    # Returns the total score
    def getScore(self):
        return self.score
    
    # Returns the percent complete as a decimal
    def getCompletion(self):
        return self.percentComplete

# Represents the game board as a list of lists containing Gem objects
class Board:
    def __init__(self, boardDim):
        self.board = [[None for x in range(self.boardDim.x)] for y in range(self.boardDim.y)]
            
    # Updates the board to reflect the given move, including removing gems
    # and making them 'fall' into empty spaces. New unknown gems are
    # represented by None
    def makeMove(self, move):
        self.swapGems(move)
        return self.removeMatches()
        
    # Updates the board to represent just the swapping of two Gems without
    # removing any matches
    def swapGems(self, move):
        pt1, pt2 = move.pointTuple()
        
        temp = self.board[pt1.y][pt1.x]
        self.board[pt1.y][pt1.x] = self.board[pt2.y][pt2.x]
        self.board[pt2.y][pt2.x] = temp
    
    # Removes any matches, placing special Gems in case of L, T, or 4- or
    # 5-in-a-row
    # Returns the number of points gained
    def removeMatches(self):
        pass

# Represents a 2D point
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

# Represents an RGB value as a 3D vector
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

# Represents a move the player can make
class Move:
    def __init__(self, point1, point2, score):
        self.point1 = point1
        self.point2 = point2
        self.score = score

    def pointTuple(self):
        return (self.point1, self.point2)
    
    def __repr__(self):
        return 'Move(%s, %s, %i)' % (self.point1, self.point2, self.score)
