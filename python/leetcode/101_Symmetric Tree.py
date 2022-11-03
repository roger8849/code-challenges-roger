'''
100. Same Tree
Easy

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameSymmetricTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # If both roots are None then are equal
        if left == None and right == None: return True
        # If not then are not equal
        elif (left==None and right != None) or (left!=None and right==None): return False

        # If nodes are equal and left and right tree are equal then true
        if left.val == right.val and self.isSameSymmetricTree(left.left, right.right) and self.isSameSymmetricTree(left.right, right.left):
            return True
        # Otherwise false.
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameSymmetricTree(root.left, root.right)
        