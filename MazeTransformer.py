import binascii


class MazeTransformer:

    hexString = '0x09'
    hexNumber = int(hexString.lstrip('0x'))
    print(type(hexNumber))
    number = hexNumber
    bin_number = bin(number).lstrip('0b').zfill(4)
    print(bin_number)

    # NESW gör om till NSWE