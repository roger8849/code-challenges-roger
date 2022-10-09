'''
https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
# 6 4 2 6%4 =2 + 2 = 4 -1 = 3 
# 19 7 2    19%7= 5 + 2 + 7-1 = 6 
# 7  3 3    7 % 3 = 1 + 3 = 4 - 1 = 3

def saveThePrisoner(n, m, s):
    return (s + m - 1) % n if (s + m - 1) % n != 0 else n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
