"""LeetCode problem 2114. Maximum Number of Words Found in Sentences

Link:       https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:30) 61 ms 13.9 MB
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([i.split().__len__() for i in sentences])
