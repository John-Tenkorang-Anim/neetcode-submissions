
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for i in range(n):
            for j in range(m):
                res.append(matrix[i][j])
        return target in res


        