"""LeetCode problem 69. Sqrt(x)

Link:       https://leetcode.com/problems/sqrtx/
Difficulty: Easy
Status:     Accepted (01/22/2022 16:42) 35 ms 14.2 MB
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        ln = len(str(x))
        if ln % 2 == 1:
            e = 2 * 10 ** ((ln - 1) / 2)
        else:
            e = 6 * 10 ** ((ln - 2) / 2)

        for i in range(5):
            e = 0.5 * (e + x / e)

        return int(e)
