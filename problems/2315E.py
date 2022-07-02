"""LeetCode problem 2315. Count Asterisks

Link:       https://leetcode.com/problems/count-asterisks/
Difficulty: Easy
Status:     Accepted (07/02/2022 11:50) 43 ms 13.8 MB
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        in_pair = False
        result = 0

        for i in s:
            if i == "|":
                in_pair = not in_pair
            if i == "*" and not in_pair:
                result += 1

        return result
