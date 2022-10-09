'''
https://www.hackerrank.com/challenges/find-digits/problem?h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy, n = 100, len(c)
    index = k % n
    while index != 0:
        energy -= 1
        if c[index] == 1:
            energy -= 2
        index = (index + k) % n
    return energy - 1 if c[index] == 0 else energy - 3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
