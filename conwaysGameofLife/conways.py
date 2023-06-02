import time
import random

class Cell:
    def __init__(self):
        self.Status ="Dead"

    def set_Dead(self):
        self.Status = "Dead"

    def set_Alive(self):
        self.Status = "Alive"

    def is_Alive(self):
        if self.Status == "Alive":
            return True
        return False

    def print_Character(self):
        if self.is_Alive():
            return "X"
        return " "

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._grid = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]

        self.generateBoard()

    def draw_board(self):
        for row in self._grid:
            for column in row:
                print(column.print_Character(),end='')
            print()

    def generateBoard(self):
        for row in self._grid:
            for column in row:
                chanceNumber = random.randint(0,2)
                if chanceNumber == 1:
                    column.set_Alive()
    def updateBoard(self):
        goes_alive = []
        gets_killed = []
        #self.newgrid=
        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                check_neighbour = self.checkneighbour(row, column)

                livingCount = []

                for neighboursCell in check_neighbour:
                    if neighboursCell.is_Alive():
                        livingCount.append(neighboursCell)

                cellObject = self._grid[row][column]
                statusMainCell = cellObject.is_Alive()

                if statusMainCell == True:
                    if len(livingCount) <2 or len(livingCount) > 3:
                        gets_killed.append(cellObject)

                    elif len(livingCount) == 3 or len(livingCount) == 2:
                        goes_alive.append(cellObject)
                else:
                    if len(livingCount) == 3:
                        goes_alive.append(cellObject)

        for cellItems  in goes_alive:
            cellItems.set_Alive()

        for cellItems in gets_killed:
            cellItems.set_Dead()

    def checkneighbour(self,checkRow, checkColumn):
        searchMin = -1
        searchMax = 2

        neighbourList = []
        for row in range(searchMin, searchMax):
            for column in range(searchMin, searchMax):
                neighbourRow = checkRow + row
                neighbourColumn = checkColumn + column

                validNeighbour = True

                if (neighbourRow) == checkRow and (neighbourColumn) == checkColumn:
                    validNeighbour = False

                elif (neighbourRow) < 0 or (neighbourRow) >= self.rows:
                    validNeighbour = False

                elif (neighbourColumn) < 0 or (neighbourColumn)  >= self.columns:
                    validNeighbour = False

                if validNeighbour:
                    neighbourList.append(self._grid[neighbourRow][neighbourColumn])
        return neighbourList

def main():
    Var = Board(20, 20)
    Var.draw_board()
    num = 2
    for i in range(49):
        print('\n' * 5)
        print("Generation:", num)
        num += 1
        Var.updateBoard()
        Var.draw_board()
        time.sleep(3)

main()
