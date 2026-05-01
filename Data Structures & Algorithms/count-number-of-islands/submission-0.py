class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        def dfs(r,c):
            if not ( 0 <= r < nrows and 0 <= c < ncols and grid[r][c] == "1"):
                return 
            
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        count = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    dfs (r,c)
                    count += 1
        return count
        
        