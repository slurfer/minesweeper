import random
from typing import List, Tuple


class Coordinations:
    def __init__(self, x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Coordinations):
            return self.x == __o.x and self.y == __o.y
        return False
    
    def __str__(self) -> str:
        return f'{{x: {str(self.x)}, y: {str(self.y)}}}'


class Board:
    def __init__(self) -> None:
        self.board:List[Tile] = [] # game board
        self.board_width = 20
        self.board_height = 20
        self.is_generated = False
        for board_y in range(self.board_height):
            line = []
            for board_x in range(self.board_width):
                line.append(Tile(False, 0))
            self.board.append(line)

    def generate_board(self, seed_coordinations: Coordinations):
        mine_coordinates = self.generate_mines_coordinations(seed_coordinations)
        for mine in mine_coordinates:
            self.board[mine.y][mine.x] = Tile(True)

        #RENDER NUMBERS
        for board_y in range(self.board_height):
            for board_x in range(self.board_width):
                if not self.board[board_y][board_x].value == None:
                    value = 0
                    was_clicked = False 
                    # ___
                    # 1x_
                    # ___
                    if board_y-1>=0 and board_x-1>=0:
                        if str(self.board[board_y-1][board_x-1])=='x':
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
        print(self)
        return self


    def get_zero_coordinations(self)->List[Coordinations]:
        output = []
        for row in range(len(self.board)):
            for cell in range(len(self.board)):
                if self.board[row][cell].value == 0:
                    output.append(Coordinations(cell, row))
        return output
    
    def generate_mines_coordinations(self, seed_coordinates: Coordinations)->List[Coordinations]:
        mines = []
        seed_x = seed_coordinates.x
        seed_y = seed_coordinates.y
        protected_area = [[seed_x, seed_y], [seed_x-1, seed_y-1], [seed_x-1, seed_y], [seed_x-1, seed_y+1], [seed_x+1, seed_y], [seed_x+1, seed_y+1], [seed_x+1, seed_y], [seed_x+1, seed_y-1], [seed_x, seed_y-1]]
        protected_area = [Coordinations(seed_x, seed_y)]
        for a in range(100):
            while True:
                coordination = Coordinations(random.randint(0, len(self.board)-1), random.randint(0, len(self.board)-1))
                if coordination in mines or coordination in protected_area:
                    continue
                else:
                    break
            mines.append(coordination)
        return mines
    
    def get_zero_area_from_coordinations(self, coords:Coordinations, output: List[Coordinations])->List[Coordinations]:
        # x = coordinations.x
        # y = coordinations.y
        active_tile = self.board[coords.y][coords.x]
        value = active_tile.value
        # ___
        # 0x_
        # ___
        if coords.x-1>=0 and not Coordinations(coords.x-1, coords.y) in output:
            if self.board[coords.y][coords.x-1].value == 0:
                output += [Coordinations(coords.x-1, coords.y)]
                output = self.get_zero_area_from_coordinations(Coordinations(coords.x-1, coords.y), output)
        
        # _0_
        # _x_
        # ___
        if coords.y-1>=0:
            if self.board[coords.y-1][coords.x].value == 0 and not Coordinations(coords.x, coords.y-1) in output:
                output += [Coordinations(coords.x, coords.y-1)]
                output = self.get_zero_area_from_coordinations(Coordinations(coords.x, coords.y-1), output)
        
        # ___
        # _x0
        # ___
        if coords.x+1<len(self.board[0]) and not Coordinations(coords.x+1, coords.y) in output:
            if self.board[coords.y][coords.x+1].value == 0:
                output += [Coordinations(coords.x+1, coords.y)]
                output = self.get_zero_area_from_coordinations(Coordinations(coords.x+1, coords.y), output)
        
        # ___
        # _x_
        # _0_
        if coords.y+1<len(self.board) and not Coordinations(coords.x, coords.y+1) in output:
            if self.board[coords.y+1][coords.x].value == 0:
                output += [Coordinations(coords.x, coords.y+1)]
                output = self.get_zero_area_from_coordinations(Coordinations(coords.x, coords.y+1), output)

        return output
    
    def show_tile(self, coords:Coordinations)->List[Coordinations]:
        zeros = self.get_zero_area_from_coordinations(Coordinations(coords.x, coords.y), [Coordinations(coords.x, coords.y)])
        output = []
        for tile in zeros:
            output.append(tile)
        for tile in zeros:
            x = tile.x
            y = tile.y
            # 1__
            # _0_
            # ___
            if x-1>=0 and y-1>=0 and not (x-1, y-1) in output:
                output.append(Coordinations(x-1, y-1))
            # ___
            # 10_
            # ___
            if x-1>=0 and not (x-1, y) in output:
                output.append(Coordinations(x-1, y))
            # ___
            # _0_
            # 1__
            if x-1>=0 and y+1<len(self.board) and not (x-1, y+1) in output:
                output.append(Coordinations(x-1, y+1))
            # ___
            # _0_
            # _1_
            if y+1<len(self.board) and not (x, y+1) in output:
                output.append(Coordinations(x, y+1))
            # ___
            # _0_
            # __1
            if x+1<len(self.board[0]) and y+1<len(self.board) and not (x+1, y+1) in output:
                output.append(Coordinations(x+1, y+1))
            # ___
            # _01
            # ___
            if x+1<len(self.board[0]) and not (x+1, y) in output:
                output.append(Coordinations(x+1, y))
            # __1
            # _0_
            # ___
            if x+1<len(self.board[0]) and y-1 >= 0 and not (x+1, y-1) in output:
                output.append(Coordinations(x+1, y-1))
            # _1_
            # _0_
            # ___
            if y-1 >= 0 and not (x, y-1) in output:
                output.append(Coordinations(x, y-1))


            
        return output
            

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



""" board = Board()
board.generate_board()
board.get_zero_coordinations()
x = int(input('x:'))
y = int(input('y:'))
print(board.show_tile(x, y))
print(board) """

