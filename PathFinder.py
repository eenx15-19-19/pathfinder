# Här kan vi lägga algoritmen och saker relaterade till den
import Maze
import Cell
import sys
from HelpFunctions import HelpFunctions
from Translation import Translation


class PathFinder:

    # måste räkna medan den går, inte säkert att den tagit raka vägen
    def calc_g(self, maze, cell):
        row = cell.row
        col = cell.col
        cell.g = abs(row - maze.start_row) + abs(col - maze.start_col)   # tror detta stämmer? det stämmer inte

    # manhattan heuristic (första vektornorm)
    # hur får man denna att ta hänsyn till väggar?
    def calc_h(self, maze, cell):
        row = cell.row
        col = cell.col
        cell.h = abs(maze.end_row - row) + abs(maze.end_col - col)

    def calc_f(self, cell):
        cell.f = cell.g + cell.h


    def astar(self, maze, robot):   # Ska göras
        helper = HelpFunctions()
        translator = Translation()
        current_cell = helper.current_cell(robot, maze)
        available_cells = []
        NSWE = 'N', 'S', 'W', 'E'
        ABLR = 'A', 'B', 'L', 'R'
        walls = translator.change_wall_format(current_cell.walls, robot.current_direction, 'NSWE')

        for i in range(len(walls)):
            wall = walls[i]

            if wall == '0':
                direction = ABLR[i]
                direction = translator.change_direction_format(robot, direction, 'ABLR')
                temp_cell = helper.get_adjacent_cell(maze, robot, direction)
                available_cells.append(temp_cell)

        target_cell = Cell.Cell(helper.split_walls('0000'), 0, 0)
        target_cell.f = sys.maxsize

        for cell in available_cells:
            self.calc_g(maze, cell)
            self.calc_f(cell)

            if cell.f < target_cell.f:
                target_cell = cell
            # elif cell.f == target_cell.f:
            #   if cell.h < target_cell.h:
            #      target_cell = cell
                # kan vi hamna i fallet då f är lika och h är lika samtidigt?

        direction = helper.get_direction(current_cell, target_cell)

        print('Direction: ' + str(direction))
        return direction, target_cell    # 'N/S/W/E'

    def right_hand_rule(self, maze, robot):
        row = robot.current_pos_row
        print('Current position row = ' + str(row))
        col = robot.current_pos_col
        print('Current position col = ' + str(col))
        current_cell = maze.matrix[row][col]

        if row == maze.end_row and col == maze.end_col:
            return '0'

        helper = HelpFunctions()
        translator = Translation()
        print(str(current_cell.walls))
        walls = translator.change_wall_format(current_cell.walls, robot.current_direction, 'NSWE') # walls blir på ABLR
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
        direction = translator.change_direction_format(robot, direction, 'ABLR')
        robot.current_direction = direction
        print('New Direction: ' + direction)

        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        return direction

    def run_pathfinder(self, maze, robot):

        direction, target_cell = self.astar(maze, robot)

        if target_cell.visited:
            i = maze.shortest_path.index(target_cell)
            del maze.shortest_path[i:len(maze.shortest_path)]
            # hantera att cell är visited men inte med i listan

        cell = maze.matrix[target_cell.row][target_cell.col]
        cell.visited = True
        maze.shortest_path.append(cell)

        return direction





