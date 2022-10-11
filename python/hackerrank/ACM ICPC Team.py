"""
ACM ICPC Team
https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
"""

#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    maxTopic = -1
    topicsDict = defaultdict(int)
    
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            topics = str(int(topic[i]) + int(topic[j]))
            numTopics = topics.count('1') + topics.count('2')
            topicsDict[numTopics] += 1
            maxTopic = max(maxTopic, numTopics)

    return [maxTopic, topicsDict[maxTopic]]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    '''
        4 5
        10101
        11100
        11010
        00101
    '''
    assert result == [5,2] if topic == ['10101', '11100', '11010', '00101'] else True

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
