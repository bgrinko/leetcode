"""LeetCode problem 867. Transpose Matrix

Link:       https://leetcode.com/problems/transpose-matrix/
Difficulty: Easy
Status:     Accepted (06/30/2022 21:28) 124 ms 14.9 MB
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
