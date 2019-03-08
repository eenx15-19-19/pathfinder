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
            
        #tar en sträng walls (tex. '0000') och gör till en lista ['0', '0', '0', '0'}
    def split_walls(self, walls):
        walls_list = list(walls)
        return walls_list

        # walls är sträng med 1:or och 0:or, current_direction är robotens riktning, finns i Maze
        # current_type är antingen 'ABLR' eller 'NSWE'
        # skriv om den här snyggare!
    def change_wall_format(self, walls, current_direction, current_type):
        # börja med NSWE till ABRL
        new_walls = ['', '', '', '']
        # peka norr. N = A, S = B, W = L, E = R
        if current_type == 'NSWE':
            if current_direction == 'N':
                new_walls[0] = walls[0]
                new_walls[1] = walls[1]
                new_walls[2] = walls[2]
                new_walls[3] = walls[3]

            # peka syd. N = B, S = A, W = R, E = L
            elif current_direction == 'S':
                new_walls[0] = walls[1]
                new_walls[1] = walls[0]
                new_walls[2] = walls[3]
                new_walls[3] = walls[2]

            # peka väst. N = R, S = L, W = A, E = B
            elif current_direction == 'W':
                new_walls[0] = walls[2]
                new_walls[1] = walls[3]
                new_walls[2] = walls[1]
                new_walls[3] = walls[0]

            # peka öst. N = L, S = R, W = B, E = A
            elif current_direction == 'E':
                new_walls[0] = walls[3]
                new_walls[1] = walls[2]
                new_walls[2] = walls[0]
                new_walls[3] = walls[1]

            else:
                print('Direction error')

        elif current_type == 'ABLR':
            print('Cannot handle format "ABLR" atm')

        else:
            print('Format is wrong')

        return new_walls

    def update_cell_in_maze(self, maze, cell):
        x = maze.current_pos_x
        y = maze.current_pos_y
        maze[x][y] = cell
