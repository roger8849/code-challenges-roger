"""
https://www.hackerrank.com/challenges/magic-square-forming/problem?h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&isFullScreen=true
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    minCost = sys.maxsize
    # there are only 8 magic squares with 5 in the middle. other possibilities are rotations around 5.
    magicSquares = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]

    for matrix in magicSquares:
        matrixCost = (
            abs(matrix[0][0]-s[0][0]) + abs(matrix[0][1]-s[0][1]) + abs(matrix[0][2]-s[0][2]) 
            + abs(matrix[1][0]-s[1][0]) + abs(matrix[1][1]-s[1][1]) + abs(matrix[1][2]-s[1][2])
            + abs(matrix[2][0]-s[2][0]) + abs(matrix[2][1]-s[2][1]) + abs(matrix[2][2]-s[2][2])
        )
        minCost = matrixCost if matrixCost < minCost else minCost
    return minCost


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    assert result == 4
    # fptr.write(str(result) + '\n')

    # fptr.close()
