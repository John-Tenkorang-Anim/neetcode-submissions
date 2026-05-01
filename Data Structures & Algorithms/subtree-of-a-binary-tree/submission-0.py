# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node, res):
            if not node:
                return

            dfs(node.left,res)
            dfs(node.right,res)
            res.append(node.val)
        res1 = []
        res2 = []
        dfs(root,res1)
        dfs(subRoot,res2)

        for i in range(len(res2)):
            if res2[i] != res1[i]:
                return False
        return True

