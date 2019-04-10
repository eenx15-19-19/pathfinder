class CustomList(object):

    def __init__(self):
        self.custom_list = []

    def add(self, node):
        index = self.get_index(self.custom_list, node)     # hitta den plats där den ska sättas in
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

    def get_index(self, custom_list, node):
        # sök på f
        if len(custom_list) == 0:
            return 0

        index_f = self.bin_search(custom_list, node, 0)
        index = index_f

        if custom_list[index].fake_f == node.fake_f:
            # sortera på h
            sublist_f, list_index = self.get_sublist_f(custom_list, index, node)
            index_h = self.bin_search(sublist_f, node, 1)

            index = list_index + index_h

            if custom_list[index].fake_h == node.fake_h:
            # sortera på direction
                sublist_h, list_index = self.get_sublist_h(custom_list, index, node)
                index_dir = self.bin_search(sublist_h, node, 2)

                index = list_index + index_dir

        return index

    def get_sublist_f(self, custom_list, index, node):
        lo = index
        hi = index

        sublist = []

        value = node.fake_f

        while hi < len(custom_list) - 1:
            if custom_list[hi + 1].fake_f == value:
                hi = hi + 1
            else:
                break

        while lo > 0:
            if custom_list[lo - 1].fake_f == value:
                lo = lo - 1
            else:
                break

        list_index = lo

        while lo <= hi:
            sublist.append(custom_list[lo])
            lo = lo + 1

        return sublist, list_index

    def get_sublist_h(self, custom_list, index, node):
        lo = index
        hi = index

        sublist = []

        value = node.fake_h

        while hi < len(custom_list) - 1:
            if custom_list[hi + 1].fake_h == value:
                hi = hi + 1
            else:
                break

        while lo > 0:
            if custom_list[lo - 1].fake_h == value:
                lo = lo - 1
            else:
                break

        list_index = lo

        while lo <= hi:
            sublist.append(custom_list[lo])
            lo = lo + 1

        return sublist, list_index


    def bin_search(self, custom_list, node, value_comp):
        lo = 0
        hi = len(custom_list)
        mid = (lo + hi)//2  # // är för floored integer division

        if value_comp == 0:
            value = node.fake_f     # börja med att jämföra f
        elif value_comp == 1:
            value = node.fake_h
        elif value_comp == 2:
            value = node.direction_value
        else:
            value = 0

        other_value = 0     # måste ha ett initialt värde, ändras i while-loopen sen. Kan inte sätta
                            # custom_list[mid].fake_f pga kaos om listan är tom
        while hi != lo:

            if value_comp == 0:
                other_value = custom_list[mid].fake_f
            elif value_comp == 1:
                other_value = custom_list[mid].fake_h
            elif value_comp == 2:
                other_value = custom_list[mid].direction_value

            if value < other_value:
                hi = mid
                mid = (hi + lo)//2

            elif value > other_value:
                lo = mid + 1
                mid = (hi + lo)//2

            elif value == other_value:
                return int(mid)
          #  elif value == other_value:      # jämför på nästa sak
          #      if value_comp == 0:
          #          value = node.fake_h
          #          other_value = custom_list[mid].fake_h
          #      elif value_comp == 1:
          #          value = node.direction_value
          #          other_value = custom_list[mid].direction_value
          #      elif value_comp == 2:
          #          return mid
          #      else:
          #          hi = lo

                #value_comp = value_comp + 1

        return int(mid)
