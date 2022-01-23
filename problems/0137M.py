"""LeetCode problem 137. Single Number II

Link:       https://leetcode.com/problems/single-number-ii/
Difficulty: Medium
Status:     Accepted (01/22/2022 18:23) 64 ms 15.8 MB
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        r = 0
        for i in nums:
            k = (k ^ i) & (~r)
            r = (r ^ i) & (~k)
        return k
