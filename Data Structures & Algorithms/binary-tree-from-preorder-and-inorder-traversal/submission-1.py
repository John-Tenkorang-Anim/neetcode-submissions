# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        curr_idx = 0
        index_map = {val: i for i, val in enumerate(inorder)}

        def build(l, r):

            nonlocal curr_idx

            if l > r:
                return None
            
            val = preorder[curr_idx]
            node = TreeNode(val)
            curr_idx += 1

            node.left = build(l, index_map[val] - 1)
            node.right = build(index_map[val]+1, r)

            return node
        
        return build(0, len(inorder) - 1)
            
        