
from .distances import Distances

class Cell():
    def __init__(self, row, column):
        self.row    = row
        self.column = column
        self.linkd  = {}
        self.north  = False
        self.south  = False
        self.east   = False
        self.west   = False

    def link(self, cell, bidi = True):
        self.linkd[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi = True):
        del self.linkd[cell]
        if bidi:
            cell.unlink(self, False)

    def links(self):
        return list(self.linkd.keys())

    def is_linked(self, cell):
        return cell in self.linkd and self.linkd[cell]


    def neighbors(self):
        list = []
        if self.north: list.append(self.north)
        if self.south: list.append(self.south)
        if self.east:  list.append(self.east)
        if self.west:  list.append(self.west)
        return list

    def __repr__(self):
        return f'({self.row},{self.column})'

    def distances(self):
        distances = Distances(self)
        distances[self] = 0
        frontier = [ self ]
        while any(frontier):
            new_frontier = []
            for cell in frontier:
                for linked in cell.links():
                    if distances[linked] >= 0: continue
                    distances[linked] = distances[cell] + 1
                    new_frontier.append(linked)
            frontier = new_frontier
        return distances
