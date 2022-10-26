'''
Game of Thrones - I
https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations
#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    freq = Counter(s)
    oddFeq = 0
    for val in freq.values():
        if val % 2 == 1:
            oddFeq += 1
        if oddFeq > 1:
            return 'NO'
    return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
