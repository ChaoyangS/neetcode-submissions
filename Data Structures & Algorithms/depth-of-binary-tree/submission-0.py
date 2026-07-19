# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursively
        maxdepth = 0
        if not root:
            return 0
        maxdepth = max(self.maxDepth(root.right)+1, 1+ self.maxDepth(root.left))
        return maxdepth
        