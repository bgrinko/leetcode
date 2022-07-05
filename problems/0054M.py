"""LeetCode problem 54. Spiral Matrix

Link:       https://leetcode.com/problems/spiral-matrix/
Difficulty: Medium
Status:     Accepted (07/05/2022 22:48) 40 ms 13.9 MB
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        n = r * c
        if r == 1:
            return matrix[0]
        path = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = []
        i = j = d = k = 0

        while k < n:
            result.append(matrix[i][j])
            k += 1
            matrix[i][j] = -500

            if not (0 <= i + path[d][0] < r) or not (0 <= j + path[d][1] < c):
                d += 1
                d %= 4

            if matrix[i + path[d][0]][j + path[d][1]] == -500:
                d += 1
                d %= 4

            i += path[d][0]
            j += path[d][1]

        return result
