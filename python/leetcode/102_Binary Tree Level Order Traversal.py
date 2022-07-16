'''
102. Binary Tree Level Order Traversal
Medium

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, levelArray, helperQueue = [], [], []
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
                # Push existing and then start a new level.
                if levelArray:
                    result.append(levelArray)
                # Start a new level.
                levelArray=[]
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

    result = sol.levelOrder(root)
    assert result == [[1], [2,3], [4,5]]


if __name__ == "__main__":
    main()


