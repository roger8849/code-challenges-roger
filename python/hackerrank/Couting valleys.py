"""
https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    pivot, valleys = 0, 0

    for s in steps :
        if s == 'U':
            pivot +=1
        elif s == 'D' :
            # This means climber has started a valley.
            if pivot == 0:
                valleys += 1
            pivot -=1
    return valleys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
