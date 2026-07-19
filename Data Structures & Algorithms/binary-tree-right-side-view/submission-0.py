# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])

        res = []
        while q:
            level_res = []
            level_len = len(q)
            for _ in range(level_len):
                cur = q.popleft()
                level_res.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level_res:
                res.append(level_res[-1])
        return res
            
        