import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        dist = [0.0]*n
        res = []
        for idx,point in enumerate(points):
            dist[idx]=(point[0]**2+point[1]**2)**0.5

        minHeap = []
        for idx, dis in enumerate(dist):
            minHeap.append([dis,idx])
        heapq.heapify(minHeap)

        while k>0:
            cur,curidx = heapq.heappop(minHeap)
            k-=1
            res.append(points[curidx])
        
        return res




        