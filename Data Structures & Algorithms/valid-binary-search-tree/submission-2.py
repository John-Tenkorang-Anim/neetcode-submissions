# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, res):
            if not root:
                return
            
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

            return res
        res = []
        dfs(root, res)
        for i in range(len(res)-1):
            if res[i] >= res[i + 1]:
                return False
        return True
