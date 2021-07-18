#!/usr/bin/env python

from mazes import *
import argparse
from distutils.util import strtobool

default_rows               = 25
default_columns            = 25
default_algorithm          = 'binarytree'
default_start_row          = 0
default_start_column       = 0
default_destination_row    = default_rows - 1
default_destination_column = default_columns - 1

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rows',
                    help=f'Set the number of maze rows (default {default_rows}).',
                    type=int,
                    default=default_rows)
parser.add_argument('-c', '--columns',
                    help=f'Set the number of maze columns (default {default_columns}).',
                    type=int,
                    default=default_columns)
parser.add_argument('-a', '--algorithm',
                    help=f'Choose the algorithm used to build the maze (default {default_algorithm}).',
                    type=str,
                    default=default_algorithm,
                    choices=['binarytree', 'sidewinder'])
parser.add_argument('-R', '--start-row',
                    help=f'Row for distances display (default {default_start_row}). Requires -d.',
                    type=int,
                    default=default_start_row)
parser.add_argument('-C', '--start-column',
                    help=f'Column for distances display (default {default_start_column}). Requires -d.',
                    type=int,
                    default=default_start_column)
parser.add_argument('-d', '--show-distances',
                    help='Show the distances from Row and Column arguments.',
                    const=True,
                    default=False,
                    type=strtobool,
                    nargs='?')
parser.add_argument('-y', '--destination-row',
                    help=f'Destination row for path display (default {default_destination_row}). Requires -p.',
                    type=int,
                    default=default_destination_row)
parser.add_argument('-x', '--destination-column',
                    help=f'Destination column for path display (default {default_destination_column}). Requires -p.',
                    type=int,
                    default=default_destination_column)
parser.add_argument('-p', '--show-path',
                    help='Show path from start to destination. Implies -d.',
                    const=True,
                    default=False,
                    type=strtobool,
                    nargs='?')

args = parser.parse_args()
if args.show_path:
    args.show_distances = True
if args.start_row < 0: args.start_row = 0
if args.start_row >= args.rows: args.start_row = args.rows - 1
if args.start_column < 0: args.start_column = 0
if args.start_column >= args.columns: args.start_column = args.columns -1
if args.destination_row < 0: args.destination_row = 0
if args.destination_row >= args.rows: args.destination_row = args.rows - 1
if args.destination_column < 0: args.destination_column = 0
if args.destination_column >= args.columns: args.destination_column = args.columns -1
algorithm = build_bt_maze
if args.algorithm == 'sidewinder':
    algorithm = build_sidewinder_maze

if args.show_distances:
    grid = DistanceGrid(args.rows, args.columns)
    algorithm(grid)
    grid.distances_from(grid[args.start_row,args.start_column])
    print(grid)
    if args.show_path:
        grid.path_to(grid[args.destination_row, args.destination_column])
        print(grid)
else:
    grid = Grid(args.rows, args.columns)
    algorithm(grid)
    print(grid)
