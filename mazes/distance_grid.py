
from .grid import Grid
from .distances import Distances
from .exceptions import NoStartingPointException

class DistanceGrid(Grid):
    def __init__(self, rows, columns):
        self.distances = False
        super().__init__(rows, columns)

    def contents_of(self, cell):
        if self.distances and self.distances[cell] >= 0:
            return f'{self.distances[cell]:^3d}'
        else:
            return super().contents_of(cell)

    def distance_to(self, cell):
        if not self.distances:
            raise NoStartingPointException('Must first calculate distances from a starting point.')
        return self.distances[cell]

    def distances_from(self, cell):
        self.distances = cell.distances()

    def path_to(self, goal):
        if not self.distances:
            raise NoStartingPointException('Must first calculate distances from a starting point.')
        self.distances = self.distances.path_to(goal)

    def max(self):
        if not self.distances:
            raise NoStartingPointException('Must first calculate distances from a starting point.')
        return self.distances.max()

    def longest_path(self):
        self.distances = self[0,0].distances()
        (cell, distance) = self.distances.max()
        self.distances = cell.distances()
        (cell, distance) = self.distances.max()
        self.distances = self.distances.path_to(cell)
