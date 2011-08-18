class AI:
    
    #board1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]
    #boardNotWideEnough = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
    #boardNotTallEnough = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

    #takes a board and returns a tuple of two points that should be switched
    def determineMove(board):
        height = len(board)
        if height < 4:
            print "invalid board"
            return
        width = len(board[0])
        if width < 4:
            print "invalid board"
            return
        
        for i in range(height):
            for j in range(width - 3):
                gem1 = board[height-1-i][j]
                gem2 = board[height-1-i][j+1]
                gem3 = board[height-1-i][j+2]
                gem4 = board[height-1-i][j+3]
                
                #case XXoX
                if colorsMatch(gem1, gem2, gem4):
                    return (gem3.point, gem4.point)
                    
                #case XoXX
                if colorsMatch(gem1, gem3, gem4):
                    return (gem1.point, gem2.point)
                    
                
        for i in range (width):
            for j in range(height - 3):
                gem1 = board[height-j-1][i]
                gem2 = board[height-j-2][i]
                gem3 = board[height-j-3][i]
                gem4 = board[height-j-4][i]

                #case
                #X
                #X
                #o
                #X
                if gem1.color == gem2.color == gem4.color:
                    return (gem3.point, gem4.point)

                #case
                #X
                #o
                #X
                #X
                if gem1.color == gem3.color == gem4.color:
                    return (gem1.point, gem2.point)
            
    def colorsMatch(gem1, gem2, gem3):
        return gem1.color == gem2.color == gem3.color
        
