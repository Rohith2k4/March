//1727. Largest Submatrix With Rearrangements
from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2: Process each row
        for row in matrix:
            row.sort(reverse=True)
            
            for i in range(n):
                max_area = max(max_area, row[i] * (i + 1))
        
        return max_area
