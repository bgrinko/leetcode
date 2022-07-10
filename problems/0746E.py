"""LeetCode problem 746. Min Cost Climbing Stairs

Link:       https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Status:     Accepted (07/10/2022 20:13) 69 ms 14.1 MB
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[len(cost)]
