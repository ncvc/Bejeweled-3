def determineMove(board):
    height = board.length()
    if !height > 3:
        exit()
    width = board[0].length()
    if !width > 3:
        exit()
    i = 0
    j = 0
    for i in range(height):
        for j in range(width) - 3:
            gem1 = board[height-1-i][j]
            gem2 = board[height-1-i][j+1]
            gem3 = board[height-1-i][j+2]
            gem4 = board[height-1-i][j+3]

            if colorsMatch(gem1, gem2, gem4):
                swap(point(), point())
                
            
            
            


        

def colorsMatch(gem1, gem2, gem3):
    return gem1.color == gem2.color == gem3.color

def swap(point1, point2)
    #call to UI here
        
    
    
