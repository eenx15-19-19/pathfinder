import Cell
from HelpFunctions import HelpFunctions
import Node
from operator import itemgetter
import queue
import CustomList

class test:

    test_list = []
    helper = HelpFunctions()
    cell1 = Cell.Cell(helper.split_walls('0000'), 1, 1)
    cell2 = Cell.Cell(helper.split_walls('0100'), 2, 2)
    cell3 = Cell.Cell(helper.split_walls('1000'), 3, 3)
    cell4 = Cell.Cell(helper.split_walls('1100'), 4, 4)

    node1 = Node.Node(cell1)
    node1.fake_f = 4
    node1.fake_h = 2
    node1.direction_value = 2

    node2 = Node.Node(cell2)
    node2.fake_f = 4
    node2.fake_h = 2
    node2.direction_value = 2

    node3 = Node.Node(cell3)
    node3.fake_f = 4
    node3.fake_h = 2
    node3.direction_value = 2

    node4 = Node.Node(cell4)
    node4.fake_f = 4
    node4.fake_h = 3
    node4.direction_value = 6

    custom_list = CustomList.CustomList()

    custom_list.add(node2)
    custom_list.add(node1)

    custom_list.add(node3)
    custom_list.add(node4)

    print(custom_list)

