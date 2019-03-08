class Cell(object):
    # walls är string (t.ex. '0000') pga 0000 = 0
    # g = avstånd från start, h = avstånd till mål
    def __init__(self, walls, coordinate_x, coordinate_y):
        self.walls = walls
        self._visited = False
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self._g = 0
        self._h = 0
        self._f = self._g + self._h

    def __str__(self):
        walls_string = ''.join(self.walls)
        return walls_string

    def __repr__(self):
        walls_string = ''.join(self.walls)
        return walls_string

# måste ha "_" innan attributer som ska ha setters. Inte förstått varför än
# verkar funka utan getters och setters. Låter de vara så länge
    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        self._visited = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value


