"""LeetCode problem 1662. Check If Two String Arrays are Equivalent

Link:       https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:37) 47 ms 13.7 MB
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
