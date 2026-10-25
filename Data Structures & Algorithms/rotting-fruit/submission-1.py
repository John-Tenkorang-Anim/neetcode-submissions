from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 

        fresh_oranges = 0
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        minute_elasped = 0
        dirs = [(0, -1), (0, 1), (1,0), (-1, 0)]

        while q and fresh_oranges > 0:
            minute_elasped += 1

            for _ in range(len(q)):

                r , c = q.popleft()

                for dr , dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_oranges -= 1
                            q.append((nr, nc))

        return minute_elasped if fresh_oranges == 0 else - 1





        