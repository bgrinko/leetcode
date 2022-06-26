"""LeetCode problem 1816. Truncate Sentence

Link:       https://leetcode.com/problems/truncate-sentence/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:42) 36 ms 13.9 MB
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
