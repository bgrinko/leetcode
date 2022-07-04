"""LeetCode problem 455. Assign Cookies

Link:       https://leetcode.com/problems/assign-cookies/
Difficulty: Easy
Status:     Accepted (07/04/2022 09:28) 200 ms 15.7 MB
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        k = 0

        for i in range(len(s)):
            if s[i] >= g[k]:
                k += 1
            if k >= len(g):
                break

        return k
