"""LeetCode problem 695. Max Area of Island

Link:       https://leetcode.com/problems/max-area-of-island/
Difficulty: Medium
Status:     Accepted (01/25/2022 00:27) 144 ms 17 MB
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = [[False for x in range(C)] for y in range(R)]

        def find(r, c) -> int:
            if grid[r][c] != 1 or visited[r][c]:
                return 0

            visited[r][c] = True
            result = 1
            if r >= 1: result += find(r - 1, c)
            if r + 1 < R: result += find(r + 1, c)
            if c >= 1: result += find(r, c - 1)
            if c + 1 < C: result += find(r, c + 1)

            return result

        res = 0
        for i in range(R):
            for j in range(C):
                res = max(res, find(i, j))
        return res
