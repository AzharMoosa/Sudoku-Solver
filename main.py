# Displays Sudoku Board
def display_board(board):
    print_linebreak()
    for i, row in enumerate(board):
        if (i != 0 and i % SQUARE_SIZE == 0):
            print_linebreak()
        for j, value in enumerate(row):
            if (j != 0 and j % SQUARE_SIZE == 0):
                print(" | ", end="")
            if (j == BOARD_SIZE - 1):
                print(value)
            else:
                print(str(value) + " ", end="")
    print_linebreak()


# Prints Line Break Depending On Board Size
def print_linebreak():
    line_scale = 23 / 9
    dash_number = round(line_scale * BOARD_SIZE)
    print("-" * dash_number)


# Finds Empty Space
def empty_space(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if (value == 0):
                return (i, j)
    return None


# Finds Valid Space
def valid_space(board, value, position):
    row, column = position

    # Check Row
    for i in range(len(board[0])):
        if (column != i and board[row][i] == value):
            return False

    # Check Column
    for i in range(len(board)):
        if (row != i and board[i][column] == value):
            return False

    square_x = column // SQUARE_SIZE
    square_y = row // SQUARE_SIZE

    search_start_y = square_y * SQUARE_SIZE
    search_end_y = square_y * SQUARE_SIZE + SQUARE_SIZE
    search_start_x = square_x * SQUARE_SIZE
    search_end_x = square_x * SQUARE_SIZE + SQUARE_SIZE

    for i in range(search_start_y, search_end_y):
        for j in range(search_start_x, search_end_x):
            if ((i, j) != position and board[i][j] == value):
                return False

    return True


# Backtracking Algorithm
def sudoku_solver(board):
    empty = empty_space(board)
    if not empty:
        return True
    row, column = empty
    for i in range(1, BOARD_SIZE + 1):
        if (valid_space(board, i, (row, column))):
            board[row][column] = i
            if sudoku_solver(board):
                return True
            board[row][column] = 0

    return False


# 9x9 Sudoku Board
BOARD_SIZE = 9
SQUARE_SIZE = 3
sudoku_board = [
    [3, 0, 0, 2, 1, 0, 4, 0, 9],
    [0, 0, 6, 0, 8, 7, 5, 0, 0],
    [0, 8, 0, 5, 0, 9, 3, 0, 0],
    [1, 0, 0, 0, 5, 0, 0, 0, 6],
    [0, 9, 3, 8, 6, 2, 0, 4, 5],
    [5, 6, 0, 9, 7, 0, 0, 0, 8],
    [0, 7, 9, 1, 0, 0, 0, 5, 3],
    [4, 3, 5, 0, 0, 0, 6, 1, 0],
    [0, 1, 2, 6, 3, 0, 0, 0, 4],
]

# 4x4 Sudoku Board
# BOARD_SIZE = 4
# SQUARE_SIZE = 2
# sudoku_board = [
#     [3, 0, 0, 2],
#     [0, 0, 6, 0],
#     [0, 8, 0, 5],
#     [1, 0, 0, 0],
# ]

sudoku_solver(sudoku_board)
display_board(sudoku_board)
