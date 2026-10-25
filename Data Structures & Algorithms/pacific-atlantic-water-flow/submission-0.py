from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        nrows = len(heights)
        ncols = len(heights[0])

        pac = [[False] * ncols for _ in range(nrows)]
        atl = [[False] * ncols for _ in range(nrows)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr , dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < nrows and 0 <= nc < ncols 
                    and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        res = []
        pacific = []
        atlantic = []

        for c in range(ncols):
            pacific.append((0, c))
            atlantic.append((nrows - 1, c))

        for r in range(nrows):
            pacific.append((r, 0))
            atlantic.append((r, ncols - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        for r in range(nrows):
            for c in range(ncols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
        