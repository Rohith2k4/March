//1878. Get Biggest Three Rhombus Sums in a Grid
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # diagonal prefix sums
        d1 = [[0]*(n+2) for _ in range(m+1)]
        d2 = [[0]*(n+2) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                val = grid[i-1][j-1]
                d1[i][j] = d1[i-1][j-1] + val
                d2[i][j] = d2[i-1][j+1] + val

        vals = set()

        for i in range(m):
            for j in range(n):
                vals.add(grid[i][j])  # single cell rhombus

                size = 1
                while True:
                    ux, uy = i, j
                    dx, dy = i + 2*size, j
                    lx, ly = i + size, j - size
                    rx, ry = i + size, j + size

                    if dx >= m or ly < 0 or ry >= n:
                        break

                    s = (
                        d2[lx+1][ly+1] - d2[ux][uy+2] +
                        d1[rx+1][ry+1] - d1[ux][uy] +
                        d1[dx+1][dy+1] - d1[lx][ly] +
                        d2[dx+1][dy+1] - d2[rx][ry+2] -
                        grid[ux][uy] - grid[dx][dy] - grid[lx][ly] - grid[rx][ry]
                    )

                    vals.add(s)
                    size += 1

        return sorted(vals, reverse=True)[:3]
