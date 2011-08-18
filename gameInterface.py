from autopy import mouse, alert, bitmap
from gameState import Point, GameState, Gem
import time
import os

# Image directory
IMG_DIR = os.path.join(os.getcwd(), 'images')

# Gem directory
GEM_DIR = os.path.join(IMG_DIR, 'gems')

# Path to the calibration image
CALIBRATION_IMAGE_PATH = os.path.join(IMG_DIR, 'hint.bmp')

# Game offset relative to the calibration image
GAME_OFFSET = Point(-66, -354)

# Total size of the game
GAME_SIZE = Point(640, 480)

# Board offset relative to the game
BOARD_OFFSET = Point(198, 60)

# Distance between pieces
PIECE_OFFSET = Point(47, 47)

class GameInterface:
    def __init__(self):
        self.gameOffset = Point()
        self.boardOffset = Point()
        
        self.gemImgs = {}
        
        self.gameState = GameState()
        
        self.calibrate()
        self.loadGems()
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
    
    # Reads the board from the screen and returns a GameState
    def readGame(self):
        gemList = []
        bmp = bitmap.capture_screen()
        
        print self.gemImgs
        totalGems = 0
        maxX = maxY = 0
        
        for gemColor, gemImg in self.gemImgs.items():
            gemCoords = bmp.find_every_bitmap(gemImg, .6)
            gemColors=0
            for x, y in gemCoords:
                if x > self.boardOffset.x and x < self.boardOffset.x + PIECE_OFFSET.x * 8 and y > self.boardOffset.y and y < self.boardOffset.y + PIECE_OFFSET.y * 8:
                    gemColors+=1
                    totalGems+=1
                    gemRelPt = Point(x, y) - self.boardOffset
                    gemBoardX = int(gemRelPt.x / PIECE_OFFSET.x)
                    gemBoardY = int(gemRelPt.y / PIECE_OFFSET.y)
                    
                    if gemBoardX > maxX:
                        maxX = gemBoardX
                    
                    if gemBoardY > maxY:
                        maxY = gemBoardY
                    
                    gemBoardPt = Point(gemBoardX, gemBoardY)
                    
                    gem = Gem(gemColor, 'status', gemBoardPt)
                    gemList.append(gem)
        
        gems = [[Gem('red.bmp', 'default', Point(x, y)) for x in range(8)] for y in range(8)]
        for gem in gemList:
            gemPt = gem.point
            gems[gemPt.y][gemPt.x] = gem
        
        self.gameState.board = gems
        
        return self.gameState
    
    # Loads all gem images into self.gemImgs, with the filename as the key
    def loadGems(self):
        files = os.listdir(GEM_DIR)
        
        for fileName in files:
            self.gemImgs[fileName] = bitmap.Bitmap.open(os.path.join(GEM_DIR, fileName))
    
    # Click and drag the mouse to make a move - takes a tuple of board coordinates
    def makeMove(self, move):
        firstPt, secondPt = move
        
        absFirst = self.boardToAbsPt(firstPt)
        absSecond = self.boardToAbsPt(secondPt)
        
        mouse.move(absFirst.x, absFirst.y)
        mouse.toggle(True)
        mouse.move(absSecond.x, absSecond.y)
        mouse.toggle(False)

    # Converts board coordinates to absolute screen coordinates
    def boardToAbsPt(self, boardPt):
        absX = self.boardOffset.x + boardPt.x * PIECE_OFFSET.x + PIECE_OFFSET.x / 2
        absY = self.boardOffset.y + boardPt.y * PIECE_OFFSET.y + PIECE_OFFSET.y / 2
        
        return Point(absX, absY)


if __name__ == '__main__':
    time.sleep(2)
    gi = GameInterface()
    
    print gi.readGame()