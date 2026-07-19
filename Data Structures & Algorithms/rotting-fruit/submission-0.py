class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        time = 0
        fresh = 0
        direction = ((0,1),(0,-1),(1,0),(-1,0))

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh +=1
                if grid[i][j]==2:
                    q.append([i,j])
        while q and fresh>0:
            
            for i in range(len(q)):
                i,j=q.popleft()
                for dr,dc in direction:
                    row, col = i+dr, j+dc
                    if row<0 or row == m or col<0 or col==n or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh -=1
            time +=1
        return time if fresh == 0 else -1

                    
        