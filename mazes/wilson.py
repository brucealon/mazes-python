
from .helpers import sample

def build_wilson_maze(grid):
    unvisited = []
    for cell in grid.each_cell():
        unvisited.append(cell)

    first = sample(unvisited)
    unvisited.remove(first)

    while len(unvisited) > 0:
        cell = sample(unvisited)
        path = [cell]

        while cell in unvisited:
            cell = sample(cell.neighbors())
            if cell in path:
                idx = path.index(cell)
                path = path[0:idx+1]
            else:
                path.append(cell)

        for idx in range(len(path) - 1):
            path[idx].link(path[idx + 1])
            unvisited.remove(path[idx])
