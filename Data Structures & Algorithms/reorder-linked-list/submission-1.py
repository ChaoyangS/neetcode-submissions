# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        # reverse the second half
        # merge the two parts

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev,cur = None,slow
        
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        #merge
        first,second = head,prev
        

        while second.next:
            first.next,first = second,first.next
            
            second.next,second = first,second.next
            
        

        