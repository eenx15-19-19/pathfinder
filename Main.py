import Cell
import Maze
from PathFinder import PathFinder
from HelpFunctions import HelpFunctions
import RobotContact
import pprint


class Main:

    helper = HelpFunctions()
    maze = Maze.Maze(3, 2)

    maze.matrix[0][0].walls = helper.split_walls('1110')
    maze.matrix[0][1].walls = helper.split_walls('0001')
    maze.matrix[1][0].walls = helper.split_walls('1010')
    maze.matrix[1][1].walls = helper.split_walls('0001')
    maze.matrix[2][0].walls = helper.split_walls('0011')
    maze.matrix[2][1].walls = helper.split_walls('0111')

    for i in range(len(maze.matrix)):
        print(*maze.matrix[i])

    finder = PathFinder()
    matrix = maze.matrix
    rows = maze.rows
    cols = maze.cols

    for i in range(rows):
        for j in range(cols):
            finder.calc_g(maze, i, j)
            finder.calc_h(maze, i, j)
            finder.calc_f(maze, i, j)

    # startruta
    finder.right_hand_rule(maze)
