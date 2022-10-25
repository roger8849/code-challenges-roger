"""
Pangrams
https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true4
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    letterCount = Counter(s.lower())
    # print(letterCount)
    start, end = ord('a'), ord('z')
    for i in range(start, end + 1):
        char = chr(i)
        if not char in letterCount:
            return "not pangram"
    return "pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
