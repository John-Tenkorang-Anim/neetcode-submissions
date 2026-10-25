class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n - 1 != len(edges):
            return False
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):

            if node in visited:
                return 
            
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        return len(visited) == n
        