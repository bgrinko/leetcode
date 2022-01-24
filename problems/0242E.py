"""LeetCode problem 242. Valid Anagram

Link:       https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Status:     Accepted (01/25/2022 00:57) 84 ms 14.3 MB
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = dict(), dict()
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        for i in t:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1

        return a == b
