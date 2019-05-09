# -*- coding: utf-8 -*-
#from typing import List, Union

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
import time

class Main:

    def pi_pi(self):
        finder = PathFinder()
        builder = PathBuilder.PathBuilder()
        helper = HelpFunctions()
        # Initiera maze och robot
        maze = Maze.Maze(16, 16)
        for i in range(maze.rows):
            for j in range(maze.cols):
                finder.calc_h(maze, maze.matrix[i][j])

        robot = Robot.Robot(maze)
        sensor_data = maze.matrix[15][0].walls
        win = False
        while not win:
            instruction = self.run(maze, robot, sensor_data)  # Används ej nu. Skickas annars till microkontroller

            # Skicka instruktion till microkontroller
            # sensor_data = skickametod(instruction)

            # Kontrollera om vi är framme
            if (robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col):
                win = True

        # Letar väg från aktuell position till start
        instructions = finder.goal_start(maze, robot)
        # Send instructions to robot
        # ...

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Innan fas 2 måste roboten vända 180 grader för att vara redo för 'A'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Fas 2
        instructions_2 = finder.path_reverse(instructions)
        # Send instructions_2 to robot
        # ...

    def sim_pi(self):
        t0 = time.time()
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
        t0 = time.time()
        # Letar väg från aktuell position till start
        instructions = finder.goal_start(maze, robot)
        # Send instructions to robot
        # ...
        t1 = time.time()
        calc_time = t1-t0
        print('calc_time' + str(calc_time))

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Innan fas 2 måste roboten vända 180 grader för att vara redo för 'A'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        # Fas 2
        t0 = time.time()
        instructions_2 = finder.path_to_instructions(robot, maze.shortest_path, 'start')
        t1 = time.time()
        inst_time = t1 - t0
        print('inst_time: ' + str(inst_time))
        print(maze.shortest_path)
        #instructions_2 = finder.path_reverse(instructions)
        # Send instructions_2 to robot
        # ...
        print(instructions_2)
        #print(instructions_2)
        print('Kortaste vägen med pb är: ' + str(len(instructions)) + ' antal steg.')

        if win:
            print('Enkelt')
            t1 = time.time()
            total_time = t1 - t0
            print('Total time: ' + str(total_time))

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

        if robot.current_pos_row < maze.explored_row:
            maze.explored_row = robot.current_pos_row
        if robot.current_pos_col > maze.explored_col:
            maze.explored_col = robot.current_pos_col

        maze.path.append(helper.current_cell(robot, maze))

        print('Current cell: ' + '[' + str(robot.current_pos_row) + '][' + str(robot.current_pos_col) + ']' )
        instruction = translator.change_direction_format(robot.current_direction, direction, 'NSWE')

        return instruction  # Returnera instruktion

    def run(self, maze, robot, sensor_data):    # Vill ha data från sensorer

        finder = PathFinder()
        translator = Translation()
        helper = HelpFunctions()

        # Från robot: få information om väggar
        current_walls = sensor_data
        # Uppdatera cell.wall i maze
        maze.matrix[robot.current_pos_row][robot.current_pos_col].walls =\
            translator.change_wall_format(current_walls, robot.current_direction, 'ABLR')

        direction = finder.run_pathfinder(maze, robot)      # NSWE

        # Uppdatera robot
        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        instruction = translator.change_direction_format(robot.current_direction, direction, 'NSWE')

        instruction = translator.change_instruction_format(instruction)

        return instruction # Returnera instruktion


main = Main()
main.sim_pi()
