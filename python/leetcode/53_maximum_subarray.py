'''
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            Implement Kadane's algorithm
        '''
        # Initialize max sum with min value
        max_sum = -(sys.maxsize * 2 + 1)
        # Current sum is 0
        current_sum = 0
        for num in nums:
            current_sum = current_sum + num
            # Max sum is max of current sum and max sum
            max_sum = max(current_sum, max_sum)
            # If current sum is 0 reset the sum to avoid substract values.
            if current_sum < 0:
                current_sum = 0
        return max_sum

def main():
    solution = Solution()
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(f'Maximum sum of array {array} is {solution.maxSubArray(array)}')
    array = [1]
    print(f'Maximum sum of array {array} is {solution.maxSubArray(array)}')
    array = [5,4,-1,7,8]
    print(f'Maximum sum of array {array} is {solution.maxSubArray(array)}')
    

if __name__ == "__main__":
    main()
