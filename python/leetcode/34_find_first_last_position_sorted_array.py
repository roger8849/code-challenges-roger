'''
34. Find First and Last Position of Element in Sorted Array
Medium
Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List


class Solution:
    def findFirst(self, nums: List[int], target: int)-> List[int]:
        '''
            Use Binary search to find first occurrence.
        '''
        start, end = 0, len(nums) - 1
        answer = -1
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            if nums[mid] == target:
                answer = mid
                end = mid -1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return answer
    
    def findLast(self, nums: List[int], target: int)-> List[int]:
        '''
            Use Binary search to find last occurrence.
        '''
        start, end = 0, len(nums) - 1
        answer = -1
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            if nums[mid] == target:
                answer = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return answer

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        first = self.findFirst(nums, target)
        if first == -1 :
            last = first
            return [first,last]
        else:
            last = self.findLast(nums, target)
        return [first,last]

def main():
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(f'First and last position in array {nums} of {target} is {solution.searchRange(nums, target)}')
    target = 5
    print(f'First and last position in array {nums} of {target} is {solution.searchRange(nums, target)}')
    target = 6
    print(f'First and last position in array {nums} of {target} is {solution.searchRange(nums, target)}')
    
    nums = []
    target = 0
    print(f'First and last position in array {nums} of {target} is {solution.searchRange(nums, target)}')


if __name__ == "__main__":
    main()