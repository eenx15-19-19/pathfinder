class Translation:
    # walls är sträng med 1:or och 0:or, current_direction är robotens riktning, finns i Robot
    # current_type är antingen 'ABLR' eller 'NSWE'
    # skriv om den här snyggare!
    def change_wall_format(self, walls, current_direction, current_type):
        # börja med NSWE till ABLR
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
            # print('Cannot handle format "ABLR" atm')

            if current_direction == 'N':
                new_walls[0] = walls[0]
                new_walls[1] = walls[1]
                new_walls[2] = walls[2]
                new_walls[3] = walls[3]

            elif current_direction == 'S':
                new_walls[0] = walls[1]
                new_walls[1] = walls[0]
                new_walls[2] = walls[3]
                new_walls[3] = walls[2]

            elif current_direction == 'W':
                new_walls[0] = walls[3]
                new_walls[1] = walls[2]
                new_walls[2] = walls[0]
                new_walls[3] = walls[1]

            elif current_direction == 'E':
                new_walls[0] = walls[2]
                new_walls[1] = walls[3]
                new_walls[2] = walls[1]
                new_walls[3] = walls[0]


        else:
            print('Format is wrong')

        return new_walls

    # uppdatera! uppdatera bara listan med väggar
    def update_cell_in_maze(self, maze, cell):
        x = maze.current_pos_row
        y = maze.current_pos_col
        maze[x][y] = cell

    # direction är sträng av en bokstav. current_format = 'ABLR' eller 'NSWE'
    # Skriv om bättre.
    # Borde gå att göra mycket bättre än hårdkodning
    def change_direction_format(self, current_direction, direction, current_format):
        new_direction = ''

        if current_format == 'ABLR':

            if current_direction == 'N':
                if direction == 'A':
                    new_direction = 'N'
                elif direction == 'B':
                    new_direction = 'S'
                elif direction == 'L':
                    new_direction = 'W'
                elif direction == 'R':
                    new_direction = 'E'
                else:
                    print('Error')
            elif current_direction == 'S':
                if direction == 'A':
                    new_direction = 'S'
                elif direction == 'B':
                    new_direction = 'N'
                elif direction == 'L':
                    new_direction = 'E'
                elif direction == 'R':
                    new_direction = 'W'
                else:
                    print('Error')
            elif current_direction == 'W':
                if direction == 'A':
                    new_direction = 'W'
                elif direction == 'B':
                    new_direction = 'E'
                elif direction == 'L':
                    new_direction = 'S'
                elif direction == 'R':
                    new_direction = 'N'
                else:
                    print('Error')
            elif current_direction == 'E':
                if direction == 'A':
                    new_direction = 'E'
                elif direction == 'B':
                    new_direction = 'W'
                elif direction == 'L':
                    new_direction = 'N'
                elif direction == 'R':
                    new_direction = 'S'
                else:
                    print('Error')

        elif current_format == 'NSWE':
            if current_direction == 'N':
                if direction == 'N':
                    new_direction = 'A'
                elif direction == 'S':
                    new_direction = 'B'
                elif direction == 'W':
                    new_direction = 'L'
                elif direction == 'E':
                    new_direction = 'R'
                else:
                    print('Error')
            elif current_direction == 'S':
                if direction == 'N':
                    new_direction = 'B'
                elif direction == 'S':
                    new_direction = 'A'
                elif direction == 'W':
                    new_direction = 'R'
                elif direction == 'E':
                    new_direction = 'L'
                else:
                    print('Error')
            elif current_direction == 'W':
                if direction == 'N':
                    new_direction = 'R'
                elif direction == 'S':
                    new_direction = 'L'
                elif direction == 'W':
                    new_direction = 'A'
                elif direction == 'E':
                    new_direction = 'B'
                else:
                    print('Error')
            elif current_direction == 'E':
                if direction == 'N':
                    new_direction = 'L'
                elif direction == 'S':
                    new_direction = 'R'
                elif direction == 'W':
                    new_direction = 'B'
                elif direction == 'E':
                    new_direction = 'A'
                else:
                    print('Error')
        else:
            print('Format error')

        return new_direction

    def change_maze_format(self, walls):
        # to NSWE from WSEN
        new_walls = ['', '', '', '']

        new_walls[0] = walls[3]
        new_walls[1] = walls[1]
        new_walls[2] = walls[0]
        new_walls[3] = walls[2]

        return new_walls

    def change_instruction_format(self, instruction):

        new_instruction = instruction
        if instruction == 'A':
            new_instruction = 'f'
        elif instruction == 'B':
            new_instruction = 'bf'
        elif instruction == 'L':
            new_instruction = 'lf'
        elif instruction == 'R':
            new_instruction = 'rf'

        return new_instruction