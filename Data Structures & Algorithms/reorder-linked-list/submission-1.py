# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of LL
        r = slow.next
        rPrev = slow.next = None
        while r:
            rTemp = r.next
            r.next = rPrev
            rPrev = r
            r = rTemp
        
        # Alternately rearrange LL
        r = rPrev
        l = head
        while l and r:
            tempL = l.next
            tempR = r.next
            l.next = r
            r.next = tempL
            l = tempL
            r = tempR
        

        
        