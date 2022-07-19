'''
543. Diameter of Binary Tree
Easy

Share
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, root: TreeNode)-> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTreeInefficient(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        option1 = self.height(root.left) + self.height(root.right)
        option2 = self.diameterOfBinaryTreeInefficient(root.left)
        option3 = self.diameterOfBinaryTreeInefficient(root.right)
        return max(option1, option2, option3)
    def heightDiameter(self, root: TreeNode):
        if root == None:
            return 0, 0
        leftH, leftD = self.heightDiameter(root.left)
        rightH, rightD = self.heightDiameter(root.right)

        height = 1 + max(leftH, rightH)
        diameter = max(leftH + rightH, leftD, rightD)
        return height, diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.heightDiameter(root)
        return diameter