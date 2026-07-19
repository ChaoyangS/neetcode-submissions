class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        res = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res +=1
                    grid[i][j] = "0"
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        for d in directions:
                            dx = x+d[0]
                            dy = y+d[1]

                            if(0<=dx<m and 0<=dy<n and grid[dx][dy]=="1"):
                                q.append((dx,dy))
                                grid[dx][dy]="0"
        return res
        