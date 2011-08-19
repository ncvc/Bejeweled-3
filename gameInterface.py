from autopy import mouse, alert, bitmap, color
from gameState import Point, GameState, Gem, RGB
import time
import os

# Image directory
IMG_DIR = os.path.join(os.getcwd(), 'images')

# Path to the calibration image
CALIBRATION_IMAGE_PATH = os.path.join(IMG_DIR, 'hint.bmp')

# Path to the submit button image
SUBMIT_IMAGE_PATH = os.path.join(IMG_DIR, 'submit.bmp')

# Path to the replay button image
REPLAY_IMAGE_PATH = os.path.join(IMG_DIR, 'replay.bmp')

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
        
        self.gameState = GameState(boardDim)
        
        self.calibrate()
        
        self.submitImg = bitmap.Bitmap.open(SUBMIT_IMAGE_PATH)
        self.replayImg = bitmap.Bitmap.open(REPLAY_IMAGE_PATH)
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
    
    # Reads the board from the screen and returns a GameState
    def readGame(self):
        bmp = bitmap.capture_screen()
        
        submitPt = bmp.find_bitmap(self.submitImg)
        
        if submitPt != None:
            mouse.move(submitPt[0], submitPt[1])
            mouse.click()
            self.replayGame()
            return
        
        for y in range(self.gameState.boardDim.y):
            for x in range(self.gameState.boardDim.x):
                gem = self.getGem(bmp, Point(x, y))
                self.gameState.board[y][x] = gem
                
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

    # Click and drag the mouse to make a move - takes a Move object
    # Attempts to place the cursor back where it found it
    def makeMove(self, move):
        self.gameState.makeMove(move)
        
        firstPt, secondPt = move.pointTuple()
        
        absFirst = self.boardToAbsPt(firstPt)
        absSecond = self.boardToAbsPt(secondPt)
        
        lastX, lastY = mouse.get_pos()
        
        mouse.move(absFirst.x, absFirst.y)
        mouse.toggle(True)
        mouse.move(absSecond.x, absSecond.y)
        mouse.toggle(False)
        
        mouse.move(lastX, lastY)
    
    # Move mouse off the board
    def moveOffBoard(self):
        mouse.move(self.gameOffset.x - 10, self.gameOffset.y - 10)
    
    def isMouseOnGame(self):
        (x, y) = mouse.get_pos()
        
        #return x > self.gameOffset.x and x < self.gameOffset.x + GAME_SIZE.x and y > self.gameOffset.y and y < self.gameOffset.y + GAME_SIZE.y
        return x > self.gameOffset.x and x < self.gameOffset.x + 10 and y > self.gameOffset.y and y < self.gameOffset.y + 10

    # Converts board coordinates to absolute screen coordinates (the center of the tile)
    def boardToAbsPt(self, boardPt):
        absX = self.boardOffset.x + boardPt.x * PIECE_OFFSET.x + PIECE_OFFSET.x / 2
        absY = self.boardOffset.y + boardPt.y * PIECE_OFFSET.y + PIECE_OFFSET.y / 2
        
        return Point(absX, absY)
    
    def replayGame(self):
        replayPt = None
        
        while replayPt == None:
            bmp = bitmap.capture_screen()
            replayPt = bmp.find_bitmap(self.replayImg)
        
        mouse.move(replayPt[0], replayPt[1])
        mouse.click()
        
        time.sleep(2)
        mouse.move(self.gameOffset.x + GAME_SIZE.x / 2, self.gameOffset.y + GAME_SIZE.y / 2)
        mouse.click()
        
        time.sleep(2)
        mouse.move(self.gameOffset.x + 100, self.gameOffset.y + 100)
        mouse.click()


if __name__ == '__main__':
    time.sleep(2)
    gi = GameInterface(Point(8, 8))
    
    print gi.readGame()
