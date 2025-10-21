# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = set()
        pos = head
        while pos:
            res.add(pos)
            pos = pos.next
            if pos in res:
                return True
        return False