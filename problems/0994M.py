"""LeetCode problem 994. Rotting Oranges

Link:       https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium
Status:     Accepted (01/30/2022 21:30) 108 ms 13.9 MB
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = set()
        rotten = set()
        k = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    rotten.add(f"{i}-{j}")
                elif grid[i][j] == 1:
                    fresh.add(f"{i}-{j}")

        def split(q, w):
            fresh.remove(f"{q}-{w}")
            rotten.add(f"{q}-{w}")

        while True:
            before = len(fresh)
            for i in rotten.copy():
                l, r = int(i.split("-")[0]), int(i.split("-")[1])
                split(l + 1, r) if f"{l + 1}-{r}" in fresh else None
                split(l - 1, r) if f"{l - 1}-{r}" in fresh else None
                split(l, r + 1) if f"{l}-{r + 1}" in fresh else None
                split(l, r - 1) if f"{l}-{r - 1}" in fresh else None
            after = len(fresh)

            if before == after and before == 0:
                return 0
            elif before == after:
                return -1
            elif after == 0:
                return k + 1

            k += 1
