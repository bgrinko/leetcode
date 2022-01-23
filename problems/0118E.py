"""LeetCode problem 118. Pascal's Triangle

Link:       https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy
Status:     Accepted (01/23/2022 00:36) 59 ms 14 MB
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            mr = [result[i - 1][0]]
            for j in range(1, i):
                mr.append(result[i - 1][j - 1] + result[i - 1][j])
            mr.append(result[i - 1][-1])
            result.append(mr)

        return result
