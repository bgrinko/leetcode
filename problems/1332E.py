"""LeetCode problem 1332. Remove Palindromic Subsequences

Link:       https://leetcode.com/problems/remove-palindromic-subsequences/
Difficulty: Easy
Status:     Accepted (06/30/2022 21:49) 52 ms 13.9 MB
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
