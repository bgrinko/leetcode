"""LeetCode problem 58. Length of Last Word

Link:       https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
Status:     Accepted (07/05/2022 22:00) 54 ms 13.9 MB
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
