'''
Luck Balance
https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    
    n = len(contests)
    nonImportantLuck = sum([contests[i][0] for i in range(n) if contests[i][1] != 1])
    importants = [contests[i][0] for i in range(n) if contests[i][1] == 1]
    importants.sort(reverse=True)
    lowerImportants = []
    for i in range(len(importants) - k):
        if importants:
            lowerImportants.append(importants.pop())

    return nonImportantLuck + sum(importants) - sum(lowerImportants)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))


    '''
    STDIN       Function
    -----       --------
    6 3         n = 6, k = 3
    5 1         contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    2 1
    1 1
    8 1
    10 0
    5 0
    '''

    result = luckBalance(k, contests)

    assert result == 29 if k==3 and contests == [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]] else True

    # fptr.write(str(result) + '\n')

    # fptr.close()
