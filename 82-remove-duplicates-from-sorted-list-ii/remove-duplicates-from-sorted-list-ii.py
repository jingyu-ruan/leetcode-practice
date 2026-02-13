# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        D 1 2 3 3 4 4 5
        c n
        '''
        if not head:
            return 
        dummy = ListNode(0, head)
        cur = dummy
        nxt = head
        while cur and nxt:
            while nxt and nxt.next and nxt.val == nxt.next.val:
                value = nxt.val
                while nxt and nxt.val == value:
                    nxt = nxt.next
            cur.next = nxt
            nxt = nxt.next if nxt else None
            cur = cur.next
        return dummy.next
