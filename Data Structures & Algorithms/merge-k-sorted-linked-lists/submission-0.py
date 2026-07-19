# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        def mergeTwoLists(list1,list2):
            cur = dummy = ListNode(0)
            while list1 and list2:
                if list1.val<=list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list1
                    list1 = cur.next.next
                cur = cur.next
            if not list1:
                cur.next = list2
            else:
                cur.next = list1    
            return dummy.next
        amount = len(lists)
        interval = 1
        while interval<amount:
            for i in range(0,amount-interval, interval*2):
                lists[i]=mergeTwoLists(lists[i],lists[i+interval])
            interval *= 2
        return lists[0] if amount >0 else None



        

        