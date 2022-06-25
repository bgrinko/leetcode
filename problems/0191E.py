"""LeetCode problem 191. Number of 1 Bits

Link:       https://leetcode.com/problems/number-of-1-bits/
Difficulty: Easy
Status:     Accepted (06/25/2022 21:28) 53 ms 13.8 MB
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            n &= n - 1
            count += 1

        return count
