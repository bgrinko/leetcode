"""LeetCode problem 119. Pascal's Triangle II

Link:       https://leetcode.com/problems/pascals-triangle-ii/
Difficulty: Easy
Status:     Accepted (01/23/2022 00:46) 56 ms 14 MB
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(1, rowIndex + 1):
            mr = [result[0]]
            for j in range(1, i):
                mr.append(result[j - 1] + result[j])
            mr.append(result[-1])
            result = mr

        return result
