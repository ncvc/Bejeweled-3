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
        self.loadGems()
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
        mouse.move(self.boardOffset.x, self.boardOffset.y)
    
    # Reads the board from the screen and returns a GameState
    def readGame(self):
        board = []
        bmp = bitmap.capture_screen()
        f = open('lol.txt', 'w')
        for x in range(self.boardDim.x):
            for y in range(self.boardDim.y):
                gem = self.getGem(bmp, Point(x, y))
                print gem
                f.write(str(gem) + ' ')
            f.write('\n')
        f.close()
        self.gameState.board = board
        
        return self.gameState
    
    def getGem(self, bmp, point):
        absPt = self.boardToAbsPt(point)
        
        halfSize = 5
        total = 0
        totalColor = RGB()
        colors = []
        
        for x in range(absPt.x - halfSize, absPt.x + halfSize):
            for y in range(absPt.y - halfSize, absPt.y + halfSize):
                hexColor = bmp.get_color(x, y)
                r, g, b = color.hex_to_rgb(hexColor)
                rgb = RGB(r, g, b)
                
                totalColor += rgb
                total += 1
                colors.append(rgb)
                #mouse.move(x, y)
                #time.sleep(.01)
        
        avg = totalColor / total
        lol = '''mult = .5
        total = totalColor = 0
        for color in colors:
            if color < avg * (1 + mult) and color > avg * (1 - mult):
                total += 1
                totalColor += color
        
        print total'''
        
        return avg
    
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

    # Converts board coordinates to absolute screen coordinates (the center of the tile)
    def boardToAbsPt(self, boardPt):
        absX = self.boardOffset.x + boardPt.x * PIECE_OFFSET.x + PIECE_OFFSET.x / 2
        absY = self.boardOffset.y + boardPt.y * PIECE_OFFSET.y + PIECE_OFFSET.y / 2
        
        return Point(absX, absY)


if __name__ == '__main__':
    time.sleep(2)
    gi = GameInterface(Point(8, 8))
    
    print gi.readGame()