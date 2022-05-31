'''
35. Search Insert Position
Easy

Share
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

from typing import List

class Solution:
    # Using python built in functions.
    def searchInsertBuilIn(self, nums: List[int], target: int) -> int:
        #Insert the element
        nums.append(target)
        # sort the new element
        nums.sort()
        # if the element exist return the first index.
        return nums.index(target)

    # Use of binary iterative to find the element and/or the insert index
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        mid = 0
        while low <= high:
            mid = (high+low) // 2
            # if target is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1 
            # if target is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1
            # Means element is present at mid.
            else:
                return mid
        # If the element is not found then should be inserted in low. because low > high.
        return low

def main():
    solution = Solution()
    print('--- Built in functions ---')
    print(solution.searchInsert([1,3,5,6],5))
    print(solution.searchInsert([1,3,5,6],2))
    print(solution.searchInsert([1,3,5,6],7))
    print('--- Binary Search ---')
    print(solution.searchInsert([1,3,5,6],5))
    print(solution.searchInsert([1,3,5,6],2))
    print(solution.searchInsert([1,3,5,6],7))

if __name__ == "__main__":
    main()