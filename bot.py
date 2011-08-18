import gameInterface
import gameState
import AI

class Bot:
    def __init__(self):
        self.ai = AI()
        self.gameInterface = gameInterface.GameInterface()
        self.gameState = gameState.GameState()
    
    def start(self):
        while self.gameState.gameOver != True:
            self.gameState = self.gameInterface.readGame()
            move = self.ai.determineMove(self.gameState)
            self.gameInterface.swap(move)
        
        return self.gameState

def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()
