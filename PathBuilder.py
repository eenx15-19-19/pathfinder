from typing import List, Any

import Node
from Translation import Translation
from HelpFunctions import HelpFunctions
import PathFinder
import queue as q
import CustomList

class PathBuilder:

    def path_builder(self, maze, robot, node: Node, queue: q.Queue, end_nodes: CustomList.CustomList, list_cells, end):

        #if node.cell not in list_cells:
        #    list_cells.append(node.cell)

     #  if node.cell.row == 15 and node.cell.col == 9:
     #       print('hej')

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
                direction = translator.change_direction_format(robot, helper.get_direction(
                    current_node.parent.cell, current_node.cell), 'NSWE')
            else:
                direction = 'None'  # måste ha något värde, spelar ingen roll vad
            fake_path = self.construct_fake_path(maze, robot, node)
            if maze.matrix_robot[maze.end_row][maze.end_col] not in fake_path and \
                    maze.matrix[maze.end_row][maze.end_col] not in fake_path:
                print('Dead end!')
            else:
            #path_list = []
            #current_node = node

            # lista från noden vi tittar på till där roboten står
            #for i in range(current_node.depth):
            #    current_node = current_node.parent
            #    path_list.append(current_node.cell)

            #manhattan_list1, manhattan_list2 = self.manhattan_list_gen(maze, node)

            #crossing_cells1 = list(set(path_list).intersection(manhattan_list1))
            #crossing_cells2 = list(set(path_list).intersection(manhattan_list2))

            # crossing_cells1 = False
            # crossing_cells2 = False

            #   for i in range(len(manhattan_list1)):
            #       if manhattan_list1[i].visited == True:
            #           crossing_cells1 = True

            #   for i in range(len(manhattan_list2)):
            #       if manhattan_list2[i].visited == True:
            #           crossing_cells2 = True

            #   if not crossing_cells1 or not crossing_cells2:
            #if len(crossing_cells1) == 0 or len(crossing_cells2) == 0:
                #print(path_list)

                node.fake_h = node.cell.h + node.depth
                node.fake_f = node.fake_h + node.cell.g

                # direction från dess förälder till sig
                # själv, dvs hur den behöver gå för att ta sig hit

                if direction == 'A':    # om den går rakt fram, lågt värde. Annars spelar det ingen roll?
                    node.direction_value = 0
                    maze.countA = maze.countA + 1

                else:
                    node.direction_value = 1
                    maze.countOther = maze.countOther + 1

             #   if node.cell.row == 15 and node.cell.col == 9:
             #       print('hej')
                end_nodes.add(node)     # knasar något så kolla om
                # depth ska adderas såhär på g

        if queue.empty():
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

    def construct_fake_path_old(self, maze, robot, node: Node.Node):
        current_node = node
        helper = HelpFunctions()
        pf = PathFinder.PathFinder()

        NSWE = 'N', 'S', 'W', 'E'

        fake_path = []
        explored_cells = []
        explored_quad = []

        row_diff = abs(maze.end_row-node.cell.row)
        col_diff = abs(maze.end_col-node.cell.col)
        while row_diff != 0 or col_diff != 0:
            fake_path.append(current_node.cell)
            explored_cells.append(current_node.cell)

            if current_node.cell.row - maze.end_row < 0:
                i_step = 1
            elif current_node.cell.row - maze.end_row > 0:
                i_step = -1
            else:
                i_step = 0

            if current_node.cell.col - maze.end_col < 0:
                j_step = 1
            elif current_node.cell.col - maze.end_col > 0:
                j_step = -1
            else:
                j_step = 0

            available_cells = []
            walls = current_node.cell.walls
            for i in range(len(walls)):
                wall = walls[i]

                if wall == '0':
                    direction = NSWE[i]
                    temp_cell = helper.get_adjacent_cell_robot(maze, current_node.cell, direction)
                    if not temp_cell.visited:
                        available_cells.append(temp_cell)

            change_made = False

            # måste ändra ordningen på vilken cell den försöker gå till först. Det beror på vilken kvadrant vi är i
            # om gränsen mellan två kvadranter, ta den vi inte kom från.
            # 1:a: i_step = 1, j_step = -1
            # 2:a: i_step = 1, j_step = 1
            # 3:e: i_step = -1, j_step = 1
            # 4:e: i_step = -1, j_step = -1
            temp_cell = maze.matrix_robot[current_node.cell.row + i_step][current_node.cell.col]
            if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                current_node = Node.Node(temp_cell)
                change_made = True
            else:
                temp_cell = maze.matrix_robot[current_node.cell.row][current_node.cell.col + j_step]
                if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                    current_node = Node.Node(temp_cell)
                    change_made = True
                else:
                    if 0 <= current_node.cell.row - i_step < 16:
                        temp_cell = maze.matrix_robot[current_node.cell.row - i_step][current_node.cell.col]
                        if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                            current_node = Node.Node(temp_cell)
                            change_made = True
                        else:
                            if 0 <= current_node.cell.col - j_step < 16:
                                temp_cell = maze.matrix_robot[current_node.cell.row][current_node.cell.col - j_step]
                                if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                                    current_node = Node.Node(temp_cell)
                                    change_made = True
                    else:
                        if 0 < current_node.cell.col - j_step < 16:
                            temp_cell = maze.matrix_robot[current_node.cell.row][current_node.cell.col - j_step]
                            if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                                current_node = Node.Node(temp_cell)
                                change_made = True

            if not change_made:

                if i_step == 0:
                    temp_pos_row = robot.current_pos_row
                    k = 0
                    while temp_pos_row == maze.end_row:
                        last_cell = maze.shortest_path[len(maze.shortest_path) - 1 - k]
                        temp_pos_row = last_cell.row
                        k = k + 1
                    if temp_pos_row > maze.end_row:
                        i_dir = -1
                    elif temp_pos_row < maze.end_row:
                        i_dir = 1
                    else:
                        i_dir = 0

                    temp_cell = maze.matrix_robot[current_node.cell.row + i_dir][current_node.cell.col]
                    if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                        current_node = Node.Node(temp_cell)
                        change_made = True
                    else:
                        temp_cell = maze.matrix_robot[current_node.cell.row - i_dir][current_node.cell.col]
                        if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                            current_node = Node.Node(temp_cell)
                            change_made = True

                elif j_step == 0:
                    temp_pos_col = robot.current_pos_col
                    k = 0
                    while temp_pos_col == maze.end_col:
                        last_cell = maze.shortest_path[len(maze.shortest_path) - 1 - k]
                        temp_pos_col = last_cell.col
                        k = k + 1
                    if temp_pos_col > maze.end_col:
                        j_dir = -1
                    elif temp_pos_col < maze.end_col:
                        j_dir = 1
                    else:
                        j_dir = 0

                    temp_cell = maze.matrix_robot[current_node.cell.row][current_node.cell.col + j_dir]
                    if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                        current_node = Node.Node(temp_cell)
                        change_made = True
                    else:
                        temp_cell = maze.matrix_robot[current_node.cell.row][current_node.cell.col - j_dir]
                        if not temp_cell.visited and temp_cell in available_cells and temp_cell not in explored_cells:
                            current_node = Node.Node(temp_cell)
                            change_made = True

            if not change_made:
                return fake_path

            row_diff = abs(maze.end_row-current_node.cell.row)
            col_diff = abs(maze.end_col-current_node.cell.col)

            if current_node.cell.row == maze.end_row and current_node.cell.col == maze.end_col:
                fake_path.append(current_node.cell)
                return fake_path

    def construct_fake_path(self, maze, robot, node):
        current_node = node
        helper = HelpFunctions()
        pf = PathFinder.PathFinder()

        NSWE = 'N', 'S', 'W', 'E'
        # Problem: Kollar bara en väg. Om t.ex. första valet leder till ingen väg måste övriga vägar också kollas.
        # Lista av listor i explored cells så vi sparar gamla queues? Måste göra en DFS. Återanvända mer från PB?
        fake_path = []
        explored_cells = []
        explored_quad = []
        node_queue = CustomList.CustomList()

        row_diff = abs(maze.end_row-node.cell.row)
        col_diff = abs(maze.end_col-node.cell.col)

        while not current_node.cell.row == maze.end_row or not current_node.cell.col == maze.end_col:
            #fake_path.append(maze.matrix_robot[current_node.cell.row][current_node.cell.col])
            explored_cells.append(maze.matrix_robot[current_node.cell.row][current_node.cell.col])

            if current_node.cell.row - maze.end_row < 0:
                i_step = 1
            elif current_node.cell.row - maze.end_row > 0:
                i_step = -1
            else:
                i_step = 0

            if current_node.cell.col - maze.end_col < 0:
                j_step = 1
            elif current_node.cell.col - maze.end_col > 0:
                j_step = -1
            else:
                j_step = 0

            available_cells = []
            walls = current_node.cell.walls
            for i in range(len(walls)):
                wall = walls[i]

                if wall == '0':
                    direction = NSWE[i]
                    temp_cell = helper.get_adjacent_cell_robot(maze, current_node.cell, direction)
                    if not temp_cell.visited:
                        available_cells.append(temp_cell)
                        if not temp_cell.visited and temp_cell not in explored_cells:
                            temp_node = Node.Node(temp_cell)
                            temp_node.parent = current_node
                            temp_node.depth = temp_node.parent.depth + 1

                            #for i in range(temp_current_node.depth - 1):
                            #    temp_current_node = temp_current_node.parent

                            translator = Translation()
                            direction = translator.change_direction_format(robot, helper.get_direction(
                                temp_node.parent.cell, temp_node.cell), 'NSWE')

                            if direction == 'A':  # om den går rakt fram, lågt värde. Annars spelar det ingen roll?
                                temp_node.direction_value = 0
                                maze.countA = maze.countA + 1

                            else:
                                temp_node.direction_value = 1
                                maze.countOther = maze.countOther + 1

                            pf.calc_h(maze, temp_node.cell)
                            temp_node.fake_h = temp_node.cell.h + temp_node.depth
                            temp_node.fake_f = temp_node.fake_h + temp_node.cell.g

                            node_queue.add(temp_node)

            if node_queue.empty():
                break
            current_node = node_queue.pop(0)
            #node_queue = CustomList.CustomList()

        fake_path.append(current_node.cell)
        for i in range(current_node.depth):
            current_node = current_node.parent
            fake_path.append(current_node.cell)

        #fake_path.append(current_node.cell)
        return fake_path