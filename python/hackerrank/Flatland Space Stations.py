'''
Flatland Space Stations
https://www.hackerrank.com/challenges/flatland-space-stations/problem?isFullScreen=true
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    c.insert(0,-c[0]) # Insert left edge to validate if city 0 has the longest distance
    c.append(2*(n-1)-c[-1]) # Insert right edge to validate if city n-1 has the longest distance
    m = len(c)
    return max([(c[i+1] - c[i])//2 for i in range(m-1)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    '''
    20 5
    13 1 11 10 6
    6
    '''

    fptr.write(str(result) + '\n')

    fptr.close()
