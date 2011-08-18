from autopy import mouse, alert, bitmap
from gameState import Point, Board, Gem
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

class BoardReader:
    def __init__(self):
        self.gameOffset = Point()
        self.boardOffset = Point()
        
        self.gems = []
        
        self.level = 0
        self.score = 0
        self.percentComplete = 0
        
        self.calibrate()
        self.loadGems()
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
    
    def read(self):
        bmp = self.getScreen()
    
    def getScreen(self):
        topLeft = BOARD_OFFSET.toTuple()
        bottomRight = (BOARD_OFFSET + GAME_SIZE).toTuple()
        rect = (topLeft, bottomRight)
        
        return bitmap.capture_screen_portion(rect)
    
    def loadGems(self):
        files = os.listdir(GEM_DIR)
        
        for fileName in files:
            self.gems.append(bitmap.Bitmap.open(os.path.join(GEM_DIR, fileName)))

if __name__ == '__main__':
    time.sleep(2)
    br = BoardReader()
    
    mouse.move(br.gameOffset.x, br.gameOffset.y)
    time.sleep(2)
    mouse.move(br.boardOffset.x, br.boardOffset.y)

def lol():
    print br.gameOffset
    print br.SEPt
    
    time.sleep(1)
    
    rect = ((Point() - br.gameOffset).toTuple(), br.SEPt.toTuple())
    rect = ((100, 100), (1024, 1024))
    print rect
    bitmap.capture_screen(rect).save('C:/Users/Nathan/Programming/Bejeweled-3/lol.bmp')
    
    alert.alert('done', 'lol')

def pixels():
    alert.alert('Place the cursor at the top left of the flash game and press space', 'BoardReader')
    (NWX, NWY) = mouse.get_pos()
    self.gameOffset = Point(NWX, NWY)
    
    alert.alert('Place the cursor at the bottom right of the flash game and press space', 'BoardReader')
    (SEX, SEY) = mouse.get_pos()          #lol
    self.SEPt = Point(SEX, SEY)