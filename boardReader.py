from autopy import mouse, alert, bitmap
from gameState import Point, Game, Gem
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
        
        self.gemImgs = {}
        
        self.game = Game()
        
        self.calibrate()
        self.loadGems()
    
    # Sets the location of the top left of the board - all other points are represented relative to the gameOffset
    def calibrate(self):
        calibrationImg = bitmap.Bitmap.open(CALIBRATION_IMAGE_PATH)
        
        bmp = bitmap.capture_screen()
        (x, y) = bmp.find_bitmap(calibrationImg)
        
        self.gameOffset = Point(x, y) + GAME_OFFSET
        self.boardOffset = self.gameOffset + BOARD_OFFSET
    
    # Reads the board from the screen and returns a Board representing the game board
    def read(self):
        gemList = []
        bmp = bitmap.capture_screen()
        
        maxX = maxY = 0
        
        for gemColor, gemImg in self.gemImgs.items():
            (x, y) = bmp.find_bitmap(gemImg)
            gemRelPt = Point(x, y) - BOARD_OFFSET - GAME_OFFSET
            gemBoardX = int(gemRelPt.x / PIECE_OFFSET.x)
            gemBoardY = int(gemRelPt.y / PIECE_OFFSET.y)
            
            if gemBoardX > maxX:
                maxX = gemBoardX
            
            if gemBoardY > maxY:
                maxY = gemBoardY
            
            gemBoardPt = Point(gemBoardX, gemBoardY)
            
            gem = Gem(gemColor, 'status', gemBoardPt)
            gemList.append(gem)
        
        gems = [[] for i in range(maxY)]
        for gem in gemList:
            gemPt = gem.point
            gems[gemPt.y][gemPt.x] = gem
        
        self.game.board = gems
        
        return self.game
    
    # Loads all gem images into self.gemImgs, with the filename as the key
    def loadGems(self):
        files = os.listdir(GEM_DIR)
        
        for fileName in files:
            self.gemImgs[fileName] = bitmap.Bitmap.open(os.path.join(GEM_DIR, fileName))


if __name__ == '__main__':
    time.sleep(2)
    br = BoardReader()
    

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