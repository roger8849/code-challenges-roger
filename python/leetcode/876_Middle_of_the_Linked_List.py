'''
876. Middle of the Linked List
Easy

Share
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
Accepted
697,714
Submissions
957,113
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        slow_index, fast_index = head, head.next

        while fast_index and fast_index.next:
            slow_index = slow_index.next
            fast_index = fast_index.next.next
        else:
            if not fast_index:
                return slow_index
            elif not fast_index.next:
                return slow_index.next

def main():
    pass

if __name__ == "__main__":
    main()