from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] +=1
        q = deque([i for i in range(numCourses) if indegree[i]==0])

        res = []
        total = 0
        while q:
            cur = q.popleft()
            res.append(cur)
            total +=1
            for nei in adj[cur]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if total == numCourses else []



        