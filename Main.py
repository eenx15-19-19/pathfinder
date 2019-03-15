import Cell
import Maze
from PathFinder import PathFinder
from HelpFunctions import HelpFunctions
from Translation import Translation
import Robot
import RobotContact
from Translation import Translation
import pprint   # pprint.pprint(matrix) ger fin print


class Main:

    def sim_pi(self):

        finder = PathFinder()
        # Initiera maze och robot
        maze = Maze.Maze(3, 4)
        for i in range(maze.rows):
            for j in range(maze.cols):
                finder.calc_h(maze, maze.matrix[i][j])

        robot = Robot.Robot(maze)

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
        maze.matrix[0][0].walls = helper.split_walls('1011')
        maze.matrix[0][1].walls = helper.split_walls('1010')
        maze.matrix[0][2].walls = helper.split_walls('1100')
        maze.matrix[0][3].walls = helper.split_walls('1001')
        maze.matrix[1][0].walls = helper.split_walls('0011')
        maze.matrix[1][1].walls = helper.split_walls('0011')
        maze.matrix[1][2].walls = helper.split_walls('1010')
        maze.matrix[1][3].walls = helper.split_walls('0001')
        maze.matrix[2][0].walls = helper.split_walls('0110')
        maze.matrix[2][1].walls = helper.split_walls('0101')
        maze.matrix[2][2].walls = helper.split_walls('0111')
        maze.matrix[2][3].walls = helper.split_walls('0111')

        for i in range(len(maze.matrix)):
            print(*maze.matrix[i])
                                        # Endast för simulering slut

        # Vill loopa och anropa run_sim
        win = False

        while not win:
            instruction = self.run_sim(maze, robot)     # Används ej nu. Skickas annars till microkontroller

            # Skicka instruktion till microkontroller

            # Kontrollera om vi är framme

            if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
                win = True

        if win:
            print('Enkelt')

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

        print('Current cell: ' + '[' + str(robot.current_pos_row) + '][' + str(robot.current_pos_col) + ']' )
        instruction = translator.change_direction_format(robot, direction, 'NSWE')

        return instruction # Returnera instruktion

    def run(self, maze, robot, sensor_data):    # Vill ha data från sensorer
        # Från robot: få information om väggar
        # Uppdatera cell.wall i maze

        finder = PathFinder()
        translator = Translation()
        helper = HelpFunctions()

        direction = finder.run_pathfinder(maze, robot)      # NSWE

        # Uppdatera robot
        robot.current_direction = direction
        helper.update_current_cell(maze, robot)

        instruction = translator.change_direction_format(robot, direction, 'NSWE')
        return instruction # Returnera instruktion


main = Main()
main.sim_pi()
