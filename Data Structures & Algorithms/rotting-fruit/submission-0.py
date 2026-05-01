from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        if nrows == 0:
            return -1
        ncols = len(grid[0])

        q = deque()
        fresh_oranges = 0

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        time = 0
        while q and fresh_oranges > 0:
            n = len(q)

            for _ in range(n):
                r, c = q.popleft()

                for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr , nc = dr + r, dc + c

                    if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr, nc))
            
            if q:
                time += 1
        
        if fresh_oranges == 0:
            return time
        else:
            return -1

