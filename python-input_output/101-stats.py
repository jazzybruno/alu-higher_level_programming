#!/usr/bin/python3
"""Reads access-log lines from stdin and prints running statistics.

Every 10 lines, at the end of input and on CTRL+C, prints the total
file size and the number of lines per known status code.
"""
import sys

CODES = ("200", "301", "400", "401", "403", "404", "405", "500")


def print_stats(total_size, counts):
    """Print the total file size and the non-zero status code counts."""
    print("File size: {}".format(total_size))
    for code in CODES:
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


if __name__ == "__main__":
    total_size = 0
    counts = {code: 0 for code in CODES}
    nb_lines = 0
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                if parts[-2] in counts:
                    counts[parts[-2]] += 1
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
            nb_lines += 1
            if nb_lines % 10 == 0:
                print_stats(total_size, counts)
        print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise
