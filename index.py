# index.py

import sys

from typing import List
import argparse

Row = List[int]
Matrix = List[Row]


def create_matrix(raw_matrix: str) -> Matrix:
    """Converts a raw string into a matrix of 0 and 1"""

    rows = raw_matrix.split(";")

    try:
        matrix = [list(map(int, row.split(","))) for row in rows]
    except ValueError:
        raise Exception("Please provide a valid input")

    return matrix


def get_areas(matrix: Matrix) -> int:
    """Returns the number of areas formed of number 1"""

    def has_previous_neighbors(i: int, j: int) -> bool:
        has_left_neighbor = (j > 0) and matrix[i][j - 1] == 1
        has_upper_neighbor = (i > 0) and matrix[i - 1][j] == 1

        return has_left_neighbor or has_upper_neighbor

    num_areas = 0

    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column == 1 and not has_previous_neighbors(i, j):
                num_areas += 1

    return num_areas


def main(raw_matrix: str) -> int:
    """Main entry, converts a raw string into a matrix and returns the number of areas formed of number 1"""

    matrix = create_matrix(raw_matrix)

    num_areas = get_areas(matrix)

    return num_areas


def parse_args(args):
    """Parse args from arguments"""
    parser = argparse.ArgumentParser(description="Returns the number of areas in a matrix.")
    parser.add_argument("matrix", 
        help='A matrix of values 0 and 1, columns are separated by commas (,) \
            and rows are separated by semicolons (;): "1,0,1;0,1,0"')

    return parser.parse_args(args)


if __name__ == '__main__':
    parser = parse_args(sys.argv[1:])

    print(main(parser.matrix))
    sys.exit(0)
