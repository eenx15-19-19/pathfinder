# -*- coding: utf-8 -*-
import serial
import io
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5

)
import Robot
from PathFinder import PathFinder
import Maze
from Main import Main

def main():
    print("Running Main!")
    finder = PathFinder()

    run_instruction = None

    maze = None
    robot = None
    
    while run_instruction == None: 
        run_instruction = ser.readline()
        print("Run Instruction: " + str(run_instruction))
        if run_instruction == b'fas1\n':
            print("--------- FAS1 ----------")
            sLast=0

            # Initiera maze och robot
            maze = Maze.Maze(13, 6)
            for i in range(maze.rows):
                for j in range(maze.cols):
                    finder.calc_h(maze, maze.matrix[i][j])

            robot = Robot.Robot(maze)

            run_instruction=fas1(sLast, maze, robot)

            if run_instruction == 'fas2':
                run_instruction = fas2(maze, robot)
        elif run_instruction == 'fas3':
            run_instruction = fas3(maze, robot)
        else:
            run_instruction = None


def fas1(sLast, maze, robot):
    while not maze.win:
        cell=ser.readline()
        print("Cell: " + str(cell))
        if cell == b'e':
            print(" ------------    ERROR fas1() -----------")
            # return None
        #while sLast == b+cell[0]:#Check if package is replica of the one before.
         #   print("wrong package")
          #  cell=ser.readline()
        #sLast = cell[0]
        cell = cell[1:]   #remove the sequence number
        print(" ------------------ CELL IS OF TYPE ------------")
        print(type(cell))
        print(type(str(cell)))
        main_class = Main()
        direction = main_class.run(maze, robot, cell)
        print("Sending command: " + direction)
        ser.write(direction)

        if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
            maze.win = True
            ser.write('s')
            return 'fas2'

def fas2(maze, robot):
    finder = PathFinder()

    directions = finder.goal_start(maze, robot) #Big packages with all instructions for solving the labyrinth
    directions = ''.join(directions)

    ser.write(directions)

    return None

def fas3(maze, robot):
    finder = PathFinder()

    #temp_directions = finder.goal_start(maze, robot)  # Big packages with all instructions for solving the labyrinth
    directions = finder.path_to_instructions(robot, maze.shortest_path, 'start')
    directions = ''.join(directions)

    ser.write(directions)

    return None


main()
