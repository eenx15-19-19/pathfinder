import Cell
from MazeTransformer import MazeTransformer
from HelpFunctions import HelpFunctions

class Maze(object):
    # rows = antal rader, cols = antal kolonner
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.start_col = 0
        self.start_row = rows - 1
        # lösningen placerad i övre högre hörnet
        self.end_row = 7
        self.end_col = 8
        self.explored_row = self.start_row
        self.explored_col = self.start_col
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

        helper = HelpFunctions()
        # matris för att spara det roboten har upptäckt
        self._matrix_robot = [[Cell.Cell('0000', i, j) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self._matrix_robot[i][j] = Cell.Cell('0000', i, j)

        self._matrix_robot[self.start_row][self.start_col] = self.matrix[self.start_row][self.start_col]

        # Tom labyrint, men med ytterväggar
        for i in range(15):
            self._matrix_robot[i][0].walls = helper.split_walls('0010')
            self._matrix_robot[i][15].walls = helper.split_walls('0001')
            self._matrix_robot[0][i].walls = helper.split_walls('1000')
            self._matrix_robot[15][i].walls = helper.split_walls('0100')

        self._matrix_robot[0][0].walls = helper.split_walls('1010')
        self._matrix_robot[0][15].walls = helper.split_walls('1001')
        self._matrix_robot[15][0].walls = helper.split_walls('0110')
        self._matrix_robot[15][15].walls = helper.split_walls('0101')

        # lista för shortest path
        self.shortest_path = [self.matrix[self.start_row][self.start_col]]
        self.path = [self.matrix[self.start_row][self.start_col]]

        self.count_fake = 0
        self.count_unvisited = 0
        self.count_pb = 0
    @property
    def matrix(self):
        return self._matrix

    @property
    def matrix_robot(self):
        return self._matrix_robot
