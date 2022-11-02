'''
Jim and the Orders
https://www.hackerrank.com/challenges/jim-and-the-orders/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    n = len(orders)
    res = []
    for i in range(n):
        order = orders[i][0]
        prep = orders[i][1]
        res.append([i+1, order +prep])        
    res = sorted(res, key = lambda x: (x[1], x[0]))
    # print(res)
    return [customer[0] for customer in res]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
