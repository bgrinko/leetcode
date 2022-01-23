"""LeetCode problem 28. Implement strStr()

Link:       https://leetcode.com/problems/implement-strstr/
Difficulty: Easy
Status:     Accepted (01/22/2022 14:37) 32 ms 14.4 MB
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
