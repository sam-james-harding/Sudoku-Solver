from itertools import product

class SudokuSolver:
    GRID_SIZE = 9
    SQUARE_SIZE = 3

    @staticmethod
    def __valInRow(board: list[list[int]], val: int, row: int) -> bool:
        return val in board[row]

    @staticmethod
    def __valInCol(board: list[list[int]], val: int, col: int) -> bool:
        return val in [row[col] for row in board]

    @staticmethod
    def __valInSquare(board: list[list[int]], val: int, row: int, col: int) -> bool:
        startRow = row - row % SudokuSolver.SQUARE_SIZE
        startCol = col - col % SudokuSolver.SQUARE_SIZE

        squareRows = range(startRow, startRow+SudokuSolver.SQUARE_SIZE)
        squareCols = range(startCol, startCol+SudokuSolver.SQUARE_SIZE)

        for row, col in product(squareRows, squareCols):
            if board[row][col] == val: return True
        return False

    @staticmethod
    def __isValidPlacement(board: list[list[int]], val: int, row: int, col: int) -> bool:
        # to be valid, the value cannot be in the row, column or square
        return not any([
            SudokuSolver.__valInRow(board, val, row),
            SudokuSolver.__valInCol(board, val, col),
            SudokuSolver.__valInSquare(board, val, row, col)
        ])

    @staticmethod
    def solve(board: list[list[int]]) -> bool:
        # For each coordinate in the sodoku, first check if it is unfilled. If not, skip the the
        # next coordinate. Then, for each possible value from 1 to GRID_SIZE, check if it is valid.
        # If it is, set the current coordinate's value to that value, and if the sodoku can then
        # be solved (via recursive call of solve function) return True to indicate success,
        # otherwise set the value back to 0 to backtrack that step. If no value can be found, it is
        # unsolvable, so return False. If every value has been filled, thus reaching the end of the
        # loop, return True.
        for row, col in product(range(SudokuSolver.GRID_SIZE), range(SudokuSolver.GRID_SIZE)):
            if board[row][col] != 0: continue
            
            for val in range(1, SudokuSolver.GRID_SIZE+1):
                if not SudokuSolver.__isValidPlacement(board, val, row, col): continue

                board[row][col] = val
                if SudokuSolver.solve(board): return True
                else: board[row][col] = 0

            return False
        return True