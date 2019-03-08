# Här kan vi lägga algoritmen och saker relaterade till den
import Maze
import Cell
from HelpFunctions import HelpFunctions


class PathFinder:


    def calc_g(self, maze, row, col):
        cell = maze.matrix[row][col]
        cell.g = abs(row - maze.start_row) + abs(col - maze.start_col)   # tror detta stämmer?

    # manhattan heuristic (första vektornorm)
    def calc_h(self, maze, row, col):
        cell = maze.matrix[row][col]
        cell.h = abs(maze.end_row - row) + abs(maze.end_col - col)

    def calc_f(self, maze, row, col):
        cell = maze.matrix[row][col]
        cell.f = cell.g + cell.h


    def astar(self, maze):
        direction = None
        return direction    # 'N/S/W/E'

    def right_hand_rule(self, maze):

        row = maze.current_pos_row
        print('Current position row = ' + str(row))
        col = maze.current_pos_col
        print('Current position col = ' + str(col))
        current_cell = maze.matrix[row][col]

        if row == maze.end_row and col == maze.end_col:
            return '0'

        helper = HelpFunctions()
        print(str(current_cell.walls))
        walls = helper.change_wall_format(current_cell.walls, maze.current_direction, 'NSWE') # walls blir på ABLR
        print(str(walls))

        # välj håll att gå. Prio: Höger, Rätt fram, Vänster, Vänd
        direction = ''

        if walls[3] == '0':
            direction = 'R'

        elif walls[0] == '0':
            direction = 'A'

        elif walls[2] == '0':
            direction = 'L'

        elif walls[1] == '0':
            direction = 'B'

        else:
            print('No direction without walls')

        print('Direction: ' + direction)
        direction = helper.change_direction_format(maze, direction, 'ABLR')
        print('New Direction: ' + direction)

        return direction



