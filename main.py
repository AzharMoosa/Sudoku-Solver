def display_board(board):
    print_linebreak()
    for i, row in enumerate(board):
        if (i != 0 and i % square_size == 0):
            print_linebreak()
        for j, value in enumerate(row):
            if (j != 0 and j % square_size == 0):
                print(" | ", end="")
            if (j == board_size - 1):
                print(value)
            else:
                print(str(value) + " ", end="")
    print_linebreak()


def print_linebreak():
    scale = 23 / 9
    dash_number = round(scale * board_size)
    print("-" * dash_number)


def empty_space(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if (value == 0):
                return (i, j)


# 9x9 Sudoku Board
board_size = 9
square_size = 3
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
# board_size = 4
# square_size = 2
# sudoku_board = [
#     [3, 0, 0, 2],
#     [0, 0, 6, 0],
#     [0, 8, 0, 5],
#     [1, 0, 0, 0],
# ]

display_board(sudoku_board)
