
from context import *

class TestGenerators:
    def test_binary_tree(self):
        grid = Grid(25, 25)
        build_bt_maze(grid)
        distances = grid[0,0].distances()
        for cell in grid.each_cell():
            assert distances[cell] >= 0

    def test_sidewinder(self):
        grid = Grid(25, 25)
        build_sidewinder_maze(grid)
        distances = grid[0,0].distances()
        for cell in grid.each_cell():
            assert distances[cell] >= 0