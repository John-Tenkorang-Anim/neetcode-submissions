from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrows = len(grid)
        ncols = len(grid[0])

        q = deque()

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()

            for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr , nc = dr + r, dc + c

                if 0<= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
