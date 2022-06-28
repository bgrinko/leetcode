"""LeetCode problem 1051. Height Checker

Link:       https://leetcode.com/problems/height-checker/
Difficulty: Easy
Status:     Accepted (06/28/2022 17:26) 81 ms 13.9 MB
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        return sum([heights[i] != expected[i] for i in range(heights.__len__())])
