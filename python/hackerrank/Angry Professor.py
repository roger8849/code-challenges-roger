"""
https://www.hackerrank.com/challenges/angry-professor/problem?h_r=next-challenge&h_v=zen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from turtle import ontimer

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    onTime = [time for time in a if time<=0]
    return 'NO' if len(onTime) >= k else 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

    #     fptr.write(result + '\n')

    # fptr.close()
