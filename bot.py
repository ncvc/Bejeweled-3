import gameInterface
import gameState
import AI
import time
from autopy import mouse, alert

class Bot:
    def __init__(self):
        self.ai = AI.AI()
        self.gameInterface = gameInterface.GameInterface(gameState.Point(8,8))
        self.gameState = gameState.GameState()
    
    def start(self):
        time.sleep(2)
        while self.gameState.gameOver != True:
            if self.gameInterface.isMouseOnGame():
                if alert.alert('Paused', 'Quit?'):
                    break
                
            self.gameState = self.gameInterface.readGame()
            move = self.ai.determineMove(self.gameState.board)

            if move == None:
                print self.gameState.board
            else:
                self.gameInterface.makeMove(move)
                
            #self.gameInterface.moveOffBoard()
        
        print 'done!'
        
        return self.gameState

def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()
