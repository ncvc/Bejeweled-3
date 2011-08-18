import boardReader
import gameState

class Bot:
    def __init__(self):
        self.ai = AI()
        self.boardReader = boardReader.BoardReader()
        self.game = gameState.Game()
    
    def start(self):
        while self.game.gameOver != True:
            self.game = self.boardReader.read()
            boardReader.swap(self.ai.determineMove(self.game))
        
        return self.game

def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()
