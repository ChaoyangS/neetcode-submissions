class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        i,j = 0,len(heights)-1
        while i<j:
            cur = (j-i)*min(heights[i],heights[j])
            maxwater = max(maxwater,cur)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return maxwater
        