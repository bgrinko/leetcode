"""LeetCode problem 70. Climbing Stairs

Link:       https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
Status:     Accepted (07/02/2022 15:21) 41 ms 13.9 MB
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        r, l = 0, 1
        for i in range(n):
            r, l = l, r + l
        return l
