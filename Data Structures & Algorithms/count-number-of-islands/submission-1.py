class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):

            if not (0 <= r < rows and 0 <= c < cols):
                return 
            
            if grid[r][c] != "1":
                return
            
            grid[r][c] = '0'

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)


        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands


        