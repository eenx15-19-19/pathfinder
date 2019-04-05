import sys


class Node(object):

    def __init__(self, cell):
        self.cell = cell
        self.parent = None
        self.depth = None
        self.explored = False


