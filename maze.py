#!/usr/bin/env python3

from random import randint

class Cell():
    def __init__(self, row, column):
        self.row    = row
        self.column = column
        self.links  = {}
        self.north  = False
        self.south  = False
        self.east   = False
        self.west   = False

    def link(self, cell, bidi = True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi = True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def links(self):
        return list(self.links.keys())

    def is_linked(self, cell):
        return cell in self.links and self.links[cell]
    

    def neighbors(self):
        list = []
        if self.north: list.append(self.north)
        if self.south: list.append(self.south)
        if self.east:  list.append(self.east)
        if self.west:  list.append(self.west)
        return list

    def __repr__(self):
        return f'({self.row},{self.column})'

class Grid():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, coords):
        row, column = coords
        if not row > -1: return None
        if not row < self.rows: return None
        if not column > -1: return None
        if not column < self.columns: return None

        return self.grid[row][column]

    def __iter__(self):
        return iter(self.grid)

    def prepare_grid(self):
        return [ [ Cell(row, column) for column in range(0, self.columns) ] for row in range(0, self.rows) ]

    def configure_cells(self):
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.east = self[row, column + 1]
            cell.west = self[row, column - 1]

    def random_cell(self):
        row = randint(0, self.rows - 1)
        column = randint(0, self.columns - 1)
        return self.grid[row][column]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        return iter(self.grid)

    def each_cell(self):
        return iter([ cell for row in self.grid for cell in row ])

    def __repr__(self):
        output = '+' + '---+' * self.columns + '\n'
        for row in self:
            top = '|'
            bottom = '+'
            
            for cell in row:
                body = '   '
                east = ' ' if cell.is_linked(cell.east) else '|'
                top += body + east
                south = '   ' if cell.is_linked(cell.south) else '---'
                bottom += south + '+'

            output += top + '\n'
            output += bottom + '\n'

        return output

def binary_tree(grid):
    for cell in grid.each_cell():
        neighbors = []
        if cell.north: neighbors.append(cell.north)
        if cell.east:  neighbors.append(cell.east)

        if len(neighbors) > 0:
            neighbor = neighbors[randint(0, len(neighbors) - 1)]
            if neighbor != None: cell.link(neighbor)
    
if __name__ == '__main__':
    g = Grid(30, 30)
    binary_tree(g)
    print(g)
