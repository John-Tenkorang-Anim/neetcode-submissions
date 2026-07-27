from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        nrows = len(board)
        ncols = len(board[0])

        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(nrows):
            for c in range(ncols):
                num = board[r][c]
                if num == ".":
                    continue
                elif not (num in row[r] or num in col[c] or num in grid[(r//3,c//3)]):
                    row[r].add(num)
                    col[c].add(num)
                    grid[(r//3,c//3)].add(num)
                else:
                    return False

        return True

        