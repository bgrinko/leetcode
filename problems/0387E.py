"""LeetCode problem 387. First Unique Character in a String

Link:       https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy
Status:     Accepted (07/08/2022 01:48) 110 ms 14 MB
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)

        for i, j in enumerate(s):
            if c[j] == 1:
                return i
        return -1
