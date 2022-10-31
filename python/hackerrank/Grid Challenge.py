'''
Grid Challenge
https://www.hackerrank.com/challenges/grid-challenge/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    # Sort each row.
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    # Check each column is sorted.
    for column in range(len(grid[0])):
        column_list = [grid[row][column] for row in range(len(grid))]
        if not column_list == sorted(column_list):
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
