//1582. Special Positions in a Binary Matrix
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        row_count = [0] * rows
        col_count = [0] * cols
        
        # Count 1s in each row and column
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        special = 0
        
        # Check special positions
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        
        return special
