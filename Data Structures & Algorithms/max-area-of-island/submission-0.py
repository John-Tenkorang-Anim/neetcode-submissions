class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]

        max_area = 0


        rows = len(grid)
        cols = len(grid[0])


        def dfs(r, c):

            if not (0 <= r < rows and 0 <= c < cols):
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            area = 1
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    area += dfs(nr, nc)

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area
        