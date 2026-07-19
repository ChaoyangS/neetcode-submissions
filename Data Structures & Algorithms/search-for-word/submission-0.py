class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)
        path = set()
        def dfs(a,b,i):
            if i == k:
                return True
            if (a<0 or b<0 or a>=m or b>=n or word[i]!=board[a][b] or (a,b) in path):
                return False
            path.add((a,b))
            res = (dfs(a+1,b,i+1) or dfs(a-1,b,i+1) or dfs(a,b+1,i+1) or dfs(a,b-1,i+1))
            path.remove((a,b))
            return res
            
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False


        