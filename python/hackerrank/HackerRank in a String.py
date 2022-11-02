'''
HackerRank in a String!
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    hackerrank = 'hackerrank'
    globalIndex = 0 
    for h in hackerrank:
        while globalIndex < len(s):
            if s[globalIndex] == h:
                globalIndex += 1
                break
            else:
                globalIndex += 1
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
