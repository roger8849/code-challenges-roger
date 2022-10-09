"""
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distCatA = abs(x-z)
    distCatB = abs(y-z)
    if distCatA == distCatB:
        return "Mouse C"
    elif distCatA < distCatB:
        return "Cat A"
    else:
        return "Cat B"



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

    #     fptr.write(result + '\n')

    # fptr.close()
