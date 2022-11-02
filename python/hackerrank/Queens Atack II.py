'''
Queen's Attack II
https://www.hackerrank.com/challenges/queens-attack-2/problem
TODO SOLVE THE PROBLEM.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
# TODO Solve issue


def checkDiagonals(matrix, n, row, column):
    ans = 0
    # Top left diagonal.
    i, j = row - 1, column - 1
    while i >= 0 and j >= 0 and matrix[i][j] == 0:
        ans += 1
        i, j = i - 1, j - 1

    # Top right diagonal.
    i, j = row - 1, column + 1
    while i >= 0 and j < n and matrix[i][j] == 0:
        ans += 1
        i, j = i - 1, j + 1

    # Bottom left diagonal.
    i, j = row + 1, column - 1
    while i < n and j >= 0 and matrix[i][j] == 0:
        ans += 1
        i, j = i + 1, j - 1

    # Bottom right diagonal.
    i, j = row + 1, column + 1
    while i < n and j < n and matrix[i][j] == 0:
        ans += 1
        i, j = i + 1, j + 1

    return ans


def checkHorizontal(matrix, n, row, column):
    ans = 0

    # Check left horizontal
    j = column - 1
    while j >= 0 and matrix[row][j] == 0:
        ans += 1
        j -= 1

    # Check right horizontal
    j = column + 1
    while j < n and matrix[row][j] == 0:
        ans += 1
        j += 1

    return ans


def checkVertical(matrix, n, row, column):
    ans = 0

    # Check top vertical
    i = row - 1
    while i >= 0 and matrix[i][column] == 0:
        ans += 1
        i -= 1

    # Check right horizontal
    i = row + 1
    while i < n and matrix[i][column] == 0:
        ans += 1
        i += 1

    return ans


def queensAttackNaive(n, k, r_q, c_q, obstacles):
    # Write your code here
    matrix = [[0 for j in range(n)] for i in range(n)]
    ans = 0
    for o in obstacles:
        matrix[o[0]-1][o[1]-1] = 1

    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    ans += checkDiagonals(matrix, n, r_q - 1, c_q - 1)
    ans += checkVertical(matrix, n, r_q - 1, c_q - 1)
    ans += checkHorizontal(matrix, n, r_q - 1, c_q - 1)

    return ans


def getCellsQueenCanAttack(queenX, queenY, n):
    '''
        getCellsQueenCanAttack() – The queen can attack diagonal and orthogonal. 
        For orthogonal, the number of cells is 2n -2 for diagonals the number of 
        cells is given by 2n – 2 – |x – y| – |x + y – n – 1|. 
        Just add the two and you’ll already pass tests for cases with no obstacles.
    '''
    orthogonals = 2 * n - 2
    diagonals = 2 * n - 2 - abs(queenX - queenY) - abs(queenX + queenY - n - 1)
    return orthogonals + diagonals
def getRelativeLocation(queenX, queenY, pawnX, pawnY):
    '''
    getRelativeLocation(queenX, queenY, pawnX, pawnY): this function returns one of the position of the pawn relative to the queen. U for up, D for down, L for left, R for right, UL for upper left, DL for down left etc
    '''
    if pawnY == queenY and pawnX < queenX:
        return 'L'
    if pawnY == queenY and pawnX > queenX:
        return 'R'
    if queenX == pawnX and pawnY < queenY:
        return 'U'
    if queenX == pawnX and pawnY > queenY:
        return 'D'
    
    if abs(queenX - pawnX) == abs(queenY - pawnY):
        if pawnY > queenY and pawnX < queenX:
            return 'UL'
        
        if pawnY > queenY and pawnX > queenX:
            return 'UR'
        
        if pawnY < queenY and pawnX > queenX:
            return 'DR'
        
        if pawnY < queenY and pawnX < queenX:
            return 'DL'
def getCellsBlockedByPawns(queenX, queenY, pawns):
    blockedCells = set()   
    for pawn in pawns:
        x = pawn[1]
        y = pawn[0]
        position = getRelativeLocation(queenX, queenY, x, y)
        if position == 'U':
            for i in range(y, n+1):
                blockedCells.add((i, x))
        if position == 'D':
            for i in range(y, 0, -1):
                blockedCells.add((i, x))
        if position == 'L':
            for i in range(x, 0, -1):
                blockedCells.add((y, i))
        if position == 'R':
            for i in range(x, n+1):
                blockedCells.add((y, i))   
        if position == 'UL':
            while y <= n and x > 0:
                blockedCells.add((y, x))
                x -= 1
                y += 1   
        if position == 'UR':
            while y <= n and x <= n:
                blockedCells.add((y, x))
                x += 1
                y += 1 
        if position == 'DR':
            while y > 0 and x <= n:
                blockedCells.add((y, x))
                x += 1
                y -= 1   
        if position == 'DL':
            while y > 0 and x > 0:
                blockedCells.add((y, x))
                x -= 1
                y -= 1 
    return len(blockedCells)

def queensAttack(n, k, r_q, c_q, obstacles):
    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    '''
    TC 1
    4 0
    4 4

    TC 2
    5 3
    4 3
    5 5
    4 2
    2 3

    TC 3
    1 0
    1 1

    TC 4
    100000 0
    4187 5068
    '''

    assert result == 9 if n == 4 and k == 0 and r_q == 4 and c_q == 4 else True
    assert result == 10 if n == 5 and k == 3 and r_q == 4 and c_q == 3 else True
    assert result == 0 if n == 1 and k == 0 and r_q == 1 and c_q == 1 else True
    assert result == 308369 if n == 100000 and k == 0 and r_q == 4187 and c_q == 5068 else True

    # fptr.write(str(result) + '\n')

    # fptr.close()
