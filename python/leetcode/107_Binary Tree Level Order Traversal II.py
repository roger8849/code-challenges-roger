'''
107. Binary Tree Level Order Traversal II
Medium

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, levelArray, helperStack = [], [], collections.deque()
        if not root:
             return result
        
        helperStack.appendleft(root)
        helperStack.appendleft(None)
        # helperStack.insert(0, root)
        # helperStack.insert(0, None)

        while helperStack:
            topElement = helperStack.pop()
            if topElement:
                levelArray.append(topElement.val)
                if topElement.left:
                    helperStack.appendleft(topElement.left)
                    # helperStack.insert(0, topElement.left)
                if topElement.right:
                    helperStack.appendleft(topElement.right)
                    # helperStack.insert(0, topElement.right)
            else:
                if levelArray:
                    result.append(levelArray)

                levelArray = []

                if helperStack:
                    helperStack.appendleft(None)
                    # helperStack.insert(0, None)
        return result

def main():
    sol = Solution()

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(3)
    root.right.right = TreeNode(5)

    result = sol.levelOrderBottom(root)
    result.reverse()
    assert result == [[4,5], [2,3], [1]]


if __name__ == "__main__":
    main()


