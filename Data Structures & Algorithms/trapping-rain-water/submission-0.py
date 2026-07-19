class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        #from right to left
        maxL = [0]*len(height)
        maxR = [0]*len(height)
        for i in range(1,len(height)):
            maxL[i] = max(maxL[i-1],height[i-1])
        for j in range(len(height)-2,-1,-1):
            maxR[j] = max(maxR[j+1],height[j+1])
        for i in range(len(height)):
            cur = min(maxL[i],maxR[i])-height[i]
            curw = cur if cur>0 else 0
            res += curw

           
                
        return res
        