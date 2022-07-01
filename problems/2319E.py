"""LeetCode problem 2319. Check if Matrix Is X-Matrix

Link:       https://leetcode.com/problems/check-if-matrix-is-x-matrix/
Difficulty: Easy
Status:     Accepted (07/01/2022 13:15) 384 ms 15 MB
"""


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                    continue
                elif grid[i][j] != 0:
                    return False
        return True
