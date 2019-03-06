# Här kan vi lägga algoritmen och saker relaterade till den
import Maze


class HelpFunctions:

    def currentCell(self, maze):
        return maze.x, maze.y

    # lastDirection är sträng (NSWE), t.ex. N
    def updateCurrentCell(self, maze, lastDirection):
        if lastDirection == 'N':
            maze.y = maze.y + 1
        elif lastDirection == 'S':
            maze.y = maze.y - 1
        elif lastDirection == 'W':
            maze.x = maze.x - 1
        elif lastDirection == 'E':
            maze.x = maze.x + 1
        else:
            None










