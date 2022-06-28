"""LeetCode problem 77. Combinations

Link:       https://leetcode.com/problems/combinations/
Difficulty: Medium
Status:     Accepted (06/28/2022 22:41) 103 ms 17.7 MB
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
