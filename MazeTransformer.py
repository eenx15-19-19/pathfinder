from Translation import Translation

class MazeTransformer:
    f = open("5x5.c", "r")
    whole = f.read()
    hextype = whole[-1577:-26]
    matrixh = []
    matrixb = []
    for i in range(256):
        matrixh.append(int(hextype[hextype.index(",", 1 + i * 6) - 4:hextype.index(",", 1 + i * 6)], 16))
    for element in matrixh:
        matrixb.append(translator.change_maze_format(f'{element:0>4b}'))
    print(matrixb)



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