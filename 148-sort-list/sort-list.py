# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        cur = head
        lst = []
        while cur:
            lst.append((cur.val, cur))
            cur = cur.next
        lst.sort(key=lambda x: x[0])
        head2 = lst[0][1]
        cur = head2
        for i in range(1, len(lst)):
            cur.next = lst[i][1]
            cur = cur.next
        
        cur.next = None
        return head2