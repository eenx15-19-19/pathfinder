import serial
ser = serial.Serial(
    port='/dev/ttys0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,

)
import Robot
from PathFinder import PathFinder
import Maze
from Main import Main

def main():
    finder = PathFinder()

    run_instruction = None

    maze = Maze.Maze(16, 16)
    robot = Robot.Robot(maze)

    while run_instruction.equals(None):
        run_instruction = ser.read()

        if run_instruction=='fas1':
            sLast=1

            # Initiera maze och robot
            maze = Maze.Maze(16, 16)
            for i in range(maze.rows):
                for j in range(maze.cols):
                    finder.calc_h(maze, maze.matrix[i][j])

            robot = Robot.Robot(maze)

            run_instruction=fas1(sLast, maze, robot)

            if run_instruction == 'fas2':
                run_instruction = fas2(maze, robot)

        if run_instruction == 'fas3':
            run_instruction = fas3(maze, robot)


def fas1(sLast, maze, robot):
    while not maze.win:
        cell=ser.read()
        if cell == 'abort':
            return None
        while sLast == cell[0]: #Check if package is replica of the one before.
            ser.write('wrong package')
            cell=ser.read()
        sLast = cell[0]
        cell = cell[1:]   #remove the sequence number

        main_class = Main()
        direction = main_class.run(maze, robot, cell)

        ser.write(direction)

        if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
            maze.win = True
            ser.write('fas2')
            return 'fas2'

def fas2(maze, robot):
    finder = PathFinder()

    directions = finder.goal_start(maze, robot) #Big packages with all instructions for solving the labyrinth
    directions = ''.join(directions)

    ser.write(directions)
    ser.write('b')

    return None

def fas3(maze, robot):
    finder = PathFinder()

    temp_directions = finder.goal_start(maze, robot)  # Big packages with all instructions for solving the labyrinth
    directions = finder.path_reverse(temp_directions)
    directions = ''.join(directions)

    ser.write(directions)
    ser.write('done')

    return None


