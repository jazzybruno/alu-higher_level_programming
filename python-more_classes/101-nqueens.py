#!/usr/bin/python3
"""Prints every solution to the N queens puzzle using backtracking."""
import sys


def solve(n):
    """Return all placements of n non-attacking queens.

    Each solution is a list of [row, column] pairs, one per row.
    """
    solutions = []
    cols = []

    def place(row):
        """Try every safe column for this row, then recurse."""
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(cols)])
            return
        for col in range(n):
            if all(c != col and abs(c - col) != row - r
                   for r, c in enumerate(cols)):
                cols.append(col)
                place(row + 1)
                cols.pop()

    place(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in solve(n):
        print(solution)
