"""LeetCode problem 136. Single Number

Link:       https://leetcode.com/problems/single-number/
Difficulty: Easy
Status:     Accepted (01/22/2022 17:38) 128 ms 16.6 MB
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            k = k ^ i
        return k
