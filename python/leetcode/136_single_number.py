'''
136. Single Number
Easy

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
            This solution is using xor properties:
            A^A=0
            A^0=A
            A^B^A^C^C = B equals cancel to each other
        '''
        unique = 0
        for i in nums:
            unique ^= i
        return unique
def main():
    solution = Solution()
    nums = [2,2,1]
    print(f'single number in {nums} is {solution.singleNumber(nums)}')

    nums = [4,1,2,1,2]
    print(f'single number in {nums} is {solution.singleNumber(nums)}')

    nums = [1]
    print(f'single number in {nums} is {solution.singleNumber(nums)}')

if __name__ == "__main__":
    main()