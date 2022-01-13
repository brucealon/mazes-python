
from .helpers import sample

def hunt(grid):
    for cell in grid.each_cell():
        visited = [n for n in cell.neighbors() if len(n.links()) > 0]
        if len(cell.links()) == 0 and len(visited) > 0:
            cell.link(sample(visited))
            return cell

def build_hk_maze(grid):
    cell = grid.random_cell()

    while cell:
        unvisited = [n for n in cell.neighbors() if len(n.links()) == 0]

        if len(unvisited) > 0:
            neighbor = sample(unvisited)
            cell.link(neighbor)
            cell = neighbor
        else:
            cell = hunt(grid)
