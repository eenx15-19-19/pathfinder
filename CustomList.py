class CustomList(object):

    def __init__(self):
        self.custom_list = []

    def add(self, node):
        index = self.bin_search(self.custom_list, node)     # hitta den plats där den ska sättas in
        self.custom_list.insert(index, node)

    def delete(self, node):
        index = self.bin_search(self.custom_list, node)
        self.custom_list.pop(index)

    def get_first(self):
        return self.custom_list[0]

    def __str__(self):
        string = ''
        for i in range(len(self.custom_list)):
            string = string + str(self.custom_list[i]) + ', '

        return string

    def cell_search(self, cell):
        index = -1

        for i in range(len(self.custom_list)):
            if self.custom_list[i].cell == cell:
                index = i
                break

        return index

    def bin_search(self, custom_list, node):
        lo = 0
        hi = len(custom_list)
        mid = (lo + hi)//2  # // är för floored integer division

        value = node.fake_f     # börja med att jämföra f
        value_comp = 0      # räknar vilken sak vi jämför (f, h, direction)

        other_value = 0     # måste ha ett initialt värde, ändras i while-loopen sen. Kan inte sätta
                            # custom_list[mid].fake_f pga kaos om listan är tom
        while hi != lo:
            if value_comp == 0:
                other_value = custom_list[mid].fake_f

            if value < other_value:
                hi = mid
                mid = (hi + lo)//2

            elif value > other_value:
                lo = mid + 1
                mid = (hi + lo)//2

            elif value == other_value:      # jämför på nästa sak
                if value_comp == 0:
                    value = node.fake_h
                    other_value = custom_list[mid].fake_h
                elif value_comp == 1:
                    value = node.direction_value
                    other_value = custom_list[mid].direction_value
                elif value_comp == 2:
                    return mid
                else:
                    hi = lo

                value_comp = value_comp + 1

        return int(mid)