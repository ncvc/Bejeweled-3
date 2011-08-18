import gameInterface
import gameState
import AI
import time

class Bot:
    def __init__(self):
        self.ai = AI.AI()
        self.gameInterface = gameInterface.GameInterface()
        self.gameState = gameState.GameState()
    
    def start(self):
        while self.gameState.gameOver != True:
            time.sleep(2)
            self.gameState = self.gameInterface.readGame()
            move = self.ai.determineMove(self.gameState.board)
            self.gameInterface.makeMove(move)
        
        return self.gameState

def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()
