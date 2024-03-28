#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys

codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) > 4:
            size = int(tokens[-1])
            code = tokens[-2]
            if code in codes.keys():
                codes[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print(f'File size: {total_size}')
            for key, value in codes.items():
                if value != 0:
                    print(f'{key}: {value}')

except Exception as err:
    pass

finally:
    print('File size: {total_size}')
    for key, value in codes.items():
        if value != 0:
            print(f'{key}: {value}')
