from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1: return 0
        if nums[0] == 0: return -1
        
        ladder = nums[0] # Max reachable index
        stair = nums [0] # current ladder
        jump = 1
        for i in range(1, size):
            if i == size-1: return jump
            if i + nums[i] > ladder:
                ladder = i + nums[i]
            stair -= 1 # Traversing current ladder

            if stair == 0: # current ladder finished
                jump += 1
                if i >= ladder: return -1 # Cannot reach any index
                stair = ladder - i

        return -1


def main():
    solution = Solution()
    nums = [2,3,1,1,4]
    print(f'Number of steps to reach last index in {nums} = {solution.jump(nums)}')
    nums = [3,2,1,0,4]
    print(f'Number of steps to reach last index in {nums} = {solution.jump(nums)}')

if __name__ == "__main__":
    main()