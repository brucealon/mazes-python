
from .cell import Cell

class Grid():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, coords):
        row, column = coords
        if not row > -1:              return None
        if not row < self.rows:       return None
        if not column > -1:           return None
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

    def contents_of(self, cell):
        return '   '

    def __repr__(self):
        output = '+' + '---+' * self.columns + '\n'
        for row in self:
            top = '|'
            bottom = '+'

            for cell in row:
                body = self.contents_of(cell)
                east = ' ' if cell.is_linked(cell.east) else '|'
                top += body + east
                south = '   ' if cell.is_linked(cell.south) else '---'
                bottom += south + '+'

            output += top + '\n'
            output += bottom + '\n'

        return output
