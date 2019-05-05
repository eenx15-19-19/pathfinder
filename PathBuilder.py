from typing import List, Any

import Node
from Translation import Translation
from HelpFunctions import HelpFunctions
import PathFinder
import queue as q
import CustomList

class PathBuilder:

    def path_builder(self, maze, robot, node: Node, queue: q.Queue, end_nodes: CustomList.CustomList, list_cells, end):

        helper = HelpFunctions()
        pf = PathFinder.PathFinder()

        available_cells = []
        NSWE = 'N', 'S', 'W', 'E'
        walls = node.cell.walls

        if node.cell.visited:
            for i in range(len(walls)):
                wall = walls[i]

                if wall == '0':
                    direction = NSWE[i]
                    temp_cell = helper.get_adjacent_cell(maze, node.cell, direction)
                    available_cells.append(temp_cell)

            for i in range(len(available_cells)):
                temp_node = Node.Node(available_cells[i])

                if temp_node.cell not in list_cells:
                    temp_node.parent = node
                    temp_node.depth = node.depth + 1
                    queue.put(temp_node)
                    list_cells.append(temp_node.cell)

        # om inte slutväg söks (end = false) läggs noden till i end_cells bara om den inte är besökt. Om vi söker
        # slutväg (end = true) läggs alla noder till i end_cells
        if (not end and not node.cell.visited) or end:
            pf.calc_h(maze, node.cell)

            # roten har inte en förälder, ställer till problem om end = true
            if node.parent:
                pf.calc_g(node.parent, node)

                current_node = node

                for i in range(current_node.depth - 1):
                    current_node = current_node.parent

                translator = Translation()
                direction = translator.change_direction_format(robot.current_direction, helper.get_direction(
                    current_node.parent.cell, current_node.cell), 'NSWE')
            else:
                direction = 'None'  # måste ha något värde, spelar ingen roll vad
            fake_path = self.construct_fake_path(maze, robot, node, end)

            goal = False
            outside_explored_area = False
            if (maze.matrix_robot[maze.end_row][maze.end_col] in fake_path or
                    maze.matrix[maze.end_row][maze.end_col] in fake_path):
                goal = True
            if fake_path[0].row < maze.explored_row and fake_path[0].col > maze.explored_col:
                outside_explored_area = True

            # med explored area: if not goal and not outside_explored_area:
            # utan: if maze.matrix_robot[maze.end_row][maze.end_col] not in fake_path and \
             #       maze.matrix[maze.end_row][maze.end_col] not in fake_path:
            #    print('Dead end!')
            if goal or outside_explored_area:
                node.fake_h = node.cell.h + node.depth
                node.fake_f = node.fake_h + node.cell.g

                # direction från dess förälder till sig
                # själv, dvs hur den behöver gå för att ta sig hit

                if direction == 'A':    # om den går rakt fram, lågt värde. Annars spelar det ingen roll?
                    node.direction_value = 0

                else:
                    node.direction_value = 1

                end_nodes.add(node)     # knasar något så kolla om
                # depth ska adderas såhär på g

        if queue.empty():
           # print('Maze.count_unvisited: ' + str(maze.count_unvisited))
            #maze.count_unvisited = 0
           # print('Maze.count_pb: ' + str(maze.count_pb))
            #maze.count_pb = 0
            return end_nodes
        else:
            next_node = queue.get()
            return self.path_builder(maze, robot, next_node, queue, end_nodes, list_cells, end)

    def find_best(self, end_nodes):

        best_node = end_nodes.get_first()

        for i in range(best_node.depth - 1):
            best_node = best_node.parent

        return best_node

    def find_path(self, end_node):

        prev_node = end_node

        path_list = []

        for i in range(prev_node.depth + 1):
            path_list.append(prev_node.cell)
            prev_node = prev_node.parent

        return path_list

    def manhattan_list_gen(self, maze, end_node: Node.Node):
        manhattan_list = []
        list_list1 = []
        list_list2 = []
        if end_node.cell.row - maze.end_row < 0:
            i_step = 1
        else:
            i_step = -1

        if end_node.cell.col - maze.end_col < 0:
            j_step = 1
        else:
            j_step = -1

        for i in range(end_node.cell.row, maze.end_row+i_step, i_step):
            list_list1.append(maze.matrix[i][end_node.cell.col])
            list_list2.append(maze.matrix[i][maze.end_col])

        for j in range(end_node.cell.col, maze.end_col + j_step, j_step):
            list_list2.append(maze.matrix[end_node.cell.row][j])
            list_list1.append(maze.matrix[maze.end_row][j])

        manhattan_list.append(list_list1)
        manhattan_list.append(list_list2)
        return list_list1, list_list2

    def construct_fake_path(self, maze, robot, node, end):
        current_node = node
        helper = HelpFunctions()
        pf = PathFinder.PathFinder()
        NSWE = 'N', 'S', 'W', 'E'

        fake_path = []
        explored_cells = []
        node_queue = CustomList.CustomList()
        continue_search = True

        # med explored area ska detta ansvändas
        if current_node.cell.row == maze.end_row and current_node.cell.col == maze.end_col:
            continue_search = False
        elif current_node.cell.row < maze.explored_row and current_node.cell.col > maze.explored_col:
            continue_search = False

        explored_cells.append(maze.matrix_robot[current_node.cell.row][current_node.cell.col])

        #med explored area ska detta användas
        while continue_search:

        # utan explored area ska detta användas
        #while not current_node.cell.row == maze.end_row or not current_node.cell.col == maze.end_col:

            #maze.count_fake = maze.count_fake + 1

            #if maze.count_fake == 200:
            #    print('So much fake')

            walls = current_node.cell.walls
            for i in range(len(walls)):
                wall = walls[i]

                if wall == '0':
                    direction = NSWE[i]
                    temp_cell = helper.get_adjacent_cell_robot(maze, current_node.cell, direction)
                    add = True
                    if end:
                        visited = False
                        if temp_cell.visited:
                            visited = True

                        if visited:
                            for j in range(len(explored_cells)):
                                if explored_cells[j].row == temp_cell.row and explored_cells[j].col == temp_cell.col:
                                    add = False
                                    break
                                else:
                                    add = True

                        else:
                            add = False
                        #if not temp_cell not in explored_cells:
                        #    add = True
                    else:
                        visited = False
                        if temp_cell.visited:
                            visited = True

                        explored = False

                        if not visited:
                            for k in range(len(explored_cells)):
                                if explored_cells[k].row == temp_cell.row and explored_cells[k].col == temp_cell.col:
                                    explored = True
                                    break
                                else:
                                    explored = False

                        if not explored and not visited:
                            add = True
                        else:
                            add = False

                       # if not temp_cell.visited:
                       #     for k in range(len(explored_cells)):
                       #         if explored_cells[k].row == temp_cell.row and explored_cells[k].col == temp_cell.col:
                       #             add = False
                       # else:
                       #     add = False
                       # if not temp_cell.visited and temp_cell not in explored_cells:
                       #     add = True
                    if add:
                        temp_node = Node.Node(temp_cell)
                        temp_node.parent = current_node
                        temp_node.depth = temp_node.parent.depth + 1

                        translator = Translation()
                        direction = translator.change_direction_format(robot, helper.get_direction(
                                temp_node.parent.cell, temp_node.cell), 'NSWE')

                        if direction == 'A':  # om den går rakt fram, lågt värde. Annars spelar det ingen roll?
                            temp_node.direction_value = 0

                        else:
                            temp_node.direction_value = 1

                        pf.calc_h(maze, temp_node.cell)
                        temp_node.fake_h = temp_node.cell.h + temp_node.depth
                        temp_node.fake_f = temp_node.fake_h + temp_node.cell.g

                        explored_cells.append(maze.matrix_robot[temp_node.cell.row][temp_node.cell.col])
                        node_queue.add(temp_node)

            if node_queue.empty():
                break
            current_node = node_queue.pop_queue(0)

            # med explored area ska dessa loopar användas
            if current_node.cell.row == maze.end_row and current_node.cell.col == maze.end_col:
                continue_search = False
            elif current_node.cell.row < maze.explored_row and current_node.cell.col > maze.explored_col:
                continue_search = False

        fake_path.append(current_node.cell)
        for i in range(current_node.depth):
            current_node = current_node.parent
            fake_path.append(current_node.cell)

        #print('Maze.count_fake: ' + str(maze.count_fake))
        #maze.count_fake = 0
        return fake_path

