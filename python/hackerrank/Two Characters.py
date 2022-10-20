'''
Two Characters
https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from itertools import combinations

def alternate(s):
    # Write your code here
    uniques = set(s)
    maxLen = 0
    for a,b in combinations(uniques,2):
        alternates = ''.join([c for c in s if c in (a,b)])
        if not (a*2 in alternates or b*2 in alternates) and len(alternates) > maxLen:
            maxLen = len(alternates)
    return maxLen

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)
    '''
    STDIN       Function
    -----       --------
    10          length of s = 10
    beabeefeab  s = 'beabeefeab'
    '''
    assert result == 5 if s == 'beabeefeab' else True
    # fptr.write(str(result) + '\n')

    # fptr.close()
