class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashset requires O(n) memory
        # linked list cycle
        # think of the values as pointer
        #multiple nodes points to the same node - cycle
        # floyd's to find the beginning of a cycle

        #for a list - if the value is bounded, it's a natural linked list, with index and value, value is the pointer, index is the node#
        #2 passes, first pass to find the meeting point
        #second pass to find the start of the loop
        fast,slow = 0,0
        while True:
            slow = nums[slow]
            #one step faster
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        