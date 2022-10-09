"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def removeDuplicates(ranked) -> int:
    # init left index in 0
    left_index = int()
    # right index starts at 1 until len of the array nums
    for right_index in range(1, len(ranked)):
        # if nums left_index is not nums in right index, replace
        if not ranked[left_index] == ranked[right_index]:
            #replace in left index + 1 to not replace original.
            ranked[left_index + 1] = ranked[right_index]
            #move left index to replace next element
            left_index += 1
    ranked = ranked[:left_index+1]
    return ranked

# Use of binary iterative to find the element and/or the insert index
def searchInsert(ranked, score) -> int:
    start = 0
    end = len(ranked) - 1
    mid = 0
    # Base cases
    if score >= ranked[0]:
        return 1
    elif score == ranked[-1]:
        return end + 1
    elif score < ranked[-1]:
        return end + 2
    # Binary search.
    while start <= end:
        mid = start + (end-start)//2

        if score == ranked[mid]:
            return mid + 1
        elif score < ranked[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start + 1

def climbingLeaderboard(ranked, player):
    ranked = removeDuplicates(ranked)
    result = list()
    for score in player:
        result.append(searchInsert(ranked, score))
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    assert ranked == [100,50,40,20,10]

    assert result == [6,4,2,1]

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
