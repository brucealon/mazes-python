#!/usr/bin/env python

from mazes import *
import argparse
import sys

default_rows               = 25
default_columns            = 25
default_algorithm          = 'binarytree'
default_start_row          = 0
default_start_column       = 0
default_destination_row    = default_rows - 1
default_destination_column = default_columns - 1
algorithms = {
    'binarytree': build_bt_maze,
    'sidewinder': build_sidewinder_maze
    }

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm',
                        help=f'Choose the algorithm used to build the maze (default {default_algorithm}).',
                        type=str,
                        default=default_algorithm,
                        choices=['binarytree', 'sidewinder'])

    parser.add_argument('-H', '--rows',
                        help=f'Set the number of maze rows (default {default_rows}).',
                        type=int,
                        default=default_rows)
    parser.add_argument('-W', '--columns',
                        help=f'Set the number of maze columns (default {default_columns}).',
                        type=int,
                        default=default_columns)

    parser.add_argument('-r', '--start-row',
                        help=f'Row for distances display (default {default_start_row}). Requires -d.',
                        type=int,
                        default=default_start_row)
    parser.add_argument('-c', '--start-column',
                        help=f'Column for distances display (default {default_start_column}). Requires -d.',
                        type=int,
                        default=default_start_column)

    parser.add_argument('-R', '--destination-row',
                        help=f'Destination row for path display (default {default_destination_row}). Requires -p.',
                        type=int,
                        default=default_destination_row)
    parser.add_argument('-C', '--destination-column',
                        help=f'Destination column for path display (default {default_destination_column}). Requires -p.',
                        type=int,
                        default=default_destination_column)

    parser.add_argument('-d', '--show-distances',
                        help='Show the distances from Row and Column arguments.',
                        action='store_true')
    parser.add_argument('-l', '--show-longest',
                        help='Show the longest path. Implies -d.',
                        action='store_true')
    parser.add_argument('-m', '--show-maximum',
                        help='Show the cell with the maximum distance from the start. Implies -d.',
                        action='store_true')
    parser.add_argument('-p', '--show-path',
                        help='Show path from start to destination. Implies -d.',
                        action='store_true')

    parser.set_defaults(show_distances=False,
                        show_longest=False,
                        show_maximum=False,
                        show_path=False)

    return parser.parse_args()

def validate_arguments(args):
    if args.show_path or args.show_maximum or args.show_longest:
        args.show_distances = True

    messages = []
    if args.start_row < 0 or args.start_row >= args.rows:
        messages.append('Bad start row value.')
    if args.start_column < 0 or args.start_column > args.columns:
        messages.append('Bad start column value.')

    if args.destination_row < 0 or args.destination_row >= args.rows:
        messages.append('Bad destination row value.')
    if args.destination_column < 0 or args.destination_column >= args.columns:
        messages.append('Bad destination column value.')

    if len(messages) > 0:
        print('Unable to comply:')
        for message in messages:
            print('    ' + message)
        print(f'Rows for distances and path should be 0 through {args.rows - 1}.')
        print(f'Columns for distances and path should be 0 through {args.columns - 1}.')
        sys.exit(1)

if __name__ == '__main__':
    args = parse_arguments()
    validate_arguments(args)

    algorithm = algorithms[args.algorithm]

    if args.show_distances:
        grid = DistanceGrid(args.rows, args.columns)
        algorithm(grid)
        grid.distances_from(grid[args.start_row,args.start_column])
        print(grid)

        if args.show_path:
            grid.path_to(grid[args.destination_row, args.destination_column])
            print(grid)

        if args.show_maximum:
            (cell, dist) = grid.max()
            print(f'Farthest cell from {args.start_row}, {args.start_column} is {cell.row}, {cell.column}; distance is {dist}')

        if args.show_longest:
            grid.longest_path()
            print(grid)
    else:
        grid = Grid(args.rows, args.columns)
        algorithm(grid)
        print(grid)
