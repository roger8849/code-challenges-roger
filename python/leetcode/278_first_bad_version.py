'''
278. First Bad Version
Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1
'''

from typing import List
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False

class Solution:
    def findFirstBadVersionHelper(self, start:int, end:int) -> int:
        '''
            This algorithm use binary search to search for the bad version
        '''
        # there is no bad version
        answer = -1
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            # If is not a bad version then the answer is in the left
            if isBadVersion(mid):
                answer = mid
                end = mid - 1
            else :
                start = mid + 1
        return answer

    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        return self.findFirstBadVersionHelper(start, end)