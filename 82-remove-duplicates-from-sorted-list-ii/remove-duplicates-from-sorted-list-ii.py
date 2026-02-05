# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        D 1 2 3 3 4 4 5
            ↑ p r r
        '''
        if not head:
            return
        dummy = ListNode(0, head)
        cur = head
        vals = defaultdict(int)
        while cur:
            vals[cur.val] += 1
            cur = cur.next
        cur = dummy
        while cur:
            nxt = cur.next
            while nxt and vals[nxt.val] > 1:
                nxt = nxt.next
            cur.next = nxt
            cur = cur.next
        return dummy.next
            
