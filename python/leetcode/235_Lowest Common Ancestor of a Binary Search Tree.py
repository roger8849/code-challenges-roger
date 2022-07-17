'''
235. Lowest Common Ancestor of a Binary Search Tree
Easy

Share
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
            Assumptions:    nodes are in the tree.
                            Is a binary search tree
                            The tree only contains unique elements.
        '''
        while root:
            # if any of the values is the root the we found the lowest common ancestor.
            if p==root or q==root:
                return root
            # if values are lower both go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # if values are greater both go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # this is the common ancestor because the values are in different sides of the tree
                return root

        return None
def main():
    sol = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    result = sol.lowestCommonAncestor(root, root.left.right.right, root.left)
    assert result ==  root.left

    result = sol.lowestCommonAncestor(root, root.left.right.right, root.right.right)
    assert result == root
    
    result = sol.lowestCommonAncestor(root, root.left.right.left, root.left.right.right)
    assert result == root.left.right

if __name__ == "__main__":
    main()