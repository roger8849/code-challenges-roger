# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper_head = head
        if not head: return head
        while head:
            while head and head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return helper_head

def main():
    solution = Solution()
    solution.deleteDuplicates()
if __name__ == '__main__':
    main()