import Node
from Translation import Translation
from HelpFunctions import HelpFunctions
import PathFinder
import queue as q
import CustomList

class PathBuilder:

    def path_builder(self, maze, robot, node: Node, queue: q.Queue, end_nodes: CustomList.CustomList, list_cells, end):

        if node.cell.row == 13 and node.cell.col == 6:
            print('hej')

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
                    current_node.cell, current_node.parent.cell), 'NSWE')
            else:
                direction = 'None'  # måste ha något värde, spelar ingen roll vad

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

    def manhattan_list_gen(self, maze, cell, end_node: Node.Node):
        manhattan_list = []
        for i in range(end_node.cell.row, maze.end_row):
            for j in range(end_node.cell.col, maze.end_col):
                if not end_node.cell.row < i < maze.end_row:
                    if not end_node.cell.col < j < maze.end_col:
                        manhattan_list.append(cell[i][j])
        return manhattan_list
