
from random import sample

def build_aldous_broder_maze(grid):
    cell = grid.random_cell()
    unvisited = grid.size() - 1

    while unvisited > 0:
        neighbor = sample(cell.neighbors(), 1)[0]

        if len(neighbor.links()) == 0:
            cell.link(neighbor)
            unvisited = unvisited - 1

        cell = neighbor

