import Cell


class Maze(object):
    # rows = antal rader, cols = antal kolonner, x = aktuell position x-led, y = aktuell position y-led
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.x = 0
        self.y = 0
        # inga väggar finns förrän roboten ser dem
        self._matrix = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell.Cell('0000', i, j)

    @property
    def matrix(self):
        return self._matrix


myObjectX = Maze(2,3)
print(myObjectX.matrix)



