import Node
import Translation as translator
from HelpFunctions import HelpFunctions
from PathFinder import PathFinder
import queue as q


class PathBuilder:

    def path_builder(self, maze, node: Node, queue: q, end_nodes, list_cells):
        list_cells.append(node.cell)

        helper = HelpFunctions()
        pf = PathFinder()

        available_cells = []
        NSWE = 'N', 'S', 'W', 'E'
        ABLR = 'A', 'B', 'L', 'R'
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

        else:
            pf.calc_h(maze, node.cell)
            end_nodes.append(node)

        if not queue:
            return self.find_best()

        next_node = queue.get()
        self.path_builder(maze, next_node, queue, end_nodes, list_cells)

    def find_best(self):
        None