class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def rob1(nums):
            n = len(nums)
            dp = [0]*(n+2)
            for i, num in enumerate(nums):
                dp[i+2]=max(dp[i+1],dp[i]+num)
            return dp[n+1]
        
        return max(rob1(nums[1:]),rob1(nums[2:-1])+nums[0])


        