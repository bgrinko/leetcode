"""LeetCode problem 62. Unique Paths

Link:       https://leetcode.com/problems/unique-paths/
Difficulty: Medium
Status:     Accepted (07/14/2022 01:33) 53 ms 13.8 MB
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)
