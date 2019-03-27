from Translation import Translation
import pprint

class MazeTransformer:
    translator = Translation()

    f = open("5x5.c", "r")
    whole = f.read()
    hextype = whole[-1577:-26]
    matrixh = []
    matrixb = []
    rows = 16
    cols = 16

    matrix = [['0000' for j in range(16)] for i in range(16)]
    test_matrix = [['0000' for j in range(16)] for i in range(16)]
    matrix2 = [['0000' for j in range(16)] for i in range(16)]
    new_matrix = [['0000' for j in range(16)] for i in range(16)]
    m = 0
    n = 0
    for i in range(256):
        test_number = hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16
        number = int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16)
        number2 = int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16)

        bin_number2 = f'{number2:0>4b}'
        bin_number = translator.change_maze_format(f'{number:0>4b}')
        matrixh.append(int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16))
        for j in range(rows):
            for k in range(cols):
                matrix[m][n] = bin_number
                test_matrix[m][n] = test_number
                matrix2[m][n] = bin_number2

        n = n + 1
        if n == cols:
            n = 0
            m = m + 1

    print(test_matrix)
    print(matrix2)
    print(matrix)

    
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