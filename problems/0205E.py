"""LeetCode problem 205. Isomorphic Strings

Link:       https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy
Status:     Accepted (07/09/2022 12:51) 54 ms 14.2 MB
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        for i in range(len(s)):
            if s[i] in d1 and d1[s[i]] != t[i]:
                return False
            if t[i] in d2 and d2[t[i]] != s[i]:
                return False
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]

        return True
