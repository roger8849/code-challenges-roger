'''
Non-Divisible Subset
https://www.hackerrank.com/challenges/non-divisible-subset/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here

    # Count array to count the frequency of the remainders of k
    count = [0] * k
    for num in s:
        modulo = num % k
        count[modulo] += 1

    # Considering only 1 ocurrence when num % k == 0 or if there's no elements even better take 0.
    ans = min(count[0], 1)

    # Second case when k is even then (k//2 + k//2)  % k  ==0 then only take 1 number.
    if k%2 == 0:
        ans += min(count[k//2], 1)

    for i in range(1, k//2 + 1): #Check for pairs and take the appropiate count.
        if i != k - i: # Avoid over-counting when k is even.
            ans += max(count[i], count[k-i])
    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
