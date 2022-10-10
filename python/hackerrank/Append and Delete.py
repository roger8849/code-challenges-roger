'''
https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&isFullScreen=false
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    len_s = len(s)
    len_t = len(t)
    y = 'Yes'
    n = 'No'
    idx = 0
    if (len_s + len_t) % 2 != 0 and k % 2 == 0 and k < (len_s + len_t):
        return n
    if (len_s + len_t) % 2 == 0 and k % 2 != 0 and k < (len_s + len_t):
        return n
    for i in range(min(len_s,len_t)):
        if s[i] != t[i]:
            break
        else:
            idx = i+1
    if (max(len_s,len_t) - idx + min(len_s,len_t) - idx) <= k:
        return y
    else:
        return n
    



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    # fptr.write(result + '\n')

    # fptr.close()
