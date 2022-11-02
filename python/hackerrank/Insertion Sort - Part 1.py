'''
Insertion Sort - Part 1
https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    for i in range(len(arr)-1, -1,-1):
        if i > 0:
            if val < arr[i-1]:
                arr[i] = arr[i-1]
            else:
                arr[i]=val
                print(*arr)
                break
        else:
            arr[0] = val
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

