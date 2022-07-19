'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Share
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTreeHelper(self, inorder: List[int], postorder: List[int], inorderStart: int, inorderEnd: int, postorderStart: int, postorderEnd: int) -> TreeNode:
        if inorderStart > inorderEnd:
            return None
        rootData = postorder[postorderEnd]
        rootIndex = -1
        for i in range(inorderStart, inorderEnd + 1):
            if inorder[i] == rootData:
                rootIndex = i
                break
        
        leftInorderStart = inorderStart
        leftInorderEnd = rootIndex - 1
        leftPostorderStart = postorderStart
        leftPostorderEnd = leftPostorderStart + leftInorderEnd - leftInorderStart

        rightInorderStart = rootIndex + 1
        rightInorderEnd = inorderEnd
        rightPostorderStart = leftPostorderEnd + 1
        rightPostorderEnd = postorderEnd - 1

        root = TreeNode(rootData)
        root.left = self.buildTreeHelper(inorder, postorder, leftInorderStart, leftInorderEnd, leftPostorderStart, leftPostorderEnd)
        root.right = self.buildTreeHelper(inorder, postorder, rightInorderStart, rightInorderEnd, rightPostorderStart, rightPostorderEnd)
        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        return self.buildTreeHelper(inorder, postorder, 0, n-1, 0, n-1)
        