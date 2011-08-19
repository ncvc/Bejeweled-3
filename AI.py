from gameState import Move

class AI:
    
    #board1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]
    #boardNotWideEnough = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
    #boardNotTallEnough = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

    #takes a board and returns a tuple of two points that should be switched
    def determineMove(self, board):
        self.height = len(board)
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
        directionFactor = throwAwayGem.Point.x - movingGem.point.x
        x = throwAwayGem.point.x
        y = throwAwayGem.point.y
        if self.gemAtCoords(x + 2*(directionFactor), y) and \
        movingGem.color == \
        self.gemAtCoords(x + 1*(directionFactor), y).color == \
        self.gemAtCoords(x + 2*(directionFactor), y).color:
            self.moves.append(Move(throwAwayGem.point, movingGem.point, 5))
        

    def gemAtCoords(self, x, y):
        if x < self.width and x > 0 and y < self.height and y > self.height:
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
            
        
    def __init__(self):
        self.moves = []
