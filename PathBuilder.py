import Node
import Translation as translator
from HelpFunctions import HelpFunctions
from PathFinder import PathFinder
import queue as q


class PathBuilder:

    def path_builder(self, maze, node: Node, queue: q.Queue, end_nodes: q.PriorityQueue, list_cells):
        list_cells.append(node.cell)

        helper = HelpFunctions()
        pf = PathFinder()

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

        else:
            pf.calc_h(maze, node.cell)
            pf.calc_g(node.parent, node)
            node.fake_f = node.cell.h + node.depth + node.cell.g
            end_nodes.put(node)     # knasar något så kolla om
            # depth ska adderas såhär på g

        if not queue:
            return self.find_best(end_nodes)

        next_node = queue.get()
        self.path_builder(maze, next_node, queue, end_nodes, list_cells)

    def find_best(self, end_nodes):

        best_node = end_nodes.get()

        for i in range(best_node.depth - 1):
            best_node = best_node.parent

        return best_node

