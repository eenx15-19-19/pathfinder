# innehåller all information om roboten


class Robot(object):
    def __init__(self, maze):
        self.current_pos_row = maze.start_row # börjar i start
        self.current_pos_col = maze.start_col
        self.current_direction = 'N'    # börjar med att peka norr
        self._g = 0  # antal effektiva steg från start

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

