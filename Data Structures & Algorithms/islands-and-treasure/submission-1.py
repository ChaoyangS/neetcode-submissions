class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS from the gate, reverse thinking, simultaneously do BFS from both gates
        # O(mn)
        # m = len(grid)
        # n = len(grid[0])
        # visit = set()
        # q = deque()
        # def addRoom(r,c):
        #     if (r<0 or r==m or c<0 or c==n or (r,c) in visit or grid[r][c]==-1):
        #         return
        #     visit.add((r,c))
        #     q.append([r,c])

        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c]==0:
        #             q.append([r,c])
        #             visit.add((r,c))
        # dist = 0
        # while q:
        #     for i in range(len(q)):
        #             r,c = q.popleft()
        #             grid[r][c] = dist
        #             addRoom(r+1,c)
        #             addRoom(r-1,c)
        #             addRoom(r,c+1)
        #             addRoom(r,c-1)
        #     dist +=1
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])

        def dfs(r, c, dist):
            # Boundary or wall check
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] < dist:
                return
            grid[r][c] = dist
            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)