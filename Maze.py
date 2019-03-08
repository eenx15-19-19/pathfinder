import Cell


class Maze(object):
    # rows = antal rader, cols = antal kolonner
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start_y = 0
        self.start_x = rows - 1
        self.current_pos_x = self.start_x # börjar i start
        self.current_pos_y = self.start_y
        self.end_x = 0
        self.end_y = cols - 1
        # inga väggar finns förrän roboten ser dem
        self._matrix = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell.Cell('0000', i, j)
        self.current_direction = 'N' # börjar med att peka norr

    @property
    def matrix(self):
        return self._matrix
