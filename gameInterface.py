from autopy import mouse, alert, bitmap, color
from gameState import Point, GameState, Gem, RGB
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

# Color constants
COLOR_CONSTANTS = {'white':     RGB(232, 232, 232),
                   'blue':      RGB(12, 120, 235),
                   'orange':    RGB(242, 155, 65),
                   'yellow':    RGB(253, 240, 33),
                   'red':       RGB(247, 27, 56),
                   'purple':    RGB(215, 20, 215),
                   'green':     RGB(37, 205, 70)}

class GameInterface:
    # Takes boardDim, a Point representing the board dimensions (8x8 board is represented by Point(8,8))
    def __init__(self, boardDim):
        self.gameOffset = Point()
        self.boardOffset = Point()
        
        self.gemImgs = {}
        
        self.boardDim = boardDim
        
        self.gameState = GameState()
        
        self.calibrate()
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
    
    # Reads the board from the screen and returns a GameState
    def readGame(self):
        board = [[None for x in range(self.boardDim.x)] for y in range(self.boardDim.y)]
        bmp = bitmap.capture_screen()
        
        for y in range(self.boardDim.y):
            for x in range(self.boardDim.x):
                gem = self.getGem(bmp, Point(x, y))
                board[y][x] = gem
                
        self.gameState.board = board
        
        return self.gameState
    
    def getGem(self, bmp, point):
        absPt = self.boardToAbsPt(point)
        
        halfSize = 5
        total = 0
        totalColor = RGB()
        
        for x in range(absPt.x - halfSize, absPt.x + halfSize):
            for y in range(absPt.y - halfSize, absPt.y + halfSize):
                hexColor = bmp.get_color(x, y)
                r, g, b = color.hex_to_rgb(hexColor)
                rgb = RGB(r, g, b)
                
                totalColor += rgb
                total += 1
                
        avgRGB = totalColor / total
        gemColor = self.RGBToGem(avgRGB)
        
        return Gem(gemColor, 'status', point)

    # Determines color of RGB value
    def RGBToGem(self, RGB):
        minDistance = None;
        color = 'none'
        for key, value in COLOR_CONSTANTS.items():
            if RGB.distSquared(value) < minDistance or minDistance == None:
                color = key
                minDistance = RGB.distSquared(value)
        return color

    # Click and drag the mouse to make a move - takes a tuple of board coordinates
    # Attempts to place the cursor back where it found it
    def makeMove(self, move):
        firstPt, secondPt = move
        
        absFirst = self.boardToAbsPt(firstPt)
        absSecond = self.boardToAbsPt(secondPt)
        
        (lastX, lastY) = mouse.getpos()
        
        mouse.move(absFirst.x, absFirst.y)
        mouse.toggle(True)
        mouse.move(absSecond.x, absSecond.y)
        mouse.toggle(False)
        
        mouse.move(lastX, lastY)
    
    # Move mouse off the board
    def moveOffBoard(self):
        mouse.move(self.gameOffset.x, self.gameOffset.y)

    # Converts board coordinates to absolute screen coordinates (the center of the tile)
    def boardToAbsPt(self, boardPt):
        absX = self.boardOffset.x + boardPt.x * PIECE_OFFSET.x + PIECE_OFFSET.x / 2
        absY = self.boardOffset.y + boardPt.y * PIECE_OFFSET.y + PIECE_OFFSET.y / 2
        
        return Point(absX, absY)


if __name__ == '__main__':
    time.sleep(2)
    gi = GameInterface(Point(8, 8))
    
    print gi.readGame()
