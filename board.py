class Board:
    def __init__(self) -> None:
        self.board = []
        self.board_width = 10
        self.board_height = 10

    def generate_board(self):
        for board_y in range(self.board_height):
            line = []
            for board_x in range(self.board_width):
                line.append('a')
            self.board.append(line)
    
    def __str__(self) -> str:
        output = ''
        for line in self.board:
            for cell in line:
                output += cell
            output += '\n'
        return output

class Tile:
    def __init__(self) -> None:
        self.is_mine = False
        self.value = 0
    
    def __str__(self) -> str:
        if self.is_mine == True:
            return 

board = Board()
board.generate_board()
print(board)