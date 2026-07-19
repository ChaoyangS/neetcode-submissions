class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra
        minheap = [(0,k)]
        t = 0
        visit = set()
        while minheap:
            time,node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            t = max(t,time)
            for s,e,w in times:
                if s==node and e not in visit:
                    heapq.heappush(minheap,(t+w,e))
        return t if len(visit)==n else -1
        