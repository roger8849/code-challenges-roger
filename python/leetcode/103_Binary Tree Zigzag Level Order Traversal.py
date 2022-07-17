'''
103. Binary Tree Zigzag Level Order Traversal
Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, levelArray, helperQueue = [], [], []
        leftToRight = True
        if not root:
            return result
        helperQueue.append(root)
        helperQueue.append(None)
        while helperQueue:
            firstElement = helperQueue.pop(0)
            # If first element is not None flag
            if firstElement:
                # Add it to the level
                levelArray.append(firstElement.val)
                # Add left if exists.
                if firstElement.left:
                    helperQueue.append(firstElement.left)
                # Add right if exists.
                if firstElement.right:
                    helperQueue.append(firstElement.right)
            else:
                if not leftToRight:
                    levelArray = levelArray[::-1]
                # Push existing and then start a new level.
                if levelArray:
                    result.append(levelArray)
                # Start a new level.
                levelArray=[]
                # Once a level is completed then revert the order.
                leftToRight = not leftToRight
                # If queue still has elements then add flag for new level.
                if helperQueue:
                    helperQueue.append(None)
        return result

def main():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(3)
    root.right.right = TreeNode(5)

    result = sol.zigzagLevelOrder(root)
    assert result == [[1], [3,2], [4,5]]


if __name__ == "__main__":
    main()