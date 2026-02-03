# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1, p2 = list1, list2
        dummy = ListNode(0)
        cur = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        while p1:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
        while p2:
            cur.next = p2
            p2 = p2.next
            cur = cur.next
        # cur.next = None
        return dummy.next
        

