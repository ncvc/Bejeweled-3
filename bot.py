import boardReader
import gameState

class Bot:
    def __init__(self):
        self.ai = AI()
        self.boardReader = boardReader.BoardReader()
        self.board = gameState.Board()
    
    def start(self):
        while self.board.gameOver != True:
            self.board = self.boardReader.read()
            self.ai.move(self.board)
        
        return self.board

def main():
    bot = Bot()
    
    return bot.start()

if __name__ == '__main__':
    main()