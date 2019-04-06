import Cell
from HelpFunctions import HelpFunctions
import Node
from operator import itemgetter
import queue
import CustomList

class test:

    test_list = []
    helper = HelpFunctions()
    cell1 = Cell.Cell(helper.split_walls('0000'), 0, 0)
    cell2 = Cell.Cell(helper.split_walls('0100'), 1, 1)
    cell3 = Cell.Cell(helper.split_walls('1000'), 2, 2)
    cell4 = Cell.Cell(helper.split_walls('1100'), 3, 3)

    node1 = Node.Node(cell1)
    node1.fake_f = 4
    node1.fake_h = 2
    node1.direction_value = 3

    node2 = Node.Node(cell2)
    node2.fake_f = 4
    node2.fake_h = 3
    node2.direction_value = 6

    node3 = Node.Node(cell3)
    node3.fake_f = 3
    node3.fake_h = 5
    node3.direction_value = 2

    node4 = Node.Node(cell3)
    node4.fake_f = 1
    node4.fake_h = 6
    node4.direction_value = 2

    test_list.append([node2, node2.fake_f, node2.fake_h, node2.direction_value])
    test_list.append([node1, node1.fake_f, node1.fake_h, node1.direction_value])
    test_list.append([node3, node3.fake_f, node3.fake_h, node3.direction_value])

    print(test_list)

    test_list.sort(key=itemgetter(1))

    print(test_list)

    test_list.sort(key=itemgetter(2))

    print(test_list)

    pq = queue.PriorityQueue()
    pq.put((node2.fake_f, node2.fake_h, node2.direction_value, node2))
    pq.put((node4.fake_f, node4.fake_h, node4.direction_value, node4))
    pq.put((node3.fake_f, node3.fake_h, node3.direction_value, node3))
    pq.put((node1.fake_f, node1.fake_h, node1.direction_value, node1))


    print(pq.get())

    custom_list = CustomList.CustomList()

    custom_list.add(node2)
    custom_list.add(node1)

    custom_list.add(node3)
    custom_list.add(node4)

    print(custom_list)