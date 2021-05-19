# Sudoku Solver

Sudoku Solver Built In Python Using Backtracking Algorithm

## Description

This is an implementation of a backtracking algorithm used to solve a sudoku puzzle.

- Rules (9x9 Grid):
  1. Each square contains a single number from 1 to 9
  2. Each 3x3 square can only contain each number from 1 to 9 once
  3. Each vertical column can only contain 1 to 9 once
  4. Each horizontal column can only contain 1 to 9 once

## Getting Started

### Dependencies

- Python 3

### Executing Program

- Clone Repo

```
git clone https://github.com/AzharMoosa/Sudoku-Solver
```

- Execute Program

```
python3 sudoku_solver.py
```

### How It Works

- Backtracking Algorithm:
  1. Find empty position on board
  2. Place a number and check if it is valid horizontally, vertically and in its corresponding grid
  3. If it is not valid, then backtrack and repeat step 2
  4. Once there are no empty spaces, we have found a solution
- Time Complexity: O(n<sup>m</sup>), where n is the number of possibilities in each square and m is the number of empty squares.
