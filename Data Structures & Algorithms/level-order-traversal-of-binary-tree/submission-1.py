# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque([root])
        res = []

        while q:
            #get level length
            level_len = len(q)
            level_res = []
            for _ in range(level_len):
                #get the # of pops through the level length
                cur = q.popleft()
                level_res.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level_res:
                res.append(level_res)
        return res




        