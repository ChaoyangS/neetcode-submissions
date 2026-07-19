from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #create adjacency list, indegree
        #topological sort
        #identify cycle, if there's cycle, return false, if not, return true


        if len(edges)!=n-1:
            return False
        adj = defaultdict(list)
        
        # indegree = [0]*n

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = set()
        
        q = deque([0])
        visited.add(0)

        while q:
            cur = q.popleft()
            

            for nei in adj[cur]:
                if nei in visited:
                    continue
                visited.add(nei)
                adj[nei].remove(cur)
                q.append(nei)
        return len(visited)==n
