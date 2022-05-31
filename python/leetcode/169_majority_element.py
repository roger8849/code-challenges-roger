'''
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

'''

from typing import List

class Solution:
    # Brute force, iterate each element and check the rest of the list to identify the majority element
    def majorityElementBruteForce(self, nums:List[int])-> int:
        majority_element = None
        # To not import sys.minint then init in -1
        max_occurrence = -1
        for i in range(len(nums)-1):
            majority_element = nums[i] if not majority_element else majority_element
            current_occurrence = 1
            for j in range(i+1, len(nums)):
                if majority_element == nums[j]:
                    current_occurrence +=1
            if current_occurrence > max_occurrence:
                majority_element = nums[i]
                max_occurrence = current_occurrence

        return majority_element

    # Save the occurence in a dictionary count the occurrences and then iterate the dictionary
    # O(m+n) where N number of elements and M number of unique elements in list.
    # S(m) Number of unique elements in nums.
    def majorityElementMemorization(self, nums:List[int])-> int:
        occurrences_map = dict()
        # Iterate elements and count them.
        for num in nums:
            if num in occurrences_map:
                occurrences_map[num] += 1
            else:
                occurrences_map[num] = 1

        max_occurence = -1
        majority_element = None

        # Find majority element in dictionary.
        for num, ocurrence in occurrences_map.items():
            if ocurrence > max_occurence:
                max_occurence = ocurrence
                majority_element = num

        return majority_element

    # Sort the array and because there is always a majority element is in the n/2 index
    # This is because the majority element is in the array > n/2
    # O(nlog n) use Timsort which has that complexity.
    # S(1) no extra space.
    def majorityElementSorting(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums)//2]

    # Boyer Moore voting algorithm the majority element always have more votes because has more that n/2 elements.
    # O(n) iterate entire list.
    # S(1) no extra space
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = None
        count = 0

        # Base algorithm.
        #length = len(nums)
        #if not length:
        #    return None
        #elif length == 1:
        #    return nums[0]

        for num in nums:
            # Assume that first element is the majority element.
            majority_element = num if not majority_element else majority_element
            if majority_element == num:
                count += 1
            else:
                count -= 1
            # if count is 0 then the count starts at 1 and num is my new candidate
            if count == 0:
                majority_element = num
                count = 1

        return majority_element

def main():
    solution = Solution()
    print('---Boyer Moore algorithm---')
    print(solution.majorityElement([3,2,3]))
    print(solution.majorityElement([2,2,1,1,1,2,2]))

    print('---Sorting algorithm---')
    print(solution.majorityElementSorting([3,2,3]))
    print(solution.majorityElementSorting([2,2,1,1,1,2,2]))
    
    print('---Memorization algorithm---')
    print(solution.majorityElementMemorization([3,2,3]))
    print(solution.majorityElementMemorization([2,2,1,1,1,2,2]))
    
    print('---Brute Force algorithm---')
    print(solution.majorityElementBruteForce([3,2,3]))
    print(solution.majorityElementBruteForce([2,2,1,1,1,2,2]))

if __name__ == "__main__":
    main()