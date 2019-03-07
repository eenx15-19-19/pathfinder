import Cell


class Maze(object):
    # rows = antal rader, cols = antal kolonner
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.current_pos_x = 0
        self.current_pos_y = 0
        self.start_x = 0
        self.start_y = 0
        self.end_x = 6
        self.end_y = 13
        # inga väggar finns förrän roboten ser dem
        self._matrix = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell.Cell('0000', i, j)
        self.current_direction = 'N'

    @property
    def matrix(self):
        return self._matrix



myObjectX = Maze(2,3)
print(myObjectX.matrix)
myObjectX.current_direction = 'S'
print(myObjectX.current_direction)



