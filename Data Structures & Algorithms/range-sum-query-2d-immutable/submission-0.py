class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        nrows = len(matrix)
        ncols = len(matrix[0])

        self.pre = [[0] * (ncols + 1) for _ in range(nrows + 1)]

        for r in range(nrows):
            for c in range(ncols):
                self.pre[r+1][c+1] = (matrix[r][c] 
                + self.pre[r][c+1] 
                + self.pre[r+1][c] 
                - self.pre[r][c] )
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.pre[row2 + 1][col2+ 1] 
        - self.pre[row1][col2+1] 
        - self.pre[row2+1][col1] 
        + self.pre[row1][col1] )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)