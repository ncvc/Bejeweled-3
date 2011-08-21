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
        self.boardDim = boardDim
        self.board = [[None for x in range(self.boardDim.x)] for y in range(self.boardDim.y)]
        self.matchTypes = {'5 consecutive': self.getMatch5,
                           'L or T': self.getMatchLT,
                           '4 consecutive': self.getMatch4,
                           '3 consecutive': self.getMatch3}
            
    # Updates the board to reflect the given move, including removing gems
    # and making them 'fall' into empty spaces. New unknown gems are
    # represented by None.
    # Returns the number of points gained
    def makeMove(self, move):
        self.swapGems(move)
        return self.removeMatches()
        
    # Updates the board to represent just the swapping of two Gems without
    # removing any matches
    def swapGems(self, move):
        pt1, pt2 = move.pointTuple()
        
        if self.isOnBoard(pt1) and self.isOnBoard(pt2):
            temp = self.board[pt1.y][pt1.x]
            self.board[pt1.y][pt1.x] = self.board[pt2.y][pt2.x]
            self.board[pt2.y][pt2.x] = temp
    
    # Removes any matches, placing special Gems in case of L, T, or 4- or
    # 5-in-a-row
    # Returns the number of points gained
    def removeMatches(self):
        for matchName, matchFunc in self.matchTypes:
            print 'Searching for matches of type: %s' % matchName
            
            for x in range(self.boardDim.x):
                for y in range(self.boardDim.y):
                    gem = self.board[y][x]
                    
                    if gem != None:
                        match = matchFunc(gem)
                        
                        # Remove all Gems that 
                        for gem in match.matchedGems:
                            self.board[gem.point.y][gem.point.x] = None
                        
                        pt = match.replaceGem.point
                        if pt != None:
                            self.board[pt.y][pt.x] = match.replaceGem
    
    # Finds matches containing point - only search down and to the right
    # Returns a Match object representing the match found, or None if no match
    # was found
    def findMatches(self, point):
        right = Point(1, 0)
        down = Point(0, 1)
        
        self.findMatchesHelper(point, right, 1, False)
        self.findMatchesHelper(point, down, 1, False)
    
    def findMatchesHelper(self, point, direction, numInARow, isPerp):
        newPt = point + direction
        if self.isOnBoard(newPt):
            color = self.board[point.y][point.x].color
    
    def getMatch5(self, gem):
        return self.getMatchX(gem, 5)
    
    def getMatchLT(self, gem):
        dirs = (Point(1,0),Point(0,1))
        for direction in dirs:
            matchedGems = self.getMatchedConsec(gem, 3, direction)
            
    
    def getMatch4(self, gem):
        return self.getMatchX(gem, 4)
    
    def getMatch3(self, gem):
        return self.getMatchX(gem, 3)
    
    # Returns a Match if gem is the topleft-most gem in a sequence of x
    # same-colored gems, or None otherwise
    def getMatchX(self, gem, x):
        dirs = (Point(1,0), Point(0,1))
        for direction in dirs:
            matchedGems = self.getMatchedGemsXDir(gem, x, direction)
            if matchedGems != None:
                return Match(matchedGems, gem)
        return None
    
    # Returns a list of gems if gem is the first in a sequence of x same-colored
    # gems in direction
    def getMatchedGemsXDir(self, gem, x, direction):
        matchedGems = []
        for i in range(1, x):
            newPt = direction * i + gem.point
            newGem = self.board[newPt.y][newPt.x]
            if newGem.color != gem.color:
                return None
            matchedGems.append(newGem)
        return matchedGems
    
    # Returns True if the given point is on the board and False otherwise
    def isOnBoard(self, point):
        return point.x >= 0 and point.y >= 0 and point.x < self.boardDim.x and point.y < self.boardDim.y

# Represents a Gem match
class Match:
    def __init__(self, matchedGems, replaceGem):
        self.matchedGems = matchedGems
        self.replaceGem = replaceGem
        
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
