'''
Extra Long Factorials
https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    n1=1
    # Factorial DP
    for i in range(1,n+1):
        n1 = i * n1
    print(n1)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
