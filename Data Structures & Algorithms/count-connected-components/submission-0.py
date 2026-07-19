class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        cc = 0
        adj = defaultdict(list)
        visited = set()
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        for i in range(n):
            if i in visited:
                continue
            cc += 1  # New connected component
            q = deque([i])
            visited.add(i)
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return cc

        