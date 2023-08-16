import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            column = loc % self.dim_size
            if board[row][column] == '*':
                continue
            board[row][column] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, column):
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, column - 1), min(self.dim_size - 1, column + 1) + 1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, column):
        self.dug.add((row, column))
        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, column - 1), min(self.dim_size - 1, column + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for column in range(self.dim_size):
                if (row, column) in self.dug:
                    visible_board[row][column] = str(self.board[row][column])
                else:
                    visible_board[row][column] = ' '
        string_rep = '    ' + '   '.join(map(str, range(self.dim_size))) + ' \n'
        string_rep += '-' * (self.dim_size * 5 + 2) + '\n'
        for i, row in enumerate(visible_board):
            string_rep += f'{i} | ' + ' | '.join(row) + ' |\n'
            string_rep += '-' * (self.dim_size * 5 + 2) + '\n'
        return string_rep

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    safe = True
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, column: "))
        row, column = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or column < 0 or column >= dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, column)
        if not safe:
            break
    if safe:
        print("CONGRATULATIONS !!!!  YOU ARE VICTORIOUS !")
    else:
        print("UNFORTUNATELY You have been bombarded!!! >> GAME OVER !!!!")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
