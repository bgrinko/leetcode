"""LeetCode problem 200. Number of Islands

Link:       https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Status:     Accepted (07/14/2022 00:28) 305 ms 16.7 MB
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = [[False for x in range(C)] for y in range(R)]


        def find(r, c) -> int:
            if grid[r][c] != "1" or visited[r][c]:
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
                if find(i, j):
                    res += 1
        return res

