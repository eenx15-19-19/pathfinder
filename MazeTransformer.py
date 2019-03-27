from Translation import Translation
import pprint


class MazeTransformer:

    def transpose_matrix(self, matrix):
        # antal rader och kolumner i matrisen
        rows = 3
        cols = 3
        # lista med rows*cols antal element
        list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # index för matris
        row = 0
        col = 0

        # börjar hantera första 'raden' i listan
        current_row = 1

        # flyttar alltid vänster 1 pga nollindexering, ökar när vi backar i raden
        move_left = 1

        print(matrix)

        for k in range(len(list_example)):

            # index på element i listan
            index = cols * current_row

            # flytta vänster 1 pga nollindexering + 1 till för varje redan tillagt element
            number = list_example[index - move_left]

            matrix[row][col] = number

            # flytta ner en rad
            row = row + 1

            # om vi når botten av matrisen, flytta upp till toppen igen
            if row > rows:
                row = 0
                current_row = current_row + 1
                col = col + 1
                # om vi når högerkanten, flytta tillbaka till vänster igen
                if col > cols:
                    col = 0

                # byter vi rad ska denna nollställas
                move_left = 0

                # backa en gång för varje avklarat element
            move_left = move_left + 1

        return matrix

    translator = Translation()

    f = open("5x5.c", "r")
    whole = f.read()
    hextype = whole[-1577:-26]
    matrixh = []
    matrixb = []
    rows = 16
    cols = 16

    matrix = [['0000' for j in range(16)] for i in range(16)]

    m = 0
    n = 0
    
    for i in range(256):

        number = int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16)

        bin_number = translator.change_maze_format(f'{number:0>4b}')

        matrixh.append(int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16))

        for j in range(rows):
            for k in range(cols):
                matrix[m][n] = bin_number

        n = n + 1
        if n == cols:
            n = 0
            m = m + 1





   # for element in matrixh:
    #    matrixb.append(translator.change_maze_format(f'{element:0>4b}'))

 #   for i in range(rows):
  #      for j in range(cols):
   #         number = matrix[i][j]

    #        number = int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16)
     #       matrix[i][j] = translator.change_maze_format(f'{number:0>4b}')

  #  print(matrixh)
  #  print(matrix)

    #hexString = '0x01'
    #hexNumber = int(hexString.lstrip('0x'))
    #print(type(hexNumber))
    #number = hexNumber
    #bin_number = bin(number).lstrip('0b').zfill(4)
    #print(bin_number)

    #translator = Translation()

    #wall = translator.change_maze_format(bin_number)
    #print(wall)
    # NESW gör om till NSWE