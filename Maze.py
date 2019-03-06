class Maze(object):
    import Cell

    def __init__(self, x, y):
        self.rows = x
        self.cols = y
        # inga väggar finns förrän roboten ser dem
        self._matrix = [[Cell() for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = i, j

    @property
    def matrix(self):
        return self._matrix

myObjectX = Maze(2, 3)
print(myObjectX.matrix)


