# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        dummy = ListNode(0, head)
        cur = head
        left = dummy
    
        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate_val = cur.val
                while cur and cur.val == duplicate_val:
                    cur = cur.next
                left.next = cur
            else:
                left = cur
                cur = cur.next
        
        return dummy.next