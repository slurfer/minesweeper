import random

class Board:
    def __init__(self) -> None:
        self.board = [] # game board
        self.board_width = 20
        self.board_height = 20

    def generate_board(self):
        for board_y in range(self.board_height):
            line = []
            for board_x in range(self.board_width):
                line.append(Tile(False, 0))
            self.board.append(line)
        mine_coordinates = self.generate_mines_coordinations()
        for mine in mine_coordinates:
            mine_x = mine[0]
            mine_y = mine[1]
            self.board[mine_y][mine_x] = Tile(True)

        #RENDER NUMBERS
        for board_y in range(self.board_height):
            for board_x in range(self.board_width):
                if not self.board[board_y][board_x].value == None:
                    value = 0
<<<<<<< HEAD
                    
                    # 1__
                    # _x_
                    # ___
                    if board_y-1>=0 and board_x-1>=0:
                        if str(self.board[board_y-1][board_x-1])=='x':
=======
                    was_clicked = False 
                    if board_y-1>0 and board_x-1>0:
                        if str(board.board[board_y-1][board_x-1])=='x':
>>>>>>> Terka
                            value += 1
                    
                    # ___
                    # 1x_
                    # ___
                    if board_y>=0 and board_x-1>=0:
                        if str(self.board[board_y][board_x-1])=='x':
                            value += 1
                    
                    # ___
                    # _x_
                    # 1__
                    if board_y+1<len(self.board) and board_x-1>=0:
                        if str(self.board[board_y+1][board_x-1])=='x':
                            value += 1
                    
                    # ___
                    # _x_
                    # _1_
                    if board_y+1<len(self.board) and board_x<len(self.board[0]):
                        if str(self.board[board_y+1][board_x])=='x':
                            value += 1
                    
                    # ___
                    # _x_
                    # __1
                    if board_y+1<len(self.board) and board_x+1<len(self.board[0]):
                        if str(self.board[board_y+1][board_x+1])=='x':
                            value += 1
                    
                    # ___
                    # _x1
                    # ___
                    if board_y>=0 and board_x+1<len(self.board[0]):
                        if str(self.board[board_y][board_x+1])=='x':
                            value += 1
                    
                    # __1
                    # _x_
                    # ___
                    if board_y-1>=0 and board_x+1<len(self.board[0]):
                        if str(self.board[board_y-1][board_x+1])=='x':
                            value += 1
                    
                    # _1_
                    # _x_
                    # ___
                    if board_y-1>=0 and board_x<len(self.board[0]):
                        if str(self.board[board_y-1][board_x])=='x':
                            value += 1
                    self.board[board_y][board_x].value = value


    def generate_mines_coordinations(self):
        mines = []
        for a in range(100):
            while True:
                coordination = (random.randint(0, len(self.board)-1), random.randint(0, len(self.board)-1))
                if coordination in mines:
                    continue
                else:
                    break
            mines.append(coordination)
        return mines
    
    def __str__(self) -> str:
        output = ''
        for line in self.board:
            for cell in line:
                output += str(cell) + '|'
            output += '\n'
        return output[:-1]

class Tile:
    def __init__(self, is_mine, value = None, was_clicked = False) -> None:
        self.is_mine = is_mine
        self.value = value
        self.was_clicked = was_clicked
    
    def __str__(self) -> str:
        if self.is_mine == True:
            return 'x'
        else:
            return str(self.value)
<<<<<<< HEAD
=======


board = Board()
board.generate_board()
print(board)
>>>>>>> Terka
