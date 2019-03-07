# Här kan vi lägga algoritmen och saker relaterade till den
import Maze
import Cell


class Pathfinder:

    def calc_g(self, maze, x, y):
        cell = maze[x][y]
        cell.g = abs(x - maze.start_x) + abs(y - maze.start_y)   # tror detta stämmer?

    # manhattan heuristic (första vektornorm)
    def calc_h(self, maze, x ,y):
        cell = maze[x][y]
        cell.h = abs(maze.end_x - x) + abs(maze.end_y - y)

    def calc_f(self, maze, x, y):
        cell = maze[x][y]
        cell.f = cell.g + cell.h

    def astar(self, maze):
        direction = None
        return direction    # 'N/S/W/E'

    def right_hand_rule(self, maze):
        direction = None
        return direction

