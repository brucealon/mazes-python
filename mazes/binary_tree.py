
from random import randint

def build_bt_maze(grid):
    for cell in grid.each_cell():
        neighbors = []
        if cell.north: neighbors.append(cell.north)
        if cell.east:  neighbors.append(cell.east)

        if len(neighbors) > 0:
            neighbor = neighbors[randint(0, len(neighbors) - 1)]
            if neighbor != None: cell.link(neighbor)
