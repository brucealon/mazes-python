
import pytest
from context import Cell

class TestCells:
    def test_cell_links(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        cell3 = Cell(1, 0)
        cell1.link(cell2)
        assert cell2.is_linked(cell1)
        assert cell1.is_linked(cell2)
        assert not cell1.is_linked(cell3)
        assert not cell2.is_linked(cell3)

    def test_cell_unlink(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        cell1.link(cell2)
        assert cell2.is_linked(cell1)
        assert cell1.is_linked(cell2)
        cell1.unlink(cell2)
        assert not cell1.is_linked(cell2)
        assert not cell2.is_linked(cell1)

    def test_cell_neighbors(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 1)
        cell1.south = cell2
        cell2.north = cell1
        assert cell1 in cell2.neighbors()
        assert cell2 in cell1.neighbors()

    def test_distances(self):
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
        assert distances[cell1] == 0
        assert distances[cell2] == 1
        assert distances[cell3] == 2
        assert distances[cell4] == 5
        assert distances[cell5] == 4
        assert distances[cell6] == 3
        assert distances[cell7] == 6
        assert distances[cell8] == 5
        assert distances[cell9] == 4
