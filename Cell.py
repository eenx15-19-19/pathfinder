class Cell(object):
    # walls är lista av strängar t.ex. ['0', '0', '0', '1'], NSWE
    # g = avstånd från start, h = avstånd till mål
    def __init__(self, walls, row, col):
        self.walls = walls
        self._visited = False

        # cellens position
        self.row = row
        self.col = col

        # till heuristics
        self._g = 0
        self._h = 0
        self._f = self._g + self._h

    def __str__(self):
        string = '[' + str(self.row) + '][' + str(self.col) + '] Walls: ' + ''.join(self.walls)
        return string

    def __repr__(self):
        coord = '[' + str(self.row) + '][' + str(self.col) + ']'
        return coord


# måste ha "_" innan attributer som ska ha setters. Inte förstått varför än.
# Verkar funka utan getters och setters. Låter de vara så länge
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

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value
