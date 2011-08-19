from gameState import Move

class AI:
    
    #board1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]
    #boardNotWideEnough = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
    #boardNotTallEnough = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

    #takes a board and returns a tuple of two points that should be switched
    def determineMove(self, board):
        height = len(board)
        if height < 4:
            print "invalid board"
            return
        width = len(board[0])
        if width < 4:
            print "invalid board"
            return
        moves = []   
        for i in range(height):
            for j in range(width - 3):
                gem1 = board[height-1-i][j]
                gem2 = board[height-1-i][j+1]
                gem3 = board[height-1-i][j+2]
                gem4 = board[height-1-i][j+3]
                
                #XXoX, X's are same color, o's are any other color
                if self.colorsMatch(gem1, gem2, gem4):
                    moves.append(Move(gem3.point, gem4.point, 3))
                    checkLRightThenUpOrDown(gem1, gem2, gem3, gem4)
                    
                #XoXX
                if self.colorsMatch(gem1, gem3, gem4):
                    moves.append(Move(gem1.point, gem2.point, 3))
                    
                
        for i in range (width):
            for j in range(height - 3):
                gem1 = board[height-j-1][i]
                gem2 = board[height-j-2][i]
                gem3 = board[height-j-3][i]
                gem4 = board[height-j-4][i]

                #X 1
                #X 2
                #o 3
                #X 4
                if self.colorsMatch(gem1, gem2, gem4):
                    moves.append(Move(gem3.point, gem4.point, 3))

                #X
                #o
                #X
                #X
                if self.colorsMatch(gem1, gem3, gem4):
                    moves.append(Move(gem1.point, gem2.point, 3))
                
        for i in range(height-1):
            for j in range(width - 2):
                gem1 = board[height-1-i][j]
                gem2 = board[height-1-i][j+1]
                gem3 = board[height-1-i][j+2]
                gem4 = board[height-2-i][j]
                gem5 = board[height-2-i][j+1]
                gem6 = board[height-2-i][j+2]
                
                #ooX 4,5,6
                #XXo 1,2,3
                if self.colorsMatch(gem1, gem2, gem6):
                    moves.append(Move(gem3.point, gem6.point, 3))
                    checkHorizontalSixL(gem3, gem6)

                #XXo 4,5,6
                #ooX 1,2,3
                if self.colorsMatch(gem3, gem4, gem5):
                    moves.append(Move(gem3.point, gem6.point, 3))
                    checkHorizontalSixL(gem3, gem6)

                #XoX 4,5,6
                #oXo 1,2,3
                if self.colorsMatch(gem2, gem4, gem6):
                    moves.append(Move(gem2.point, gem5.point, 3))
                    

                #oXo 4,5,6
                #XoX 1,2,3
                if self.colorsMatch(gem1, gem3, gem5):
                    moves.append(Move(gem2.point, gem5.point, 3))

                #Xoo 4,5,6
                #oXX 1,2,3
                if self.colorsMatch(gem2, gem3, gem4):
                    moves.append(Move(gem1.point, gem4.point, 3))
                    checkHorizontalSixL(gem1, gem4)

                #oXX 4,5,6
                #Xoo 1,2,3
                if self.colorsMatch(gem1, gem5, gem6):
                    moves.append(Move(gem1.point, gem4.point, 3))
                    checkHorizontalSixL(gem1, gem4)
                
        for i in range (width-1):
            for j in range(height - 2):
                gem1 = board[height-j-1][i]
                gem2 = board[height-j-2][i]
                gem3 = board[height-j-3][i]
                gem4 = board[height-j-1][i+1]
                gem5 = board[height-j-2][i+1]
                gem6 = board[height-j-3][i+1]

                #Xo 6,3
                #oX 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem2, gem6):
                    moves.append(Move(gem3.point, gem6.point, 3))

                #oX 6,3
                #Xo 5,2
                #Xo 4,1
                if self.colorsMatch(gem3, gem4, gem5):
                    moves.append(Move(gem3.point, gem6.point, 3))
                
                #Xo 6,3
                #oX 5,2
                #Xo 4,1
                if self.colorsMatch(gem2, gem4, gem6):
                    moves.append(Move(gem2.point, gem5.point, 3))
                
                #oX 6,3
                #Xo 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem3, gem5):
                    moves.append(Move(gem2.point, gem5.point, 3))
                
                #oX 6,3
                #oX 5,2
                #Xo 4,1
                if self.colorsMatch(gem2, gem3, gem4):
                    moves.append(Move(gem1.point, gem4.point, 3))
                
                #Xo 6,3
                #Xo 5,2
                #oX 4,1
                if self.colorsMatch(gem1, gem5, gem6):
                    moves.append(Move(gem1.point, gem4.point, 3))


        
                
    def colorsMatch(self, gem1, gem2, gem3):
        return gem1.color == gem2.color == gem3.color


    def checkHorizontalSixL(throwAwayGem, movingGem):
        directionFactor = throwAwayGem.point.y - movingGem.point.y
        x = throwAwayGem.point.x
        y = throwAwayGem.point.y
        if gemAtCoords(x,y + 2*(directionFactor)) and \
        throwAwayGem.color == \
        gemAtCoords(x, y + 1*(directionFactor)).color == \
        gemAtCoords(x, y + 2*(directionFactor)).color:
            moves.append(Move(throwAwayGem.point, movingGem.point, 5))

    def gemAtCoords(x, y):
        if x < width and x > 0 and y < height and y > height:
            return board[y][x]
        else:
            return false

    def bestMove():
        twoToSwap = None
        maxScore = 0
        for item in self.moves:
            if item.score > maxScore or twoSwap == None:
                twoToSwap = (item.point1, item.point2)
                maxScore = item.score
        return twoToSwap
            
        
    def __init__(self):
        self.moves = []
