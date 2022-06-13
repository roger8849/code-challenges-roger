from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n-1
        while start <= end:
            mid = start + (end - start)//2 # (start+end)//2 to avoid int overflow
            next = (mid + 1 )% n
            prev = (mid - 1 + n)% n

            if nums[mid] <= nums[prev] and nums[mid]<=nums[next]:
                # How many times a sorted array is rotated
                # return mid
                return nums[mid]
            elif nums[mid] <= nums[end]:
                end = mid - 1
            elif nums[mid] >= nums[start]:
                start = mid + 1
        return -1 # never executed there's always a min element in rotated sorted array.

def main():
    solution = Solution()
    nums = [3,4,5,1,2]
    print(f'Min element in nums {nums} is {solution.findMin(nums)}')
    nums = [4,5,6,7,0,1,2]
    print(f'Min element in nums {nums} is {solution.findMin(nums)}')
    nums = [11,13,15,17]
    print(f'Min element in nums {nums} is {solution.findMin(nums)}')

if __name__ == "__main__":
    main()