# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lst = deque()
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        
        for _ in range(k % len(lst)):
            node = lst.pop()
            lst.appendleft(node)
        
        dummy = ListNode(0)
        cur = dummy
        for i in range(len(lst)):
            cur.next = lst[i]
            cur = cur.next
        
        cur.next = None
        
        return dummy.next
