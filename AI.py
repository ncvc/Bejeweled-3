from gameState import Move, Point
import copy, time

class AI:
    
    #board1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]
    #boardNotWideEnough = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
    #boardNotTallEnough = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

    # Constructor - takes the board dimesion as a Point and the number of moves to look ahead when calculating the best move
    def __init__(self, boardDim, depth):
        self.moves = self.getAllPossibleMoves(boardDim)
        self.depth = depth
        
    # Returns a list of all possible moves given a point representing the dimesions of the board
    def getAllPossibleMoves(self, boardDim):
        dirs = (Point(1,0), Point(0,1))
        moves = []
        for x in range(boardDim.x):
            for y in range(boardDim.y):
                p1 = Point(x, y)
                for direction in dirs:
                    moves.append(Move(p1, p1 + direction, 0))
        
        return moves
        
    # Takes a board and returns a Move
    def determineMove(self, board):
        startTime = time.time()
        points, move, totalMatches, matches = self.getBestMove(board, 0, 1)
        totalTime = time.time() - startTime
        move.score = points
        
        print 'Best move calculated in %fs! %i projected points earned in the next %i turns with %i matches' % (totalTime, points, self.depth, totalMatches)
        print board
        return move
        
    def getBestMove(self, board, totalPoints, moveNum):
        bestMove = None
        maxPoints = -1
        totalMatches = 0
        matches = []
        print 'moveNum:', moveNum
        
        for move in self.moves:
            if board.moveMakesMatch(move):
                # Don't want to affect the actual board while simulating moves
                newBoard = copy.deepcopy(board)
                
                points, numMatches, matchList = newBoard.makeMove(move)
                
                if points > 0 and moveNum < self.depth:
                    points, nextMove, dummyNumMatches, dummyMatches = self.getBestMove(newBoard, totalPoints + points, moveNum + 1)
                
                if maxPoints < totalPoints + points:
                    bestMove = move
                    maxPoints = totalPoints + points
                    totalMatches = numMatches
                    matches = matchList
                    
        return maxPoints, bestMove, totalMatches, matches
                
        
    '''
        if self.height < 4:
            print "invalid board"
            return
        self.width = len(board[0])
        if self.width < 4:
            print "invalid board"
            return
        self.moves = []   
        for i in range(self.height):
            for j in range(self.width - 3):
                gem1 = board[self.height-1-i][j]
                gem2 = board[self.height-1-i][j+1]
                gem3 = board[self.height-1-i][j+2]
                gem4 = board[self.height-1-i][j+3]
                
                #XXoX, X's are same color, o's are any other color
                if self.colorsMatch(gem1, gem2, gem4):
                    self.moves.append(Move(gem3.point, gem4.point, 3))
                    
                #XoXX
                if self.colorsMatch(gem1, gem3, gem4):
                    self.moves.append(Move(gem1.point, gem2.point, 3))
                    
                
        for i in range (self.width):
            for j in range(self.height - 3):
                gem1 = board[self.height-j-1][i]
                gem2 = board[self.height-j-2][i]
                gem3 = board[self.height-j-3][i]
                gem4 = board[self.height-j-4][i]

                #X 1
                #X 2
                #o 3
                #X 4
                if self.colorsMatch(gem1, gem2, gem4):
                    self.moves.append(Move(gem3.point, gem4.point, 3))

                #X
                #o
                #X
                #X
                if self.colorsMatch(gem1, gem3, gem4):
                    self.moves.append(Move(gem1.point, gem2.point, 3))
                
        for i in range(self.height-1):
            for j in range(self.width - 2):
                gem1 = board[self.height-1-i][j]
                gem2 = board[self.height-1-i][j+1]
                gem3 = board[self.height-1-i][j+2]
                gem4 = board[self.height-2-i][j]
                gem5 = board[self.height-2-i][j+1]
                gem6 = board[self.height-2-i][j+2]
                
                #ooX 4,5,6
                #XXo 1,2,3
                if self.colorsMatch(gem1, gem2, gem6):
                    self.moves.append(Move(gem3.point, gem6.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem3, gem6)

                #XXo 4,5,6
                #ooX 1,2,3
                if self.colorsMatch(gem3, gem4, gem5):
                    self.moves.append(Move(gem3.point, gem6.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem6, gem3)

                #XoX 4,5,6
                #oXo 1,2,3
                if self.colorsMatch(gem2, gem4, gem6):
                    self.moves.append(Move(gem2.point, gem5.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem5, gem2)

                #oXo 4,5,6
                #XoX 1,2,3
                if self.colorsMatch(gem1, gem3, gem5):
                    self.moves.append(Move(gem2.point, gem5.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem2, gem5)

                #Xoo 4,5,6
                #oXX 1,2,3
                if self.colorsMatch(gem2, gem3, gem4):
                    self.moves.append(Move(gem1.point, gem4.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem1, gem4)

                #oXX 4,5,6
                #Xoo 1,2,3
                if self.colorsMatch(gem1, gem5, gem6):
                    self.moves.append(Move(gem1.point, gem4.point, 3))
                    self.checkSixGemHorizontalFivePointMove(gem4, gem1)
                
        for i in range (self.width-1):
            for j in range(self.height - 2):
                gem1 = board[self.height-j-1][i]
                gem2 = board[self.height-j-2][i]
                gem3 = board[self.height-j-3][i]
                gem4 = board[self.height-j-1][i+1]
                gem5 = board[self.height-j-2][i+1]
                gem6 = board[self.height-j-3][i+1]

                #Xo 6,3
                #oX 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem2, gem6):
                    self.moves.append(Move(gem3.point, gem6.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem3, gem6)

                #oX 6,3
                #Xo 5,2
                #Xo 4,1
                if self.colorsMatch(gem3, gem4, gem5):
                    self.moves.append(Move(gem3.point, gem6.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem6, gem3)
                
                #Xo 6,3
                #oX 5,2
                #Xo 4,1
                if self.colorsMatch(gem2, gem4, gem6):
                    self.moves.append(Move(gem2.point, gem5.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem5, gem2)
                
                #oX 6,3
                #Xo 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem3, gem5):
                    self.moves.append(Move(gem2.point, gem5.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem2, gem5)
                
                #oX 6,3
                #oX 5,2
                #Xo 4,1
                if self.colorsMatch(gem2, gem3, gem4):
                    self.moves.append(Move(gem1.point, gem4.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem1, gem4)
                
                #Xo 6,3
                #Xo 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem5, gem6):
                    self.moves.append(Move(gem1.point, gem4.point, 3))
                    self.checkSixGemVerticalFivePointMove(gem4, gem1)
                    
        return self.bestMove()


        
                
    def colorsMatch(self, gem1, gem2, gem3):
        return gem1.color == gem2.color == gem3.color


    def checkSixGemHorizontalFivePointMove(self, throwAwayGem, movingGem):
        directionFactor = throwAwayGem.point.y - movingGem.point.y
        x = throwAwayGem.point.x
        y = throwAwayGem.point.y
        if self.gemAtCoords(x,y + 2*(directionFactor)) and \
        throwAwayGem.color == \
        self.gemAtCoords(x, y + 1*(directionFactor)).color == \
        self.gemAtCoords(x, y + 2*(directionFactor)).color:
            self.moves.append(Move(throwAwayGem.point, movingGem.point, 5))

    def checkSixGemVerticalFivePointMove(self, throwAwayGem, movingGem):
        directionFactor = throwAwayGem.point.x - movingGem.point.x
        x = throwAwayGem.point.x
        y = throwAwayGem.point.y
        if self.gemAtCoords(x + 2*(directionFactor), y) and \
        movingGem.color == \
        self.gemAtCoords(x + 1*(directionFactor), y).color == \
        self.gemAtCoords(x + 2*(directionFactor), y).color:
            self.moves.append(Move(throwAwayGem.point, movingGem.point, 5))
        

    def gemAtCoords(self, x, y):
        if x < self.width and x > 0 and y < self.height and y > 0:
            return self.board[y][x]
        else:
            return False

    def bestMove(self):
        move = None
        maxScore = 0
        for item in self.moves:
            if item.score > maxScore or move == None:
                move = item
                maxScore = item.score
        return move
        '''
            
        
