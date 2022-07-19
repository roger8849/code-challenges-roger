'''
98. Validate Binary Search Tree
Medium

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
import math
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def helper(self,root: TreeNode, minValue: int, maxValue: int) -> bool:
        if not root:
            return True
        isLeft = self.helper(root.left, minValue, root.val)
        isRight = self.helper(root.right, root.val, maxValue)

        if isLeft and isRight and root.val > minValue and root.val < maxValue :
            return True
        return False

    def isValidBSTUsingIndex(self, root: Optional[TreeNode]) -> bool:
        infinity = sys.maxsize
        return self.helper(root, -infinity, infinity)

    # In order traversal 
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

