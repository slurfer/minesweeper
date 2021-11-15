class Board:
    def __init__(self) -> None:
        self.board = []
        self.board_width = 10
        self.board_height = 10

    def generate_board(self):
        for board_y in range(self.board_height):
            line = []
            for board_x in range(self.board_width):
                line.append(Tile(False, 0))
            self.board.append(line)
        self.board[3][4] = Tile(True)
        
    
    def __str__(self) -> str:
        output = ''
        for line in self.board:
            for cell in line:
                output += str(cell) + '|'
            output += '\n'
        return output

class Tile:
    def __init__(self, is_mine, value = None) -> None:
        self.is_mine = is_mine
        self.value = value
    
    def __str__(self) -> str:
        if self.is_mine == True:
            return 'x'
        else:
            return str(self.value)

