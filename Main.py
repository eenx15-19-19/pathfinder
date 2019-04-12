from typing import List, Union

import Cell
import Maze
from PathFinder import PathFinder
from HelpFunctions import HelpFunctions
from Translation import Translation
import Robot
import RobotContact
from Translation import Translation
import pprint   # pprint.pprint(matrix) ger fin print
import PathBuilder
import Node
import queue
import CustomList

class Main:

    def sim_pi(self):

        finder = PathFinder()
        # Initiera maze och robot

        maze = Maze.Maze(16, 16)
        for i in range(maze.rows):
            for j in range(maze.cols):
                finder.calc_h(maze, maze.matrix[i][j])

        robot = Robot.Robot(maze)

        print(maze.matrix[maze.end_row][maze.end_col])
                                        # Endast för simulering början
        helper = HelpFunctions()

        # 3x2
        # maze.matrix[0][0].walls = helper.split_walls('1110')
        # maze.matrix[0][1].walls = helper.split_walls('1001')
        # maze.matrix[1][0].walls = helper.split_walls('1010')
        # maze.matrix[1][1].walls = helper.split_walls('0001')
        # maze.matrix[2][0].walls = helper.split_walls('0111')
        # maze.matrix[2][1].walls = helper.split_walls('0111')

        # 3x4
       # maze.matrix[0][0].walls = helper.split_walls('1011')
       # maze.matrix[0][1].walls = helper.split_walls('1010')
       # maze.matrix[0][2].walls = helper.split_walls('1100')
       # maze.matrix[0][3].walls = helper.split_walls('1001')
       # maze.matrix[1][0].walls = helper.split_walls('0011')
        #maze.matrix[1][1].walls = helper.split_walls('0011')
        #maze.matrix[1][2].walls = helper.split_walls('1010')
        #maze.matrix[1][3].walls = helper.split_walls('0001')
        #maze.matrix[2][0].walls = helper.split_walls('0110')
        #maze.matrix[2][1].walls = helper.split_walls('0101')
        #maze.matrix[2][2].walls = helper.split_walls('0111')
        #maze.matrix[2][3].walls = helper.split_walls('0111')

      #  for i in range(len(maze.matrix)):
      #      print(*maze.matrix[i])
                                        # Endast för simulering slut

        # Vill loopa och anropa run_sim
        win = False

        length = 0  # debug
        while not win:
            instruction = self.run_sim(maze, robot)     # Används ej nu. Skickas annars till microkontroller

            # för debuggning
            length = length + 1
            print('Steg tagna: ' + str(length))
            if length == 16:
                print('nu börjar kaos')
            # slut på för debuggning

            # Skicka instruktion till microkontroller

            # Kontrollera om vi är framme

            if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
                win = True

        # Letar väg från aktuell position till start
        builder = PathBuilder.PathBuilder()
        test_queue = queue.Queue()
        end_nodes = CustomList.CustomList()
        list_cells = []
        end_cell: Cell.Cell = maze.matrix[robot.current_pos_row][robot.current_pos_col]
        end_node = Node.Node(end_cell)

        end_nodes = builder.path_builder(maze, robot, end_node, test_queue, end_nodes, list_cells, True)

        start_cell = maze.matrix[maze.start_row][maze.start_col]
        goal_index = end_nodes.cell_search(start_cell)

        goal = end_nodes.custom_list[goal_index]

        path_list = builder.find_path(goal)
        path_list.reverse()

        print(path_list)
        print('Kortaste vägen med pb är: ' + str(len(path_list)) + ' antal steg.')

        if win:
            print('Enkelt')

        else:
            print('Svårt')

    def run_sim(self, maze, robot):
        # (Görs ej i sim) Från robot: få information om väggar
        # (Görs ej i sim) Uppdatera cell.wall i maze

        finder = PathFinder()
        translator = Translation()
        helper = HelpFunctions()

        direction = finder.run_pathfinder(maze, robot)  # NSWE

        # Uppdatera robot
        robot.current_direction = direction
        helper.update_current_cell(maze, robot)
        maze.path.append(helper.current_cell(robot, maze))

        print('Current cell: ' + '[' + str(robot.current_pos_row) + '][' + str(robot.current_pos_col) + ']' )
        instruction = translator.change_direction_format(robot, direction, 'NSWE')

        return instruction # Returnera instruktion

    def run(self, maze, robot, sensor_data):    # Vill ha data från sensorer
        # Från robot: få information om väggar
        # Uppdatera cell.wall i maze

        finder = PathFinder()
        translator = Translation()
        helper = HelpFunctions()

        direction = finder.run_pathfinder(maze, robot)      # NSWE

        # Uppdatera robot
        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        instruction = translator.change_direction_format(robot, direction, 'NSWE')
        return instruction # Returnera instruktion


main = Main()
main.sim_pi()
