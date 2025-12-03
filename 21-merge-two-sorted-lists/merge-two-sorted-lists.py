# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur1, cur2 = list1, list2
        cur = dummy
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        
        if cur1:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        
        if cur2:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next

        return dummy.next