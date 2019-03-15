import Cell
import Maze
from PathFinder import PathFinder
from HelpFunctions import HelpFunctions
from Translation import Translation
import Robot
import RobotContact
from Translation import Translation
import pprint   # pprint.pprint(matrix) ger fin print


class Main(object):

    helper = HelpFunctions()

    def sim_pi(self):
        # Initiera maze och robot
        # Vill loopa och anropa run_sim
        print('hej')

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

        instruction = translator.change_direction_format(robot, direction, 'NSWE')
        return instruction  # Returnera instruktion

    def run(self, maze, robot, sensor_data):    # Vill ha data från sensorer
        # Från robot: få information om väggar
        # Uppdatera cell.wall i maze

        finder = PathFinder()
        translator = Translation()
        helper = HelpFunctions()

        direction = finder.run_pathfinder(maze, robot) #NSWE

        # Uppdatera robot
        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        instruction = translator.change_direction_format(robot, direction, 'NSWE')
        return instruction # Returnera instruktion

    maze = Maze.Maze(3, 2)



    # 3x2
    maze.matrix[0][0].walls = helper.split_walls('1110')
    maze.matrix[0][1].walls = helper.split_walls('0001')
    maze.matrix[1][0].walls = helper.split_walls('1010')
    maze.matrix[1][1].walls = helper.split_walls('0001')
    maze.matrix[2][0].walls = helper.split_walls('0011')
    maze.matrix[2][1].walls = helper.split_walls('0111')

    # 3x4
    # maze.matrix[0][0].walls = helper.split_walls('1011')
    # maze.matrix[0][1].walls = helper.split_walls('1010')
    # maze.matrix[0][2].walls = helper.split_walls('1100')
    # maze.matrix[0][3].walls = helper.split_walls('1001')
    # maze.matrix[1][0].walls = helper.split_walls('0011')
    # maze.matrix[1][1].walls = helper.split_walls('0011')
    # maze.matrix[1][2].walls = helper.split_walls('1010')
    # maze.matrix[1][3].walls = helper.split_walls('0001')
    # maze.matrix[2][0].walls = helper.split_walls('0110')
    # maze.matrix[2][1].walls = helper.split_walls('0101')
    # maze.matrix[2][2].walls = helper.split_walls('0111')
    # maze.matrix[2][3].walls = helper.split_walls('0111')

    for i in range(len(maze.matrix)):
        print(*maze.matrix[i])

    finder = PathFinder()
    matrix = maze.matrix
    rows = maze.rows
    cols = maze.cols
    matrix_f = maze.matrix_f
    robot = Robot.Robot(maze)

    for i in range(rows):
        for j in range(cols):
            finder.calc_g(maze, i, j)
            finder.calc_h(maze, i, j)
            f = finder.calc_f(maze, i, j)
            matrix_f[i][j] = f

    for i in range(len(matrix_f)):
        print(*matrix_f[i])

    direction = ''
    while direction != '0':
        direction = finder.right_hand_rule(maze, robot)

    if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
        print('Maze solved!')

    test_list = ['1', '2', '3', '4']
    del test_list[2:len(test_list)]
    print(test_list)
