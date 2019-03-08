import Cell


class Maze(object):
    # rows = antal rader, cols = antal kolonner
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start_col = 0
        self.start_row = rows - 1
        self.current_pos_row = self.start_row   # börjar i start
        self.current_pos_col = self.start_col
        self.end_row = 0
        self.end_col = cols - 1
        # inga väggar finns förrän roboten ser dem
        self._matrix = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell.Cell('0000', i, j)
        self.current_direction = 'N' # börjar med att peka norr

    @property
    def matrix(self):
        return self._matrix
