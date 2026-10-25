class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n == 0:
            return 0

        parent = list(range(n))
        size = [1] * n
        connected = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x,y):
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
            if union(u,v):
                connected -= 1

        return connected
        