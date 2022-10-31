'''
Maximum perimeter triangle
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # Sort the sticks
    sticks.sort()
    n=len(sticks)
    # Start iterating backwards. until the index 1 to avoid out of bounds.
    for i in range(n-1, 1, -1):
        # if previous 2 sides are greater than current element, return the solution.
        if sticks[i] < sticks[i-1] + sticks[i-2]:
            return [sticks[i-2], sticks[i-1], sticks[i]]
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
