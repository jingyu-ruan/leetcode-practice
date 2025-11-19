# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = set()
        cur = head
        while cur:
            if cur in dic:
                return cur
            if cur not in dic:
                dic.add(cur)
            
            cur = cur.next
        return None