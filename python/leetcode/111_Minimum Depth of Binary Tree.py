'''
111. Minimum Depth of Binary Tree
Easy

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        helperQueue = []

        minDepthLevel = 0 
        if not root:
            return minDepthLevel

        helperQueue.append(root)
        helperQueue.append(None)
        minDepthLevel = 1

        while helperQueue:
            firstElement = helperQueue.pop(0)
            # If first element is not None flag
            if firstElement:
                if firstElement.left is None and firstElement.right is None:
                    return minDepthLevel
                # Add left if exists.
                if firstElement.left:
                    helperQueue.append(firstElement.left)
                # Add right if exists.
                if firstElement.right:
                    helperQueue.append(firstElement.right)
            else:
                # If queue still has elements then add flag for new level.
                if helperQueue:
                    helperQueue.append(None)
                    minDepthLevel += 1

        return minDepthLevel