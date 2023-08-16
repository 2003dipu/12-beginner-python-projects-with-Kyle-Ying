def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, column):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    column_vals = [puzzle[i][column] for i in range(9)]
    if guess in column_vals:
        return False
    
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    row, column = find_next_empty(puzzle)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_sudoku(puzzle):
                return True
            puzzle[row][column] = -1
            
    return False

# Example puzzle
sudoku_puzzle = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

solve_sudoku(sudoku_puzzle)
for row in sudoku_puzzle:
    print(row)
