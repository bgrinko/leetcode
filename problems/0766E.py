"""LeetCode problem 766. Toeplitz Matrix

Link:       https://leetcode.com/problems/toeplitz-matrix/
Difficulty: Easy
Status:     Accepted (06/27/2022 20:30) 193 ms 13.8 MB
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
