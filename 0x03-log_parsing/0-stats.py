#!/usr/bin/python3
""" Reads metrics from stdin, computes an prints back to stdout """
import sys


def print_metrics(total, cache):
    """ prints metric in specified format """
    print(f"File size: {total}")
    for code, count in cache.items():
        if count:
            print(f"{code}: {count}")


codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
         "405": 0, "500": 0}
size = 0
line_number = 0

try:
    for line in sys.stdin:
        tokens = line.split(" ")
        if len(tokens) == 9:
            file_size = int(tokens[-1])
            status = tokens[-2]
            if status in codes:
                codes[status] += 1
            line_number += 1
            size += file_size
        if line_number == 10:
            print_metrics(size, codes)
            line_number = 0

except Exception as error:
    pass

finally:
    print_metrics(size, codes)
