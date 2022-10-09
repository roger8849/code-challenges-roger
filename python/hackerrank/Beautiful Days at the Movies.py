"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def reverseNumber(number):
    rNumber = 0
    while number != 0:
        number, digit = divmod(number, 10)
        rNumber = rNumber * 10 + digit
    return rNumber

def beautifulDays(i, j, k):
    # Write your code here
    bd = 0
    while i <= j:
        temp = abs(i-reverseNumber(i))
        bd = bd + 1 if temp % k == 0 else bd
        i += 1
    return bd

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
