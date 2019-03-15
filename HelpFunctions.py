class HelpFunctions:

    def current_cell(self, robot, maze):
        cell = maze.matrix[robot.current_pos_row, robot.current_pos_col]

        if robot.current_pos_col < 0 or robot.current_pos_row < 0 or robot.current_pos_col > maze.cols-1 or \
                robot.current_pos_row > maze.rows-1:
            print('Indexes out of range, robot has escaped')

        return cell

    # current_direction är sträng (NSWE), t.ex. N
    def update_current_cell(self, maze, robot):
        if robot.current_direction == 'N':
            robot.current_pos_row = robot.current_pos_row - 1
        elif robot.current_direction == 'S':
            robot.current_pos_row = robot.current_pos_row + 1
        elif robot.current_direction == 'W':
            robot.current_pos_col = robot.current_pos_col - 1
        elif robot.current_direction == 'E':
            robot.current_pos_col = robot.current_pos_col + 1
        else:
            None

        if robot.current_pos_col < 0 or robot.current_pos_row < 0 or robot.current_pos_col > maze.cols-1 or \
                robot.current_pos_row > maze.rows-1:
            print('Indexes out of range, robot has escaped')

        # tar en sträng walls (tex. '0000') och gör till en lista ['0', '0', '0', '0'}
    def split_walls(self, walls):
        walls_list = list(walls)
        return walls_list

