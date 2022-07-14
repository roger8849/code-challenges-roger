'''
86. Partition List
Medium

Share
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead, leftTail, rightHead, rightTail = None, None, None, None
        while head:
            if head.val < x:
                if not leftHead:
                    leftHead = ListNode(head.val)
                    leftTail = leftHead
                else:
                    leftTail.next = ListNode(head.val)
                    leftTail = leftTail.next
            else:
                if not rightHead:
                    rightHead = ListNode(head.val)
                    rightTail = rightHead
                else:
                    rightTail.next = ListNode(head.val)
                    rightTail = rightTail.next
            head = head.next
        else:
            if leftTail:
                leftTail.next = rightHead
        # Left head if there are elements less than x if not then return right head.
        return leftHead if leftHead else rightHead

