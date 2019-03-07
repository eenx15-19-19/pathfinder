class HelpFunctions:

    def current_cell(self, maze):
        return maze.x, maze.y

    # lastDirection är sträng (NSWE), t.ex. N
    def update_current_cell(self, maze):
        if maze.current_direction == 'N':
            maze.y = maze.y + 1
        elif maze.current_direction == 'S':
            maze.y = maze.y - 1
        elif maze.current_direction == 'W':
            maze.x = maze.x - 1
        elif maze.current_direction == 'E':
            maze.x = maze.x + 1
        else:
            None

        # walls är sträng med 1:or och 0:or, current_direction är robotens riktning, finns i Maze
        # current_type är antingen 'RLAB' eller 'NSWE'
    def change_wall_format(self, walls, current_direction, current_type):
        new_walls = walls # + lite magi. Lägg till magi
        return new_walls

    def update_cell_in_maze(self, maze, cell):
        x = maze.current_pos_x
        y = maze.current_pos_y
        maze[x][y] = cell
