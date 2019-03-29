import Cell
from MazeTransformer import MazeTransformer

class Maze(object):
    # rows = antal rader, cols = antal kolonner
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start_col = 0
        self.start_row = rows - 1

        # lösningen placerad i övre högre hörnet
        self.end_row = 8
        self.end_col = 7

        transformer = MazeTransformer()
        self._matrix = transformer.get_matrix()
        # inga väggar finns förrän roboten ser dem
       # self._matrix = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self._matrix[i][j] = Cell.Cell(self._matrix[i][j], i, j)

        self.shortest_path = []
        # startnoden är besökt
        self.matrix[self.start_row][self.start_col].visited = True

        # tillfällig matris för att spara f
        self._matrix_f = [[0 for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix_f[i][j] = 0

        # lista för shortest path
        self.shortest_path = [self.matrix[self.start_row][self.start_col]]
        self.path = [self.matrix[self.start_row][self.start_col]]
    @property
    def matrix(self):
        return self._matrix

    @property
    def matrix_f(self):
        return self._matrix_f
