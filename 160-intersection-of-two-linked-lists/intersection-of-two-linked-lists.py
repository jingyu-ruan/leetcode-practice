# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cura = headA
        curb = headB
        seta = set()
        while cura:
            seta.add(cura)
            cura = cura.next
        while curb:
            if curb in seta:
                return curb
            curb = curb.next
        
        return None