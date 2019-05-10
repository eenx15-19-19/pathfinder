# -*- coding: utf-8 -*-
import serial
import Robot
from PathFinder import PathFinder
import Maze
from Main import Main
import io
import time
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=10.0

)

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
        elif run_instruction == b'fas3\n':
            run_instruction = fas3(maze, robot)
        else:
            run_instruction = None


def fas1(sLast, maze, robot):
    while not maze.win:

        print("--------------------- NEW CELL -------------------------")
        cell = ser.readline()
        print("Cell before: " + str(cell))
        cell = cell.decode("utf-8")


       # if cell == b'e':
        #    print(" ------------    ERROR fas1() -----------")
            # return None
        #while sLast == b+cell[0]:#Check if package is replica of the one before.
         #   print("wrong package")
          #  cell=ser.readline()
       # sLast = cell[0]
        cell = cell[1:-1]   #remove the sequence numberi
        print("Cell 4 bytes: " + cell)
        if len(cell) == 4:
            print("Length is 4")
            ok = True
            for character in cell:
                print("Character: " + character)
                if character != '0' and character != '1':
                    ok = False
                    break
            if ok:
                #print("Cell type:")
                #print(type(cell))
                print("Cell updated :" + cell)
                print('Current cell is: ' + str(maze.matrix[robot.current_pos_row][robot.current_pos_col]))
                main_class = Main()
                direction = main_class.run(maze, robot, cell)

                print('Target cell: ' + str(maze.matrix[robot.current_pos_row][robot.current_pos_col]))
                #print("Sending command before: " + direction)
                direction = direction.encode('utf-8')
                #print("Sending command after: " + str(direction))
                #print(type(direction))
                #time.sleep(5)
                time.sleep(1) #Just for easier debugging
                ser.write(direction)
                ser.write(b'\n')

                if robot.current_pos_row == maze.end_row and robot.current_pos_col == maze.end_col:
                    maze.win = True
                    ser.readline()  # kan orsaka fel, kanske behöver kolla vad den läst

                    ser.write(b's\n')

                    return 'fas2'

def fas2(maze, robot):
    finder = PathFinder()

    directions = finder.goal_start(maze, robot) #Big packages with all instructions for solving the labyrinth
    directions = ''.join(directions)
    time.sleep(1)   # sleep pga båda byter till fas2 samtidigt, bra att vänta

    ser.write(directions.encode("utf-8"))
    ser.write(b'\n')

    return None

def fas3(maze, robot):
    finder = PathFinder()

    #temp_directions = finder.goal_start(maze, robot)  # Big packages with all instructions for solving the labyrinth
    directions = finder.path_to_instructions(robot, maze.shortest_path, 'start')
    print(directions)
    directions = ''.join(directions)

    ser.write(directions.encode("utf-8"))
    ser.write(b'\n')

    return None


main()
