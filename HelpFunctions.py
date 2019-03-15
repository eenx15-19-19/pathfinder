class HelpFunctions:

    def current_cell(self, robot, maze):
        cell = maze.matrix[robot.current_pos_row][robot.current_pos_col]

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

    def get_adjacent_cell(self, maze, robot, direction):
        row = robot.current_pos_row
        col = robot.current_pos_col

        if direction == 'N':
            row = robot.current_pos_row - 1
        elif direction == 'S':
            row = robot.current_pos_row + 1
        elif direction == 'W':
            col = robot.current_pos_col - 1
        elif direction == 'E':
            col = robot.current_pos_col + 1
        else:
            None

        return maze.matrix[row][col]

    def get_direction(self, cell_start, cell_end):
        direction = ''
        if cell_end.row - cell_start.row < 0:
            direction = 'N'
        elif cell_end.row - cell_start.row > 0:
            direction = 'S'
        elif cell_end.col - cell_start.col < 0:
            direction = 'W'
        elif cell_end.col - cell_start.col > 0:
            direction = 'E'
        else:
            None
        return direction

    # tar en sträng walls (tex. '0000') och gör till en lista ['0', '0', '0', '0'}
    def split_walls(self, walls):
        walls_list = list(walls)
        return walls_list
