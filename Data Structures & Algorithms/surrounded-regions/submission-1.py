class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        nrows = len(board)
        ncols = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if not (0 <= r < nrows and 0 <= c < ncols):
                return

            if board[r][c] != "O":
                return

            board[r][c] = "T"

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

                
        for r in range(nrows):
            dfs(r, 0)
            dfs(r, ncols - 1)

        for c in range(ncols):
            dfs(0, c)
            dfs(nrows - 1, c)

        # Step 2: Capture surrounded regions
        # Step 3: Restore safe regions
        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        