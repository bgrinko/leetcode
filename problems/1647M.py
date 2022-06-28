"""LeetCode problem 1647. Minimum Deletions to Make Character Frequencies Unique

Link:       https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
Difficulty: Medium
Status:     Accepted (06/28/2022 23:19) 555 ms 14.9 MB
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        c = [0] * 26
        for i in s:
            c[ord(i) - ord('a')] += 1

        e = 0
        f = set()
        for i in range(26):
            while c[i] and c[i] in f:
                c[i] -= 1
                e += 1
            f.add(c[i])

        return e
