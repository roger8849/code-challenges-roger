'''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from typing import List


class Solution:

    # Only works if the List is sorted.
    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        while start < end:
            sum = nums[start]+nums[end]
            if sum > target:
                end -=1
            elif sum < target:
                start +=1
            else:
                return [start,end]
        return list()
    
    #Worst approach.
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return list()
    
    #Using extra space.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()
        # Base case if list hast less of two elements.
        size = len(nums)
        if size < 2:
            return list()
        
        for index in range(size) :
            # print(index)
            # If the dictionary is empty then add first element
            if not bool(memory) :
                memory[nums[index]] = index
            else:
                compliment = target - nums[index]
                # If compliment is not less than 0 to avoid index less than 0
                # if not compliment < 0:
                if compliment in memory :
                    return [memory[compliment], index]
                else :
                    memory[nums[index]] = index
                    
        return list()

def main():
    solution = Solution()

    # print(solution.twoSumBruteForce([2,7,11,15],9))
    # print(solution.twoSumBruteForce([3,2,4],6))
    # print(solution.twoSumBruteForce([3,3],6))

    # print(solution.twoSumSort([2,7,11,15],9))
    # print(solution.twoSumSort([3,2,4],6))
    # print(solution.twoSumSort([3,3],6))
    
    # print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))
    print(solution.twoSum([3,3],6))
    print(solution.twoSum([-16,3,2,10,4],6))

if __name__ == "__main__":
    main()