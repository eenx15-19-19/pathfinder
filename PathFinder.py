# -*- coding: utf-8 -*-
# Här kan vi lägga algoritmen och saker relaterade till den
import Maze
import Cell
import sys
from HelpFunctions import HelpFunctions
from Translation import Translation
import Node
from PathBuilder import PathBuilder
import queue as q
import CustomList
import time


class PathFinder:

    # måste räkna medan den går, inte säkert att den tagit raka vägen
    def set_g(self, robot, cell):
        cell.g = robot.g

    def calc_g(self, parent_node, child_node):
        child_node.cell.g = parent_node.cell.g + 1

    # manhattan heuristic (första vektornorm)
    # hur får man denna att ta hänsyn till väggar?
    def calc_h(self, maze, cell):
        cell.h = 1 * (abs(maze.end_row - cell.row) + abs(maze.end_col - cell.col))

    def calc_f(self, cell):
        cell.f = cell.g + cell.h

    def astar(self, maze, robot):  # Ska göras
        t0 = time.time()
        helper = HelpFunctions()

        current_cell = helper.current_cell(robot, maze)

        queue = q.Queue()
        end_nodes = CustomList.CustomList()
        current_node = Node.Node(current_cell)
        list_cells = []

        pb = PathBuilder()
        end_nodes = pb.path_builder(maze, robot, current_node, queue, end_nodes, list_cells, False)
        # print('end_nodes: ' + str(end_nodes))
        next_node = pb.find_best(end_nodes)

        direction = helper.get_direction(current_cell, next_node.cell)

        t1 = time.time()
        astar_time = t1 - t0
        print('A*-time = ' + str(astar_time))

        return direction, next_node.cell

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
        walls = translator.change_wall_format(current_cell.walls, robot.current_direction, 'NSWE')  # walls blir på ABLR
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
        direction = translator.change_direction_format(robot.current_direction, direction, 'ABLR')
        robot.current_direction = direction
        print('New Direction: ' + direction)

        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        return direction

    def run_pathfinder(self, maze, robot):

        direction, target_cell = self.astar(maze, robot)

        if target_cell.visited:
            # i = maze.shortest_path.index(target_cell)
            # del maze.shortest_path[i:len(maze.shortest_path)]
            robot.g = target_cell.g
            # hantera att cell är visited men inte med i listan

        cell = maze.matrix[target_cell.row][target_cell.col]
        cell.visited = True
        maze.matrix_robot[target_cell.row][target_cell.col] = cell
        robot.g = robot.g + 1
        self.set_g(robot, cell)

        maze.shortest_path.append(cell)
        #print('Current cell is: ' + str(maze.matrix[robot.current_pos_row][robot.current_pos_col]))
        #print('Current robot cell is: ' + str(maze.matrix_robot[robot.current_pos_row][robot.current_pos_col]))

        #print('Direction: ' + direction)
        return direction

    def goal_start(self, maze, robot):
        helper = HelpFunctions()
        translator = Translation()
        builder = PathBuilder()
        test_queue = q.Queue()
        end_nodes = CustomList.CustomList()
        list_cells = []
        end_cell = maze.matrix[robot.current_pos_row][robot.current_pos_col]
        end_node = Node.Node(end_cell)
        instruction_final = []
        direction_final = [robot.current_direction]

        end_nodes = builder.path_builder(maze, robot, end_node, test_queue, end_nodes, list_cells, True)

        start_cell = maze.matrix[maze.start_row][maze.start_col]
        goal_index = end_nodes.cell_search(start_cell)
        goal = end_nodes.custom_list[goal_index]

        path_list = builder.find_path(goal)
       # print(path_list)

        path_list.reverse()
       # print(path_list)
        instruction_final = self.path_to_instructions(robot, path_list, 'goal')

       # for i in range(len(path_list) - 1):
       #     current_cell = path_list[i]
       #     next_cell = path_list[i + 1]
       #     direction_final.append(helper.get_direction(current_cell, next_cell))
       #     robot_direction = direction_final[i]
       #     direction = direction_final[i + 1]
       #     direction = translator.change_direction_format(robot_direction, direction, 'NSWE')
       #     instruction_final.append(translator.change_instruction_format(direction))
        print(path_list)
        print('Goal to start: ')
        print(instruction_final)

        path_list.reverse()
        maze.shortest_path = path_list
        return instruction_final

    def path_to_instructions(self,robot, path_list, start_point):
        helper = HelpFunctions()
        translator = Translation()
        builder = PathBuilder()

        instruction_final = []

        direction_final = []
        if start_point == 'start':
            direction_final = ['N']
        elif start_point == 'goal':
            direction_final = [robot.current_direction]

        for i in range(len(path_list) - 1):
            current_cell = path_list[i]
            next_cell = path_list[i + 1]
            direction_final.append(helper.get_direction(current_cell, next_cell))
            robot_direction = direction_final[i]
            direction = direction_final[i + 1]
            direction = translator.change_direction_format(robot_direction, direction, 'NSWE')
            instruction_final.append(translator.change_instruction_format(direction))

        return instruction_final

    def path_reverse(self, path):
        new_path = []
        for direction in path:
            if direction == 'f-':
                new_path.append('bf')
            elif direction == 'bf':
                new_path.append('f-')
            elif direction == 'lf':
                new_path.append('rf')
            elif direction == 'rf':
                new_path.append('lf')
        return new_path
