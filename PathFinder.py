# Här kan vi lägga algoritmen och saker relaterade till den
import Maze
import Cell
from HelpFunctions import HelpFunctions


class PathFinder:


    def calc_g(self, maze, x, y):
        cell = maze.matrix[x][y]
        cell.g = abs(x - maze.start_x) + abs(y - maze.start_y)   # tror detta stämmer?

    # manhattan heuristic (första vektornorm)
    def calc_h(self, maze, x ,y):
        cell = maze.matrix[x][y]
        cell.h = abs(maze.end_x - x) + abs(maze.end_y - y)

    def calc_f(self, maze, x, y):
        cell = maze.matrix[x][y]
        cell.f = cell.g + cell.h

    def astar(self, maze):
        direction = None
        return direction    # 'N/S/W/E'

    def right_hand_rule(self, maze):
        x = maze.current_pos_x
        y = maze.current_pos_y
        current_cell = maze.matrix[x][y]

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

        return direction



