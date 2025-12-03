# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. 找到这一组的第 k 个节点
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # 不足 k 个, 不再反转
                    return dummy.next

            group_next = kth.next  # 下一组的起点

            # 2. 反转这一组 [group_prev.next, kth]
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3. 接回到大链表
            # 此时 prev 是这一组反转后的头, group_prev.next 是这一组反转后的尾
            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail
