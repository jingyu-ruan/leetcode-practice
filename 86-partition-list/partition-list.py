# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = []
        right = []
        cur = head
        while cur:
            if cur.val < x:
                left.append(cur)
            else:
                right.append(cur)
            cur = cur.next
        dummy = ListNode(0)
        cur = dummy
        for i in range(len(left)):
            cur.next = left[i]
            cur = cur.next
        
        for j in range(len(right)):
            cur.next = right[j]
            cur = cur.next
        cur.next = None
        return dummy.next