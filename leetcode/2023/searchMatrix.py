class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mn = min(len(matrix),len(matrix[0]))
        for i in range(len(matrix)):
            t = bisect_left(matrix[i],target)
            if t < len(matrix[i]) and matrix[i][t] == target:
                return True
        return False