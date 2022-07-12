"""LeetCode problem 121. Best Time to Buy and Sell Stock

Link:       https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Status:     Accepted (07/12/2022 23:43) 895 ms 25 MB
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, profit = inf, -inf, 0
        for i in prices:
            if i < b:
                b, s = i, -inf
            elif i > s and b != inf:
                s = i
                profit = max(profit, s - b)
        return profit

