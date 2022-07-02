"""LeetCode problem 2278. Percentage of Letter in String

Link:       https://leetcode.com/problems/percentage-of-letter-in-string/
Difficulty: Easy
Status:     Accepted (07/02/2022 12:08) 50 ms 13.9 MB
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return trunc(s.count(letter) / len(s) * 100)
