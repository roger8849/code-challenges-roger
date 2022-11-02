'''
Mars Exploration
https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    sos = 'SOS'
    n = len(sos)
    diff = 0
    for i in range(len(s)):
        sosPos = i % n
        if s[i] != sos[sosPos]:
            diff += 1
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
