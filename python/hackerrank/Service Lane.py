'''
Service Lane
https://www.hackerrank.com/challenges/service-lane/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(cases, width):
    # Write your code here
    return [min(width[case[0]:case[1]+1]) for case in cases]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(cases=cases, width=width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
