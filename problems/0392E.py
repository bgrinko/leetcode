"""LeetCode problem 392. Is Subsequence

Link:       https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Status:     Accepted (07/09/2022 20:50) 61 ms 14 MB
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        ls, lt = len(s), len(t)

        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == ls:
            return True

        return False
