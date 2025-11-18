# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1
        
        to_repeat = list_len // k

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        cur = head

        for _ in range(to_repeat):
            group_head = cur
            prev = None

            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            prev_group_tail.next = prev
            group_head.next = cur
            prev_group_tail = group_head


        return dummy.next