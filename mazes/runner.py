
from .grid import Grid
from .binary_tree import build_bt_maze

class MazeRunner:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def run(self):
        g = Grid(self.rows, self.columns)
        build_bt_maze(g)
        print(g)
