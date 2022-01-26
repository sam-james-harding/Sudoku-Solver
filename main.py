import tkinter as tk
from pprint import pprint

from solver import SudokuSolver
from interface import SudokuBoard

def solveAndLabel(board: SudokuBoard, resultText: tk.StringVar):
    sudoku = board.getGrid()

    isSolved = SudokuSolver.solve(sudoku)

    if isSolved:
        resultText.set("Sudoku Solved Successfully")
        board.setGrid(sudoku)
    else:
        resultText.set("Sudoku is Unsolvable")

def main():
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.resizable(False, False)

    board = SudokuBoard(root)
    board.pack()

    buttonsFrame = tk.Frame(root)
    buttonsFrame.pack()

    #solve button
    tk.Button(
        buttonsFrame,
        text="Solve Sudoku",
        command=lambda: solveAndLabel(board, resultText)
    ).pack(side=tk.LEFT)

    #clear button
    tk.Button(
        buttonsFrame,
        text="Clear Sudoku",
        command=board.clear
    ).pack(side=tk.LEFT)

    #text indicating result
    resultText = tk.StringVar(value="No Sudoku Solved Yet")
    tk.Label(root, textvariable=resultText).pack()

    root.mainloop()

if __name__ == "__main__":
    main()