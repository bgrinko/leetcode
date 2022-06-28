"""LeetCode problem 771. Jewels and Stones

Link:       https://leetcode.com/problems/jewels-and-stones/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:07) 54 ms 13.8 MB
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for c in stones if c in jewels])
