import gameInterface
import gameState
import AI
import time
from autopy import alert

# Contains an AI which interacts with the game via a GameInterface. The state
# is represented by a GameState
class Bot:
    def __init__(self):
        boardDim = gameState.Point(8,8)
        
        self.ai = AI.AI(boardDim, 3)
        self.gameInterface = gameInterface.GameInterface(boardDim)
        self.gameState = gameState.GameState(boardDim)
    
    # Begins a playing a game
    def start(self):
        while self.gameState.gameOver != True:
            time.sleep(2)
            if self.gameInterface.isMouseAtExit():
                if alert.alert('Paused', 'Quit?'):
                    break
                
            self.gameState = self.gameInterface.readGame()
            
            move = self.ai.determineMove(self.gameState.board)

            if move == None:
                print 'No move!'#self.gameState.board
            else:
                self.gameInterface.makeMove(move)
                
            #self.gameInterface.moveOffBoard()
        
        print 'done!'
        
        return self.gameState
        
# Main method just to start a game
def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()
