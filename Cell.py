class Cell(object):
    # walls är string (t.ex. '0000') pga 0000 = 0
    # g = avstånd från start, h = avstånd till mål
    def __init__(self, walls, coordinateX, coordinateY):
        self.walls = walls
        self._visited = False
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self._g = 0
        self._h = 0
        self._f = self._g + self._h

    def __str__(self):
        return self.walls

    def __repr__(self):
        return self.walls

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

    @g.setter
    def h(self, value):
        self._h = value


