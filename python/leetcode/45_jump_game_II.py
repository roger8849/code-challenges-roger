"""
55. Jump Game
Medium

Share
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List


class Solution:

  def jump(self, nums: List[int]) -> int:
    size = len(nums)
    if size == 1: return 0
    if nums[0] == 0: return -1

    ladder = nums[0]  # Max reachable index
    stair = nums[0]  # current ladder
    jump = 1
    for i in range(1, size):
      if i == size - 1: return jump
      if i + nums[i] > ladder:
        ladder = i + nums[i]
      stair -= 1  # Traversing current ladder

      if stair == 0:  # current ladder finished
        jump += 1
        if i >= ladder:
          return -1  # Additionally, we have a check for whether the current index "i" has exceeded the maximum reachable index "ladder". If this is the case, it means that we cannot reach any index further, so -1 is returned to indicate this. The "stair" variable is then updated to the remaining distance to the "ladder."
        stair = ladder - i

    return -1


def main():
  solution = Solution()
  nums = [2, 3, 1, 1, 4]
  print(
      f'Number of steps to reach last index in {nums} = {solution.jump(nums)}')
  nums = [3, 2, 1, 0, 4]
  print(
      f'Number of steps to reach last index in {nums} = {solution.jump(nums)}')


if __name__ == "__main__":
  main()
