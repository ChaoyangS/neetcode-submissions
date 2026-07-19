class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs
        direction = ((0,1),(0,-1),(1,0),(-1,0))
        q = deque()
        maxisland = 0
        m= len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                curr =0
                if grid[i][j]==1:
                    curr+=1
                    
                    q.append((i,j))
                    grid[i][j]=0

                    while q:
                        x,y = q.popleft()

                        for d in direction:
                            
                            dx=x+d[0]
                            dy = y+d[1]

                            if 0<=dx<m and 0<=dy<n and grid[dx][dy]==1:
                                curr+=1
                                print(curr)
                                q.append((dx,dy))
                                grid[dx][dy]=0
                maxisland = max(maxisland, curr)
        return maxisland

        