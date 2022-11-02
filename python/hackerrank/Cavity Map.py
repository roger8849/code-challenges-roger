'''
Cavity Map
https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    m = len(grid)
    mod_grid = []
    for i in range(m):
        if i == 0 or i == m-1:
            mod_grid.append(grid[i])
            continue
        n = len(grid[i])
        tempGrid = ''
        for j in range(n):
            if j ==0 or j == n-1:
                tempGrid += grid[i][j]
                continue
            val, up, bottom, left, right = int(grid[i][j]), int(grid[i-1][j]), int(grid[i+1][j]), int(grid[i][j-1]), int(grid[i][j+1])
            if val > up and val > bottom and val > left and val > right:
                tempGrid += 'X'
            else:
                tempGrid += grid[i][j]
        mod_grid.append(tempGrid)
    return mod_grid

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    # assert result == ['989','1X1','111'] if grid == ['989','191','111'] else True

    '''
    STDIN   Function
    -----   --------
    4       grid[] size n = 4
    1112    grid = ['1112', '1912', '1892', '1234']
    1912
    1892
    1234
    '''
    assert result == ['1112','1X12','18X2','1234'] if grid == ['1112','1912','1892','1234'] else True
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
