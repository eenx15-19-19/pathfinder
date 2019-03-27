from Translation import Translation
import numpy as np

class MazeTransformer:
    translator = Translation()
    f = open("5x5.c", "r")
    whole = f.read()
    hextype = whole[-1577:-26]
    listh = []
    listb = []
    for i in range(256):
        listh.append(int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16))
    for element in listh:
        listb.append(translator.change_maze_format(f'{element:0>4b}'))
    print(listb[1][1])
    matrixb = np.empty([16, 16], dtype="S4")

    #print(matrixb[0][15])

    for x in range(15):
        for y in range(15, 0, -1):
            for k in listb[x*15+(15-y)]:

                element = listb[x*15+(15-y)]
                #print(element)
                #matrixb[y, x] = element
    #print(matrixb)


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