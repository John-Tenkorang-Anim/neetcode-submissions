from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # example of multisource bfs

        if not grid or not grid[0]:
            return 

        dirs = [(0,1), (0,-1), (1,0),(-1,0)]

        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

        