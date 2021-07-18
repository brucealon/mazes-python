
import pytest
from context import Grid

class TestGrid():
    def test_neighbors(self):
        grid = Grid(10,10)
        cell = grid[4, 4]
        assert grid[3, 4] in cell.neighbors()
        assert grid[5, 4] in cell.neighbors()
        assert grid[4, 3] in cell.neighbors()
        assert grid[4, 5] in cell.neighbors()

    def test_size(self):
        grid = Grid(10, 10)
        assert grid.size() == 100
        grid = Grid(5, 5)
        assert grid.size() == 25

    def test_each_row(self):
        grid = Grid(2, 2)
        i = grid.each_row()
        assert next(i) == [grid[0, 0], grid[0, 1]]
        assert next(i) == [grid[1, 0], grid[1, 1]]
        with pytest.raises(StopIteration):
            next(i)

    def test_each_cell(self):
        grid = Grid(2, 2)
        i = grid.each_cell()
        assert next(i) == grid[0, 0]
        assert next(i) == grid[0, 1]
        assert next(i) == grid[1, 0]
        assert next(i) == grid[1, 1]
        with pytest.raises(StopIteration):
            next(i)
