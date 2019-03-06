class Cell(object):
    def __init__(self, walls, coordinates):
        self.walls = walls
        self._visited = False
        self.coordinates = coordinates
        self._f = None

    def __str__(self):
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
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value


