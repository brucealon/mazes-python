
from .exceptions import UnreachablePathException

class Distances:
    def __init__(self, root):
        self.root = root
        self.cell_dict = {}
        self.cell_dict[root] = 0

    def __getitem__(self, cell):
        return self.cell_dict.get(cell, -1)

    def __setitem__(self, cell, distance):
        self.cell_dict[cell] = distance

    def cells(self):
        return list(self.cell_dict)

    def path_to(self, goal):
        if self[goal] == -1:
            raise UnreachablePathException

        current = goal
        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self[current]

        while current != self.root:
            for link in current.links():
                if self[link] < self[current]:
                    breadcrumbs[link] = self[link]
                    current = link
                    break
        return breadcrumbs
