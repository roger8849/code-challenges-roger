'''
484. Find Permutation
Medium

Share
A permutation perm of n integers of all the integers in the range [1, n] can be represented as a string s of length n - 1 where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the lexicographically smallest permutation perm and return it.

Example 1:

Input: s = "I"
Output: [1,2]
Explanation: [1,2] is the only legal permutation that can represented by s, where the number 1 and 2 construct an increasing relationship.
Example 2:

Input: s = "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can be represented as "DI", but since we want to find the smallest lexicographical permutation, you should return [2,1,3]
 
Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
'''

from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        start, end, result = 1, len(s) + 1, list()
        for letter in s:
            if letter == 'D':
                result.append(end)
                end -=1
            else:
                result.append(start)
                start +=1
        # Last element pending 
        result.append(start)
        return result

def main():
    solution = Solution()
    s = 'I'
    # result = solution.findPermutation(s)
    # assert result == [1,2]

    s = 'DI'
    result = solution.findPermutation(s)
    assert result == [3,1,2]

if __name__ == "__main__":
    main()