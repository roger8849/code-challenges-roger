'''
110. Balanced Binary Tree
Easy

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
Accepted
924,674
Submissions
1,926,983
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root:Optional[TreeNode]) -> bool:
        if not root:
            return 0
        lefthHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        return 1 + max(lefthHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return True if abs(leftHeight-rightHeight) < 2 else False


def main():
    solution = Solution()
    tree = TreeNode(1,TreeNode(2,TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),TreeNode(2))
    assert solution.isBalanced(tree) == False
if __name__ == "__main__":
    main()
