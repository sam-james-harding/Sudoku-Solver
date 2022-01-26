import tkinter as tk

class SudokuBoard(tk.Frame):
    GRID_SIZE = 9
    ENTRY_WIDTH = 2

    def __init__(self, root: tk.Tk):
        # initial setup (frame parent/intialisation, grid initialisation, validator registration)
        super().__init__(root)
        self.__grid: list[list[tk.StringVar]] = []
        validator = self.register(self.__validateGridEntry)

        for row in range(SudokuBoard.GRID_SIZE):
            self.__grid.append([]) #add new row to grid
            
            # add new row frame to gui grid
            newRowFrame = tk.Frame(self)
            newRowFrame.pack()

            for col in range(SudokuBoard.GRID_SIZE):
                # add new grid item (StringVar) to current grid row
                newGridItem = tk.StringVar()
                self.__grid[row].append(newGridItem)

                # add new entry to gui grid
                tk.Entry(
                    newRowFrame,
                    textvariable=newGridItem,
                    width=SudokuBoard.ENTRY_WIDTH,
                    validate="all",
                    validatecommand=(validator, "%P")
                ).pack(side=tk.LEFT)

    @staticmethod
    def __validateGridEntry(newText: str):
        return (newText.isdigit() and 1 <= int(newText) <= 9) or newText == ""

    def setGrid(self, board: list[list[int]]):
        translate = lambda x: str(x) if 1 <= x <= 9 else ""

        for row in range(SudokuBoard.GRID_SIZE):
            for col in range(SudokuBoard.GRID_SIZE):
                self.__grid[row][col].set(
                    translate(board[row][col])
                )

    def getGrid(self) -> list[list[int]]:
        translate = lambda s: 0 if s == "" else int(s)
        result: list[list[int]] = []

        for row in range(SudokuBoard.GRID_SIZE):
            result.append([])
            for col in range(SudokuBoard.GRID_SIZE):
                result[row].append(
                    translate(self.__grid[row][col].get())
                )

        return result

    def clear(self):
        for row in range(SudokuBoard.GRID_SIZE):
            for col in range(SudokuBoard.GRID_SIZE):
                self.__grid[row][col].set("")