'''
1539. Kth Missing Positive Number
Solved
Easy
Topics
Companies
Hint

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

 

Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length

 

Follow up:

Could you solve this problem in less than O(n) complexity?
'''


from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        positives = set([x for x in arr if x > 0])
        missing = 0
        for i in range(1,k + arr[-1]):
            if not i in positives:
                missing += 1
                if missing == k:
                    return i
        return arr[-1] + k
        