# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        def dfs(last_end):
            cur = last_end
            cur_start = cur.next
            for _ in range(k):
                cur = cur.next
                if not cur:
                    return
            
            cur_end = cur
            next_start = cur.next
            last_end.next = None
            cur_end.next = None
            # reverse
            p = cur_start
            prev = None
            while p:
                nxt = p.next
                p.next = prev
                prev = p
                p = nxt
            
            last_end.next = cur_end
            cur_start.next = next_start
            dfs(cur_start)
        
        dfs(dummy)
        return dummy.next