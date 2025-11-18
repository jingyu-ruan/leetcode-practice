# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            nxt = cur.next
            nxtnxt = cur.next.next
            nxtnxtnxt = cur.next.next.next
            cur.next = nxtnxt
            nxtnxt.next = nxt
            nxt.next = nxtnxtnxt
            cur = cur.next.next
        return dummy.next