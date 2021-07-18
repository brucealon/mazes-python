
import pytest
from context import Cell, Distances
from context import UnreachablePathException

class TestDistances:
    def test_distance(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        distances = Distances(cell1)
        distances[cell2] = 1
        assert distances[cell1] == 0
        assert distances[cell2] == 1

    def test_path_to(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        cell3 = Cell(0, 2)
        cell4 = Cell(1, 0)
        cell5 = Cell(1, 1)
        cell6 = Cell(1, 2)
        cell7 = Cell(2, 0)
        cell8 = Cell(2, 1)
        cell9 = Cell(2, 2)

        cell1.link(cell2)
        cell2.link(cell3)
        cell3.link(cell6)
        cell4.link(cell5)
        cell4.link(cell7)
        cell5.link(cell6)
        cell5.link(cell8)
        cell6.link(cell9)

        distances = cell1.distances()
        path = distances.path_to(cell9)
        assert path[cell1] == 0
        assert path[cell2] == 1
        assert path[cell3] == 2
        assert path[cell6] == 3
        assert path[cell9] == 4
        assert path[cell4] == -1
        assert path[cell5] == -1
        assert path[cell7] == -1
        assert path[cell8] == -1

    def test_unreachable_path(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        distances = cell1.distances()
        with pytest.raises(UnreachablePathException):
            distances.path_to(cell2)
