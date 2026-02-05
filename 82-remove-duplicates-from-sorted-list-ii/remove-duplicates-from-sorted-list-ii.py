# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        D 1 2 3 3 4 4 5
            ↑ p r r
        '''
        if not head:
            return
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                v = cur.val
                while cur and cur.val == v:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next
            
