from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        good_pos = size - 1
        for i in range(size-2, -1, -1):
            if i + nums[i] >= good_pos:
                good_pos = i
        if good_pos == 0:
            return True 
        else: return False
def main():
    solution = Solution()
    nums = [2,3,1,1,4]
    print(f'Can reach last index in {nums} = {solution.canJump(nums)}')
    nums = [3,2,1,0,4]
    print(f'Can reach last index in {nums} = {solution.canJump(nums)}')

if __name__ == "__main__":
    main()