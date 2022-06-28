"""LeetCode problem 461. Hamming Distance

Link:       https://leetcode.com/problems/hamming-distance/
Difficulty: Easy
Status:     Accepted (06/28/2022 17:17) 48 ms 13.8 MB
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        v = x ^ y
        while v > 0:
            res += 1
            v = v & (v - 1)
        return res
