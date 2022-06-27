"""LeetCode problem 1486. XOR Operation in an Array

Link:       https://leetcode.com/problems/xor-operation-in-an-array/
Difficulty: Easy
Status:     Accepted (06/27/2022 20:35) 61 ms 13.8 MB
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])
