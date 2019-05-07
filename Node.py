# -*- coding: utf-8 -*-
import sys


class Node(object):

    def __init__(self, cell):
        self.cell = cell
        self.parent = None
        self.depth = 0
        self.fake_f = sys.maxsize
        self.fake_h = sys.maxsize
        self.direction_value = 0

    def __str__(self):
        string = str(self.cell)
        return string

    def __repr__(self):
        string = str(self.cell)
        return string

