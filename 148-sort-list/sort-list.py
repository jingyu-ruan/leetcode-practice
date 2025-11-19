# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        
        arr.sort(key = lambda x: x.val)

        dummy = ListNode(0)
        cur = dummy
        for node in arr:
            cur.next = node
            cur = cur.next
        
        cur.next = None

        return dummy.next
