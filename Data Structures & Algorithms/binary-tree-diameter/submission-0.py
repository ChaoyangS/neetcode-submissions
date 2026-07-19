# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def height(node):

            if not node:
                return 0
            lefth = height(node.left)
            righth = height(node.right)
        
            self.max_diameter = max(self.max_diameter,lefth+righth)
            return 1+ max(lefth,righth)
        height(root)
        return self.max_diameter

        