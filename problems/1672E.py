"""LeetCode problem 1672. Richest Customer Wealth

Link:       https://leetcode.com/problems/richest-customer-wealth/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:27) 102 ms 13.9 MB
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])

