"""LeetCode problem 1512. Number of Good Pairs

Link:       https://leetcode.com/problems/number-of-good-pairs/
Difficulty: Easy
Status:     Accepted (06/27/2022 03:16) 69 ms 13.9 MB
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = [0] * 1000

        for i in nums:
            n[i] += 1

        result = 0

        for i in n:
            result += i * (i - 1) // 2

        return result
