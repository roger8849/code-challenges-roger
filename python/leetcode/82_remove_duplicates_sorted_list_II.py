# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        prev = dummy_head
    
        if not head or not head.next: return head
        
        while head:
            if head and head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head.next = head.next.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy_head.next

def main():
    solution = Solution()
    solution.deleteDuplicates()
if __name__ == '__main__':
    main()