'''
206. Reverse Linked List
Easy

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Reversing a linkedlist
        '''
        if not head: return None
        
        previous, current, next = None, head, None
        # While there is still elements in the list
        while current:
            next = current.next # Save the next element before breaking the reference
            current.next = previous # Reverse the link
            previous = current # Move forward
            current = next # Move forward to the saved next
        return previous


def main():
    solution = Solution()
    a, a.next, a.next.next, a.next.next.next, a.next.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)

if __name__ == "__main__":
    main()