"""LeetCode problem 567. Permutation in String

Link:       https://leetcode.com/problems/permutation-in-string/
Difficulty: Medium
Status:     Accepted (01/27/2022 23:13) 2516 ms 14 MB
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        c1 = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if c1 == Counter(s2[i:len(s1) + i]):
                return True

        return False
