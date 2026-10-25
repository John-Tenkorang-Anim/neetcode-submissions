"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        hmap = {}

        def dfs(node):
            if not node:
                return None

            if node in hmap:
                return hmap[node]

            if node not in hmap:
                new_node = Node(node.val)
                hmap[node] = new_node

                for n in node.neighbors:
                    new_node.neighbors.append(dfs(n))

            return new_node
        return dfs(node)
        