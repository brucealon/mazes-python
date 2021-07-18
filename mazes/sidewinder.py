
from random import randint, sample

def should_close(cell):
    if cell.east == None: return True
    if cell.north != None and randint(0, 1) == 0: return True

    return False

def build_sidewinder_maze(grid):
    for row in grid.each_row():
        run = []
        for cell in row:
            run.append(cell)
            if should_close(cell):
                if len(run) > 0:
                    member = sample(run, 1)[0]
                    if member.north: member.link(member.north)
                    run.clear()
            else:
                cell.link(cell.east)
