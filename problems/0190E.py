"""LeetCode problem 190. Reverse Bits

Link:       https://leetcode.com/problems/reverse-bits/
Difficulty: Easy
Status:     Accepted (07/02/2022 19:30) 52 ms 13.8 MB
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        bi = '{:0>32s}'.format(bin(n)[2:])
        return int(bi[::-1], 2)
