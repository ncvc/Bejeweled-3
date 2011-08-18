from autopy import *

class BoardReader:
    def __init__(self):
        self.NWPt = Point()
        self.SEPt = Point()
        
        self.level = 0
        self.score = 0
        self.percentComplete = 0
        
        self.calibrate()
    
    def calibrate(self):
        alert.alert(msg='Place the cursor at the top left of the flash game and press space', title='BoardReader')
        (NWX, NWY) = mouse.get_pos()
        self.NWPt = Point(NWX, NWY)
        
        alert.alert(msg='Place the cursor at the bottom right of the flash game and press space', title='BoardReader')
        (SEX, SEY) = mouse.get_pos()        #lol
        self.SEPt = Point(SEX - NWX, SEY - NWY)
    
    def read(self):
        pass

if __name__ == '__main__':
    br = BoardReader()