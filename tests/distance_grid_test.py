
import pytest
from context import Grid, DistanceGrid
from context import NoStartingPointException

class TestDistanceGrid:
    def test_contents_of_empty(self):
        grid = DistanceGrid(2, 2)
        assert grid.contents_of(grid[0,0]) == '   '
        assert grid.contents_of(grid[1,1]) == '   '

    def test_contents_of_non_empty(self):
        grid = DistanceGrid(2, 2)
        grid[0,0].link(grid[0,1])
        grid[0,1].link(grid[1,1])
        grid[1,1].link(grid[1,0])
        distances = grid.distances_from(grid[0,0])
        assert grid.contents_of(grid[0,0]) == ' 0 '
        assert grid.contents_of(grid[0,1]) == ' 1 '
        assert grid.contents_of(grid[1,1]) == ' 2 '
        assert grid.contents_of(grid[1,0]) == ' 3 '

    def test_path_to_no_start(self):
        grid = DistanceGrid(2, 2)
        with pytest.raises(NoStartingPointException):
            grid.path_to(grid[1,1])

    def test_path_to_with_start(self):
        grid = DistanceGrid(2, 2)
        grid[0,0].link(grid[0,1])
        grid[0,1].link(grid[1,1])
        grid[1,1].link(grid[1,0])
        grid.distances_from(grid[1,0])
        grid.path_to(grid[1,1])
        grid.distance_to(grid[0,0]) == 0
        grid.distance_to(grid[0,1]) == 1
        grid.distance_to(grid[1,1]) == 2
        grid.distance_to(grid[1,0]) == -1
