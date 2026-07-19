class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashset requires O(n) memory
        # linked list cycle
        # think of the values as pointer
        #multiple nodes points to the same node - cycle
        # floyd's to find the beginning of a cycle
        fast,slow = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        