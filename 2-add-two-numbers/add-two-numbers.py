# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        lst1 = deque()
        lst2 = deque()
        while cur1:
            lst1.appendleft(cur1.val)
            cur1 = cur1.next
        while cur2:
            lst2.appendleft(cur2.val)
            cur2 = cur2.next
        
        sum_num = sum_num = str(int(''.join(str(i) for i in lst1)) + int(''.join(str(i) for i in lst2)))
        dummy = ListNode(0)
        cur = dummy
        for i in reversed(sum_num):
            cur.next = ListNode(int(i))
            cur = cur.next
        
        cur.next = None
        
        return dummy.next
