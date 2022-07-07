"""LeetCode problem 97. Interleaving String

Link:       https://leetcode.com/problems/interleaving-string/
Difficulty: Medium
Status:     Accepted (07/07/2022 18:14) 77 ms 13.9 MB
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_l, s2_l, s3_l = len(s1), len(s2), len(s3)

        if s3_l != s1_l + s2_l:
            return False

        d = [False] * (s2_l + 1)

        for i in range(s1_l + 1):
            for j in range(s2_l + 1):
                if i == j and i == 0:
                    d[j] = True
                elif i == 0:
                    d[j] = d[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    d[j] = d[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    d[j] = (d[j] and s1[i - 1] == s3[i + j - 1]) or (d[j - 1] and s2[j - 1] == s3[i + j - 1])

        return d[s2_l]
