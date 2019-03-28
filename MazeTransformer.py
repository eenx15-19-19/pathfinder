from Translation import Translation
import pprint


class MazeTransformer:

    def transpose_matrix(self, rows, cols, element_list):
        #anta 16x16
        matrix = [['0000' for j in range(16)] for i in range(16)]
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

            if row > 15:
                print('1')
            if col > 15:
                print('2')
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

        f = open("5x5.c", "r")
        whole = f.read()
        # får med '\n ' ibland, men antas bara vara element. Steg 1 är att hantera det. Sen kan det finnas mer knas
        hextype = whole[-1577:-26]
        matrixh = []
        matrixb = []
        hex_list = []
        rows = 16
        cols = 16

       # matrix = [['0000' for j in range(16)] for i in range(16)]

        m = 0
        n = 0


        for i in range(256):
            test_string = hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16
            print(test_string)
            number = int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16)

            bin_number = translator.change_maze_format(f'{number:0>4b}')
            hex_list.append(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)])

            matrixh.append(int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16))

           # for j in range(rows):
            #    for k in range(cols):
             #       matrix[m][n] = number

            n = n + 1
            if n == cols:
                n = 0
                m = m + 1

        #matrix = self.transpose_matrix(matrix, hextype)
        #print(matrixh)
        print(hextype)
        print(matrixh)
        print(hex_list)
        #print(len(matrixh))
        matrix = transformer.transpose_matrix(rows, cols, matrixh)

        temp_matrix = [['0000' for j in range(16)] for i in range(16)]

        for i in range(16):
            for j in range(16):
                temp_matrix[i][j] = hex(matrix[i][j])
        #print(matrix)
        #print(temp_matrix)


transformer = MazeTransformer()
new_matrix = transformer.get_matrix()
print(new_matrix)

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