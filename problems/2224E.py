"""LeetCode problem 2224. Minimum Number of Operations to Convert Time

Link:       https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
Difficulty: Easy
Status:     Accepted (07/02/2022 01:08) 56 ms 13.9 MB
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cu_h = int(current[0:2]) * 60
        co_h = int(correct[0:2]) * 60
        cu_m = int(current[3:])
        co_m = int(correct[3:])
        result = co_h - cu_h + co_m - cu_m
        t = result // 60
        result = result % 60
        t += result // 15
        result = result % 15
        t += result // 5
        result = result % 5
        t += result
        return t
