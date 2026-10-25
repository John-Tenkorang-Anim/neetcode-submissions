class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = list(range(n))
        size = [1] * n

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]

            return True
        
        for u, v in edges:
            if not union(u,v):
                return False
                
        return True