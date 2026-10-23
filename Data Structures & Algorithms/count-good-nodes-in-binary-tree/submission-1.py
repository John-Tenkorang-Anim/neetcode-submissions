# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(node, max_value):
            if not node:
                return 0
            
            if node.val >= max_value:
                return 1 + good(node.left, node.val) + good(node.right, node.val)
            else:
                return good(node.left, max_value) + good(node.right, max_value)
        
        left = good(root.left, root.val)
        right = good(root.right, root.val)

        return 1 + left + right
        