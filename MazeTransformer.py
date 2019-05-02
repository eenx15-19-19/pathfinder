from Translation import Translation
import pprint


class MazeTransformer:

    def transpose_matrix(self, rows, cols, element_list):
        #anta 16x16
        matrix = [['0000' for j in range(rows)] for i in range(cols)]
        # antal rader och kolumner i matrisen
        rows = rows
        cols = cols
        # lista med rows*cols antal element

        # index för matris
        row = 0
        col = 0

        # börjar hantera första 'raden' i listan
        current_row = 1

        # flyttar alltid vänster 1 pga nollindexering, ökar när vi backar i raden
        move_left = 1

        for k in range(len(element_list)):

            # index på element i listan
            index = cols * current_row

            # flytta vänster 1 pga nollindexering + 1 till för varje redan tillagt element
            number = element_list[index - move_left]

            matrix[row][col] = number

            # flytta ner en rad
            row = row + 1

            # om vi når botten av matrisen, flytta upp till toppen igen
            if row > rows-1:
                row = 0
                current_row = current_row + 1
                col = col + 1
                # om vi når högerkanten, flytta tillbaka till vänster igen
                if col > cols-1:
                    col = 0

                # byter vi rad ska denna nollställas
                move_left = 0

                # backa en gång för varje avklarat element
            move_left = move_left + 1

        return matrix

    def get_matrix(self):
        translator = Translation()

        f = open("boston.c", "r")
        whole = f.read()
        hextype = whole[-1577:-26]
        elements_list = []
        rows = 16
        cols = 16

        k = 0
        for i in range(256):
            elements_list.append(int(hextype[hextype.index(",", 1 + i * 6 + k) - 4:
                                             hextype.index(",", 1 + i * 6 + k)], 16))

            if i % rows == 0:
                k = k + 1

        matrix = transformer.transpose_matrix(rows, cols, elements_list)

        for i in range(rows):
            for j in range(cols):
                number = matrix[i][j]
                matrix[i][j] = translator.change_maze_format(f'{number:0>4b}')

        return matrix


transformer = MazeTransformer()
new_matrix = transformer.get_matrix()

#print(new_matrix)
